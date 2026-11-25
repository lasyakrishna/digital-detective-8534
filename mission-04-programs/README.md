# Mission 4 — How programs run

## 1. Task / objective
Run a simple one-line Python program (`hello.py`) from Terminal and compare how compilers and interpreters translate or execute programs.

## 2. Work completed
* Created `hello.py` inside `mission-04-programs` to display `"Hello from Python"`.
* Executed `hello.py` using Python 3 in Terminal and confirmed `"Hello from Python"` printed on screen.
* Completed the comparison table and written explanation between a compiler and an interpreter.

## Task 4.1 — Create and run a Python program

### Code in `hello.py`
```python
print("Hello from Python")
```

### Command Used & Output
* **Command run in Terminal:**
  ```bash
  python3 hello.py
  ```
* **Observed Output:**
  ```text
  Hello from Python
  ```

---

## Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code before the program runs, then executes the translated program separately. | Translates and executes the source code line by line at runtime while the program is running. |
| **Typical output** | Produces a separate standalone machine-code or executable file (e.g., `.exe` or binary). | Does not create a separate executable file; directly outputs the program's results as it runs. |
| **One example** | C, C++, or Rust (`gcc` / `clang`) | Python (`python3`) or JavaScript |
| **One advantage** | Runs much faster once compiled because translation is already finished before execution. | Easier to test and debug quickly since code runs immediately without waiting for a separate compile step. |

### Explanation in My Own Words
As shown in the comparison table, the main difference between a compiler and an interpreter is when the code gets translated into machine-readable instructions. A compiler translates the entire program all at once beforehand and creates a separate executable file, which makes languages like C run very fast later on. In contrast, an interpreter—like Python—reads and executes the code line by line while the program is running without generating a standalone executable. This makes interpreted languages easier to test and debug step by step, even though execution is generally slower than compiled code.

---

 
## 3. Commands / tools used
* `python3 hello.py` : Runs the Python 3 interpreter to execute `hello.py`.
* `VS Code` : Used to write `hello.py` and `README.md`.
* `git add`, `git commit`, `git push` : Committed `hello.py` and `README.md` to GitHub.

## 4. My understanding
* Computers cannot execute human-readable source code directly; it must be translated into machine instructions first.
* Compilers translate everything upfront for maximum execution speed, while interpreters translate line by line for flexibility and quick debugging.

## 5. Difficulties faced
* No major difficulties.

## 6. How I resolved them
* Not applicable.

## 7. Evidence / files
* `mission-04-programs/hello.py`
* `mission-04-programs/README.md`

## 8. Commit details
* Commit message: `"Compare compilers and interpreters"`
* Commit repository: `digital-detective-8534`
* Push status: Committed and pushed to GitHub (`main` branch).