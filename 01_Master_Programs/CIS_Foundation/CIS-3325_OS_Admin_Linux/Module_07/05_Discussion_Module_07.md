# Discussion: Module 07 — User and Group Administration

## Course: CIS-3325 OS Administration Linux

**Certification Alignment:** CompTIA Linux+ (XK0-005)

---

## Overview

This discussion asks you to connect the technical content of Module 7 to real-world professional practice. User account management is not just a technical task — it intersects with HR processes, security compliance, audit requirements, and organizational policy. Strong administrators think about these connections.

**Participation Requirements:**

- Post your initial response (minimum 200 words) by Thursday at 11:59 PM
- Reply to at least two classmates (minimum 75 words each) by Sunday at 11:59 PM
- Responses must demonstrate engagement with the technical content, not just general agreement

---

## Discussion Prompt

### The Principle of Least Privilege in Practice

The Principle of Least Privilege (PoLP) states that every user, process, and system should have only the minimum permissions needed to do their job. In Module 7, we saw this principle built into Linux at every level: UID-based access control, the `/etc/shadow` permission model, `sudo` delegation, and PAM authentication.

**Respond to the following:**

**Part A — Technical Analysis**

Consider this scenario: A mid-size company has been running their Linux servers with a loose policy. Developers all have accounts with `sudo ALL=(ALL) NOPASSWD: ALL` in sudoers because "it was easier." The company recently hired a security consultant who flagged this as a critical risk.

Describe a more secure sudo configuration for a team of five developers where:

- Two senior developers can restart application services (nginx, nodejs app services)
- Two mid-level developers can view logs with `journalctl` and `tail`
- One junior developer can only check service status

Include the actual sudoers syntax you would write. Use fenced code blocks.

**Part B — Process and Policy**

Beyond technical configuration, describe the process you would recommend for managing the account lifecycle at this company. Consider:

- How should new accounts be created and documented?
- How should accounts be handled when an employee leaves?
- How often should account audits occur, and what would you look for?

**Part C — Personal Reflection**

Have you encountered (in a job, internship, course, or personal project) a situation where poor access control caused a problem — or where good access control prevented one? If you have not had a direct experience, describe a documented real-world case (such as the 2020 Twitter hack, the SolarWinds breach, or any incident involving excessive privilege) and connect it to the Linux concepts from this module.

---

## Discussion Grading Rubric

| Criterion | Points |
|---|---|
| Part A: Correct and functional sudoers syntax | 30 |
| Part B: Thorough account lifecycle process | 25 |
| Part C: Meaningful real-world connection | 20 |
| Two substantive peer replies | 15 |
| Writing clarity and technical accuracy | 10 |
| **Total** | **100** |

---

## Thought Starters

If you are unsure how to approach Part A, start with what we covered in the video:

```bash
# Sudoers User_Alias syntax
User_Alias  SENIOR_DEVS = alice, bob
User_Alias  MID_DEVS    = carol, dave
User_Alias  JUNIOR_DEVS = eve

# Cmnd_Alias syntax
Cmnd_Alias  APPSVC = /bin/systemctl restart nginx, /bin/systemctl restart nodeapp
```

Fill in the rest using the sudoers rules syntax from the video and reading guide. Your answer does not need to be perfect — explaining your reasoning matters as much as the exact syntax.

For Part B, think about what happens during onboarding, role changes, and offboarding. What could go wrong if each step is skipped?

For Part C, consider that the 2020 Twitter hack involved an insider with excess privilege escalating access to internal admin tools. The SolarWinds attack involved compromised service account credentials. Both are directly related to principles covered in this module.

---

## Peer Reply Guidelines

When replying to classmates:

- Comment specifically on their sudoers syntax — is it correct? Would it work? Is there a safer way to write it?
- Challenge or expand their lifecycle process with something they may have missed
- Share a different perspective on the real-world case they chose, or draw a connection to your own experience

Replies that only say "great post" or "I agree" will receive no credit.
