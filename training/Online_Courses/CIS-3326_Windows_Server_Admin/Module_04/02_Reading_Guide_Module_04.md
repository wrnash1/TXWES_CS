# Reading Guide: Module 04 - File Services
## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction
Welcome to **Module 04 - File Services**! This week's study material focuses on the core foundations and configuration mechanics of **File Services** as aligned with the **3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **DFS Namespaces (DFSN)**: Allows you to group shared folders located on different servers into one logically structured namespace. Instead of mapping a drive to `\\ServerA\HR` and `\\ServerB\IT`, users just go to `\\corp.local\Files` and see both.
*   **DFS Replication (DFSR)**: An efficient, multiple-master replication engine that keeps folders synchronized across multiple servers (e.g., syncing a file server in Dallas with one in London).
*   **File Server Resource Manager (FSRM)**: A suite of tools that allows administrators to set Quotas (limiting how much space a user can consume) and File Screens (preventing users from saving MP3s or MP4s to the company server).
*   **Focus Area**: Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap**: Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource**: To reinforce these concepts visually, review this targeted search query: [YouTube Exam Study Reference Link](https://www.youtube.com/results?search_query=3326_Windows_Server_Admin+-+Microsoft+Windows+Server+Administration+%28Active+Directory%29+File+Services).

---

### 2. Certification Exam Tips
*   **Focus Area:** Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap:** Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource:** To reinforce these concepts visually, review this targeted search query: [YouTube Exam Study Reference Link](https://www.youtube.com/results?search_query=3326_Windows_Server_Admin+-+Microsoft+Windows+Server+Administration+%28Active+Directory%29+File+Services).

---

### Lab & Command Integration
In this week's hands-on lab, you will run command sequences to verify configuration files and check service statuses. Make sure to execute administrative commands using elevated privileges (sudo/Administrator) and review console outputs for errors.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Watch the curated YouTube study streams matching **File Services**.
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
