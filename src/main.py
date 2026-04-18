#!/usr/bin/env python3
"""
Auto PR Creator - Enhanced version with multi-collaborator support
"""

import argparse
from pathlib import Path
from datetime import datetime
import sys
import logging

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config_manager import ConfigManager
from src.git_operations import GitOperations
from src.github_client import GitHubClient
from src.notification_manager import NotificationManager
from src.collaborator_manager import CollaboratorManager
from src.telemetry import TelemetryClient, verify_telemetry
from src import utils
import requests

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

PAIR_EXT_BANNER_LOG = """
 [bold green] [PAIR_EXT] >> CO-PILOT ENGAGED[/bold green]
 [bold green] [PAIR_EXT] >> MODE: COLLABORATIVE AMPLIFICATION[/bold green]
 [bold green] [PAIR_EXT] >> STATUS: MONITORING STACK[/bold green]
"""

def pair_ext_log(msg, severity=None):
    prefix = "[PAIR_EXT] >> "
    ts = datetime.now().strftime("%H:%M:%S")
    
    severity_map = {
        "CRITICAL": "🔴 CRITICAL",
        "WARN": "🟡 WARN",
        "SUGGEST": "🟢 SUGGEST"
    }
    
    status_text = severity_map.get(severity, "")
    if status_text:
        status_text = f" | {status_text}"
        
    color = "white"
    if severity == "CRITICAL": color = "bold red"
    elif severity == "WARN": color = "bold yellow"
    elif severity == "SUGGEST": color = "bold green"

    console.print(f"[{ts}] [{color}]{prefix}{msg}{status_text}[/{color}]")

logger = logging.getLogger(__name__)


class AutoPRCreator:
    """Main application class with multi-collaborator support"""

    def __init__(self, config_path="config/config.json", dry_run=False):
        utils.setup_logging()
        self.dry_run = dry_run
        self.mode = None
        
        verify_telemetry()

        if dry_run:
            logger.info("🔧 DRY RUN MODE - No changes will be made")

        try:
            self.config = ConfigManager(config_path)
            self.git = GitOperations(self.config)
            self.github = GitHubClient(self.config)
            self.notifier = NotificationManager(self.config)
            self.collaborator_manager = CollaboratorManager(self.config)
            
            token = self.config.get_github_token()
            username = "Unknown_User"
            try:
                r = requests.get("https://api.github.com/user", headers={"Authorization": f"Bearer {token}"}).json()
                if "login" in r:
                    username = r["login"]
            except Exception:
                pass
                
            self.telemetry = TelemetryClient(github_username=username, github_token=token)
            self.display_aesthetic_banner(token, username)
            self.session_prs = 0
            
            pair_ext_log("Auto PR Creator initialized successfully", severity="SUGGEST")

        except Exception as e:
            logger.error(f"❌ Failed to initialize: {e}")
            raise

    def display_aesthetic_banner(self, token: str, username: str):
        """Displays a non-truncating, fully responsive banner via Rich."""
        try:
            with open("ascii-art.txt", "r", encoding="utf-8") as f:
                art = f.read()
        except Exception:
            art = "[blue]ASCII ART NOT FOUND[/blue]"

        title_art = r"""
    ____        _             ______      __                      
   / __ \____ _(_)____       / ____/___ _/ /___ __  ____  __     
  / /_/ / __ `/ / ___/      / / __/ __ `/ / __ `/ |/_/ / / /     
  / ____/ /_/ / / /         / /_/ / /_/ / / /_/ />  </ /_/ /      
/_/    \__,_/_/_/          \____/\__,_/_/\__,_/_/|_|\__, /       
                                                   /____/        
"""
        title_text = Text(title_art, style="bold green", justify="center")

        info_table = Table.grid(padding=(0, 1))
        info_table.add_column(style="bold cyan", justify="left")
        info_table.add_column(style="cyan", no_wrap=False)

        info_table.add_row("User:", username)
        info_table.add_row("Dashboard:", f"{username} + [yellow]{token}[/yellow]")
        info_table.add_row("", "")
        info_table.add_row("GitHub Repo:", "[blue]https://github.com/itxashancode/Pair-Extraordinaire-Automation[/blue]")
        info_table.add_row("Follow Me:", "[blue]https://github.com/itxashancode[/blue]")

        content_table = Table.grid(padding=(0, 2))
        content_table.add_column(ratio=2) 
        content_table.add_column(ratio=1) 
        
        content_table.add_row(info_table, Text(art, style="cyan", justify="right"))

        full_layout = Table.grid(padding=(1, 0))
        full_layout.add_column(justify="center")
        full_layout.add_row(title_text)
        full_layout.add_row(content_table)

        panel = Panel(full_layout, border_style="green", padding=(1, 2), expand=True)
        console.print(panel)
        console.print(PAIR_EXT_BANNER_LOG)

    def run_single_user_mode(self):
        """Original single-user mode"""
        branch = utils.generate_branch_name()
        pair_ext_log(f"I've generated a new development branch: {branch}", severity="SUGGEST")

        if self.dry_run:
            logger.info(f"[DRY RUN] Would create branch: {branch}")
            logger.info("[DRY RUN] Would modify files")
            logger.info("[DRY RUN] Would commit and push changes")
            logger.info("[DRY RUN] Would create and merge PR")
            return True

        # Create branch
        self.git.create_branch(branch)

        # Modify files
        files_to_modify = self.config.get_files_to_modify()
        if not files_to_modify:
            logger.warning("No files configured to modify")
            return False

        modified_files = self.git.modify_files(files_to_modify)
        logger.info(f"📝 Modified {len(modified_files)} files")

        # Commit changes
        coauthor = self.config.get_coauthor_config()
        self.git.commit(modified_files, coauthor)

        # Push to remote
        self.git.push(branch)
        logger.info("🚀 Pushed changes to remote")

        return branch, None

    def run_collaborator_mode(self):
        """Multi-collaborator mode"""
        branch = utils.generate_branch_name(prefix="collab-pr")
        logger.info(f"🤝 Creating collaborative branch: {branch}")

        if self.dry_run:
            logger.info(f"[DRY RUN] Would create branch: {branch}")
            logger.info(f"[DRY RUN] Would create commits from {len(self.collaborator_manager.collaborators)} collaborators")
            return branch, None

        # Create branch
        self.git.create_branch(branch)

        # Create commits from multiple collaborators
        commits = self.collaborator_manager.create_multi_collaborator_commits(
            branch, 
            num_commits_per_collaborator=2
        )

        # Push all commits
        self.git.push(branch)
        logger.info(f"🚀 Pushed {len(commits)} collaborator commits to remote")

        return branch, commits

    def create_and_merge_pr(self, branch: str, commits=None):
        """Create PR and merge using squash and merge"""
        
        # Get PR configuration
        pr_config = self.config.get_pr_config()
        
        if commits:
            # Build PR body with collaborator info
            collaborators = set()
            for commit in commits:
                collaborators.add(commit['collaborator'])
            
            pr_title = f"🤝 Collaborative PR with {len(collaborators)} contributors"
            pr_body = f"""## [PAIR_EXT] >> CO-PILOT ANALYSIS
            
Context: Collaborative development cycle for {len(collaborators)} contributors.
Observation: Branch {branch} successfully aggregated multi-user contributions.
Suggestion: Review the consolidated diff for logic consistency across peer commits.
Rationale: Ensuring that independent collaborator file changes align with project architectural bounds.

### 👥 Contributors
{chr(10).join([f'- {c}' for c in collaborators])}

### 🎥 Automation Logs
- **Total commits:** {len(commits)}
- **Merge method:** Squash and merge
"""
        else:
            pr_title = pr_config.get("title", "🚀 Auto PR Update")
            pr_body = f"""## [PAIR_EXT] >> CO-PILOT ANALYSIS

Context: Individual contribution cycle.
Observation: Targeted file modifications completed on branch {branch}.
Suggestion: Verify that the automated changes meet the repository's styling guidelines.
Rationale: Maintaining codebase health via consistent automated deployments.
"""

        # Create PR
        pr = self.github.create_pr(branch, pr_title, pr_body)

        # Add labels
        labels = pr_config.get("labels", ["automated"])
        if commits:
            labels.append("collaborative")
        self.github.add_labels(pr["number"], labels)

        # Merge using squash and merge
        self.github.merge_pr(pr["number"], method="squash")
        pair_ext_log(f"Merged PR #{pr['number']} successfully. Everything looks solid.", severity="SUGGEST")

        # Send notification
        self.notifier.send_notification(pr, "merged")

        return pr

    def run(self, mode="single"):
        """
        Execute the PR creation workflow
        
        Args:
            mode: "single" or "collaborator"
        """
        try:
            self.mode = mode
            
            if mode == "collaborator":
                branch, commits = self.run_collaborator_mode()
            else:
                branch, commits = self.run_single_user_mode()

            if not self.dry_run and branch:
                pr = self.create_and_merge_pr(branch, commits)
                self.session_prs += 1
                self.telemetry.report_final(total_prs_created=self.session_prs, session_prs=self.session_prs, mode=self.mode)
                return True
            elif self.dry_run:
                return True
            else:
                return False

        except Exception as e:
            logger.error(f"❌ Automation failed: {e}")
            try:
                self.notifier.send_error_notification(e, {"mode": mode})
            except:
                pass
            return False


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Auto PR Creator - Multi-collaborator support")
    parser.add_argument("--dry-run", action="store_true", help="Simulate operations without making changes")
    parser.add_argument("--config", type=str, default="config/config.json", help="Path to configuration file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    parser.add_argument("--mode", type=str, choices=["single", "collaborator"], default="single",
                       help="Run mode: single user or multi-collaborator")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    creator = AutoPRCreator(config_path=args.config, dry_run=args.dry_run)
    success = creator.run(mode=args.mode)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()