# Reading Guide: Module 03 - Application Attacks and Software Vulnerabilities
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 03 – Application Attacks and Software Vulnerabilities**! This module covers the attack techniques that target software and web applications directly. SY0-701 tests these heavily in scenario-based questions where you must identify the attack type from a description and select the correct mitigation. Understanding how these attacks work at a conceptual level is more important than memorizing syntax.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SQL Injection (SQLi)**: An attack where malicious SQL statements are inserted into an input field and executed by the backend database. SQLi can allow an attacker to bypass authentication (entering `' OR '1'='1` as a username), dump entire databases, or delete data. The primary defense is parameterized queries (prepared statements), not input filtering alone.
*   **Cross-Site Scripting (XSS)**: An attack that injects malicious client-side scripts (typically JavaScript) into web pages viewed by other users. Stored XSS persists in the database; Reflected XSS is embedded in a URL and reflected back. XSS targets the user's browser, not the server. Defense: output encoding and Content Security Policy (CSP).
*   **Buffer Overflow**: An attack that writes more data to a memory buffer than it can hold, overwriting adjacent memory. This can corrupt program execution or allow an attacker to inject and execute shellcode. Buffer overflows are a classic vulnerability in C/C++ applications that lack bounds checking. Defense: ASLR, DEP/NX, and safe coding practices.
*   **Cross-Site Request Forgery (CSRF)**: An attack that tricks an authenticated user's browser into sending an unauthorized request to a web application where they are already logged in. For example, a malicious link could silently transfer funds from a banking session. Defense: anti-CSRF tokens and SameSite cookie attributes.
*   **Directory Traversal**: An attack that manipulates file path inputs (e.g., `../../etc/passwd`) to access files and directories outside the intended web root. It exploits insufficient input validation on file path parameters. Defense: canonicalize and validate all file path inputs server-side.
*   **Race Condition (TOCTOU)**: A Time-Of-Check to Time-Of-Use vulnerability where an attacker manipulates a resource between when it is checked and when it is used. These vulnerabilities are common in multi-threaded applications and are difficult to exploit reproducibly. Defense: atomic operations and proper file locking.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Application attacks fall under **Domain 2 – Threats, Vulnerabilities, and Mitigations (22%)** of SY0-701. Expect scenario questions that describe attacker input and ask you to name the vulnerability class.
*   **SQLi vs. XSS Trap:** Both inject malicious code via input fields, but SQLi targets the server's database while XSS targets other users' browsers. If the attack runs in the victim's browser, it is XSS. If it manipulates database queries, it is SQLi.
*   **Memorize Defenses:** For every attack type, know the canonical defense: SQLi → parameterized queries; XSS → output encoding/CSP; CSRF → anti-CSRF tokens; Buffer overflow → ASLR + DEP; Directory traversal → input validation and path canonicalization.
*   **OWASP Top 10 Overlap:** SY0-701 aligns closely with the OWASP Top 10. Injections, broken authentication, XSS, and insecure direct object references all appear in exam scenarios. Familiarity with OWASP terminology is directly applicable.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include dedicated application attack sections with visual diagrams showing how each attack works step-by-step.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Application Attacks" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Pay close attention to the attack mechanism and the corresponding defensive control for each vulnerability type.
*   **Required Video:** Watch the application attack video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos use realistic web application examples to demonstrate each attack type.

---

### Lab & Command Integration
In this week's hands-on lab, you will interact with a deliberately vulnerable web application to observe SQL injection and XSS in a safe, controlled environment. The goal is to understand the attacker's perspective so you can recognize these attacks in SY0-701 performance-based questions (PBQs).

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to explain each attack mechanism and its primary defense.
- [ ] Read the "Application Attacks" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the application attack video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Create a two-column reference card: attack type on the left, primary defense on the right.
- [ ] Proceed to the weekly hands-on lab activity.
