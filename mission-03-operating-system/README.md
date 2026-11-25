# Mission 3 — Understand the operating system

# Mission 3: Understand the operating system

## 1. Task / objective
Inspect operating system details, active user identity, storage usage, running processes and PIDs, file paths, permissions, and core OS responsibilities in a privacy-safe manner.

## 2. Work completed
* Explored OS kernel details, active account identity, disk usage, and running process snapshots with sensitive identifiers redacted.
* Identified what processes and PIDs are, along with examples of user and background processes.
* Compared absolute vs. relative file paths and inspected read/write/execute permission flags (`-rw-r--r--`).
* Documented the six core responsibilities of an operating system with real examples.

## Task 3.1 — Explore your operating system

### Commands Used
```bash
uname -a
whoami
df -h
ps aux | head -n 10
```

### Observations Table (Privacy-Safe)

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the operating system kernel, version, and hardware architecture. | Running macOS/Linux `[redacted]` kernel on 64-bit architecture. |
| **Current account identity** | Displays the username of the active account running commands in the terminal. | Logged in as `[redacted]`. |
| **Available and used storage** | Shows total storage capacity, used disk space, and available free space. | Main storage drive has `[redacted]` used and `[redacted]` available space. |
| **System activity snapshot** | Displays currently running processes, CPU load, and memory usage. | Observed active user applications alongside background system services. |

---

## Task 3.2 — Understand processes

### Commands Used
```bash
ps aux | head -n 15
```

### Answers
* **What is a process?**
  A process is an active instance of a computer program that is currently loaded into memory and being executed by the CPU.
* **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique number assigned by the operating system to track and manage each running process individually.
* **Two examples of processes running on my computer:**
  1. **Application process:** Google Chrome (or text editor) — a user-opened program actively running.
  2. **Background process:** `zsh` / `bash` (or system daemon) — the command-line shell running in the background.

---

## Task 3.3 — Understand paths and permissions

### Commands Used
```bash
pwd
cd terminal-practice
pwd
ls -l notes.txt
```

### Paths Explanation & Examples
* **Difference between an absolute path and a relative path:**
  An **absolute path** specifies the complete location of a file or directory starting from the root directory (`/`), making it valid from anywhere on the system. A **relative path** specifies the location relative to your current working directory.
* **Examples from my assignment folder:**
  * **Absolute path:** `/Users/[redacted]/assignment-repo/terminal-practice`
  * **Relative path:** `./terminal-practice` (or `terminal-practice/notes.txt` from the main assignment folder)

### File Permissions Observation
* Running `ls -l notes.txt` showed the permission string `-rw-r--r--`.
* The first character (`-`) indicates a regular file, and the next three characters (`rw-`) represent the **owner's permissions**:
  * **Read (`r`):** Yes — the owner can view and read the file's contents.
  * **Write (`w`):** Yes — the owner can edit and modify the file.
  * **Execute (`x`):** No (`-`) — the owner cannot run this text file as a program.

---

## Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Starts, schedules, pauses, and stops running programs so multiple tasks share the CPU efficiently. | Running a web browser, text editor, and terminal simultaneously without crashing. |
| **Memory management** | Allocates RAM to active programs and frees it when closed so programs do not interfere with each other's data. | Assigning memory to open browser tabs and releasing it when tabs are closed. |
| **Device management** | Communicates with and controls hardware devices using software drivers. | Sending typed characters from the keyboard to the screen or audio to headphones. |
| **File management** | Organizes data into files and folders on storage drives and tracks file locations and metadata. | Creating, saving, and organizing `notes.txt` inside the `terminal-practice` directory. |
| **User interface / shell** | Provides a visual or command-line interface so users can interact with the computer. | Navigating folders in Finder/Explorer (GUI) or running `ls` and `cd` in Terminal (CLI). |
| **Security and permissions** | Protects system resources and files by authenticating users and enforcing read, write, and execute rules. | Requiring a password for system changes or restricting file edits (`-rw-r--r--`) to the owner. |

---

## 3. Commands / tools used
* `uname -a` : Displays operating system kernel and architecture information.
* `whoami` : Prints the currently logged-in account username.
* `df -h` : Shows disk usage and available space in human-readable units.
* `ps aux | head -n 15` : Lists running processes along with their PIDs and resource usage.
* `pwd` & `cd` : Verified absolute and relative directory paths.
* `ls -l` : Inspected file permission strings (`-rw-r--r--`).
* `git add`, `git commit`, `git push` : Committed and pushed Mission 3 documentation.

## 4. My understanding
* The operating system manages hardware resources (CPU, RAM, disk, devices) so applications can run safely without interfering with one another.
* Every running app or background service is tracked as a separate process with its own unique PID.
* File paths and `rwx` permission bits protect system integrity and control who can view, edit, or execute files.

## 5. Difficulties faced
* Reading the 10-character permission string (`-rw-r--r--`) and making sure no personal usernames or system paths were exposed.

## 6. How I resolved them
* Split the permission string into file type (`-`), owner (`rw-`), group (`r--`), and others (`r--`), and replaced personal details with `[redacted]`.

## 7. Evidence / files
* `mission-03-operating-system/README.md`

## 8. Commit details
* Commit message: `"Document operating system and file management"`
* Commit repository: `digital-detective-8534`
* Push status: Committed and pushed to GitHub (`main` branch).
 
