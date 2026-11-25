# Mission 6 — Git and GitHub

## Task 6.1 — Understand the basic Git workflow

### Commands Used
```bash
git status
git add mission-06-git-github/README.md
git commit -m "Document basic Git workflow in Mission 6"
git log -n 5
```

### Git Operations Table

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status** (`git status`) | Shows which files have been modified, which are staged for the next commit, and which are untracked. |
| **Stage selected changes** (`git add <file>`) | Places specific modified or new files into the staging area so they are ready to be saved in the next snapshot. |
| **Create a commit** (`git commit -m "message"`) | Permanently saves a snapshot of all staged changes into the local repository history along with a descriptive message. |
| **View commit history** (`git log`) | Displays a chronological list of past commits, including their commit IDs, authors, dates, and messages. |

### Difference Between Staging and Committing
**Staging (`git add`)** prepares and selects specific file changes to be included in an upcoming snapshot without recording them yet—letting you review or group related edits together. **Committing (`git commit`)** takes everything currently in the staging area and permanently records it as a saved version in the repository's history.

---

## Task 6.2 — Create and use a branch

### Commands Used
```bash
git checkout -b update-about
git status
git add README.md
git commit -m "Add My Learning section to root README"
git push -u origin update-about
```

* Created the `update-about` branch, added the **"My Learning"** section to the root `README.md`, committed the update, and published the new branch to GitHub.

---

## Task 6.3 — Create a Pull Request

* **Pull Request Activity:** Opened a Pull Request on GitHub comparing `update-about` -> `main` with a summary of the `README.md` learning update. *(Status: Open / Merged as instructed — visible on GitHub).*
* **What a branch and a Pull Request are, and why they are useful:**
  A **branch** is an independent line of development that lets you work on new features or edits safely without breaking the main working codebase. A **Pull Request (PR)** is a formal proposal on GitHub asking to merge changes from one branch into another. Together, they are essential for teamwork because multiple people can work on different tasks simultaneously, review each other's code, discuss changes, and test everything before merging into `main`.

---

## Task 6.4 — Build your Git command glossary

| Git Operation | Command | One-Line Explanation in My Own Words |
| :--- | :--- | :--- |
| **Initialise a repository** | `git init` | Turns a regular local folder into a brand-new Git repository so Git can track its history. |
| **Check status** | `git status` | Displays the current branch and lists any modified, staged, or untracked files. |
| **Stage changes** | `git add <file>` | Adds chosen file changes to the staging area in preparation for the next commit. |
| **Commit changes** | `git commit -m "msg"` | Saves a permanent snapshot of staged changes to the local Git history with a note. |
| **View history** | `git log` | Shows the log of previous commits made in the repository. |
| **Create or list branches** | `git branch` | Lists all existing local branches, or creates a new branch when followed by a branch name. |
| **Switch branches** | `git checkout <branch>` / `git switch <branch>` | Moves your working directory from the current branch to another specified branch. |
| **Publish changes** | `git push` | Uploads your local branch commits to a remote repository like GitHub. |
| **Retrieve remote changes** | `git pull` | Downloads and merges the latest changes from the remote GitHub repository into your local branch. |

---

## Reflection & Challenges Faced
* **Summary:** Practised the full Git and GitHub collaboration workflow—staging and committing locally, creating a feature branch (`update-about`), pushing to GitHub, and opening a Pull Request.
* **Challenges:** Remembering to switch back to the `main` branch (`git checkout main`) after pushing `update-about` so future mission work stays on the right branch.
