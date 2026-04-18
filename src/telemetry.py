"""
Pair-Extraordinaire Telemetry Client
====================================
Sends PR stats → GAS Web App → Supabase → Vercel dashboard.

What is collected:
  - github_username   : dashboard identity
  - instance_id       : stable anon ID derived from username + machine
  - total_prs_created : cumulative PRs this bot has generated
  - session_prs       : PRs created in this run
  - mode              : "single" or "collaborator"
  - bot_type          : "pair_extraordinaire"
  - NO github tokens, NO private keys ever sent
"""

from dotenv import load_dotenv
load_dotenv()


import os
import sys
import time
import json
import hashlib
import hmac as _hmac
import platform as _platform
import threading
import logging
import uuid as _uuid
from typing import Optional, Dict

logger = logging.getLogger(__name__)

_REQUIRED_GAS_URL   = "https://script.google.com/macros/s/AKfycbwzWLd0vAErdQGHSYxq6lgIS55Unv_WOtjbumhDKfNaDoyIsQiJ16qRcjLXknND_XNHjA/exec"
_REQUIRED_SECRET    = "4bc16c4e696f0012eb1a330adeaa1bee054bfafebb4ae75e60a2ff0072c62316"
_REQUIRED_ENABLED   = "true"

BOT_TYPE = "pair_extraordinaire"

def verify_telemetry():
    load_dotenv()
    gas_url = os.getenv("TELEMETRY_GAS_URL", "")
    enabled = os.getenv("TELEMETRY_ENABLED", "").lower()
    secret  = os.getenv("TELEMETRY_HMAC_SECRET", "")

    ok = (
        gas_url == _REQUIRED_GAS_URL
        and enabled == _REQUIRED_ENABLED
        and secret  == _REQUIRED_SECRET
    )

    if not ok:
        print("\n" + "=" * 60)
        print("  PAIR-EXTRAORDINAIRE BOT — CRITICAL SECURITY ERROR")
        print("=" * 60)
        print("  Telemetry configuration is invalid, missing,")
        print("  or has been tampered with.")
        print()
        print("  Please restore the official .env settings.")
        print("  The bot cannot proceed without valid telemetry.")
        print("=" * 60 + "\n")
        sys.exit(1)


def _derive_instance_id(username: str) -> str:
    machine_raw  = f"{_platform.node()}{_platform.machine()}{_platform.system()}"
    machine_hash = hashlib.sha256(machine_raw.encode()).hexdigest()[:16]
    return hashlib.sha256(f"{username.lower()}:{machine_hash}".encode()).hexdigest()[:32]

def _hmac_sha256(secret: str, message: str) -> str:
    return _hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()


class TelemetryClient:
    _MIN_INTERVAL = 300
    _MAX_RETRIES  = 3
    _TIMEOUT      = 20

    def __init__(self, github_username: str, github_token: str):
        self.username     = github_username
        self.github_token = github_token
        self.instance_id  = _derive_instance_id(github_username)
        self._gas_url     = os.getenv("TELEMETRY_GAS_URL", "")
        self._secret      = os.getenv("TELEMETRY_HMAC_SECRET", "")
        self.enabled      = os.getenv("TELEMETRY_ENABLED", "true").lower() == "true"
        self._last_sent: Optional[float] = None
        self._lock        = threading.Lock()
        logger.debug(f"Telemetry init: instance={self.instance_id[:12]} bot={BOT_TYPE}")
        
        # ── Startup Handshake ──
        if self.enabled:
            self._perform_handshake()

    def report(self, total_prs_created: int, session_prs: int, mode: str):
        if not self.enabled: return
        with self._lock:
            if self._last_sent and (time.time() - self._last_sent) < self._MIN_INTERVAL:
                return
        threading.Thread(
            target=self._send,
            args=(total_prs_created, session_prs, mode, "session", False),
            daemon=True,
        ).start()

    def report_final(self, total_prs_created: int, session_prs: int, mode: str):
        if not self.enabled: return
        threading.Thread(
            target=self._send,
            args=(total_prs_created, session_prs, mode, "session_final", True),
            daemon=True,
        ).start()

    def _perform_handshake(self):
        import requests as _requests
        token_hash = hashlib.sha256(self.github_token.encode()).hexdigest()
        payload = {
            "bot_type":        BOT_TYPE,
            "instance_id":     self.instance_id,
            "github_username": self.username,
            "token_hash":      token_hash,
            "event_type":      "handshake",
        }
        body    = json.dumps(payload, sort_keys=True, separators=(',', ':'))
        nonce   = _uuid.uuid4().hex
        ts      = str(int(time.time() * 1000))
        # Use SHA-256 Body Hash for signature (matches hardened code.gs)
        body_hash = hashlib.sha256(body.encode()).hexdigest()
        message = f"{ts}.{nonce}.{body_hash}"
        sig     = _hmac_sha256(self._secret, message)
        params  = {"ts": ts, "nonce": nonce, "sig": sig}
        
        try:
            resp = _requests.post(self._gas_url, data=body, params=params, timeout=15)
            if resp.status_code == 200:
                logger.info("Handshake OK")
                return
            
            print("\n" + "!" * 60)
            print("  PAIR-EXTRAORDINAIRE — UNAUTHORIZED INSTANCE")
            print("!" * 60)
            print("  Your GitHub account is not registered on the dashboard.")
            print(f"  Account: {self.username}")
            print("\n  Please register to continue.")
            print("!" * 60 + "\n")
            sys.exit(1)
        except Exception as e:
            logger.warning(f"Handshake skipped (Server offline): {e}")

    def _build_payload(self, total_prs_created: int, session_prs: int, mode: str, event_type: str) -> Dict:
        # Secure token hashing for dashboard mapping
        token_hash = hashlib.sha256(self.github_token.encode()).hexdigest()
        
        return {
            "bot_type":          BOT_TYPE,
            "instance_id":       self.instance_id,
            "github_username":   self.username,
            "token_hash":        token_hash,
            "total_prs_created": int(total_prs_created),
            "session_prs":       int(session_prs),
            "mode":              str(mode),
            "event_type":        event_type,
        }

    def _send(self, total_prs_created: int, session_prs: int, mode: str, event_type: str, force: bool):
        with self._lock:
            if not force and self._last_sent and (time.time() - self._last_sent) < self._MIN_INTERVAL:
                return
            try:
                payload = self._build_payload(total_prs_created, session_prs, mode, event_type)
                body    = json.dumps(payload, sort_keys=True, separators=(',', ':'))
                nonce   = _uuid.uuid4().hex
                ts      = str(int(time.time() * 1000))
                # Use SHA-256 Body Hash for signature (matches hardened code.gs)
                body_hash = hashlib.sha256(body.encode()).hexdigest()
                message = f"{ts}.{nonce}.{body_hash}"
                sig     = _hmac_sha256(self._secret, message)
                params  = {"ts": ts, "nonce": nonce, "sig": sig}
            except Exception as exc:
                logger.debug(f"Telemetry build error: {exc}")
                return

        try:
            import requests as _requests
        except ImportError:
            return

        headers = {"Content-Type": "application/json", "User-Agent": "PairExtraordinaireBot/1.0"}

        for attempt in range(self._MAX_RETRIES):
            try:
                resp = _requests.post(
                    self._gas_url, data=body, params=params, headers=headers,
                    timeout=self._TIMEOUT, allow_redirects=True
                )
                if resp.status_code == 200:
                    with self._lock:
                        self._last_sent = time.time()
                    return
                elif resp.status_code == 429:
                    return
                elif resp.status_code >= 500:
                    time.sleep(2 ** attempt)
                else:
                    return
            except Exception as exc:
                time.sleep(2 ** attempt)
