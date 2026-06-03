# Discussion: Module 08 — File System Permissions and Ownership

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Overview

This discussion bridges Module 8's technical permission content with the real-world decisions administrators face when designing and auditing access controls. Permissions that look fine in isolation often create vulnerabilities or usability problems when combined with user behavior and organizational context.

**Participation Requirements:**

- Post your initial response (minimum 200 words) by Thursday at 11:59 PM
- Reply to at least two classmates (minimum 75 words each) by Sunday at 11:59 PM
- All technical claims must be grounded in the module content

---

## Discussion Prompt

### Designing a Permissions Architecture

You have been hired as the Linux administrator for a small healthcare technology company with three teams:

- **Developers** — write and deploy application code
- **QA Engineers** — test the application; need to read logs and config files, but should not be able to modify production configs
- **Auditors** — external compliance auditors who need read-only access to specific log files for 90 days; should have no access to source code or configurations

The application runs as a system account (`appuser`). Logs are written to `/var/log/medapp/`. Configuration lives in `/etc/medapp/`. Source code is deployed to `/opt/medapp/`.

**Part A — Permission Design**

Design a complete permissions architecture for these three directories. For each directory, specify:

- Recommended ownership (user:group)
- Recommended permissions (octal and what it means)
- Whether ACLs are needed and why (or why not)
- Any special bits (SUID, SGID, sticky) and your justification

Show the actual commands you would run to implement your design.

**Part B — The Auditor Problem**

The traditional Unix permission model cannot cleanly grant the auditors read-only access to `/var/log/medapp/` without either:

- Adding them to a group that also has other permissions you do not want them to have
- Making the logs world-readable (which may violate HIPAA)

Explain in detail how ACLs solve this problem. Include the specific `setfacl` commands you would use, including default ACLs to ensure new log files are automatically covered.

**Part C — Security vs. Usability Tension**

Strict permissions improve security but can create friction for legitimate users. Share an example (real or hypothetical) where overly strict permissions caused a legitimate operational problem — for instance, a deployment script that failed because it lacked write access to a config directory, or a developer who could not check a log file during an incident.

What is the correct way to resolve this tension? Is the answer always "make it more permissive"? Or are there permission patterns that are both secure and operationally practical?

---

## Discussion Grading Rubric

| Criterion | Points |
|---|---|
| Part A: Correct and well-justified permission design | 30 |
| Part B: Correct ACL solution with default ACLs | 25 |
| Part C: Thoughtful analysis of security vs. usability | 20 |
| Two substantive peer replies | 15 |
| Technical accuracy and command syntax | 10 |
| **Total** | **100** |

---

## Thought Starters

For Part A, consider each directory's access pattern:

```bash
# Who writes to /var/log/medapp? (appuser)
# Who reads it? (developers, QA, auditors — with different scopes)
# Who should NEVER touch it? (everyone else)

# Who writes to /etc/medapp? (root for maintenance; appuser reads)
# Who should read it? (developers need to see it; QA can read; auditors should NOT)

# Who writes to /opt/medapp? (developers deploy here)
# Who should execute it? (appuser runs the app)
# Who should NOT be able to read source code? (auditors)
```

For Part B, the key insight is that ACLs allow you to express "this specific user gets this specific access to this specific path" without putting them in a group that carries other permissions elsewhere on the system.

For Part C, consider patterns like:

- Using groups correctly instead of loosening individual file permissions
- Using SGID on directories to ensure consistent group ownership
- Using ACLs for surgical access grants that expire (can be scripted to remove after 90 days)
- The difference between "temporarily loosening for debugging" and "permanently insecure"

---

## Peer Reply Guidelines

When replying to classmates:

- Point out any permission setting that would be insecure (e.g., world-writable configuration files)
- Suggest a more appropriate permission if you see an issue
- Discuss whether their ACL design handles the new-file-inheritance problem (default ACLs)
- Challenge or support their Part C position with specific examples

Focus your feedback on the permission design, not just the writing style.
