### 2. Video Script 3.2: Security Filtering and WMI Filters
**Estimated Duration:** 5 minutes
**Visual:** Screencast of the Group Policy Management Console (GPMC).
**[Alt-text: A screencast of the GPMC interface. The user selects a GPO, navigates to the 'Scope' tab, removes 'Authenticated Users' from the Security Filtering section, and adds a specific security group named 'Executives'.]**
**Audio:** "By default, when you link a GPO to an OU, it applies to every single 'Authenticated User' inside that OU. But what if you only want the policy to apply to the managers inside the Sales OU? You use Security Filtering. You remove 'Authenticated Users' and add the specific 'Managers' security group. Alternatively, you can use WMI filters. A WMI filter asks the computer a question before applying the policy, such as: 'Are you running Windows 11?' If the computer answers no, the policy is skipped."

---
