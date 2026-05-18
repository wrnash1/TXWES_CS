# Video Resources: Module 3 — Operators

**Course:** CIS-1310 Introduction to Python Programming
**Institution:** Texas Wesleyan University
**Module Topic:** Arithmetic operators, precedence, comparison, logical (and/or/not), bitwise, identity, membership

> Choose the resources that match your learning style. All are free.

---

## Primary Video Resources

### 1. Python Operators — Programming with Mosh
**Channel:** Programming with Mosh
**Search:** `"Python Operators" Programming with Mosh beginners`
**Direct Link:** [https://www.youtube.com/watch?v=kqtD5dpn9C8](https://www.youtube.com/watch?v=kqtD5dpn9C8) (jump to arithmetic operators section ~30:00)
**Covers for Module 3:** Arithmetic operators, comparison operators, logical operators
**Why Watch:** Mosh provides clear visual comparisons for how Python operators differ from what you may have seen in other languages. Pay special attention to his treatment of `//` and `%`.

---

### 2. Python Operators Full Tutorial — Corey Schafer
**Channel:** Corey Schafer
**Search:** `"Python Operators" Corey Schafer`
**Playlist:** [https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
**Covers for Module 3:** Comparisons, logical operators (and/or/not), short-circuit evaluation
**Why Watch:** Corey covers `and`/`or` value return behavior — the non-obvious fact that these operators don't just return `True`/`False` — which is directly tested on the PCAP exam.

---

### 3. Python Operator Precedence Explained
**Search:** `"Python operator precedence PEMDAS tutorial"`
**Why Watch:** Step-by-step walkthrough of how Python determines evaluation order with examples of surprising results (like `-2**2 == -4`). Strongly recommended for Part 2 of the lab.

---

### 4. Python Bitwise Operators — Real Python
**Channel:** Real Python
**Search:** `"Python Bitwise Operators Real Python"`
**Direct Link:** [https://realpython.com/python-bitwise-operators/](https://realpython.com/python-bitwise-operators/) (article with embedded explanations)
**Covers for Module 3:** All bitwise operators, binary representation, shift operations
**Why Watch/Read:** Bitwise operators appear on the PCAP exam. This Real Python tutorial explains them visually with binary representations, making the concept much easier to understand than reading text descriptions alone.

---

## Supplemental Resources

### 5. Python Short-Circuit Evaluation Explained
**Search:** `"Python short circuit evaluation and or tutorial"`
**Why Watch:** Demonstrates why `x and f(x)` is safe even when `f(x)` would crash if `x` were `0` or `None`. This pattern appears in real-world Python code constantly.

### 6. Python `is` vs `==` — What's the Difference?
**Search:** `"Python is vs == identity equality explained"`
**Why Watch:** Many beginners incorrectly use `is` to compare strings and numbers. This type of video shows exactly when `is` returns unexpected results and why you should use `==` for value comparison.

### 7. Python Modulo Operator — Use Cases
**Search:** `"Python modulo operator use cases tutorial"`
**Why Watch:** Covers practical applications: even/odd detection, cyclical counters (clock arithmetic), and FizzBuzz — a classic coding interview problem that uses modulo.

---

## Official Documentation

### Python Operator Precedence Table
**Link:** [https://docs.python.org/3/reference/expressions.html#operator-precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
**Why Read:** The definitive reference table. Print or bookmark this — you will refer to it throughout the course and it is what the PCAP exam is tested against.

### edube.org PE1 Module 2 — Operators Section
**Link:** [https://edube.org/](https://edube.org/)
**Why Use:** Interactive exercises with the exact operator types and precedence questions that appear on the PCAP exam. Complete all operator exercises in this module.

---

## Video Watching Guide

| Video | Estimated Time | Best For |
|---|---|---|
| Programming with Mosh — operators (30:00+) | 20 min | Quick overview |
| Corey Schafer — comparison & logical | 20 min | `and`/`or` return values |
| Python precedence walkthrough | 15 min | Lab Part 2 prep |
| Real Python bitwise article | 30 min | PCAP bitwise questions |
| edube.org Module 2 exercises | 45–60 min | Exam practice |

**Total suggested time:** 1.5–2.5 hours

---

> **Note for Instructor:** When recording your own Module 3 lecture, recommended demonstration order: (1) arithmetic operators with type observations on `/` vs `//`, (2) precedence surprises like `-2**2` and `2**3**2`, (3) logical operator short-circuit demo showing `0 and (10/0)` not crashing, (4) `and`/`or` value return demo, (5) `is` vs `==` with a list example. Place your Canvas Media link here when ready.
