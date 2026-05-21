# Quiz: Module 08 - Identity and Access Management (IAM)
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A large organization is onboarding a new employee in the Finance department. The IT team assigns the employee the "Finance Analyst" role in the IAM system, which automatically grants access to the financial reporting application, the budgeting tool, and the shared Finance drive — but not to HR records or engineering repositories. Which access control model is the organization using?
A) Mandatory Access Control (MAC)
B) Discretionary Access Control (DAC)
C) Role-Based Access Control (RBAC)
D) Rule-Based Access Control
*   **Correct Answer:** C) Role-Based Access Control (RBAC)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* MAC assigns access based on security labels and clearance levels enforced by the operating system or policy authority — it is not based on job roles and is primarily used in government/classified environments.
    *   *Why B is incorrect:* DAC allows resource owners to grant or restrict access to their own resources at their discretion — it is not a centrally administered role-assignment model.
    *   *Why D is incorrect:* Rule-Based Access Control grants access based on system-defined rules (such as time-of-day or IP address restrictions) rather than by assigning users to organizational roles.

---

---

**Question 2**
A security auditor reviews the account of a network administrator who was promoted to a management role six months ago. The auditor finds the account still has full administrative access to all network devices, plus the new management portal permissions added at promotion. The administrator's current job requires only the management portal. What IAM principle has been violated?
A) Separation of Duties
B) Least Privilege / Privilege Creep
C) Mandatory Access Control
D) Account Lockout Policy
*   **Correct Answer:** B) Least Privilege / Privilege Creep
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Separation of Duties requires that critical tasks be split among multiple people to prevent fraud or error — this scenario describes a single user retaining excess permissions, not a failure to divide duties.
    *   *Why C is incorrect:* Mandatory Access Control is an access control model based on security labels — it is not a principle about accumulation of unneeded permissions over time.
    *   *Why D is incorrect:* Account lockout policy governs how many failed login attempts trigger an account lock — it has no bearing on what permissions an active, successfully authenticated account holds.

---

---

**Question 3**
A company's IT policy requires that the employee who submits a purchase order cannot be the same employee who approves the purchase order. The policy exists to prevent any single individual from committing financial fraud undetected. Which IAM principle does this policy enforce?
A) Least Privilege
B) Privileged Access Management (PAM)
C) Separation of Duties
D) Role-Based Access Control
*   **Correct Answer:** C) Separation of Duties
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Least privilege restricts the breadth of permissions granted to any one account — it addresses how much access a user has, not how critical tasks are divided between multiple users.
    *   *Why B is incorrect:* PAM is a security discipline focused on controlling and auditing high-privilege accounts (administrators, root) — it is not the principle that divides transactional authority between multiple employees.
    *   *Why D is incorrect:* RBAC assigns permissions by job role — it is a mechanism for granting access, not the principle requiring that a single person cannot control both sides of a sensitive transaction.

---

**Question 4**
A company hires a third-party contractor to perform a two-week maintenance project on internal servers. The security team creates a temporary account with access limited to the specific servers involved and sets the account to automatically expire at the end of the contract period. Which IAM practices does this scenario demonstrate?
A) Least privilege and time-limited provisioning
B) Separation of duties and mandatory access control
C) RBAC and certificate-based authentication
D) Password complexity enforcement and account lockout
*   **Correct Answer:** A) Least privilege and time-limited provisioning
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Separation of duties divides task authority between multiple people — this scenario involves a single contractor account, not a divided workflow. MAC assigns access by security labels, not by scoping access to specific servers for a defined duration.
    *   *Why C is incorrect:* RBAC assigns access by role — while the contractor may have been assigned a role, the defining security practices described are the scope limitation and automatic expiration, not role assignment or certificate authentication.
    *   *Why D is incorrect:* Password complexity and account lockout are authentication hardening controls — they govern how credentials are managed, not how access scope and account lifetime are restricted to match the legitimate business need.

---

**Question 5**
An organization discovers that an attacker gained access to sensitive customer data by logging in with credentials belonging to an employee who left the company three months ago. The account had never been disabled. Which IAM control failure does this incident illustrate?
A) Failure to enforce multi-factor authentication on all accounts
B) Failure to implement a role-based access control model
C) Failure to perform timely account deprovisioning after employee termination
D) Failure to encrypt the customer data at rest using AES-256
*   **Correct Answer:** C) Failure to perform timely account deprovisioning after employee termination
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While MFA would have added a layer of protection, the root cause of this breach is that a terminated employee's account was left active and accessible — the primary failure is in the account lifecycle process, not authentication strength.
    *   *Why B is incorrect:* RBAC addresses how permissions are assigned to active users — the issue here is not the access control model but the failure to disable the account when the employee's authorized need for access ended.
    *   *Why D is incorrect:* Encrypting data at rest protects against unauthorized physical access to storage media — it does not prevent an attacker who has valid credentials from accessing data through a legitimate application session on an account that should have been disabled.
