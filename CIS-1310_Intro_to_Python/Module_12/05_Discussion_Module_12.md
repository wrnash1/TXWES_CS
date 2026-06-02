# Discussion Forum: Module 12 — Exception Handling

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Background

This module covered Python's exception handling system — `try`, `except`, `else`, `finally`, the `raise` statement, the exception class hierarchy, the ordering rule for multiple `except` clauses, and custom exceptions. You saw how `finally` runs even with a `return` inside `try`, how `else` is the success-only path, and how placing a broad `except Exception:` before a specific handler creates unreachable code.

Before posting, draw directly on your lab experience. You triggered common exceptions, traced all four clauses with valid and invalid inputs, discovered the ordering bug, used bare `raise` to re-raise while logging, and wrote a custom exception class. What surprised you? What clicked? What do you understand now that you did not before?

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — try/except/else/finally: Four Clauses, One System

In the lab you traced the execution of all four clauses for both a valid input (`'42'`) and an invalid input (`'abc'`). You observed that `else` ran for valid input and was skipped for invalid, while `finally` ran for both. You also saw that `finally` runs before a `return` value is handed back to the caller — even when the `try` block contains an explicit `return` statement.

In 175–225 words, respond to the following:

- Explain in your own words what each of the four clauses is for. When does each one run? Why is `else` useful rather than just putting the success code at the end of the `try` block? What advantage does separating "success code" into `else` give you?
- Describe the `finally`-with-`return` behavior you observed in the lab. Explain why Python designed `finally` to run even in the presence of `return` — what problem does this solve? Give a real-world example of a resource (file, database connection, network socket) where you would always want cleanup to happen, regardless of whether the operation succeeded.
- A classmate argues that `else` is redundant — anything in `else` could just be placed after the `try/except` block. Explain why this is wrong: describe a specific scenario where code placed after the block and code placed in `else` would behave differently.

---

### Scenario B — The except Ordering Rule and Exception Hierarchy

In the lab you placed `except Exception:` before `except ValueError:` and observed that the `ValueError` handler was never reached — `Exception` matched first because `ValueError` is a subclass of `Exception`. You then fixed the ordering to put specific handlers first. You also examined the exception hierarchy and saw that `SystemExit` and `KeyboardInterrupt` are not under `Exception`.

In 175–225 words, respond to the following:

- Explain the ordering rule for `except` clauses in your own words. Why does the Python interpreter match the first `except` clause that fits rather than the most specific one? What is the practical consequence of putting `except Exception:` at the top of a list of handlers?
- In the lab, `ValueError` was caught by `except Exception:` because `ValueError` is a subclass of `Exception`. Explain what "subclass" means in this context — why does catching the parent class also catch all child classes? Use the exception hierarchy diagram from the reading guide to identify two other exceptions that are subclasses of `Exception`.
- Explain why bare `except:` and `except BaseException:` are considered bad practice. What do they catch that `except Exception:` does not, and why is catching those exceptions dangerous in most programs? Describe a scenario where a user would not be able to stop a program because a bare `except:` is swallowing `KeyboardInterrupt`.

---

### Scenario C — raise: Using Exceptions for Input Validation

In the lab you used `raise ValueError(...)` inside `set_age()` to reject negative or unrealistically large ages, wrote a custom `OutOfRangeError` subclass of `ValueError`, and used bare `raise` inside an `except` block to re-raise after logging. You observed that the `except` clause in the outer code caught the exception regardless of whether it was raised directly or re-raised.

In 175–225 words, respond to the following:

- Explain in your own words why raising an exception is sometimes better than returning a special value (like `-1` or `None`) to signal an error. Describe a specific scenario where a function returns `-1` to indicate failure, and explain how a caller could silently ignore that return value, leading to a bug. Show how raising an exception would force the caller to acknowledge the error.
- You wrote a custom `OutOfRangeError` class that inherits from `ValueError`. Explain the benefit of creating a custom exception rather than reusing `ValueError` directly. When would a caller want to catch `OutOfRangeError` specifically, and when would catching `ValueError` be more appropriate?
- Describe the difference between `raise ValueError('message')` and bare `raise` (no argument). In the `process()` function demo you ran in the lab, `process()` caught the exception, printed a log message, and then used bare `raise`. Explain why the outer `except ValueError:` still caught it — what does bare `raise` preserve that a new `raise ValueError(...)` would not?

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top
- Write in complete sentences — not bullet points
- Bold at least two technical terms from the Module 12 glossary
- Include at least one specific reference to your lab experience

---

## Peer Response Requirements

- **Due:** Sunday at 11:59 PM CST
- Respond to **at least two classmates** who chose **different scenarios**
- Each response: minimum **60 words**, must add substance
- Acceptable contributions: extend their example, challenge a claim, ask a follow-up question, share a related experience from your own lab, offer an alternative approach

---

## Grading Rubric — 10 Points Total

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 5–6 pts | All parts of the scenario addressed accurately. Two or more glossary terms correctly bolded. Specific lab reference included. 175–225 words. Complete sentences. |
| 3–4 pts | Most parts addressed but lacks depth, missing a glossary term, or no lab reference. Close to word count. |
| 1–2 pts | Significant parts missing or well below word count. |
| 0 pts | Not submitted. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 pts | Two or more responses to classmates with different scenarios. Each 60+ words and adds genuine value. |
| 2 pts | One peer response only, or responses lack technical substance. |
| 0 pts | No peer responses. |

---

## Tips for a Strong Post

**Scenario A: Use a concrete resource example for finally.** The strongest posts pick a specific resource — a database connection, a log file, a network socket — and trace exactly what happens if an exception occurs midway through using it. Without `finally`, the resource stays open. With `finally`, cleanup always happens. The argument against putting code after the block is also concrete: if the exception is unhandled (no matching `except`), code after the block never runs, but `finally` always does.

**Scenario B: Trace the hierarchy with a real example.** The best posts show a specific call — `except Exception:` catching `ZeroDivisionError` — and trace through the hierarchy: `ZeroDivisionError → ArithmeticError → Exception → BaseException`. They explain that every `except` clause is asking "is this exception an instance of this class or any of its subclasses?" which is why parent classes match child exceptions.

**Scenario C: The -1 return value antipattern is powerful.** The clearest Scenario C posts show real code where `-1` is returned on error, then show a caller that uses the return value in arithmetic without checking it — `total = total + get_price(item)` where `get_price` returns -1 for invalid items. Total silently becomes wrong. An exception forces the caller to handle the failure explicitly before proceeding.
