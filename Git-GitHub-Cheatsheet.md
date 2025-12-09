# Git & GitHub QUICK CHEAT SHEET

## EMERGENCY REFERENCE — Print & Keep Handy!

---

## 🚀 MOST USED COMMANDS (Master These First)

```bash
git status                    # Check what changed
git add .                     # Stage all changes
git commit -m "message"       # Save changes
git push origin main          # Upload to GitHub
git pull origin main          # Download updates
git log --oneline             # See commit history
```

---

## 📋 COMPLETE COMMAND REFERENCE

### INITIAL SETUP (One Time)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### START NEW PROJECT
```bash
mkdir project-name
cd project-name
git init                      # Create .git folder
git remote add origin https://github.com/user/repo.git
```

### CLONE EXISTING PROJECT
```bash
git clone https://github.com/user/repo.git
cd repo
```

---

## 📝 WORKFLOW: Daily Development

```bash
# 1. Check status
git status

# 2. Make changes to files (edit in VS Code or your editor)

# 3. See what changed
git diff

# 4. Stage changes
git add .
# OR specific file:
git add filename.txt

# 5. Commit
git commit -m "Clear, descriptive message"

# 6. Before pushing, pull latest
git pull origin main

# 7. Upload to GitHub
git push origin main

# 8. Verify on GitHub website ✓
```

---

## 🌿 BRANCHING WORKFLOW

```bash
# List all branches
git branch
git branch -a                 # Include remote branches

# Create new branch
git branch feature-name

# Switch to branch
git checkout feature-name

# Create & switch in one command
git checkout -b feature-name

# Delete branch (after merge)
git branch -d feature-name

# Force delete (careful!)
git branch -D feature-name
```

### MERGE WORKFLOW
```bash
# Switch to main
git checkout main

# Pull latest
git pull origin main

# Merge feature
git merge feature-name

# If conflicts:
#   1. Open conflicted file
#   2. Remove <<<<<<, =======, >>>>>>> markers
#   3. Keep correct code
#   4. git add filename
#   5. git commit -m "Merge feature-name"

# Push merged result
git push origin main
```

---

## 🔄 PULL REQUESTS (GitHub Collaboration)

```bash
# On feature branch, push your work
git checkout feature-name
git push origin feature-name

# On GitHub website:
# 1. Click "Create Pull Request"
# 2. Write description
# 3. Request reviewers
# 4. Wait for approval

# After merge on GitHub:
git checkout main
git pull origin main          # Get merged changes
git branch -d feature-name    # Cleanup
```

---

## 🚨 UNDO & FIX MISTAKES

### Undo Changes Before Commit
```bash
# See what changed
git status
git diff

# Undo ALL changes in one file
git restore filename

# Undo ALL changes in working directory
git restore .

# Unstage file (keep changes)
git restore --staged filename
```

### Undo Commits
```bash
# Undo last commit, keep changes
git reset HEAD~1

# Undo last commit, discard changes (CAREFUL!)
git reset --hard HEAD~1

# Create new commit that undoes changes (safer for shared code)
git revert HEAD

# View a specific commit
git show commit-hash
```

### Recover Lost Commits
```bash
# View all Git operations (recover anything!)
git reflog

# Go back to specific point in reflog
git reset --hard reflog-entry
```

---

## 📊 VIEW HISTORY & DETAILS

```bash
# Simple history
git log --oneline             # One line per commit

# Visual history
git log --graph --all --oneline

# Last N commits
git log -n 5

# Changes by author
git log --author="Name"

# Changes in specific file
git log filename

# See changes in specific commit
git show commit-hash

# Compare two commits
git diff commit1 commit2

# Who changed each line (blame)
git blame filename
```

---

## 🔀 ADVANCED: Stash, Cherry-Pick, Rebase

### STASH (Temporarily Save Work)
```bash
# Save changes without committing
git stash

# List stashed changes
git stash list

# Restore most recent stash
git stash pop

# Restore specific stash
git stash pop stash@{1}

# Delete stash
git stash drop
```

### CHERRY-PICK (Apply Specific Commit)
```bash
# Copy specific commit to current branch
git cherry-pick commit-hash

# If conflicts occur, resolve then:
git cherry-pick --continue
```

### REBASE (Clean History - Caution!)
```bash
# Rebase current branch on main
git rebase main

# Interactive rebase (last 3 commits)
git rebase -i HEAD~3

# If conflicts, fix then:
git rebase --continue

# Abort rebase
git rebase --abort
```

---

## 🌐 REMOTE MANAGEMENT

```bash
# List remotes
git remote -v

# Add remote
git remote add name url

# Remove remote
git remote remove name

# Rename remote
git remote rename old-name new-name

# Get updates without merging
git fetch origin

# Get updates and merge
git pull origin branch-name

# Upload to remote
git push origin branch-name

# Upload all branches
git push origin --all

# Delete remote branch
git push origin --delete branch-name
```

---

## 💾 CONFIGURATION

```bash
# View current config
git config --list

# Set config globally
git config --global user.name "Name"
git config --global user.email "email@example.com"

# Set config for this repo only
git config user.name "Name"
git config user.email "email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set default editor
git config --global core.editor "code"
```

---

## 🎯 COMMIT MESSAGE BEST PRACTICES

### FORMAT
```
Type: Brief description (50 chars max)

Optional detailed explanation here.
Explain WHY, not WHAT.

Closes #123
```

### TYPES
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation
- **style**: Formatting (not code logic)
- **refactor**: Code reorganization
- **perf**: Performance improvement
- **test**: Adding/updating tests
- **chore**: Build, dependencies, etc.

### EXAMPLES
```bash
git commit -m "feat: Add user login form"
git commit -m "fix: Correct cart total calculation"
git commit -m "docs: Add API documentation"
git commit -m "refactor: Extract validation logic"
```

---

## 🚨 COMMON SCENARIOS

### "I forgot to add a file to my last commit"
```bash
git add forgotten-file.txt
git commit --amend --no-edit
git push origin -f              # Force push (only on personal branches!)
```

### "I committed to wrong branch"
```bash
# Switch to correct branch
git checkout correct-branch

# Copy commit from other branch
git cherry-pick wrong-branch

# Delete commit from wrong branch
git checkout wrong-branch
git reset --hard HEAD~1
```

### "I need to start over"
```bash
# Delete all uncommitted changes
git clean -fd

# Reset to last commit
git reset --hard HEAD
```

### "Branch is behind, need to catch up"
```bash
git fetch origin
git rebase origin/main
# OR (if rebase is scary):
git merge origin/main
```

---

## 📱 GITHUB CLI (Optional)

```bash
# Create repo on GitHub from terminal
gh repo create

# List your repositories
gh repo list

# Create pull request
gh pr create

# View PR status
gh pr status

# Check PR reviews
gh pr review
```

---

## 🎓 LEARNING CHECKLIST

### Week 1: Basics
- [ ] git init
- [ ] git config (user name, email)
- [ ] git status
- [ ] git add
- [ ] git commit
- [ ] git log

### Week 2: Remote & GitHub
- [ ] Create GitHub account
- [ ] git clone
- [ ] git push
- [ ] git pull
- [ ] Create repo on GitHub

### Week 3: Branching
- [ ] git branch (create)
- [ ] git checkout (switch)
- [ ] git merge
- [ ] Handle merge conflicts
- [ ] Create pull request on GitHub

### Week 4: Fixing Mistakes
- [ ] git restore
- [ ] git reset
- [ ] git revert
- [ ] git reflog

### Week 5+: Advanced (Optional)
- [ ] git stash
- [ ] git cherry-pick
- [ ] git rebase
- [ ] Working with multiple remotes
- [ ] GitHub Actions / CI-CD basics

---

## ⚠️ DANGEROUS COMMANDS (Use Carefully!)

```bash
git reset --hard                # Loses all changes forever
git push origin -f              # Rewrites remote history (breaks team collaboration)
git rebase master               # Rewrites commits (don't use on shared branches)
git clean -fd                   # Deletes untracked files permanently
```

**Golden Rule**: Never use `-f` (force) unless you're 100% sure and working alone.

---

## 🆘 HELP COMMANDS

```bash
git help                        # General help
git help add                    # Help for specific command
git add --help                  # Alternate format

# Search stack overflow
# Google: "how to [your question] git"
# Or: "how to [your question] github"
```

---

## 📍 KEY CONCEPTS AT A GLANCE

| Concept | What It Is | Why You Care |
|---------|-----------|-------------|
| **Commit** | A snapshot of code | Permanent record of changes |
| **Branch** | Isolated copy | Work without breaking main code |
| **Remote** | GitHub version | Backup + collaborate with team |
| **Staging** | Middle step | Choose exactly what to commit |
| **Pull Request** | Proposed change | Team review before merging |
| **Merge** | Combine branches | Integrate features into main |
| **Conflict** | Git can't merge automatically | Manual resolution needed |
| **Stash** | Temporary save | Switch branches without committing |

---

## 🎯 REMEMBER

1. **Status Check First**: Always run `git status` before doing anything
2. **Pull Before Push**: Never push without pulling first (unless starting new project)
3. **Commit Often**: Small commits > big ones
4. **Clear Messages**: Write messages your future self understands
5. **Branch for Everything**: Never push directly to main
6. **Practice Daily**: The only way to master Git is hands-on use

---

## 💡 QUICK DECISION MAKER

```
What do you want to do?        Command to use
──────────────────────────────────────────────────
Check status                   git status
See what changed               git diff
Save changes                   git add . && git commit -m "msg"
Send to GitHub                 git push origin main
Get latest from GitHub         git pull origin main
Create feature branch          git checkout -b feature-name
Switch branches                git checkout branch-name
Merge feature to main          git merge feature-name
Fix a mistake                  git restore filename
View history                   git log --oneline
Start new project              git init
Copy existing project          git clone url
Undo last commit               git reset HEAD~1
Recover lost commit            git reflog
```

---

## 📞 STILL STUCK?

1. **Check status**: `git status`
2. **See history**: `git log --oneline`
3. **Search error message**: Copy-paste into Google
4. **Stack Overflow**: Search Git + your question
5. **GitHub Docs**: https://docs.github.com/
6. **Git Docs**: https://git-scm.com/docs
7. **Ask teammate**: Pair programming helps

---

**Version**: 1.0 | Last Updated: Dec 2025 | For Learning & Practice