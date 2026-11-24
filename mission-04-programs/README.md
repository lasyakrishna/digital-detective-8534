# Mission 4 — How programs run

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

## Reflection & Challenges Faced
* **Command / Tool Used:** Used `python3 hello.py` in Terminal to execute the Python script.
* **What I Understood:** Learned how Python acts as an interpreter to execute code directly at runtime, and how that differs from compiled languages that build an executable ahead of time.
* **Challenges Faced:** Ensuring I typed `python3` (rather than `python`) so the terminal used the right Python 3 interpreter, and matching the exact capitalization in `"Hello from Python"`.
