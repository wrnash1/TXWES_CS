# Reading Guide: Module 03 - GPOs
## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction
Welcome to **Module 03 - GPOs**! This week's study material focuses on the core foundations and configuration mechanics of **GPOs** as aligned with the **3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **User Configuration vs. Computer Configuration**: Every GPO has two halves. Computer policies apply when the machine boots up (e.g., software installation). User policies apply when the human logs in (e.g., mapped drives, folder redirection).
*   **Enforce / Block Inheritance**: You can right-click a GPO and set it to "Enforced", meaning no lower-level OU can override it. Conversely, you can right-click an OU and "Block Inheritance", preventing higher-level GPOs from flowing down.
*   **gpupdate /force**: The command-line tool used on a client computer to force it to pull the latest Group Policies immediately, rather than waiting the standard 90 minutes.

---

### 2. Certification Exam Tips
*   **Focus Area:** Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap:** Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource:** To reinforce these concepts visually, review this targeted search query: [YouTube Exam Study Reference Link](https://www.youtube.com/results?search_query=3326_Windows_Server_Admin+-+Microsoft+Windows+Server+Administration+%28Active+Directory%29+GPOs).

---

### Lab & Command Integration
In this week's hands-on lab, you will run command sequences to verify configuration files and check service statuses. Make sure to execute administrative commands using elevated privileges (sudo/Administrator) and review console outputs for errors.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Watch the curated YouTube study streams matching **GPOs**.
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
