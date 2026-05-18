# Lab 2: Variables, Literals, and Data Types

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Points:** 50 points
**Submission:** Upload your `.ipynb` or `.py` file to the Canvas Lab 2 assignment
**Due:** See Canvas for the deadline

---

## Objectives

By completing this lab, you will:

1. Create variables using correct naming conventions (PEP 8)
2. Work with all five Python primitive data types: `int`, `float`, `str`, `bool`, `NoneType`
3. Use the `type()` and `isinstance()` functions to inspect data types
4. Demonstrate the behavior of numeric literals in binary, octal, and hexadecimal
5. Practice multiple assignment and augmented assignment operators
6. Observe Python's dynamic typing in action
7. Explore truthy and falsy behavior of different values

---

## Before You Begin

Add your student header to the top of your file:

```python
# Student: [Your Full Name]
# Course: CIS-1310 Introduction to Python Programming
# Date: [Today's Date]
# Lab: Module 2 — Variables, Literals, and Data Types
```

---

## Part 1: Creating Variables and Checking Types (15 points)

### Step 1.1 — Create a Student Profile

Create a set of variables representing a student profile. Use appropriate data types for each, and follow PEP 8 naming conventions (snake_case for variables):

```python
# Create these variables with your own realistic values:
student_name  = ___       # str: Your full name as a string
student_id    = ___       # int: A 6-digit student ID number
gpa           = ___       # float: A GPA between 0.0 and 4.0
is_enrolled   = ___       # bool: True or False
advisor       = ___       # set to None (not yet assigned)
```

Replace each `___` with an appropriate value. After creating the variables, print each one along with its type using `type()`. Your output should look like:

```
student_name: Alex Johnson | Type: <class 'str'>
student_id: 123456 | Type: <class 'int'>
gpa: 3.75 | Type: <class 'float'>
is_enrolled: True | Type: <class 'bool'>
advisor: None | Type: <class 'NoneType'>
```

Write five `print()` statements (one per variable) in the format shown above. Use `sep` and string concatenation or f-strings if you already know them, but at minimum use the format: `print("label:", variable, "| Type:", type(variable))`

### Step 1.2 — Demonstrate Dynamic Typing

Write code that demonstrates Python's dynamic typing by assigning three different types to the same variable, printing the type each time:

```python
x = 42
print("x =", x, "| Type:", type(x))

x = 3.14
print("x =", x, "| Type:", type(x))

x = "now a string"
print("x =", x, "| Type:", type(x))
```

Run this and observe the output. Then write a comment (`#`) below explaining in one or two sentences what "dynamic typing" means based on what you observed.

---

## Part 2: Numeric Literal Formats (10 points)

### Step 2.1 — Non-Decimal Literals

Write the following values as Python literals in all four formats and print each one. Use variables named `value_decimal`, `value_binary`, `value_octal`, `value_hex`.

**Task:** Represent the number **255** in all four formats:

```python
value_decimal = 255
value_binary  = ___      # Write 255 in binary (0b prefix)
value_octal   = ___      # Write 255 in octal (0o prefix)
value_hex     = ___      # Write 255 in hexadecimal (0x prefix)

print("Decimal:", value_decimal)
print("Binary:", value_binary)
print("Octal:", value_octal)
print("Hex:", value_hex)
```

All four print statements should output `255` (Python converts all formats to decimal for display).

### Step 2.2 — Large Number Readability

Assign the number **1,000,000,000** (one billion) to a variable using Python's underscore separator for readability. Then assign it again without the separator. Print both and verify they are equal.

```python
one_billion_readable = ___       # Use underscores: 1_000_000_000
one_billion_plain    = ___       # Write without underscores

print(one_billion_readable)
print(one_billion_plain)
print("Are they equal?", one_billion_readable == one_billion_plain)
```

### Step 2.3 — Scientific Notation

Assign the following values using scientific notation and print them:

- The speed of light: approximately 3 × 10^8 meters per second
- Planck's constant: approximately 6.626 × 10^-34

```python
speed_of_light = ___     # 3e8
plancks_constant = ___   # 6.626e-34

print("Speed of light:", speed_of_light)
print("Planck's constant:", plancks_constant)
```

---

## Part 3: Boolean and None Values (10 points)

### Step 3.1 — Truthy and Falsy Values

For each of the following values, use `bool()` to convert it and `print()` to display the result. Before running the code, **predict** in a comment whether each will be `True` or `False`:

```python
# Predict: True or False?
print(bool(0))          # Your prediction:
print(bool(1))          # Your prediction:
print(bool(-5))         # Your prediction:
print(bool(""))         # Your prediction:
print(bool("Hello"))    # Your prediction:
print(bool(None))       # Your prediction:
print(bool(0.0))        # Your prediction:
print(bool([]))         # Your prediction: (empty list)
```

Add a comment for each line with your prediction before you run the code. After running, note which predictions were wrong and explain why in a comment.

### Step 3.2 — None as a Placeholder

Write code that demonstrates `None` as a placeholder value:

```python
# Simulate a student who hasn't been assigned a grade yet
student_grade = None
print("Grade:", student_grade)
print("Type:", type(student_grade))
print("Is grade assigned?", student_grade is not None)

# Now assign a real grade
student_grade = 95
print("Grade:", student_grade)
print("Is grade assigned?", student_grade is not None)
```

Run this code and add a comment explaining when and why you would use `None` in a real program.

### Step 3.3 — Boolean Arithmetic (Surprising Python Behavior)

Python booleans are a subclass of integers. Run the following and observe:

```python
print(True + True)         # What do you expect?
print(True + False)        # What do you expect?
print(True * 10)           # What do you expect?
print(False * 99)          # What do you expect?
print(int(True))           # What do you expect?
print(int(False))          # What do you expect?
```

Write a comment below the code block explaining why Python allows arithmetic on booleans and what `True` and `False` equal as integers.

---

## Part 4: Multiple and Augmented Assignment (10 points)

### Step 4.1 — Multiple Assignment (Same Value)

Use a single assignment statement to set three variables (`x`, `y`, `z`) all to `0`. Then print all three on one line.

```python
# Write a single assignment statement here
___
print(x, y, z)    # Expected: 0 0 0
```

### Step 4.2 — Tuple Unpacking

Use tuple unpacking to assign three course names to three variables in one statement. Then print them.

```python
course_one, course_two, course_three = "Python", "Networking", "Database"
print(course_one)
print(course_two)
print(course_three)
```

Now modify the code to also swap `course_one` and `course_three` using tuple unpacking (without a temporary variable). Print both after the swap to verify.

### Step 4.3 — Augmented Assignment Operators

A student starts with 0 points and gains points throughout a game. Write code that tracks the score using only augmented assignment operators:

```python
score = 0

score += 50       # Level 1 complete
score += 25       # Bonus collected
score *= 2        # Double points activated
score -= 30       # Penalty applied
score //= 3       # Points divided (floor division)

print("Final score:", score)    # What is the final score?
```

Before running, calculate the expected final score by hand and write your prediction as a comment. Then run and verify.

---

## Part 5: `isinstance()` and Type Checking (5 points)

### Step 5.1 — Checking Types with `isinstance()`

Given the following variables, use `isinstance()` to check each against the specified type and print the result:

```python
a = 42
b = 3.14
c = True
d = "Texas Wesleyan"
e = None

# Check each:
print(isinstance(a, int))           # Expected: True
print(isinstance(b, int))           # Expected: False
print(isinstance(c, bool))          # Expected: True
print(isinstance(c, int))           # Why is this True? Add a comment explaining.
print(isinstance(d, str))           # Expected: True
print(isinstance(e, type(None)))    # Expected: True
print(isinstance(a, (int, float)))  # Expected: True — why? Add a comment.
```

After running, explain in comments why `isinstance(True, int)` returns `True`.

---

## Submission Checklist

- [ ] Student header (name, course, date, lab number) at the top
- [ ] All 5 parts completed and code runs without errors
- [ ] Predictions written as comments before each `bool()` block (Part 3.1)
- [ ] Explanation comment for `None` use case (Part 3.2)
- [ ] Final score prediction written as comment (Part 4.3)
- [ ] Explanation comment for `isinstance(True, int)` (Part 5.1)
- [ ] File saved as `lab02_yourLastName.ipynb` or `lab02_yourLastName.py`

**Submit** to the **Lab 2** assignment in Canvas.

---

## Grading Rubric

| Part | Task | Points |
|---|---|---|
| Part 1 | Student profile variables, `type()` output, dynamic typing demo | 15 |
| Part 2 | Non-decimal literals, large numbers, scientific notation | 10 |
| Part 3 | Truthy/falsy, None placeholder, boolean arithmetic | 10 |
| Part 4 | Multiple assignment, tuple unpacking, augmented operators | 10 |
| Part 5 | `isinstance()` checks with explanations | 5 |
| **Total** | | **50** |

---

*Next: Module 3 Lab — Operators*
