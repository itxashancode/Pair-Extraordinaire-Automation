# 🤝 Pair Extraordinaire Automation

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Pair%20Extraordinaire%20Automation&fontSize=42&fontAlignY=30&animation=twinkling&fontColor=fff)

[![Typing Animation](https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=Automate+Your+GitHub+Co-Authoring;Sequential+%26+Parallel+Modes;Multi-Token+Management;Earn+Pair+Extraordinaire+Badge)](https://readme-typing-svg.demolab.com)

[![Features](https://img.shields.io/badge/Features-Explore-blue?style=for-the-badge&logo=github)](#-features)
[![Install](https://img.shields.io/badge/Install-Quick%20Start-green?style=for-the-badge&logo=python)](#-installation)
[![Usage](https://img.shields.io/badge/Usage-Guide-orange?style=for-the-badge&logo=readme)](#-usage)
[![Contribute](https://img.shields.io/badge/Contribute-Welcome-red?style=for-the-badge&logo=git)](#-contributing)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub CLI](https://img.shields.io/badge/GitHub_CLI-Required-black.svg?style=for-the-badge&logo=github)](https://cli.github.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)](https://github.com)

---

## ⚠️ Educational Purpose Only

[![Educational](https://img.shields.io/badge/⚠️-Educational_Purpose_Only-red?style=for-the-badge)](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)

This tool is designed for **educational purposes** to understand GitHub automation, co-authoring workflows, and API integration. Use responsibly and in accordance with GitHub's Terms of Service.

---

## 🏆 Earn Your Pair Extraordinaire Badge

![Pair Extraordinaire Badge](https://github.com/drknzz/GitHub-Achievements/raw/main/Media/Badges/Pair-Extraordinaire/PNG/PairExtraordinaire.png)

|  |  |  |  |
| --- | --- | --- | --- |
| **Default** 1 PR | **Bronze** 10 PRs | **Silver** 24 PRs | **Gold** 48 PRs |

*Automate co-authored PR creation and merging to unlock all achievement tiers!*

---

## 🎯 What Is Pair Extraordinaire Automation?

A **powerful Python automation framework** that streamlines GitHub co-authored Pull Request workflows at scale. Perfect for developers who want to:

| 🎯 Use Case | 📊 Benefit |
| --- | --- |
| **Co-authored Commits** | Automatic `Co-authored-by` trailers on every commit |
| **Badge Hunting** | Earn GitHub Pair Extraordinaire badge efficiently |
| **Batch Documentation** | Update files across multiple branches with a collaborator |
| **CI/CD Testing** | Stress-test co-authoring automation pipelines |
| **Learning & Research** | Study GitHub automation patterns and workflows |

---

## 📑 Table of Contents

| [🌟 Features](#-features) | [🏗️ Architecture](#%EF%B8%8F-architecture) | [📦 Installation](#-installation) | [⚙️ Configuration](#%EF%B8%8F-configuration) |
| --- | --- | --- | --- |
| [🚀 Usage](#-usage) | [🔧 Components](#-components-deep-dive) | [🔐 Security](#-security--best-practices) | [🐛 Troubleshooting](#-troubleshooting) |
| [📈 Optimization](#-performance-tips) | [🤝 Contributing](#-contributing) | [📄 License](#-license) | [📞 Support](#-support--community) |

---

## 🌟 Features

|  |  |
| --- | --- |
| 🎯 Core Capabilities ![Core](https://img.shields.io/badge/Automation-Core-blue?style=flat-square) | 🔧 Advanced Features ![Advanced](https://img.shields.io/badge/Advanced-Pro-green?style=flat-square) |
| `✅ Automated Co-authored PRs` `└─ Auto Co-authored-by trailer` `✅ Smart Auto-Merge` `└─ Intelligent PR merging` `✅ Dual Execution Modes` `└─ Sequential & Parallel` `✅ State Management` `└─ Resume from interruptions` `✅ Dry Run Mode` `└─ Test without real commits` | `✅ Multi-Token Rotation` `└─ Automatic token switching` `✅ Discord/Slack Webhooks` `└─ Real-time notifications` `✅ Rate Limit Handling` `└─ Smart API throttling` `✅ Exponential Backoff` `└─ Intelligent retry logic` `✅ Template-based Commits` `└─ Customizable messages` |

---

## 🎬 How It Works

```
graph TB
    Start([🚀 Start Automation]) --> Config[📋 Load Config & .env]
    Config --> Mode{🔀 Choose Mode}
    Mode -->|Sequential| Seq[📝 run.py]
    Mode -->|Parallel| Par[⚡ Parallel Workers]
    Seq --> Git[🔧 Git Operations]
    Par --> Git
    Git --> Branch[🌿 Create Branch]
    Branch --> Commit[💾 Co-authored Commit]
    Commit --> Push[📤 Push to Remote]
    Push --> PR[🎯 Create PR]
    PR --> AutoMerge{🤖 Auto-merge?}
    AutoMerge -->|Yes| Merge[✅ Merge PR]
    AutoMerge -->|No| Next{📊 More PRs?}
    Merge --> Next
    Next -->|Yes| Git
    Next -->|No| Notify[📢 Send Notifications]
    Notify --> End([🎉 Complete!])
```

---

## 🏗️ Architecture

### System Design Overview

[![Architecture](https://img.shields.io/badge/Architecture-Microservices-blueviolet?style=for-the-badge&logo=architecture)](https://github.com/itxashancode/Pair-Extraordinaire)

```
┌─────────────────────────────────────────────────────────────────┐
│               🤝 Pair Extraordinaire Automation                  │
│                     Core Orchestration Layer                     │
└─────────────────────────────────────────────────────────────────┘
                                │
                ┌───────────────┴───────────────┐
                │                               │
        ┌───────▼────────┐            ┌────────▼───────┐
        │  📝 Sequential │            │  ⚡ Parallel   │
        │    run.py      │            │   src/async    │
        │   Reliable     │            │   Fast Mode    │
        └───────┬────────┘            └────────┬───────┘
                │                              │
                └──────────────┬───────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
   ┌────▼─────┐         ┌─────▼────┐         ┌──────▼──────┐
   │ 🔧 src/  │         │ ⚙️ config│         │ 📄 templates│
   │ Core Bot │         │ Settings │         │  Commit Msg │
   └────┬─────┘         └─────┬────┘         └──────┬──────┘
        │                     │                      │
        └─────────────────────┼──────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
        ┌─────▼─────┐  ┌─────▼─────┐  ┌─────▼─────┐
        │ 🔑 Token  │  │ 📢 Notify │  │ 📝 Logger │
        │ Manager   │  │ Webhooks  │  │  System   │
        └───────────┘  └───────────┘  └───────────┘
```

### 🔑 Component Matrix

| Component | Role | Features |
| --- | --- | --- |
| **run.py** | 📝 Entry Point | Bootstraps automation, loads config |
| **src/** | 🔧 Core Logic | Branch, commit, push, PR, merge |
| **config/** | ⚙️ Settings | JSON/env-based configuration |
| **templates/** | 📄 Templates | Commit messages & PR body templates |
| **.env** | 🔑 Secrets | GitHub tokens & co-author credentials |

---

## 📦 Installation

### 🚀 Quick Start Guide

[![Setup Time](https://img.shields.io/badge/Setup_Time-5_Minutes-brightgreen?style=for-the-badge)](https://github.com/itxashancode/Pair-Extraordinaire)

### Prerequisites Checklist

```
✅ Python 3.8 or higher
✅ Git 2.0 or higher
✅ GitHub CLI (gh)
✅ Active GitHub account
✅ A collaborator account (for co-authoring)
✅ Write access to target repository
```

---

### Step 1️⃣: Clone Repository

**📥 Download the Code**

```bash
# Clone via HTTPS
git clone https://github.com/itxashancode/Pair-Extraordinaire.git

# Or clone via SSH
git clone git@github.com:itxashancode/Pair-Extraordinaire.git

# Navigate to directory
cd Pair-Extraordinaire
```

---

### Step 2️⃣: Install Dependencies

**🐍 Python Packages**

```bash
# Install all required packages
pip install -r requirements.txt

# Or use pip3 on some systems
pip3 install -r requirements.txt
```

**📦 What Gets Installed:**

| Package | Purpose |
| --- | --- |
| `requests` | HTTP/API calls |
| `gitpython` | Git automation |
| `python-dotenv` | Load `.env` variables |
| `colorama` | Terminal colors |
| `aiohttp` | Async HTTP (parallel mode) |

---

### Step 3️⃣: Install GitHub CLI

**🍎 macOS**

```bash
brew install gh && gh --version
```

**🐧 Linux (Debian/Ubuntu)**

```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
  sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] \
  https://cli.github.com/packages stable main" | \
  sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

sudo apt update && sudo apt install gh -y
gh --version
```

**🪟 Windows**

```bash
winget install --id GitHub.cli
# Or: choco install gh
gh --version
```

---

### Step 4️⃣: Authenticate GitHub

**🔐 Login to GitHub**

```bash
# Start authentication
gh auth login

# Follow the interactive prompts:
# 1. Choose: GitHub.com
# 2. Protocol: HTTPS
# 3. Authenticate Git: Yes
# 4. Method: Login with a web browser

# Verify authentication
gh auth status
```

**Expected Output:**

```
✓ Logged in to github.com as YourUsername
✓ Git operations for github.com configured to use https protocol.
✓ Token: *******************
```

---

### ✅ Installation Complete!

**Ready to configure? Proceed to [⚙️ Configuration](#%EF%B8%8F-configuration)**

---

## ⚙️ Configuration

### 🎛️ Setup Your Automation

[![Config](https://img.shields.io/badge/Configuration-3_Files-orange?style=for-the-badge)](https://github.com/itxashancode/Pair-Extraordinaire)

---

### 📋 File 1: Environment Variables (`.env`)

```bash
cp .env.example .env
```

```env
# GitHub credentials
GITHUB_TOKEN=your_personal_access_token_here

# Repository details
REPO_OWNER=your_github_username
REPO_NAME=your_repository_name

# Co-author details (required for Pair Extraordinaire)
CO_AUTHOR_NAME=Collaborator Name
CO_AUTHOR_EMAIL=collaborator@email.com
CO_AUTHOR_TOKEN=collaborator_github_token

# Notification webhooks (optional)
DISCORD_WEBHOOK=https://discord.com/api/webhooks/YOUR_WEBHOOK_HERE
SLACK_WEBHOOK=https://hooks.slack.com/services/YOUR_WEBHOOK_HERE
```

**📖 Configuration Reference:**

| Variable | Required | Description |
| --- | --- | --- |
| `GITHUB_TOKEN` | ✅ Yes | Your GitHub Personal Access Token |
| `REPO_OWNER` | ✅ Yes | GitHub username or org of the target repo |
| `REPO_NAME` | ✅ Yes | Name of the target repository |
| `CO_AUTHOR_NAME` | ✅ Yes | Display name of your co-author |
| `CO_AUTHOR_EMAIL` | ✅ Yes | Email used by co-author on GitHub |
| `CO_AUTHOR_TOKEN` | ⚠️ Optional | Co-author token for mutual achievements |
| `DISCORD_WEBHOOK` | ❌ Optional | Discord channel webhook URL |
| `SLACK_WEBHOOK` | ❌ Optional | Slack channel webhook URL |

---

### 📋 File 2: Main Config (`config/`)

```json
{
  "repo_path": ".",
  "base_branch": "main",
  "target_file": "README.md",
  "pr_count": 50,
  "delay_seconds": 15,
  "auto_merge": true,
  "dry_run": false,
  "max_retries": 3
}
```

**📖 Configuration Reference:**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `repo_path` | string | `"."` | Path to your Git repository |
| `base_branch` | string | `"main"` | Target branch for PRs |
| `target_file` | string | `"README.md"` | File modified in each commit |
| `pr_count` | integer | `50` | Total co-authored PRs to create |
| `delay_seconds` | integer | `15` | Wait time between PRs |
| `auto_merge` | boolean | `true` | Automatically merge created PRs |
| `dry_run` | boolean | `false` | Test mode — no actual changes |
| `max_retries` | integer | `3` | Retry attempts on failure |

---

### 📋 File 3: Commit Templates (`templates/`)

The `templates/` directory contains message templates for commits and PR bodies. Every co-authored commit automatically appends the required trailer:

```
feat: automated update #{pr_number}

This is an automated co-authored commit.

Co-authored-by: {co_author_name} <{co_author_email}>
```

GitHub detects the `Co-authored-by` trailer and awards the badge to **both users** upon merge.

---

### 🔔 Optional: Webhook Setup

**💬 Discord Webhook**

1. Discord Server → Settings → Integrations → Webhooks → New Webhook
2. Name it, select a channel, copy the URL
3. Paste into `.env` as `DISCORD_WEBHOOK`

```bash
# Test your webhook
curl -X POST "YOUR_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"content": "Test from Pair Extraordinaire!"}'
```

**💼 Slack Webhook**

1. Visit [api.slack.com/apps](https://api.slack.com/apps) → New App → Incoming Webhooks
2. Activate, add to workspace, select channel, copy URL
3. Paste into `.env` as `SLACK_WEBHOOK`

---

### ✅ Configuration Complete!

[![Ready](https://img.shields.io/badge/Status-Ready_to_Run-success?style=for-the-badge)](https://github.com/itxashancode/Pair-Extraordinaire)

**Next: [🚀 Usage Guide](#-usage)**

---

## 🚀 Usage

### 🎮 Command Center

---

### 🏁 Quick Start Commands

```bash
# 1️⃣ Basic sequential run
python run.py

# 2️⃣ Test without creating PRs
python run.py --dry-run

# 3️⃣ Custom PR count
python run.py --count 50

# 4️⃣ Resume after interruption
python run.py  # Auto-resumes from state file
```

---

### 📘 Sequential Mode (`run.py`)

```bash
python run.py [OPTIONS]
```

[![Sequential](https://img.shields.io/badge/Mode-Sequential-blue?style=for-the-badge)](https://github.com/itxashancode/Pair-Extraordinaire)

**⭐ Best For:** Reliability, debugging, smaller PR counts

| Option | Description | Example |
| --- | --- | --- |
| `--count N` | Override PR count | `python run.py --count 50` |
| `--delay N` | Seconds between PRs | `python run.py --delay 30` |
| `--dry-run` | Test mode (no commits) | `python run.py --dry-run` |
| `--no-merge` | Disable auto-merge | `python run.py --no-merge` |
| `--reset` | Start from PR #1 | `python run.py --reset` |

**📊 Example Output:**

```
🚀 Starting Pair Extraordinaire Automation from PR #1
⏱️  Delay: 15 seconds

🔹 Processing PR #1
  ├─ 🌿 Created branch: pair-auto-1-a1b2c3d4
  ├─ 💾 Committed with Co-authored-by trailer
  ├─ 📤 Pushed to remote
  └─ ✅ PR #101 created successfully

✅ PR #101 merged — both users credited
⏱️  Waiting 15 seconds...

🔹 Processing PR #2
...
```

---

### 📚 Usage Examples

**Example 1: Default Badge (1 PR)**

**Goal:** Earn the default Pair Extraordinaire badge

```bash
# Test with dry run first
python run.py --count 2 --dry-run

# Run actual automation
python run.py --count 2 --delay 10
```

**Output:**

```
🚀 Starting from PR #1

✅ PR #1-2 created and merged successfully
🎉 Default Pair Extraordinaire Badge unlocked!
```

---

**Example 2: Bronze Badge (10 PRs)**

**Goal:** Earn Bronze Pair Extraordinaire Badge

```bash
python run.py --count 12 --delay 15
# Expected time: ~3 minutes
```

**Output:**

```
🚀 Starting automation

📈 12/12 PRs complete

🎉 Bronze Pair Extraordinaire Badge unlocked!
⏱️ Completed in 3 minutes 1 second
```

---

**Example 3: Gold Badge (48 PRs)**

**Goal:** Earn Gold Pair Extraordinaire Badge

```bash
python run.py --count 50 --delay 10
# Expected time: ~8-10 minutes
```

**Output:**

```
🚀 Starting automation

📈 50/50 PRs complete ✓ 48 merged ✗ 2 retried

🎉🎉🎉 GOLD PAIR EXTRAORDINAIRE UNLOCKED! 🎉🎉🎉
⏱️ Completed in 8 minutes 45 seconds
```

---

**Example 4: Resume After Interruption**

**Scenario:** Process interrupted at PR #22

```bash
# Check current state
cat state.json
# Output: {"last_completed_pr": 22}

# Resume automatically
python run.py --count 50
# Continues from PR #23
```

---

**Example 5: Dry Run Testing**

**Goal:** Test configuration without creating real PRs

```bash
python run.py --count 5 --dry-run
```

**Output:**

```
🔍 DRY RUN MODE - No actual commits

🔹 PR #1 Simulation
  📝 Would create branch: pair-auto-1-abc123
  📝 Would modify: README.md
  📝 Would commit with Co-authored-by trailer
  📝 Would push to: origin/pair-auto-1-abc123
  📝 Would create PR: "Automated Co-authored PR #1"
  ✅ Simulation successful

✅ All 5 PRs simulated successfully
```

---

### 💡 Pro Tips

| | |
| --- | --- |
| 🎯 **Tip 1** | Always start with `--dry-run` to validate your config |
| 🤝 **Tip 2** | Make sure your co-author's email matches their GitHub account |
| 🔄 **Tip 3** | State files allow safe resuming after any interruption |
| 📊 **Tip 4** | Monitor rate limits with `gh api rate_limit` |
| ⚡ **Tip 5** | Lower `delay_seconds` for faster runs (minimum ~10s recommended) |

---

## 🔧 Components Deep Dive

### 🏗️ System Architecture Breakdown

---

### 1️⃣ Entry Point (`run.py`)

[![](https://img.shields.io/badge/Entry-Point-F05032?style=for-the-badge&logo=python&logoColor=white)](https://github.com/itxashancode/Pair-Extraordinaire)

**🎯 Purpose:** Bootstrap the automation, load configuration, and invoke the core pipeline

**🔑 Responsibilities:**

```python
# run.py high-level flow
def main():
    config = load_config()            # Load config/ and .env
    state  = load_state()             # Resume support

    for pr_num in range(start, total):
        branch = create_branch(pr_num)
        commit_with_coauthor(branch)   # Appends Co-authored-by
        push(branch)
        pr_id = create_pr(branch)
        if config.auto_merge:
            merge_pr(pr_id)
        save_state(pr_num)
        notify(pr_num)
        sleep(config.delay_seconds)
```

---

### 2️⃣ Source Modules (`src/`)

[![](https://img.shields.io/badge/Core-Modules-4CAF50?style=for-the-badge&logo=python&logoColor=white)](https://github.com/itxashancode/Pair-Extraordinaire)

**🎯 Purpose:** Core bot logic — Git operations, GitHub API calls, PR management

**✨ Key Features:**

| Module | Role |
| --- | --- |
| Git Manager | Branch creation, co-authored commits, push |
| GitHub Tool | PR create, merge, rate-limit handling |
| Token Manager | Token rotation for higher throughput |
| State Manager | Persist progress for resumable runs |

**🔑 Co-authored Commit Format:**

```bash
git commit -m "Automated update #1

Co-authored-by: Collaborator Name <collaborator@email.com>"
```

GitHub detects the `Co-authored-by` trailer and credits both users, triggering the Pair Extraordinaire badge upon merge.

**✨ Features:**

| | |
| --- | --- |
| ⏱️ **Exponential Backoff** | Retry delays: 5s → 10s → 20s |
| 🌐 **Internet Check** | Validates connection before operations |
| 🔁 **Auto-Retry** | Configurable attempts (default: 3) |
| ⏲️ **Timeout Protection** | 30-second command timeout |

---

### 3️⃣ Configuration (`config/`)

[![](https://img.shields.io/badge/Config-Management-FF9800?style=for-the-badge&logo=gear&logoColor=white)](https://github.com/itxashancode/Pair-Extraordinaire)

**🎯 Purpose:** Centralize all settings, making the bot easy to tune without editing source code

**Key responsibilities:**
- Load and validate JSON settings
- Merge with environment variables from `.env`
- Provide defaults for all optional values

---

### 4️⃣ Templates (`templates/`)

[![](https://img.shields.io/badge/Templates-Messages-9C27B0?style=for-the-badge&logo=markdown&logoColor=white)](https://github.com/itxashancode/Pair-Extraordinaire)

**🎯 Purpose:** Store reusable commit message and PR body templates

**Example Template:**

```
feat: automated update #{pr_number}

This is an automated co-authored commit for demonstration purposes.

Co-authored-by: {co_author_name} <{co_author_email}>
```

Templates make it easy to customize the message format without touching core code.

---

### 5️⃣ Notifications

[![](https://img.shields.io/badge/Notifications-Discord+Slack-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/itxashancode/Pair-Extraordinaire)

**🎯 Purpose:** Send real-time updates to Discord or Slack on automation progress

**🎨 Notification Types:**

| Level | Color | Use Case |
| --- | --- | --- |
| `info` | 🔵 Blue | Progress updates |
| `success` | 🟢 Green | PR created/merged |
| `warning` | 🟡 Yellow | Non-critical errors |
| `error` | 🔴 Red | Critical failures |

**📨 Example Notification:**

```
✅ PR #25 created and merged successfully
Branch: pair-auto-25-xyz
Co-author: CollaboratorName
Speed: 3.8 PRs/min
```

---

## 🔐 Security & Best Practices

### 🛡️ Keep Your Tokens Safe

[![](https://img.shields.io/badge/Security-Critical-red?style=for-the-badge&logo=shield&logoColor=white)](https://github.com/itxashancode/Pair-Extraordinaire)

---

### 🔒 Token Security Checklist

| | | |
| --- | --- | --- |
| ✅ | **Never commit `.env` to Git** | `.env` is in `.gitignore` by default |
| ✅ | **Use environment variables** | `export GITHUB_TOKEN="ghp_xxx"` |
| ✅ | **Rotate tokens regularly** | Every 30–90 days |
| ✅ | **Use fine-grained tokens** | Limit scope to specific repos |
| ✅ | **Enable 2FA** | Extra security layer on your account |
| ✅ | **Monitor token usage** | `gh api rate_limit` |

---

### 🔑 How to Generate GitHub Tokens

**Step-by-Step Guide:**

1. **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. Click **"Generate new token (classic)"**
   - Name: `Pair Extraordinaire Automation`
   - Expiration: `90 days`
3. **Select required scopes:** ✅ `repo` ✅ `workflow`
4. Click **"Generate token"** — copy immediately (shown only once!)
5. Add to `.env` as `GITHUB_TOKEN`

**📊 Rate Limits:**

| Authentication | Requests/Hour | Notes |
| --- | --- | --- |
| Unauthenticated | 60 | Very limited |
| OAuth Token | 5,000 | Per token |
| Multiple Tokens (rotated) | 10,000+ | Automatic rotation |

---

## 🐛 Troubleshooting

### 🔧 Common Issues & Solutions

[![](https://img.shields.io/badge/Support-Community-blue?style=for-the-badge&logo=github)](https://github.com/itxashancode/Pair-Extraordinaire/issues)

---

### ❌ Issue 1: "gh: command not found"

**📋 Problem:** GitHub CLI is not installed or not in PATH.

**✅ Solution:**

```bash
# macOS
brew install gh

# Linux
sudo apt update && sudo apt install gh -y

# Windows
winget install --id GitHub.cli

# Verify
gh --version
```

---

### ❌ Issue 2: "Authentication failed"

**📋 Problem:** GitHub CLI not authenticated or token expired.

**✅ Solution:**

```bash
gh auth login
# Or use token directly
echo "YOUR_TOKEN" | gh auth login --with-token
gh auth status
```

---

### ❌ Issue 3: "API rate limit exceeded"

**📋 Problem:** Too many API requests in a short time.

**✅ Solutions:**

```bash
# Check current rate limit
gh api rate_limit

# Increase delay in config
"delay_seconds": 60

# Add a second token to .env or config
```

---

### ❌ Issue 4: "Failed to push branch"

**📋 Problem:** Git push fails due to network or permissions.

**✅ Solutions:**

```bash
# Check connection
ping github.com

# Verify repository permissions
gh repo view --web

# Re-authenticate
gh auth refresh
```

---

### ❌ Issue 5: "Co-authored-by not recognized"

**📋 Problem:** Badge not awarded — co-author email doesn't match a GitHub account.

**✅ Solution:**

- Ensure `CO_AUTHOR_EMAIL` exactly matches the email in the co-author's GitHub account settings
- The email must be associated with their GitHub profile (set as public or verified)

---

### ❌ Issue 6: "No changes to commit"

**📋 Problem:** File already contains identical content.

**✅ Solutions:**

```bash
# Reset state and start fresh
python run.py --reset

# Or change the target file in config
"target_file": "CONTRIBUTING.md"
```

---

### 🔍 Enable Debug Mode

```bash
export LOG_LEVEL=DEBUG
python run.py
```

**Debug Output Example:**

```
DEBUG - Loaded config: pr_count=50, delay=15s
DEBUG - Co-author: CollaboratorName <email@example.com>
DEBUG - Executing: git push origin pair-auto-1-abc123
DEBUG - Command output: [SUCCESS]
DEBUG - PR created: #101
DEBUG - Merged PR #101 successfully
```

---

## 📈 Performance Tips

### ⚡ Maximize Your Speed

[![](https://img.shields.io/badge/Optimization-Guide-orange?style=for-the-badge&logo=speedtest)](https://github.com/itxashancode/Pair-Extraordinaire)

---

### 🚀 Speed Optimization Matrix

| Strategy | Impact | Difficulty | Implementation |
| --- | --- | --- | --- |
| **Reduce delay** | ⭐⭐⭐⭐ | 🟢 Easy | `--delay 10` |
| **Multiple tokens** | ⭐⭐⭐⭐ | 🟢 Easy | Add tokens to config |
| **Stable network** | ⭐⭐⭐ | 🟡 Medium | Use wired connection |
| **SSD storage** | ⭐⭐ | 🔴 Hard | Run on SSD drive |

---

### 📊 Benchmarks

**Test 1: Default Badge (2 PRs)**

```
⏱️  Time: ~30 seconds
✅ Success: 2/2 PRs
📈 Speed: ~4 PRs/min
```

**Test 2: Bronze Badge (10 PRs)**

```
⏱️  Time: ~3 minutes
✅ Success: 10/10 PRs
📈 Speed: ~3.5 PRs/min
```

**Test 3: Gold Badge (48 PRs)**

```
⏱️  Time: ~10 minutes
✅ Success: 46/48 PRs
🔁 Retries: 3 operations
📈 Speed: ~4.8 PRs/min
```

---

## 🤝 Contributing

### 💪 Join the Community

[![](https://img.shields.io/badge/Contributors-Welcome-brightgreen?style=for-the-badge&logo=github)](https://github.com/itxashancode/Pair-Extraordinaire)

---

### 🚀 How to Contribute

```bash
# 1️⃣ Fork the repository
gh repo fork itxashancode/Pair-Extraordinaire

# 2️⃣ Clone your fork
git clone https://github.com/YOUR_USERNAME/Pair-Extraordinaire.git
cd Pair-Extraordinaire

# 3️⃣ Create feature branch
git checkout -b feature/amazing-feature

# 4️⃣ Make your changes

# 5️⃣ Commit with conventional commits
git commit -m "feat: add amazing feature"

# 6️⃣ Push to your fork
git push origin feature/amazing-feature

# 7️⃣ Create Pull Request
gh pr create --title "Add amazing feature" --body "Description..."
```

---

### 📝 Code Style Guide

```python
# ✅ Good — Clear, documented, typed
def commit_with_coauthor(branch: str, pr_number: int) -> bool:
    """
    Create a co-authored commit on the given branch.

    Args:
        branch: Branch name to commit on
        pr_number: PR sequence number for the commit message

    Returns:
        True if successful, False otherwise
    """
    try:
        message = build_commit_message(pr_number)
        return git.commit(branch, message)
    except Exception as e:
        logger.error(f"Commit failed: {e}")
        return False

# ❌ Bad — Unclear, no types, no docs
def doCommit(b, n):
    return git.commit(b, buildMsg(n))
```

**🎨 Formatting Tools:**

```bash
# Auto-format with black
black *.py

# Check style with flake8
flake8 *.py

# Type checking with mypy
mypy *.py
```

---

### 🐛 Reporting Bugs

Found a bug? Help us fix it!

**Steps:**
1. Check existing issues
2. Create a new issue with the template
3. Include: OS & Python version, full error message, steps to reproduce, expected vs actual behavior

---

## 📄 License

### MIT License

[![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

```
MIT License

Copyright (c) 2026 Pair Extraordinaire Automation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Acknowledgments

### 🌟 Built With Amazing Tools

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub CLI](https://img.shields.io/badge/GitHub_CLI-181717?style=for-the-badge&logo=github&logoColor=white)](https://cli.github.com/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/)
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://slack.com/)

### 💖 Special Thanks

* **GitHub** — For excellent CLI and API tooling
* **Python Community** — For amazing open-source libraries
* **Contributors** — Everyone who improved this project
* **You** — For using Pair Extraordinaire Automation!

---

## 📞 Support & Community

| [📖 Docs](https://github.com/itxashancode/Pair-Extraordinaire/wiki) | [🐛 Issues](https://github.com/itxashancode/Pair-Extraordinaire/issues) |
| --- | --- |
| [💬 Discussions](https://github.com/itxashancode/Pair-Extraordinaire/discussions) | [👤 Profile](https://github.com/itxashancode) |

---

## 🎉 Final Words

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=150&section=footer&text=Happy%20Co-Authoring!&fontSize=40&fontColor=fff&animation=twinkling)

### 🤝 Unleash the Pair Extraordinaire! 🤝

> *Co-author smarter. Earn your badge. Ship together.*

---

<div align="center">

Made with ❤️ by [itxashancode](https://github.com/itxashancode) · [linktr.ee/itxashanvibes](https://linktr.ee/itxashanvibes)

⭐ Star this repo if you found it helpful!

</div>

# Auto-updated on 2026-04-18 22:50:42

# Auto-updated on 2026-04-18 22:57:01

# Auto-updated on 2026-04-18 23:03:52

# Auto-updated on 2026-04-18 23:11:53

# Auto-updated on 2026-04-18 23:12:50

# Auto-updated on 2026-04-18 23:28:01
