# Discussion: Module 15 — Linux Security Hardening

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This discussion is worth 50 points. Post an original response AND reply substantively to at least two classmates.

**Due Date:** By end of day Sunday of the current module week.

---

### Discussion Prompt

**Scenario:**

You are the lead Linux administrator at a healthcare organization that processes protected health information (PHI). The organization is preparing for its annual HIPAA security audit. The auditor's pre-audit questionnaire includes the following questions about your Linux server infrastructure:

- Are all servers running with access control mechanisms beyond standard Unix permissions?
- Is system call activity monitored and logged in a tamper-evident manner?
- Are brute-force login attempts automatically detected and blocked?
- Are password policies enforced programmatically, not just by policy documents?
- Have systems been assessed against an industry security benchmark?

Your organization runs a mix of Rocky Linux 9 (application servers) and Ubuntu 22.04 (developer workstations). You have 48 hours to document your current security posture and identify gaps before the auditor arrives on-site.

---

### Discussion Questions

Address ALL of the following in your initial post:

**Question 1 — MAC Controls**

For the Rocky Linux 9 servers, describe how SELinux addresses the first auditor question. What specific SELinux configuration verifies compliance? Write the commands you would run to confirm all servers are in enforcing mode. For the Ubuntu workstations, describe the equivalent AppArmor configuration and how you would verify profiles are loaded and in enforce mode. What would be a disqualifying finding if SELinux were set to Permissive on a HIPAA-covered system?

**Question 2 — Audit Logging**

Describe a comprehensive `auditd` configuration for HIPAA compliance. Which specific events should be captured? Write at least five audit rules that would be relevant to a healthcare PHI environment — think about what a compliance auditor would look for. How would you demonstrate that audit logs cannot be deleted or modified by system administrators (tamper-evidence)?

**Question 3 — Intrusion Prevention**

Describe your fail2ban configuration for the SSH service on the application servers. What `findtime`, `maxretry`, and `bantime` values are appropriate for a healthcare environment, and what is your rationale? How would you handle legitimate administrators being accidentally banned? What fail2ban jail would you add beyond SSH to protect a web application serving PHI?

**Question 4 — Password Policy**

Document the password policy configuration for both Rocky Linux 9 and Ubuntu 22.04. Include specific values for: minimum length, complexity requirements, maximum age, minimum age, warning period, and account lockout. Write the `chage` commands to apply these settings to an existing user. Explain why simply having a written password policy document is not sufficient to answer the auditor's question.

**Question 5 — Gap Analysis and Roadmap**

Based on the hardening topics covered in this module, identify what you believe are the three highest-risk gaps in a typical Linux server that has never been explicitly hardened. For each gap, describe the risk, the remediation, and the specific configuration change. Prioritize your top gap for immediate action and explain your prioritization logic.

---

### Reply Requirements

When responding to classmates:

- Compare their audit rules — would the same rules satisfy your understanding of HIPAA audit requirements?
- Challenge or validate their fail2ban values — is their ban time appropriate for the risk level?
- Suggest an additional gap they may have overlooked

---

### Grading Rubric

| Criterion | Points |
|-----------|--------|
| MAC controls: specific commands and compliance rationale for both distros | 10 |
| Audit rules: five specific, relevant rules with HIPAA justification | 12 |
| fail2ban: values with rationale, lockout recovery, second jail | 10 |
| Password policy: complete settings for both distros with enforcement rationale | 10 |
| Gap analysis: three specific gaps with risk assessment and prioritized remediation | 8 |
| **Total** | **50** |

---

### Instructor Notes

The key distinction this discussion tests is the difference between DETECTING and PREVENTING security events. `auditd` detects (logs) events after they occur. `fail2ban` prevents (blocks) further attempts. SELinux/AppArmor prevents (confines) process behavior. Password policies prevent weak credentials. A complete security posture requires all four.

The hardest question is the tamper-evidence question (Question 2). Strong responses will note that `auditd` logs can be protected by:

- Writing to a remote syslog server via `audisp-remote`
- Setting `admin_space_left_action = halt` to prevent the system from running without audit capability
- Using file integrity monitoring (AIDE, Tripwire) to detect changes to the audit log
- Setting the audit daemon to require root to modify rules but even root cannot delete logs without triggering an alert

Students who simply say "the root user can protect the logs" are missing the point — HIPAA requires protection FROM root, not just by root.
