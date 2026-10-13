# Lab Activity: Module 16 — Final Exam Submission

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Objective

Schedule and complete the official **JSE (Certified Associate in JavaScript Programming)** industry certification exam, and submit your score verification report to Professor Nash.

---

## Part 1 — Exam Registration

### Step 1 — Create an OpenEDG Account

The JSE exam is administered through the OpenEDG platform. If you do not already have an account:

1. Visit [https://edube.org](https://edube.org).
2. Click **Register** and create a free account using your university email address.
3. Verify your email.

### Step 2 — Locate the JSE Exam

1. Log in to your OpenEDG account.
2. Navigate to **Certifications** → **JS Institute** → **JSE — Certified Associate in JavaScript Programming**.
3. Review the exam description and confirm the format: 30 questions, 45 minutes, 70% passing score.

### Step 3 — Schedule or Purchase

- If Texas Wesleyan University has provided exam vouchers: enter your voucher code at checkout.
- If purchasing independently: complete payment to receive access.
- The exam may be taken online (proctored via webcam) or at an authorized testing center. Confirm which option applies for your section with Professor Nash.

---

## Part 2 — Exam Preparation Checklist

Complete this checklist before sitting for the exam.

### Knowledge Verification

- [ ] I can explain the difference between `let`, `const`, and `var` (scope, hoisting, re-assignability).
- [ ] I know what `typeof null` returns and why.
- [ ] I know the seven primitive types in JavaScript.
- [ ] I can explain loose vs strict equality (`==` vs `===`) including the `null == undefined` case.
- [ ] I know the return value of `map`, `filter`, `reduce`, and `forEach`.
- [ ] I can write a function using rest parameters and call it using spread.
- [ ] I understand why arrow functions cannot be used as constructors.
- [ ] I can explain what `for...in` vs `for...of` iterates over.
- [ ] I understand event bubbling and can describe `event.target` vs `event.currentTarget`.
- [ ] I can write a `Promise` from scratch with `resolve` and `reject`.
- [ ] I know the behavior of `Promise.all` vs `Promise.allSettled`.
- [ ] I understand why `fetch` resolves for 404 responses and how to detect HTTP errors.
- [ ] I can write a `try/catch/finally` block and explain when `finally` runs.
- [ ] I can write a custom error class that correctly sets `this.name`.
- [ ] I know all six built-in error types and which situation triggers each.

### Practice Confidence

- [ ] I have completed all 15 course quizzes.
- [ ] I have reviewed all questions I answered incorrectly and understand why the correct answer is right.
- [ ] I can write the following from memory without reference:
  - A closure that maintains state across multiple calls
  - An `async` function that fetches data, checks `response.ok`, and handles errors
  - A class with a subclass that uses `super()` and overrides a method
  - An event-delegated click handler using `event.target.closest()`

### Logistics

- [ ] I have confirmed my exam date, time, and location (online or testing center).
- [ ] I have a government-issued photo ID ready (required for proctored exams).
- [ ] I have tested my webcam and microphone if taking the exam online.
- [ ] I know the exam rules: no notes, no reference materials, no second monitors for proctored sessions.

---

## Part 3 — Complete the Exam

Sit for the JSE — Certified Associate in JavaScript Programming exam.

**During the exam:**

- Read every question carefully — watch for the word "not" in question stems.
- Answer every question — there is no penalty for guessing.
- Flag uncertain questions and return to them after answering the rest.
- You have 90 seconds per question on average; most questions take less than 30 seconds.

---

## Part 4 — Score Report Submission

After completing the exam:

1. Download your official score report PDF from your OpenEDG account. The report must show:
   - Your full name
   - The exam title (JSE — Certified Associate in JavaScript Programming)
   - Your score or pass/fail status
   - The exam date

2. Upload the score report PDF to the Canvas LMS assignment box for this module.

**Note on score:** The course grade for this lab is based on submission of your official score report — not on whether you passed. Students who do not pass on their first attempt are encouraged to schedule a retake. JSE exam policies allow multiple attempts.

---

## Part 9 — Challenge Exercise

**Optional.** This section is not graded and does not affect your lab score. Complete it after your exam or as part of your final review if you want to verify your readiness at a deeper level. Each step asks you to write code from memory, without looking at notes or course materials.

### Step 1 — Cross-Domain Coding Sprint

Write each of the following programs from scratch in a single JavaScript file. Do not reference notes or previous labs. Time yourself — each should take no more than five minutes.

1. A `counter` factory function that returns an object with `increment()`, `decrement()`, and `value()` methods. Each method must work correctly using a closure — no `class` syntax allowed.

2. An `EventEmitter` class with `on(event, fn)`, `off(event, fn)`, and `emit(event, ...args)` methods. `emit` must call all registered listeners for the event, passing `...args` to each. `off` must remove only the specific function reference.

3. An `async` function `loadAll(urls)` that accepts an array of URL strings, fetches all of them in parallel using `Promise.all`, checks `response.ok` on each, and returns an array of parsed JSON objects. If any request fails (non-2xx status or network error), the function should throw with a message that includes the failing URL.

After writing each program, open the browser DevTools console, paste your code, and confirm it behaves correctly with test inputs of your choosing.

### Step 2 — JSE High-Frequency Question Bank

Without looking at the Reading Guide, write your answers to all 15 High-Frequency Exam Topics from memory. For each item, write:

- The fact itself (one sentence)
- A short code snippet that demonstrates it
- A brief explanation of why beginners commonly get it wrong

Example format for one item:

```
Topic: typeof null
Fact: typeof null === 'object', not 'null'
Code: console.log(typeof null);  // 'object'
Why tricky: null is a primitive with no properties,
            but its type string is 'object' due to a
            legacy bug in the original JavaScript spec.
```

Produce all 15 entries, then compare your answers to the High-Frequency Exam Topics section in the Reading Guide. For any entry where your explanation was incomplete or incorrect, write a corrected version and note what you missed.

### Step 3 — Debugging Challenge

The following code contains **four bugs** — each is a distinct, realistic mistake that the JSE exam tests. Identify all four bugs, state what each bug is and why it is wrong, and write a corrected version of the entire function.

```javascript
class UserAccount {
  constructor(name, balance) {
    this.name = name
    this.balance = balance
  }

  deposit(amount) {
    if (amount <= 0) {
      throw 'Amount must be positive'
    }
    this.balance += amount
    return this.balance
  }

  static summary(accounts) {
    const total = accounts.forEach(a => a.balance)
    return { count: accounts.length, total }
  }
}

class PremiumAccount extends UserAccount {
  constructor(name, balance, tier) {
    this.tier = tier
    super(name, balance)
  }

  deposit(amount) {
    const bonus = tier === 'gold' ? amount * 0.1 : 0
    return super.deposit(amount + bonus)
  }
}
```

The four bugs involve: error handling best practice, array method return value, subclass constructor order, and a missing `this` reference. Write your corrected file, then test it in the DevTools console to confirm all four methods work correctly.

---



| Requirement | Points |
|---|---|
| Score report PDF submitted with required information | Full credit |
| Score report missing (late or not submitted) | 0 |

Contact Professor Nash before the submission deadline if you encounter registration or scheduling problems.
