# Discussion: Module 14 — SSH and Remote Administration

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

You are a systems administrator at a financial services firm. The company has 45 Linux servers spread across three data centers. Currently, all server access is via SSH with password authentication. The security team has conducted an audit and issued the following findings:

- **Finding 1**: Password authentication allows brute-force attacks; 3 servers had unauthorized login attempts last month
- **Finding 2**: Several developers are logging in directly as root via SSH
- **Finding 3**: Idle SSH sessions are left open indefinitely; one session was found open for 11 days
- **Finding 4**: There is no pre-authentication legal warning banner
- **Finding 5**: No centralized mechanism exists to revoke SSH access when employees leave; keys must be manually removed from each server

The CISO has approved a project to resolve all five findings. You have been assigned as lead.

---

### Discussion Questions

Address ALL of the following in your initial post:

**Question 1 — Migration Plan**

Describe a safe, staged plan for migrating 45 servers from password authentication to key-based authentication. What order of operations prevents locking administrators out? What verification steps would you perform at each stage? How do you handle the transition for 15 different administrators who each need access to all servers?

**Question 2 — sshd_config Changes**

Write the specific `sshd_config` directives that address Findings 1, 2, 3, and 4. For each directive, explain why it addresses the finding. What command do you run to validate the configuration before reloading? Why is `sudo sshd -t` critical before applying changes to production?

**Question 3 — Centralized Key Management (Finding 5)**

Describe two approaches for solving the centralized SSH key revocation problem. One approach should use Ansible; the other should describe SSH certificate-based authentication. For the Ansible approach, sketch the playbook structure that would remove a specific user's public key from `authorized_keys` across all 45 servers. For certificates, explain how a CA-signed SSH certificate solves the revocation problem differently from `authorized_keys` management.

**Question 4 — Automation Safety**

Your Ansible playbook for key management needs to avoid a dangerous scenario: if the playbook has a bug that removes ALL keys from `authorized_keys`, you will lose access to 45 servers simultaneously. What safeguards would you build into the playbook to prevent this? Consider using `--check` mode, limiting host scope, and verifying access before committing changes.

**Question 5 — Security Posture Reflection**

Describe a real or plausible scenario where an open idle SSH session (Finding 3) could lead to a security breach. How does `ClientAliveInterval` mitigate this risk? Is there a case where a very short idle timeout (e.g., 60 seconds) could cause operational problems? Discuss the tradeoff between security and operational convenience.

---

### Reply Requirements

When responding to classmates:

- Evaluate their migration plan — did they account for all administrators before disabling passwords?
- Review their sshd_config directives — is anything missing or incorrect?
- Challenge or support their Ansible vs. certificate comparison — add a consideration they missed

---

### Grading Rubric

| Criterion | Points |
|-----------|--------|
| Migration plan is safe, staged, and accounts for all users | 12 |
| sshd_config directives are correct and address each finding | 12 |
| Centralized key management approaches are technically sound | 10 |
| Ansible safety safeguards are practical and specific | 8 |
| Security posture reflection is thoughtful with concrete tradeoff analysis | 8 |
| **Total** | **50** |

---

### Instructor Notes

The most important concept in Question 1 is the "always keep a working session open" principle scaled to an enterprise context. Students should propose testing on one server first, verifying access from multiple clients, then rolling out in batches with a rollback plan.

For Question 3, the key insight about SSH certificates is that revocation works by setting an expiry date on the certificate. When the certificate expires, the user loses access without any changes to server `authorized_keys` files. This is a fundamentally different architecture than the append-only `authorized_keys` model.

Strong responses will also note that Ansible itself requires working SSH access — so if there is a chicken-and-egg problem (SSH is broken and you need Ansible to fix it), you need out-of-band access (console, bastion, IPMI/iDRAC) as a fallback.
