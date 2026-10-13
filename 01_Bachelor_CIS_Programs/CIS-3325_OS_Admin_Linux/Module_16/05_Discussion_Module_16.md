# Discussion: Module 16 — Linux+ XK0-005 Exam Preparation

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This is the final discussion of CIS-3325. It is worth 50 points and serves a dual purpose: reinforcing your exam preparation and encouraging you to reflect on your growth as a Linux administrator over this course.

Post an original response AND reply substantively to at least two classmates.

**Due Date:** By end of day Sunday of the current module week.

---

### Discussion Prompt

This discussion has two parts. Complete both parts in your initial post.

---

### Part A — Technical Knowledge Synthesis

Choose ONE of the following scenario challenges. These are designed to require integration of knowledge from multiple modules — the kind of multi-domain thinking the Linux+ exam's performance-based questions demand.

---

**Challenge A1 — The New Server Deployment**

You have just received a fresh Rocky Linux 9 server that needs to be ready for production as a web application server within 4 hours. List every configuration step you would perform, in order, to bring this server from a minimal installation to a production-ready, security-hardened state. Your list should include specific commands or configuration file changes for each step. Use the CIS Benchmark Level 1 as your reference framework.

At minimum, your list must cover: network configuration, hostname, firewall, SSH hardening, SELinux verification, auditd setup, package installation, systemd service configuration, user accounts, and fail2ban.

---

**Challenge A2 — The Mystery Failure**

It is 2 AM. Your monitoring system sends an alert: "Service myapp.service on prod-server-01 is DOWN." The on-call engineer has SSHed in and run `systemctl status myapp.service`. The output shows `failed` state with no helpful message.

Describe your complete diagnostic process, in order, using the specific commands you would run at each step. Start from the initial SSH connection and end with identifying the root cause. Your answer should account for at least four possible root causes and how you would distinguish between them:

- Application crash (bug in the code)
- Storage issue (disk full or permission problem)
- Network dependency failure (database or upstream service unreachable)
- SELinux or file permission denial

---

**Challenge A3 — The Security Incident**

The security team has notified you that a suspicious account was created on three of your production Linux servers sometime last night. You do not know which account was created or what it was used for.

Describe the forensic investigation process using only the tools covered in CIS-3325. Which log files, audit records, and system files would you examine? What commands would you run? How would you determine what the account did after it was created? What immediate remediation would you apply before your full investigation is complete?

---

### Part B — Course Reflection

Answer ALL of the following reflection questions in your post:

**Reflection 1 — Growth Assessment**

When you started CIS-3325, what was your Linux skill level? Describe one specific concept from this course that was genuinely difficult for you to understand at first, and explain how your understanding of it developed over the modules. What finally made it "click"?

**Reflection 2 — Most Valuable Topic**

Which single module or topic from CIS-3325 do you believe will be most valuable in your career, and why? Be specific — don't just say "security" or "networking." Reference a concrete use case where you expect to apply what you learned.

**Reflection 3 — Exam Confidence and Plan**

Rate your current confidence for the Linux+ XK0-005 exam on a scale of 1–10. What are your two weakest exam domains based on your self-assessment and quiz performance throughout this course? What specific study activities will you do in the next two weeks before the exam?

**Reflection 4 — Linux in Your Career**

Where do you see Linux administration fitting in your career path? Are you pursuing a role in systems administration, DevOps, cloud engineering, cybersecurity, or something else? How does Linux+ certification position you for that role?

---

### Reply Requirements

When responding to classmates:

- For Part A: Add one step or consideration to their deployment/diagnostic/forensic process that they may have overlooked
- For Part B: Share a related experience or offer encouragement if they identified the same weak areas you did
- Do not just write agreement — contribute new information or perspective

---

### Grading Rubric

| Criterion | Points |
|-----------|--------|
| Challenge A response: technically complete, commands are specific and correct | 20 |
| Reflection 1: genuine and specific | 5 |
| Reflection 2: specific topic with concrete career application | 8 |
| Reflection 3: honest assessment with specific study plan | 7 |
| Reflection 4: thoughtful career context | 5 |
| Two substantive replies to classmates | 5 |
| **Total** | **50** |

---

### Instructor Notes

This final discussion is the capstone of the course. The technical challenges require synthesis across modules — there is no single module that covers all of Challenge A1, A2, or A3. Students who have actively engaged with every module will handle these well; students who have been surface-level will struggle to integrate the knowledge.

For the reflection questions, the most valuable insight is usually in Reflection 1: seeing how students describe their initial confusion and subsequent understanding reveals the quality of their learning process far better than any quiz score.

Strong final posts will include specific command syntax in the technical challenge AND genuine vulnerability in the reflection — acknowledging what they don't yet know is a sign of a mature engineer.

The goal of this course was never just to prepare you for a certification exam. It was to build the mental models and muscle memory that make you effective on day one of a Linux administration role. The certification is a milestone. The real work starts after.

Good luck.
