# Lab 4: Type Conversion and User Input

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Points:** 50 points
**Submission:** Upload your `.ipynb` or `.py` file to the Canvas Lab 4 assignment
**Due:** See Canvas for the deadline

> **Note:** This is the last lab before **Unit Test 1**, which covers Modules 1–4. Use this lab as a review opportunity.

---

## Objectives

By completing this lab, you will:

1. Distinguish between implicit and explicit type conversion and know when each occurs
2. Correctly apply `int()`, `float()`, `str()`, and `bool()` conversion functions
3. Use `input()` to gather user data and convert it appropriately for calculations
4. Format output with f-strings using format specifiers
5. Observe and understand Python 3's banker's rounding via `round()`
6. Identify `ValueError` vs. `TypeError` and understand which conversion calls cause each

---

## Before You Begin

```python
# Student: [Your Full Name]
# Course: CIS-1310 Introduction to Python Programming
# Date: [Today's Date]
# Lab: Module 4 — Type Conversion and User Input
```

---

## Part 1: Explicit Type Conversion (15 points)

### Step 1.1 — `int()` Conversion Table

For each of the following `int()` calls, write your prediction as a comment, run it, and note whether it succeeds or raises an error. If it raises an error, write the error type as a comment:

```python
# Write prediction before each line:
print(int(3.9))          # Prediction: ___ (Success or Error?)
print(int(3.1))          # Prediction: ___
print(int(-3.9))         # Prediction: ___
print(int("42"))         # Prediction: ___
print(int(True))         # Prediction: ___
print(int(False))        # Prediction: ___
# The next lines will raise errors — use try/except to catch them and print the error type:
```

For the following, wrap each in `try`/`except Exception as e: print(type(e).__name__, e)` to catch the error without crashing:

```python
try:
    print(int("3.14"))   # What error type? Prediction: ___
except Exception as e:
    print(type(e).__name__, e)

try:
    print(int("hello"))  # What error type? Prediction: ___
except Exception as e:
    print(type(e).__name__, e)

try:
    print(int(None))     # What error type? Prediction: ___
except Exception as e:
    print(type(e).__name__, e)
```

After running, write a comment explaining the difference between `ValueError` and `TypeError`.

### Step 1.2 — `float()` Special Values

Run the following and observe:

```python
print(float("inf"))     # Positive infinity
print(float("-inf"))    # Negative infinity
print(float("nan"))     # Not a Number
print(float("3"))       # Integer string → float
print(float(True))      # Bool → float
```

Write a comment explaining what `inf` and `nan` represent and when they might appear in real computations.

### Step 1.3 — `bool()` Edge Cases

Predict each before running. Pay special attention to the tricky ones:

```python
print(bool(0))          # Prediction: ___
print(bool(0.0))        # Prediction: ___
print(bool(""))         # Prediction: ___
print(bool("False"))    # Prediction: ___ (TRAP!)
print(bool("0"))        # Prediction: ___ (TRAP!)
print(bool(None))       # Prediction: ___
print(bool([]))         # Prediction: ___
print(bool([0]))        # Prediction: ___ (list with one element = 0)
print(bool(0j))         # Prediction: ___ (complex zero)
```

Write a comment explaining why `bool("False")` and `bool("0")` are both `True`.

---

## Part 2: `input()` and Type Conversion (15 points)

### Step 2.1 — Understanding `input()` Return Type

Run this code and observe the output:

```python
value = input("Enter any number: ")
print("You entered:", value)
print("Type:", type(value))
print("Is it a string?", isinstance(value, str))
```

Write a comment below explaining: why does `input()` always return a string, even if the user types a number? What problem does this cause for mathematical calculations?

### Step 2.2 — Temperature Converter

Build a Celsius-to-Fahrenheit converter that:
1. Asks the user for a temperature in Celsius
2. Converts the input to a float
3. Applies the formula: `F = (C × 9/5) + 32`
4. Prints the result using an f-string with 2 decimal places

```python
celsius_str = input("Enter temperature in Celsius: ")
celsius = ___           # Convert to float
fahrenheit = ___        # Apply the formula
print(f"___ °C = ___ °F")    # Format with 2 decimal places
```

Test with: 0°C (should be 32.00°F), 100°C (should be 212.00°F), and 37°C (body temperature, should be 98.60°F).

### Step 2.3 — Simple Calculator

Build a two-number calculator using `input()`:

```python
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nResults:")
print(f"  {num1} + {num2} = {num1 + num2}")
print(f"  {num1} - {num2} = {num1 - num2}")
print(f"  {num1} × {num2} = {num1 * num2}")
```

For division, add a check: only compute `num1 / num2` if `num2 != 0`; otherwise print "Division by zero is undefined." Use a logical operator (not an if statement yet — we'll cover those in Module 5).

---

## Part 3: f-String Formatting (10 points)

### Step 3.1 — Basic f-String Practice

Rewrite each of the following using f-strings (replace string concatenation with f-strings):

```python
# Original (concatenation style):
name = "Jordan"
grade = 87.654
passed = True

print("Name: " + name)
print("Grade: " + str(round(grade, 1)))
print("Passed: " + str(passed))

# YOUR VERSION (f-string style):
# Rewrite the three print statements above as f-strings
```

### Step 3.2 — Format Specifiers

Using the variables `pi = 3.14159265`, `population = 8100000000`, and `course = "Python"`, write f-strings that produce exactly the following output:

```
Pi rounded to 2 decimal places: 3.14
Pi rounded to 4 decimal places: 3.1416
Population: 8100000000
Population (formatted): 8,100,000,000
Course name: PYTHON
Course (right-aligned, width 20):               Python
```

Hints:
- Use `:.2f` for 2 decimal places
- Use `:,` for thousands separator
- Use `.upper()` inside `{}`
- Use `:>20` for right-alignment in a field of 20 characters

### Step 3.3 — Report Card Generator

Using only hardcoded variables (no `input()` for this step), generate a formatted report card:

```python
student_name = "Morgan Williams"
student_id   = 100234
math_score   = 91.5
english_score = 87.25
science_score = 94.0

average = (math_score + english_score + science_score) / 3

# Generate this exact output using f-strings:
# ================================================
# TEXAS WESLEYAN UNIVERSITY — GRADE REPORT
# ================================================
# Student: Morgan Williams
# ID:      100234
# ------------------------------------------------
# Mathematics:   91.5
# English:       87.3
# Science:       94.0
# ------------------------------------------------
# Average:       90.92
# Status:        PASS
# ================================================
```

Match the spacing and alignment as closely as possible using f-string alignment specifiers.

---

## Part 4: `round()` and Banker's Rounding (5 points)

### Step 4.1 — Predict `round()` Output

Python 3 uses banker's rounding (round half to even). Write your prediction for each:

```python
print(round(0.5))    # Prediction: ___ (even number wins)
print(round(1.5))    # Prediction: ___
print(round(2.5))    # Prediction: ___
print(round(3.5))    # Prediction: ___
print(round(4.5))    # Prediction: ___

print(round(2.675, 2))   # Prediction: ___ (float precision issue!)
print(round(3.14159, 3)) # Prediction: ___
```

After running, write a comment explaining banker's rounding (round half to even) and why this differs from everyday rounding rules. Why might this behavior be preferred in financial applications?

---

## Part 5: Full Program — Student Enrollment System (5 points)

Build a complete program that combines `input()`, type conversion, and f-string formatting:

```python
print("=" * 45)
print("  TEXAS WESLEYAN UNIVERSITY")
print("  Student Enrollment System")
print("=" * 45)

# Collect student information:
full_name    = input("Full Name: ")
student_id   = int(input("Student ID (6 digits): "))
credits      = int(input("Credit hours enrolled: "))
tuition_rate = float(input("Tuition per credit hour ($): "))

# Calculations:
total_tuition = credits * tuition_rate
is_full_time  = credits >= 12

# Display formatted summary:
print("\n" + "=" * 45)
print(f"  ENROLLMENT CONFIRMATION")
print("=" * 45)
print(f"  Name:          {full_name}")
print(f"  Student ID:    {student_id:06d}")     # Padded to 6 digits
print(f"  Credits:       {credits}")
print(f"  Tuition/hr:    ${tuition_rate:.2f}")
print(f"  Total Tuition: ${total_tuition:,.2f}") # Thousands separator
print(f"  Full-Time:     {is_full_time}")
print("=" * 45)
```

Run the program twice with different inputs and include screenshots or copy the output as a comment at the bottom of your file.

---

## Submission Checklist

- [ ] Student header at the top
- [ ] All 5 parts completed and run without errors
- [ ] `try`/`except` blocks in Part 1.1 for invalid conversions
- [ ] Comments explaining `ValueError` vs `TypeError` (Part 1.1)
- [ ] Comments explaining `bool("False")` behavior (Part 1.3)
- [ ] Temperature converter tested with all three values (Part 2.2)
- [ ] f-string format specifiers used correctly (Part 3.2)
- [ ] Banker's rounding explanation written (Part 4.1)
- [ ] Full program run twice with different inputs (Part 5)
- [ ] File saved as `lab04_yourLastName.ipynb` or `.py`

**Submit** to the **Lab 4** assignment in Canvas.

---

## Grading Rubric

| Part | Task | Points |
|---|---|---|
| Part 1 | `int()`/`float()`/`bool()` conversion table, error handling, edge cases | 15 |
| Part 2 | `input()` type handling, temperature converter, calculator | 15 |
| Part 3 | f-string formatting, format specifiers, report card | 10 |
| Part 4 | `round()` predictions and banker's rounding explanation | 5 |
| Part 5 | Complete enrollment system program | 5 |
| **Total** | | **50** |

---

> **Reminder:** Unit Test 1 (covering Modules 1–4) is due at the end of this module week. Review all four module quizzes and the Unit Test study guide before taking the test.

---

*Next: Module 5 Lab — Conditional Statements (if/elif/else)*
