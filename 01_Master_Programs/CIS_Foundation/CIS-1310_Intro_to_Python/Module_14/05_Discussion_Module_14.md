# Discussion Forum: Module 14 — Object-Oriented Programming: Basics

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Background

This module introduced Python's object-oriented programming system — class definitions, `__init__`, `self`, instance variables, instance methods, `__str__`, class variables, and `isinstance()`. You created a `Dog` class from scratch, triggered the `self`-omission `TypeError` and read its message, demonstrated the class variable shadowing trap, added `__str__` and watched `print()` output transform from a memory address to something readable, and built a complete `BankAccount` class with encapsulation using a protected `_balance` attribute.

Before posting, draw directly on your lab experience. What was the most surprising behavior you encountered? Did the class variable shadowing trap catch you off guard? What did the `TypeError` message tell you that helped you understand what `self` actually does?

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — `self` and `__init__`: How Instance Variables Are Created

In the lab you saw that omitting `self` from a method definition causes `TypeError: method() takes 0 positional arguments but 1 was given`. You also observed that `self.name = name` inside `__init__` creates an instance variable that persists on the object, while a plain local variable `name = name` (without `self.`) would disappear when `__init__` returned.

In 175–225 words, respond to the following:

- Explain in your own words what `self` refers to and why Python requires it as the first parameter of every instance method. Why does Python not just automatically know which object a method belongs to without an explicit `self`?
- Describe the difference between `self.name = name` and just `name = name` inside `__init__`. What happens to each variable after `__init__` returns? Which one is accessible as `d.name` on the object, and why?
- In the lab you triggered `TypeError: bark() takes 0 positional arguments but 1 was given`. Explain what the error message is telling you in your own words — where does "1 was given" come from, and why does Python count it as an argument?

---

### Scenario B — Class Variables vs Instance Variables

In the lab you observed that `Dog.species = 'Changed'` updated the class variable visible to all instances, but `d1.species = 'Override'` created a new instance variable on `d1` only — leaving `d2.species` and `Dog.species` unchanged. This shadowing behavior is a classic Python exam trap.

In 175–225 words, respond to the following:

- Explain in your own words the difference between a class variable and an instance variable. Where is each one stored? Who "owns" each one?
- Walk through the shadowing scenario step by step: start with `class Dog: species = 'Canine'`, create two instances, then execute `d1.species = 'Override'`. Describe exactly what exists in memory at each step — what does `d1.__dict__` contain? What does `d2.__dict__` contain? What does `Dog.__dict__` contain?
- Describe a real-world use case where a class variable makes sense — where you would want data shared across all instances — and a real-world use case where an instance variable is required. Use specific examples like a `BankAccount` class or a `Student` class.

---

### Scenario C — `__str__` and Encapsulation

In the lab you added `__str__` to the `Dog` class and observed `print(d)` transform from `<__main__.Dog object at 0x7f...>` to a readable string. You also built `BankAccount` with a protected `_balance` attribute and public methods (`deposit`, `withdraw`, `get_balance`) as the controlled interface to that data.

In 175–225 words, respond to the following:

- Explain why `__str__` exists and what problem it solves. What does Python output if `__str__` is not defined? When you define `__str__`, what are the two requirements it must satisfy (hint: think about parameters and return type)?
- In the `BankAccount` class, `_balance` is a protected attribute accessed only through `deposit()`, `withdraw()`, and `get_balance()`. Explain what **encapsulation** means in this context. What problem does it prevent? Give a specific example of a bug that could occur if `_balance` were freely modifiable from outside the class without validation.
- A classmate argues that using `_balance` instead of just `balance` is "just a naming convention — Python doesn't actually enforce it, so why bother?" Respond to this argument. Even though Python does not prevent access to `_balance`, why does the convention still matter in a team or production codebase?

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top
- Write in complete sentences — not bullet points
- Bold at least two technical terms from the Module 14 glossary
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

**Scenario A: The `self` question has a deeper answer than "Python requires it."** The strongest posts explain that Python's method call mechanism is `Dog.bark(d)` under the hood — `d.bark()` is syntactic sugar. Without an explicit `self` parameter, Python has no place to put the instance it is passing. The local variable trap (`name = name` vs `self.name = name`) is also powerful: show that a local variable inside `__init__` disappears when the function returns, so accessing `d.name` afterward would raise `AttributeError`.

**Scenario B: Use `__dict__` to make the memory picture concrete.** After `d1.species = 'Override'`, print `d1.__dict__`, `d2.__dict__`, and `Dog.__dict__`. Students who include actual dict contents make the shadowing mechanism visible and undeniable. A good real-world example for class variables is a shared counter (how many accounts have been created), and a good instance variable example is the account balance itself (each account has its own, different value).

**Scenario C: The encapsulation argument is about contract, not enforcement.** The strongest posts explain that `_balance` signals to every developer reading the code "do not touch this directly — use the methods." Even though Python allows `acc._balance = -99999`, the underscore is a promise about the interface. In a production codebase, a developer who respects `_balance` as internal will naturally route all changes through `deposit()` and `withdraw()`, ensuring validation always runs. The convention is a team communication tool, not just a personal style choice.
