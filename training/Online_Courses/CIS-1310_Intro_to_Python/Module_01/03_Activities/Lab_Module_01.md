# Lab 1: Setting Up Python and Writing Your First Programs

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Points:** 50 points
**Submission:** Upload your `.ipynb` file (Google Colab) or `.py` file to the Canvas assignment dropbox
**Due:** See Canvas for the deadline

---

## Objectives

By completing this lab, you will:

1. Successfully configure a working Python development environment
2. Write and execute Python programs using the `print()` function
3. Control output formatting using the `sep` and `end` parameters
4. Write meaningful comments following best practices
5. Apply PEP 8 naming conventions
6. Recognize the difference between a `SyntaxError`, `NameError`, and `IndentationError`

---

## Before You Begin

**Required environment:** Google Colab (recommended) or local Python 3.x installation.

- **Google Colab:** Open [https://colab.research.google.com/](https://colab.research.google.com/), sign in, and click **New Notebook**. Each code block in this lab goes into its own **cell** (click `+ Code` to add cells).
- **Local installation:** Open IDLE or VS Code. Create a new file named `lab01_yourLastName.py` (example: `lab01_nash.py`).

> Add your **name**, **course section**, and **date** as comments at the very top of your file/notebook before starting any exercises.

```python
# Student: [Your Full Name]
# Course: CIS-1310 Introduction to Python Programming
# Date: [Today's Date]
# Lab: Module 1 — Introduction to Python
```

---

## Part 1: Your First Python Program (10 points)

### Step 1.1 — Hello, World!

Type the following code exactly as shown and run it:

```python
print("Hello, World!")
```

**Expected Output:**
```
Hello, World!
```

**If you see an error:**
- Check that you have parentheses around the argument
- Check that your quotation marks match (both single or both double)
- Check that `print` is all lowercase

### Step 1.2 — Personal Greeting

Now modify the print statement to display a greeting using your name. You must write your own statement — do not copy the example:

Expected output format (replace with your information):
```
Hello! My name is [Your Name] and I am studying Python at Texas Wesleyan University.
```

Write a single `print()` statement that produces this output.

### Step 1.3 — Multiple Print Statements

Write three separate `print()` statements, each on its own line, that output:

```
Python is powerful.
Python is readable.
Python is in demand.
```

**Deliverable:** All three statements must be separate `print()` calls. No single print call may produce all three lines (we will cover that technique in a later lab).

---

## Part 2: Exploring `print()` Parameters (15 points)

### Step 2.1 — The `sep` Parameter

The `sep` parameter controls the separator between multiple arguments in a single `print()` call.

**Task:** Write `print()` statements that produce the following exact output. Each output line must come from **one** `print()` call:

**Output Line A:**
```
Python-3-Programming
```

**Output Line B:**
```
Texas | Wesleyan | University
```

**Output Line C:**
```
2024/01/15
```

**Hint:** Use `sep` with the appropriate separator character.

### Step 2.2 — The `end` Parameter

The `end` parameter controls what character is printed after the output (default is `\n` — newline).

**Task:** Write code using **exactly two `print()` statements** that produces this single-line output:

```
First Second
```

Both words must appear on the same line. You must use the `end` parameter in your first `print()` call.

### Step 2.3 — Combining `sep` and `end`

Write code that produces the following output where all three names appear on the **same line** separated by ` >> `:

```
Alice >> Bob >> Charlie
```

This must be accomplished with a **single `print()` statement** using both `sep` and the multiple-argument format.

### Step 2.4 — Printing the Return Value of `print()`

Run the following code and observe the output carefully:

```python
result = print("What is my return value?")
print("The return value is:", result)
```

**Output:**
```
What is my return value?
The return value is: None
```

**Reflection Question (answer as a comment in your code):** Why does `print()` return `None` instead of the string it just printed? Write your answer as a `#` comment immediately after this code block.

---

## Part 3: Comments Practice (10 points)

### Step 3.1 — Single-Line Comments

Write the following code block **with appropriate inline comments** explaining what each line does. You must write original comments — do not copy from this guide.

```python
# YOUR COMMENT HERE
print("Intro to Python")

# YOUR COMMENT HERE
print("Module 1", "Lab 1", sep=" | ")

# YOUR COMMENT HERE
print("Texas Wesleyan University", end="\n\n")
```

Replace each `# YOUR COMMENT HERE` with a comment that accurately describes what the line of code below it does.

### Step 3.2 — Disabling Code with Comments

Consider the following three lines:

```python
print("Line A")
print("Line B")
print("Line C")
```

**Task:** Using comments, disable (comment out) the middle line so that only Line A and Line C are printed. Run your code to verify the output is:

```
Line A
Line C
```

### Step 3.3 — Multi-Line Documentation Block

At the top of a new cell (or a new section), write a triple-quoted string that serves as a documentation block describing what your lab file does. It should include:
- What the program does
- The author's name
- The date

Example format (write your own content):

```python
"""
Lab 1 — Introduction to Python Programming
Author: [Your Name]
Date: [Date]
Description: This lab demonstrates the print() function, comments, and
             basic Python syntax as part of the CIS-1310 curriculum.
"""
```

---

## Part 4: Identifying and Fixing Errors (10 points)

Each code block below contains **one error**. Your task is to:
1. Identify the **type of error** (SyntaxError, NameError, or IndentationError)
2. Explain what causes it (as a comment)
3. Write a corrected version of the code

### Error Block A

```python
Print("Hello, Python!")
```

In a comment, write:
- What type of error this produces
- Why Python raises this error
- Then write the corrected code

### Error Block B

```python
if True:
print("This should be indented")
```

In a comment, write:
- What type of error this produces
- Why Python raises this error
- Then write the corrected code

### Error Block C

```python
print("Hello, World!"
```

In a comment, write:
- What type of error this produces
- Why Python raises this error
- Then write the corrected code

---

## Part 5: PEP 8 Naming (5 points)

For each of the following, write the identifier name in the **correct PEP 8 format** as a Python assignment statement:

| Description | Your PEP 8–Correct Variable Name |
|---|---|
| A variable storing a student's first name | (write it here as code) |
| A constant representing the maximum number of attempts | (write it here as code) |
| A class representing a student record | (write it here as code, define a placeholder class) |
| A function that calculates a final grade | (write it here as code, define a placeholder function) |
| A module-level private variable storing an API key | (write it here as code) |

Write these as actual Python code (assignment statements or class/function definitions with `pass` as the body).

---

## Submission Checklist

Before submitting, verify the following:

- [ ] Your name, course section, and date appear as comments at the top of the file
- [ ] All 5 parts are completed and code runs without errors
- [ ] Comments are meaningful and in your own words (not copied from this guide)
- [ ] Part 3.3 documentation block is present
- [ ] Part 4 includes the error type identified in a comment and a corrected version
- [ ] File is saved as `lab01_yourLastName.ipynb` or `lab01_yourLastName.py`

**Submit** your file to the **Lab 1** assignment in Canvas before the deadline.

---

## Grading Rubric

| Part | Task | Points |
|---|---|---|
| Part 1 | Hello World, personal greeting, three print statements | 10 |
| Part 2 | `sep`, `end`, combined parameters, return value reflection | 15 |
| Part 3 | Inline comments, disabling code, documentation block | 10 |
| Part 4 | Error identification, explanation, and correction (3 blocks) | 10 |
| Part 5 | PEP 8 naming conventions (5 identifiers) | 5 |
| **Total** | | **50** |

---

*Next: Module 2 Lab — Variables, Literals, and Data Types*
