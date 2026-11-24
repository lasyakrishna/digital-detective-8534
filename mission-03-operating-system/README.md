# Mission 3 — Understand the operating system

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

## Reflection & Challenges Faced
* **Summary:** Explored operating system details, active process IDs, absolute vs. relative file paths, and file permission flags while keeping personal device identifiers `[redacted]`.
* **Challenges:** Remembering to replace personal usernames and file paths with `[redacted]` before committing, and breaking down the 10-character permission string (`-rw-r--r--`) into owner, group, and public permissions.
