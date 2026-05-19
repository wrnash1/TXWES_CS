# Reading Guide: Module 04 - Security
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

### Introduction
Welcome to **Module 04 - Security**! This week's study material focuses on the core foundations and configuration mechanics of **Security** as aligned with the **4327_Database_Admin - Google Cloud Associate Database Engineer** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Encryption at Rest**: By default, Google Cloud encrypts all customer data at rest using Google-managed encryption keys. If your company requires absolute control over the keys due to compliance, you must configure Customer-Managed Encryption Keys (CMEK) via Cloud Key Management Service (KMS).
*   **Cloud SQL Proxy**: A secure way to connect to your Cloud SQL instance from your local machine or a GKE pod without having to explicitly whitelist your IP address in the database firewall. It automatically handles authentication via IAM.
*   **Audit Logs**: Cloud Audit Logs record "Admin Activity" (who created/deleted the database) and "Data Access" (who queried the database). Data Access logs are turned off by default to save money and must be explicitly enabled.
*   **Focus Area**: Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap**: Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource**: To reinforce these concepts visually, review this targeted search query: [YouTube Exam Study Reference Link](https://www.youtube.com/results?search_query=4327_Database_Admin+-+Google+Cloud+Associate+Database+Engineer+Security).

---

### 2. Certification Exam Tips
*   **Focus Area:** Pay close attention to how these configurations behave by default. The exam frequently features questions on default ports, configuration file paths, and diagnostic console commands.
*   **Scenario Trap:** Watch out for questions asking you to troubleshoot a failing service. Always verify if basic network connectivity, local port conflicts, or permissions are violated first.
*   **Study Resource:** To reinforce these concepts visually, review this targeted search query: [YouTube Exam Study Reference Link](https://www.youtube.com/results?search_query=4327_Database_Admin+-+Google+Cloud+Associate+Database+Engineer+Security).

---

### Lab & Command Integration
In this week's hands-on lab, you will run command sequences to verify configuration files and check service statuses. Make sure to execute administrative commands using elevated privileges (sudo/Administrator) and review console outputs for errors.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Watch the curated YouTube study streams matching **Security**.
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
