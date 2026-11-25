# Mission 0 — Create your GitHub workspace
# Mission 0 — Create your GitHub workspace

## Task Completed & Repository Name
* **Task:** Created the local project workspace, set up the complete mission folder and file structure, initialized Git, and published the repository to GitHub.
* **Repository Name:** `digital-detective-8534`

---

## Tools Checked & Versions
Verified the required tools in Terminal before starting the missions:
* **Python:** `Python 3.14.7` *(checked using `python3 --version`)*
* **Git:** `git version 2.50.1` *(checked using `git --version`)*

---

## Folders and Files Created
Created the following project structure inside the root repository folder:

```text
Digital-detective-8534/
├── README.md
├── mission-00-setup/README.md
├── mission-01-computer-basics/README.md
├── mission-02-terminal/README.md
├── mission-03-operating-system/README.md
├── mission-04-programs/
│   ├── README.md
├── mission-05-numbers-data/
│   ├── README.md
│   └── number_converter.py
├── mission-06-git-github/README.md
├── mission-07-networking/README.md
├── mission-08-final-report/README.md
└── evidence/
```

---

## What a Repository Is & Why This Folder Structure Is Organised by Mission
* **What a repository is:** A repository (or "repo") is a central project folder tracked by Git that stores all project files along with a complete history of every change made over time.
* **Why the folder structure is organised by mission:** Separating the workspace into dedicated mission folders keeps each topic isolated, prevents files from getting mixed up, makes progress easy to track commit-by-commit, and allows visitors or evaluators to find any specific assignment section immediately.

---

## Setup Difficulty & Resolution
* **Difficulty Faced:** Making sure the local folder name and GitHub repository name matched the exact naming rule (`digital-detective-<last-4-USN-digits>`) and avoiding creating a duplicate `README.md` on GitHub when connecting the local repository.
* **How It Was Resolved:** Created the repository empty on GitHub without initializing a default README, linked it to the local folder using `git remote add origin`, and pushed the local structure cleanly.

| README section | Details |
|---|---|
| 1. Task / objective | Set up my workspace for the Digital Detective assignment by creating a repository named digital-detective-8534 with the folder structure for all missions, and publishing it on GitHub. |
| 2. Work completed | Created the project folder and ran git init.<br>Created the mission folders and a README.md in each.<br>Created number_converter.py in mission-05 and evidence/.gitkeep. |
| 3. Commands / tools used | `cd` moves into a folder.<br>`mkdir` creates folders.<br>`git init` creates a Git repository.<br>`touch` creates empty files.<br>`ls` lists files.<br>`python3 --version` shows Python 3.14.7.<br>`git --version` shows Git 2.50.1 (Apple Git-155).<br>`open -e` opens a file in TextEdit.<br>`cat` prints a file's contents. |
| 4. My understanding | A repository is a project folder tracked by Git that keeps the history of changes.<br>GitHub stores an online copy, so it works as a backup and others can view it. |
| 5. Difficulties faced | touch command with a wildcard failed with "zsh: no match found".<br>typed README.m once instead of README.md, and cat said the file didn't exist|
| 6. How I resolved them | I spotted the typo in the file name and re-ran the command correctly. |
| 7. Evidence / files | README.md files in the root and in each mission folder, number_converter.py, evidence/.gitkeep |
| 8. Commit details | Commit message: "Set up Digital Detective mission structure". The work was pushed to GitHub on the main branch and I confirmed the files are visible in the repository. |
