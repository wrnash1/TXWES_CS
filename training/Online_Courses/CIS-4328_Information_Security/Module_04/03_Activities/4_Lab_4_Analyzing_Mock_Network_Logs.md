### 4. Lab 4: Analyzing Mock Network Logs
**Objective:** Act as a Tier 1 SOC Analyst to identify an intrusion from a provided log file.
**Instructions:**
1. Download the `auth_logs.csv` file provided in the Blackboard module.
2. Open the file using Excel or a Linux text editor.
3. Use filtering (or `grep` in Linux) to find anomalies. Look for:
   * Excessive failed login attempts (`Event ID 4625`).
   * A successful login (`Event ID 4624`) occurring immediately after a string of failures.
   * Logins occurring at unusual times (e.g., 3:00 AM on a Sunday).
4. Identify the IP address of the attacker and the compromised username.
**Deliverable:** Submit an Incident Report (1 paragraph) identifying the attacker's IP, the compromised account, the timestamp of the successful breach, and your recommended immediate containment action.

---
