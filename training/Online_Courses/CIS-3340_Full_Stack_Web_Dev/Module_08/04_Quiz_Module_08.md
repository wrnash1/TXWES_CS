# Quiz: Module 08 - Server-Side Routing & Middleware
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Question 1
What function must be invoked at the end of a custom Express middleware handler to pass control to the next function in line?

*   A) end()
*   B) send()
*   C) next()
*   D) forward()

---

### Answer Key
*   **Correct Option:** **C**

---

### Explanation
Invoking the next() callback tells Express to progress to the subsequent handler in the pipeline.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Failing to call next() will cause the request to hang.
