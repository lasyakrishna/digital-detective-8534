# Mission 2 — Become comfortable with the Terminal

## Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display** (`pwd`) | Prints the full path of the folder I am currently working in. | Terminal displayed the exact folder path from the root directory down to my repository folder. |
| **Directory listing** (`ls`) | Lists all visible files and subfolders in the current directory. | Terminal showed the names of my mission folders and files side by side. |
| **Detailed listing** (`ls -l`) | Lists files and folders with extra details like permissions, owner, file size, and last modified date. | Each file and folder appeared on its own line with detailed metadata on the left. |
| **Change directory** (`cd ..`) | Moves into a different folder (`cd ..` moves up one level to the parent folder). | My terminal prompt updated to show the parent folder name, and `pwd` confirmed my location changed. |
| **Create directory** (`mkdir practice`) | Creates a new empty folder with the given name. | A new folder named `practice` appeared when I ran `ls`. |
| **Create empty file** (`touch notes.txt`) | Creates a new empty file without opening an editor. | Running `ls` inside `practice` showed the newly created `notes.txt` file with 0 bytes. |
| **Copy file** (`cp notes.txt copy.txt`) | Duplicates an existing file into a new file with a different name. | Both `notes.txt` and `copy.txt` appeared in the folder with identical content. |
| **Move / rename file** (`mv copy.txt renamed.txt`) | Renames a file or moves it to another folder location. | `copy.txt` disappeared and was replaced by `renamed.txt`. |
| **Display file contents** (`cat notes.txt`) | Prints the text contents of a file directly into the terminal window. | The text inside `notes.txt` was printed directly on the screen. |

---

## Task 2.2 — Practise file changes safely

### Commands Used
```bash
mkdir terminal-practice
cd terminal-practice
echo "First line of text" > notes.txt
echo "Second line of text" >> notes.txt
cat notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt notes-archive.txt
```

### Notes & Questions
* **What is the difference between replacing a file's contents and adding text to the end?**
  Replacing (`>`) overwrites the entire file, erasing any existing text before writing the new text. Adding to the end (`>>`) appends the new text to the bottom while keeping all existing content intact.
* **What is the difference between copying a file and moving a file?**
  Copying (`cp`) creates an exact duplicate so two files exist, leaving the original untouched. Moving (`mv`) transfers or renames the original file itself, so only one file remains.
* **What information does the current-directory display (`pwd`) provide?**
  It provides the exact, full directory path from the system's root folder down to the current working directory.
* **Why is a directory-listing operation (`ls`) useful?**
  It lets you inspect what files and folders exist in your current directory so you can verify changes and avoid accidentally overwriting files.

---

## Task 2.3 — Understand flags and pipes

### Commands Used
```bash
ls
ls -lah
ls -la | head -n 5
```

### Explanations
* **Comparing `ls` vs. `ls -lah`:**
  A standard `ls` only displays the names of visible files and folders. Adding flags changes how the command behaves: `-l` shows detailed permissions, dates, and sizes; `-a` reveals hidden files starting with a dot (like `.git`); and `-h` converts byte sizes into human-readable formats like `KB` or `MB`.
* **How the pipe symbol (`|`) works:**
  The pipe symbol (`|`) connects two commands by passing the output of the command on the left directly as the input to the command on the right. In `ls -la | head -n 5`, the left side generates the full detailed directory list, and `head -n 5` filters it to display only the first 5 lines.

---

## Task 2.4 — Understand package managers

* **What a package manager does:**
  A package manager (such as Homebrew on macOS) is a command-line tool that automates installing, updating, configuring, and removing software packages and their dependencies. It is useful because it saves time, avoids manual downloads, and keeps software organized and secure from a single terminal interface.

---

## Reflection & Challenges Faced
* **Summary:** Practised navigating directories, creating and modifying text files safely, combining command flags, and filtering output with pipes.
* **Challenges:** Being careful to use `>>` instead of `>` when adding a second line of text so I did not accidentally overwrite the first line.
