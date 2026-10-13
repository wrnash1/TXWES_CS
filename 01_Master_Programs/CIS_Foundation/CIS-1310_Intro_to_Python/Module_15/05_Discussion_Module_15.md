# Discussion Forum: Module 15 — Advanced OOP: Inheritance and Polymorphism

## Course: CIS-1310 Introduction to Python

**Certification Alignment:** PCAP — Certified Associate in Python Programming (Python Institute)

---

## Background

This module covered inheritance, `super()`, method overriding, polymorphism, and the Method Resolution Order. You built a three-level `Animal → Dog/Cat/Duck` hierarchy, observed that omitting `super().__init__()` causes `AttributeError` when accessing parent attributes, used `super()` both in `__init__` and inside an overriding method to extend rather than replace parent behavior, demonstrated polymorphism with a list of mixed objects all responding to `.speak()`, and traced the MRO with `ClassName.__mro__`.

You also built the `shapes.py` hierarchy where `Square` inherits from `Rectangle` and both inherit from `Shape` — and observed that an inherited `describe()` method calls `self.area()` which routes to the correct override at runtime.

Before posting, draw directly on your lab experience. What surprised you about how `super()` works? Did the Quiz Question 10 result — an inherited method calling an overridden method through `self` — feel intuitive or surprising?

---

## Discussion Prompt

### Choose ONE scenario and state your choice at the top of your post

---

### Scenario A — Inheritance and `super().__init__()`

In the lab you observed that omitting `super().__init__()` in `Dog.__init__` causes `AttributeError: 'Dog' object has no attribute 'name'`. You also saw that when `Dog` does not define `__init__` at all, Python automatically uses `Animal.__init__` and everything works.

In 175–225 words, respond to the following:

- Explain in your own words what `super().__init__()` does. Where does the call go, and what does it accomplish? What is the consequence of omitting it when the child class defines its own `__init__`?
- Describe the difference between these two situations: (1) `Dog` does not define `__init__` at all, and (2) `Dog` defines `__init__` but omits `super().__init__()`. In which case does `self.name` exist on the object, and why?
- In the lab you also used `super().describe()` inside `Car.describe()` to incorporate the parent's output and add to it. Explain why this is better than copying the parent's logic into the child method. What happens if the parent's `describe()` is later updated — which approach requires changes in the child?

---

### Scenario B — Method Overriding and Polymorphism

In the lab you created `Dog`, `Cat`, and `Duck` each with their own `speak()` method, placed them in a list, and looped through calling `.speak()` on each. You also observed Quiz Question 10 where an inherited `describe()` method called `self.area()` and Python routed the call to `Square.area()` — not `Shape.area()` — because `self` was a `Square` instance at runtime.

In 175–225 words, respond to the following:

- Explain in your own words what method overriding is. When both the parent and child define `speak()`, which version is called and why? Trace the Method Resolution Order lookup step by step for `d.speak()` where `d` is a `Dog`.
- Describe the polymorphism pattern demonstrated in the lab: a list of mixed `Animal` subclasses all responding to `.speak()`. Explain why this is useful — specifically, what would the code look like if you used `if isinstance(a, Dog): ... elif isinstance(a, Cat): ...` instead, and why is that approach worse?
- Quiz Question 10 shows that an inherited `describe()` calls `self.area()` and gets `Square.area()` even though `describe()` was defined on `Shape`. Explain this behavior. What is `self` inside `Shape.describe()` at the moment `s.describe()` is called, and why does that matter for which `area()` runs?

---

### Scenario C — Inheritance Design: is-a vs has-a

In the lab you built `Square(Rectangle)` — a `Square` inheriting from `Rectangle` with `width == height`. You also traced that `isinstance(sq, Rectangle)` returns `True`, and that `Square.__mro__` is `(Square, Rectangle, Shape, object)`. The reading guide introduced the is-a vs has-a distinction.

In 175–225 words, respond to the following:

- Explain the is-a vs has-a distinction in your own words. Give a concrete example of each: one relationship that correctly uses inheritance (is-a) and one that should use composition (has-a). Use classes you could plausibly write yourself — not just the Animal/Dog example.
- The classic "Square is a Rectangle" debate: is it always true that a `Square` should inherit from `Rectangle`? Describe a scenario where this breaks down — specifically, if `Rectangle` has a `set_width()` and `set_height()` method, what happens when you call `set_width(5)` on a `Square(4)` object? What does this violate?
- In the lab, `isinstance(sq, Rectangle)` returning `True` was useful for polymorphism — a function that accepts any `Rectangle` can accept a `Square`. Describe a practical programming scenario where knowing `isinstance(obj, ParentClass)` is `True` actually helps you write cleaner code — where you would call a parent-class method on the object without needing to know the exact subtype.

---

## Initial Post Requirements

- **Due:** Wednesday at 11:59 PM CST
- **Length:** 175–225 words
- State your chosen scenario at the top
- Write in complete sentences — not bullet points
- Bold at least two technical terms from the Module 15 glossary
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

**Scenario A: The `super()` question has two distinct answers.** The strongest posts clearly separate the two cases: (1) no `__init__` in child — Python automatically uses the parent's — and (2) child defines `__init__` but forgets `super()` — the parent's never runs, parent attributes do not exist. The extend-vs-replace point is concrete: if `Vehicle.describe()` is later updated to include a fuel type, `Car.describe()` using `super().describe()` automatically benefits. `Car.describe()` that copied the logic manually must be updated separately.

**Scenario B: The MRO trace makes the abstract concrete.** Walk through `d.speak()` step by step: Python looks in `Dog` → finds `speak()` → calls it. If `Dog` had no `speak()`, Python would look in `Animal` → find it → call it. The if/isinstance alternative is a maintenance nightmare: adding a new animal type requires editing the if-chain. With polymorphism, the new class just implements `speak()` and the existing loop needs no changes. The Quiz 10 insight — `self` inside an inherited method is still the child instance — is one of the most important OOP concepts to internalize.

**Scenario C: The Square-Rectangle debate is a classic computer science argument.** The best posts engage with it genuinely. If `set_width()` and `set_height()` exist on `Rectangle`, calling either on a `Square` violates the "squareness" invariant — the sides are no longer equal. This violates the Liskov Substitution Principle: a `Square` cannot safely substitute for a `Rectangle` everywhere. However, if `Rectangle` is immutable (you cannot change width/height independently after construction), the relationship is fine. The practical `isinstance` example is clearest with collection processing: a function that calls `.area()` on any `Shape` — it does not need to know if it is a `Circle`, `Square`, or `Triangle`.
