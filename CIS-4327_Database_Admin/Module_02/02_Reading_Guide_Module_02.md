# Reading Guide: Module 02 - Spanner
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

### Introduction
Welcome to **Module 02 - Spanner**! This week's study material focuses on the core foundations and configuration mechanics of **Spanner** as aligned with the **4327_Database_Admin - Google Cloud Associate Database Engineer** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Synchronous vs Asynchronous Replication**: HA in Cloud SQL uses *synchronous* replication (data must be written to both zones before returning success). Read Replicas use *asynchronous* replication.
*   **Failover Process**: During a failover, the primary instance is stopped, the persistent disk is attached to the standby instance, and the standby becomes the new primary. Connections are briefly dropped and must be re-established by the client application.
*   **Point-in-Time Recovery (PITR)**: PITR requires automated backups to be enabled. It allows restoration to any point within the retention period (usually up to 7 days).
*   **Focus Area**: Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap**: Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource**: To reinforce these concepts visually, review this targeted search query: [SQL & Database Administration Course by freeCodeCamp - Spanner](https://www.youtube.com/watch?v=HXV3zeQKqGY).
*   **Deliverable**: Configure and execute this validation step in your lab environment, verifying exit codes and logging output files.

---

### 2. Certification Exam Tips
*   **Focus Area:** Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap:** Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource:** To reinforce these concepts visually, review this targeted search query: [SQL & Database Administration Course by freeCodeCamp - Spanner](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section/chapter covering **Spanner** in the OER Textbook: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** Watch the video lecture on **Spanner** in the official course playlist: [SQL & Database Administration Course by freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Deliverable:**: Configure and execute this validation step in your lab environment, verifying exit codes and logging output files.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section/chapter covering **Spanner** in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the video lecture on **Spanner** in [SQL & Database Administration Course by freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
