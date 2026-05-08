### 5. Quiz 3: Group Policy (Question Bank)
**Question 1**
An administrator configures a Group Policy Object (GPO) at the Domain level that sets the minimum password length to 12 characters. However, a separate GPO linked to the "IT_Department" Organizational Unit (OU) sets the minimum password length to 15 characters. Assuming no other settings are modified, what minimum password length will apply to users in the IT_Department OU?
A) 12 characters, because Domain policies always override OU policies.
B) 15 characters, because the OU policy is applied last and overrides the Domain policy.
C) 15 characters, because GPOs always apply the most restrictive setting automatically.
D) The policies will conflict and neither will be applied.
*   **Correct Answer:** B) 15 characters, because the OU policy is applied last and overrides the Domain policy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* GPOs follow the LSDOU processing order. OU policies are processed *after* Domain policies, meaning the OU policy wins.
    *   *Why C is incorrect:* GPOs do not evaluate restrictiveness; they blindly apply the last policy processed unless the "Enforced" flag is used.
    *   *Why D is incorrect:* GPOs are designed to handle conflicts gracefully through the inheritance order.

**Question 2**
You need to deploy a specific registry key via Group Policy, but it must only be applied to computers that are running Windows 10, completely ignoring any Windows 11 machines in the same OU. What is the most efficient way to accomplish this?
A) Create two separate OUs, move the computers manually, and link the GPO to the Windows 10 OU.
B) Modify the Security Filtering to explicitly deny the 'Windows 11 Computers' security group.
C) Configure a WMI Filter on the GPO that queries the operating system version.
D) Change the GPO from a Computer Configuration to a User Configuration.
*   **Correct Answer:** C) Configure a WMI Filter on the GPO that queries the operating system version.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While this works, it is highly inefficient and creates administrative overhead to constantly move computer objects around as they are upgraded.
    *   *Why B is incorrect:* Managing OS versions via security groups requires manual tracking of which computer belongs to which group. WMI queries the hardware/OS directly and dynamically.
    *   *Why D is incorrect:* A registry key that targets machine behavior belongs in Computer Configuration. Moving it to User Configuration will apply it based on who logs in, not what OS the machine is running.
