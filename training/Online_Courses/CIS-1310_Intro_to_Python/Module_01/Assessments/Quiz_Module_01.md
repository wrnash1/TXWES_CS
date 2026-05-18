# Quiz: Module 1 — Introduction to Python Programming

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Total:** 15 Questions | 2 points each = **30 points**
**Suggested Time:** 20 minutes
**PCAP Alignment:** Section 1 — Introduction to Python

---

## Canvas Entry Instructions

When entering this quiz into Canvas:
- **Question Type:** Multiple Choice (unless noted otherwise)
- **Points per question:** 2
- **Shuffle Answers:** Yes (recommended)
- **Allowed Attempts:** 1 (or per your course policy)
- One correct answer per question

Correct answers are marked with **← CORRECT**. Add the explanation to the question feedback field in Canvas.

---

## Questions

---

### Question 1

Who created Python, and in what year was it first publicly released?

- A) Tim Berners-Lee, 1989
- B) **Guido van Rossum, 1991** ← CORRECT
- C) Linus Torvalds, 1994
- D) James Gosling, 1995

**Correct Answer: B**
**Explanation:** Guido van Rossum created Python and released version 1.0 in 1991. The language was named after *Monty Python's Flying Circus*, not the snake. James Gosling created Java; Linus Torvalds created Linux; Tim Berners-Lee created the World Wide Web.

---

### Question 2

What type of error does Python raise when a code block is missing required indentation?

- A) SyntaxError
- B) **IndentationError** ← CORRECT
- C) NameError
- D) ValueError

**Correct Answer: B**
**Explanation:** Python uses indentation to define code blocks. Missing or inconsistent indentation raises an `IndentationError`. A `SyntaxError` covers other syntax violations. A `NameError` occurs when an undefined variable is referenced. A `ValueError` occurs when a function receives a correct type but inappropriate value.

---

### Question 3

What is the output of the following code?

```python
print("Python", "is", "fun", sep="-")
```

- A) `Python is fun`
- B) **`Python-is-fun`** ← CORRECT
- C) `Python, is, fun`
- D) `Pythonisfun`

**Correct Answer: B**
**Explanation:** The `sep` parameter in `print()` replaces the default space separator with the specified string. Here, each argument is separated by `"-"`, producing `Python-is-fun`.

---

### Question 4

Which statement CORRECTLY describes the difference between Python 2 and Python 3?

- A) Python 3 allows `print "Hello"` without parentheses
- B) Python 2 and Python 3 are fully backwards-compatible
- C) **Python 2 reached end-of-life in January 2020; Python 3 is the current standard** ← CORRECT
- D) Python 3 is significantly slower than Python 2 in all use cases

**Correct Answer: C**
**Explanation:** Python 2 officially reached end-of-life on January 1, 2020. The `print` statement without parentheses is Python 2 syntax only; Python 3 requires `print()` as a function. The two versions are NOT fully compatible — many Python 2 programs will not run in Python 3 without modification.

---

### Question 5

What is the return value of the `print()` function in Python?

- A) The string that was printed
- B) An integer representing the number of characters printed
- C) **`None`** ← CORRECT
- D) A Boolean indicating whether the print was successful

**Correct Answer: C**
**Explanation:** `print()` displays output as a side effect but always returns `None`. This means `x = print("Hello")` sets `x` to `None`, not to the string `"Hello"`. This is a frequent PCAP exam trick question.

---

### Question 6

Which of the following is NOT a valid way to write a comment in Python?

- A) `# This is a comment`
- B) `""" This is a comment """`
- C) **`/* This is a comment */`** ← CORRECT
- D) `''' This is a comment '''`

**Correct Answer: C**
**Explanation:** `/* ... */` is the block comment syntax used in C, C++, and Java — it is not valid Python syntax and will raise a `SyntaxError`. The `#` symbol creates single-line comments in Python. Triple-quoted strings (`"""` or `'''`) are technically string literals but are widely used as multi-line comments when not assigned to a variable.

---

### Question 7

What is the output of the following code?

```python
print("Python")
# print("is awesome")
print("Programming")
```

- A) `Python` / `is awesome` / `Programming`
- B) **`Python` / `Programming`** ← CORRECT
- C) `Pythonis awesomeProgramming`
- D) `SyntaxError`

**Correct Answer: B**
**Explanation:** The second line begins with `#`, making it a comment. Python ignores all commented lines during execution. Only the first and third `print()` calls run, producing two lines of output.

---

### Question 8

According to PEP 8, which is the correct format for naming a variable that stores a student's last name?

- A) `StudentLastName`
- B) `STUDENTLASTNAME`
- C) `studentLastName`
- D) **`student_last_name`** ← CORRECT

**Correct Answer: D**
**Explanation:** PEP 8 specifies that variables and function names should use `snake_case` — all lowercase with words separated by underscores. `StudentLastName` is PascalCase (used for class names). `STUDENTLASTNAME` is used for constants. `studentLastName` is camelCase (used in Java/JavaScript, not standard Python).

---

### Question 9

What is the output of the following code?

```python
print("Line 1", end=" ")
print("Line 2")
```

- A) `Line 1` (newline) `Line 2`
- B) `Line 1,Line 2`
- C) **`Line 1 Line 2`** ← CORRECT
- D) `Line 1Line 2`

**Correct Answer: C**
**Explanation:** The `end=" "` parameter replaces the default newline character with a space. So the cursor stays on the same line after printing "Line 1 ", and the second `print()` continues on that same line, producing `Line 1 Line 2` on one line.

---

### Question 10

Which term describes Python's execution model where code runs line-by-line without prior compilation to native machine code?

- A) Compiled
- B) Transpiled
- C) Assembled
- D) **Interpreted** ← CORRECT

**Correct Answer: D**
**Explanation:** Python is an *interpreted* language — it executes source code (via bytecode) at runtime rather than converting it to native machine code in advance. Compiled languages (like C) generate machine code before any execution occurs. Transpiled languages convert to another high-level language (like TypeScript → JavaScript).

---

### Question 11

What does Google Colab use to store and run Python code?

- A) Standard `.py` Python files
- B) `.html` web files
- C) **Jupyter Notebooks (`.ipynb` files)** ← CORRECT
- D) Executable `.exe` binaries

**Correct Answer: C**
**Explanation:** Google Colab is a hosted Jupyter Notebook environment. Code is stored in `.ipynb` (IPython Notebook) files in Google Drive. These notebooks contain cells that mix code, output, and markdown text, making them ideal for interactive learning.

---

### Question 12

Which of the following statements about Python is FALSE?

- A) Python is case-sensitive
- B) Python uses indentation to define code blocks
- C) **Python requires a semicolon at the end of each statement** ← CORRECT (this statement is FALSE)
- D) Python supports object-oriented programming

**Correct Answer: C**
**Explanation:** Python does NOT require semicolons at the end of statements — this is a feature of languages like C, Java, and JavaScript. Python statements end at the newline. Statements A, B, and D are all true about Python.

---

### Question 13

What is the output of the following code?

```python
print("A", end="")
print("B", end="")
print("C")
```

- A) `A` (newline) `B` (newline) `C`
- B) `A B C`
- C) **`ABC`** ← CORRECT
- D) `A, B, C`

**Correct Answer: C**
**Explanation:** `end=""` removes the newline and replaces it with an empty string, so no newline or space is added between the outputs. All three print calls write directly adjacent to each other, producing `ABC` on one line.

---

### Question 14

When Python executes a `.py` file, what intermediate form does it produce before the Python Virtual Machine runs the code?

- A) Machine code (native binary)
- B) Java bytecode
- C) C source code
- D) **Python bytecode (`.pyc` files)** ← CORRECT

**Correct Answer: D**
**Explanation:** Python first compiles source code to **bytecode**, stored in `.pyc` files inside the `__pycache__` directory. The Python Virtual Machine (PVM) then interprets this bytecode. This is different from languages like C that compile directly to machine-specific binary. Bytecode is portable — the same `.pyc` file can run on any platform with the same Python version.

---

### Question 15

A developer writes the following code. What error will Python raise, and why?

```python
if True:
    x = 10
      y = 20
```

- A) `NameError` — variables are not defined before use
- B) `ValueError` — the values 10 and 20 are incompatible
- C) `SyntaxError` — the `if` statement is missing a colon
- D) **`IndentationError` — `y = 20` has unexpected extra indentation** ← CORRECT

**Correct Answer: D**
**Explanation:** Both `x = 10` and `y = 20` are inside the `if True:` block, but `y = 20` has extra leading spaces (6 vs 4), creating inconsistent indentation. Python raises an `IndentationError: unexpected indent`. Indentation in Python is syntactically meaningful — all lines in a block must share the same indentation level.

---

## Answer Key (for Instructor Reference)

| Q | Answer | Topic |
|---|---|---|
| 1 | B | Python history |
| 2 | B | IndentationError |
| 3 | B | `sep` parameter |
| 4 | C | Python 2 vs 3 |
| 5 | C | `print()` return value |
| 6 | C | Comment syntax |
| 7 | B | Comment execution behavior |
| 8 | D | PEP 8 naming |
| 9 | C | `end` parameter |
| 10 | D | Interpreted language |
| 11 | C | Google Colab / Jupyter |
| 12 | C | Python syntax (false statement) |
| 13 | C | `end=""` chaining |
| 14 | D | Python execution model |
| 15 | D | IndentationError |

---

*These questions are also included in Unit Test 1 (Modules 1–4) with additional synthesis-level questions.*
