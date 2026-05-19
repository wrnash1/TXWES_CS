# Quiz: Module 11 - Enterprise Application Integration (EAI)
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
What role does middleware like MuleSoft play in enterprise system integration?
*   A) It replaces database engines
*   B) It acts as a broker, translating and routing data payloads between disparate applications
*   C) It builds front-end client screens
*   D) It hosts virtual machines
*   **Correct Answer:** B) Middleware connects different architectures (e.g. cloud CRM to legacy on-premise ERP) by translating data formats on-the-fly.
*   **Distractor Analysis:**
    *   *Why correct:* Middleware connects different architectures (e.g. cloud CRM to legacy on-premise ERP) by translating data formats on-the-fly.
    *   It is a routing and translation layer, not storage or virtualization.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **EAI principles**?
B) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
C) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **EAI principles**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **EAI principles**.
    * *Why A is correct:* This describes the exact role and function of **EAI principles**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **EAI principles**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
C) EXPLAIN ANALYZE SELECT * FROM logs;
D) GRANT SELECT ON client_db TO analyst_role;
A) CREATE INDEX idx_email ON users(email);
B) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Enterprise Application Integration (EAI)** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Enterprise Application Integration (EAI)**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.

