# Mission 5 — Numbers and data

## 1. Task / objective
Convert numbers manually between decimal, binary, and hexadecimal, verify results in Python, build `number_converter.py`, and explain how text is encoded using ASCII and Unicode.

## 2. Work completed
* Completed 7 manual number-system conversions with step-by-step division and place-value working.
* Verified all manual answers in the `python3` interactive shell using `bin()`, `hex()`, and `int(str, base)`.
* Built and tested `number_converter.py` with three positive decimal numbers (`10`, `25`, `255`).
* Documented ASCII decimal codes (`A` = `65`, `a` = `97`) and why character encoding standards are required.

## Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | 13 ÷ 2 = 6 remainder **1**; 6 ÷ 2 = 3 remainder **0**; 3 ÷ 2 = 1 remainder **1**; 1 ÷ 2 = 0 remainder **1**. Reading remainders from bottom to top: **`1101`** (8 + 4 + 0 + 1 = 13). |
| **Convert decimal 25 to binary.** | 25 ÷ 2 = 12 remainder **1**; 12 ÷ 2 = 6 remainder **0**; 6 ÷ 2 = 3 remainder **0**; 3 ÷ 2 = 1 remainder **1**; 1 ÷ 2 = 0 remainder **1**. Reading remainders bottom to top: **`11001`** (16 + 8 + 0 + 0 + 1 = 25). |
| **Convert binary 1010 to decimal.** | (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰) = 8 + 0 + 2 + 0 = **`10`**. |
| **Convert binary 1101 to decimal.** | (1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰) = 8 + 4 + 0 + 1 = **`13`**. |
| **Convert hexadecimal A to decimal.** | In base 16, A represents 10 → 10 × 16⁰ = **`10`**. |
| **Convert hexadecimal 1F to decimal.** | (1 × 16¹) + (15 × 16⁰) = 16 + 15 = **`31`** (since F = 15). |
| **Convert binary 1111 to hexadecimal.** | First convert `1111` to decimal: 8 + 4 + 2 + 1 = 15. In hexadecimal, 15 is represented as **`F`**. |

---

## Task 5.2 — Verify using Python

Tested in the Python 3 interactive shell (`python3`):

| Expression Tested | Python Result | Matches Manual Calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes (`1101`) |
| `bin(25)` | `'0b11001'` | Yes (`11001`) |
| `int('1010', 2)` | `10` | Yes (`10`) |
| `int('1101', 2)` | `13` | Yes (`13`) |
| `int('A', 16)` | `10` | Yes (`10`) |
| `int('1F', 16)` | `31` | Yes (`31`) |
| `hex(15)` | `'0xf'` | Yes (`F`) |

---

## Task 5.3 — Build a small number converter

### Code (`number_converter.py`)
```python
decimal_num = int(input("Enter a positive decimal number: "))

binary_val = bin(decimal_num)
hex_val = hex(decimal_num)

print("Binary:", binary_val)
print("Hexadecimal:", hex_val)
```

### Test Results

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| `10` | `0b1010` | `0xa` |
| `25` | `0b11001` | `0x19` |
| `255` | `0b11111111` | `0xff` |

### How the Conversion Functions Work
* **`bin()`:** Takes an integer and converts it into its binary (base-2) string representation prefixed with `0b`.
* **`hex()`:** Takes an integer and converts it into its hexadecimal (base-16) string representation prefixed with `0x`.

---

## Task 5.4 — How is text stored?

* **ASCII decimal codes:**
  * Uppercase letter **`A`**: **`65`**
  * Lowercase letter **`a`**: **`97`**
* **Why a computer needs an encoding standard to store text:**
  Computers can only store and process binary numbers (`0`s and `1`s), so an encoding standard is needed to map every character to a specific numeric code. This ensures that text saved on one device is decoded and displayed as the exact same characters on any other device.
* **Example of a character not part of basic ASCII:**
  The emoji **`😊`** (or currency symbols like **`₹`** / accented letters like **`é`**), which require Unicode/UTF-8 instead of basic 7-bit ASCII.

---

## 3. Commands / tools used
* `python3` : Launched the interactive Python shell to verify conversions with `bin()`, `hex()`, and `int()`.
* `python3 number_converter.py` : Ran the decimal-to-binary and hexadecimal converter program.
* `git add`, `git commit`, `git push` : Committed `number_converter.py` and `README.md`.

## 4. My understanding
* Computers store all data—numbers, letters, and symbols—as binary bits (`0` and `1`).
* Hexadecimal provides a shorter, human-friendly way to represent groups of 4 binary bits.
* Encoding standards like ASCII and UTF-8 ensure text saved on one computer renders identically on any other computer.

## 5. Difficulties faced
* Encountered a `TypeError` when passing the direct return value of `input()` into `bin()` because `input()` returns a string.

## 6. How I resolved them
* Converted the user input to an integer using `int(input(...))` before calling `bin()` and `hex()`.

## 7. Evidence / files
* `mission-05-numbers-data/number_converter.py`
* `mission-05-numbers-data/README.md`

## 8. Commit details
* Commit message: `"Build number converter and document data representation"`
* Commit repository: `digital-detective-8534`
* Push status: Committed and pushed to GitHub (`main` branch).

 