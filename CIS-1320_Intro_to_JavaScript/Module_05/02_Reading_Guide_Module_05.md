# Reading Guide: Module 05 - Loops & Iteration
## Course: CIS-1320_Intro_to_JavaScript (JSE (Certified Associate in JavaScript Programming))

---

### Introduction
Welcome to **Module 05 - Loops & Iteration**! This week you will learn how to repeat blocks of code efficiently using `for`, `while`, and `do-while` loops, and how to control loop flow with `break` and `continue`. Loops are one of the most-tested topics on the JSE exam because errors in loop conditions and off-by-one mistakes are extremely common.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **for loop**: A loop construct with three optional expressions in its header: initialization (`let i = 0`), condition (`i < 10`), and update (`i++`). The loop body runs repeatedly as long as the condition is truthy. It is best used when the number of iterations is known in advance.
*   **while loop**: A loop that checks its condition before each iteration and runs the body only while the condition is truthy. If the condition is initially false, the body never executes. It is best used when the number of iterations is not known in advance.
*   **do-while loop**: A loop that executes its body first and then checks the condition. This guarantees the body runs at least once regardless of the condition, making it useful for prompting users or retrying operations.
*   **break statement**: A statement that immediately exits the nearest enclosing loop or `switch` block, transferring control to the first statement after the loop. It is used to stop iteration early when a target condition is found.
*   **continue statement**: A statement that skips the remainder of the current loop iteration and jumps to the loop's update expression (in a `for` loop) or back to the condition check (in `while`/`do-while`). It does not exit the loop; it just skips one cycle.
*   **Infinite loop**: A loop whose condition never evaluates to `false`, causing it to run forever and freeze the browser tab or runtime. Common causes include forgetting to increment the loop variable or using an always-truthy condition such as `while (true)` without a `break`.

---

### 2. Certification Exam Tips
*   **Focus Area:** The JSE exam tests off-by-one errors. Know whether a loop runs with `<` vs `<=` — for example, `for (let i = 0; i < 5; i++)` runs 5 times (indices 0–4), but `for (let i = 0; i <= 5; i++)` runs 6 times (indices 0–5).
*   **Scenario Trap:** Watch for questions showing a `while` loop where the loop variable is never updated. Recognize this as an infinite loop and select the answer that adds the missing increment or a `break` condition.
*   **Study Resource:** The [MDN – for statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for) page includes a table of all loop types and interactive examples. Also review [MDN – break](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break) and [MDN – continue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue) for their exact behavior.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read **Chapter 2 – Program Structure** of [Eloquent JavaScript](https://eloquentjavascript.net/) (free online book). The "Loops" section covers `for`, `while`, and `do` loops with worked examples.
*   **Required Video:** Watch the video lecture on **Loops & Iteration** in the official course playlist: [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg) (focus on the for/while/do-while loop segments).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a for loop that prints numbers 1 to 10**: Use `for (let i = 1; i <= 10; i++)` and log each value; confirm exactly 10 lines appear in the console.
*   **Write a while loop that processes an array**: Use an index variable and a `while` loop to iterate through an array, logging each element until the index reaches the array's length.
*   **Use continue to skip printing odd numbers**: Inside a `for` loop from 1 to 20, use `if (i % 2 !== 0) continue;` to print only even numbers.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read Chapter 2 of [Eloquent JavaScript](https://eloquentjavascript.net/).
- [ ] Watch the loops and iteration segments of the [JavaScript for Beginners Playlist](https://www.youtube.com/watch?v=PkZNo7MFNFg).
- [ ] Review the steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
