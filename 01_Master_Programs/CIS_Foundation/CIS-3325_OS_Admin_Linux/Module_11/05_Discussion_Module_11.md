# Discussion: Module 11 — Networking in Linux

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This discussion is worth 50 points and contributes to your participation grade. You must post an original response AND reply to at least two classmates to receive full credit.

**Due Date:** By end of day Sunday of the current module week.

---

### Discussion Prompt

**Scenario:**

You are a junior Linux administrator at a regional logistics company. On Monday morning, you receive a ticket with the following report from a warehouse manager:

*"Our inventory server can't reach the company ERP system. Everything was working Friday afternoon. Nobody touched the server over the weekend, but we did have a power outage Saturday night that brought the generator online for about 20 minutes."*

The inventory server runs Rocky Linux 9. The ERP system is at `10.50.1.100`. The inventory server's normal IP is `10.50.2.45/24` with a gateway of `10.50.2.1`.

**Your Initial Findings:**

After SSHing in from your workstation, you run:

```bash
ip addr show
```

Output shows the interface has no IPv4 address — only the link-local address `169.254.x.x`.

---

### Discussion Questions

Address ALL of the following in your initial post:

**Question 1 — Root Cause Analysis**

Why would a power outage cause a Linux server to lose its IP configuration? Consider what the power outage (and generator switchover) might have caused technically, and whether a properly configured server should recover automatically. What would you check first to determine whether the issue is a DHCP failure, a bad connection profile, or something else?

**Question 2 — Immediate Remediation**

Walk through the specific commands you would run — in order — to diagnose and restore connectivity on this server. Be specific: include actual command syntax, explain what each command tells you, and describe how you would interpret the output at each step.

**Question 3 — Firewall Consideration**

After restoring IP connectivity, you test `ping 10.50.1.100` from the inventory server and it fails, but `ping 10.50.2.1` (gateway) succeeds. You check the ERP server team and they confirm their server is up and reachable from other hosts. List three possible reasons the ping to the ERP server might fail, and describe how you would isolate each cause using the tools covered in Module 11.

**Question 4 — Hardening for the Future**

This incident revealed a gap: the server relies on DHCP for its IP address, making it vulnerable to DHCP failures after unexpected restarts. Describe the steps to convert this server to a static IP configuration using `nmcli`. Include all relevant parameters and explain why each one matters. Should this server's IP also be in `/etc/hosts` on other systems? Why or why not?

---

### Reply Requirements

When replying to classmates:

- Do not just write "Good answer" — engage with their technical content
- If you would diagnose the issue differently, explain your alternative approach
- If you agree with their remediation steps, add one step or consideration they may have missed
- Feel free to share a real-world experience where network troubleshooting was challenging

---

### Grading Rubric

| Criterion | Points |
|-----------|--------|
| Root cause analysis is technically accurate and complete | 12 |
| Remediation walkthrough includes correct commands in logical order | 15 |
| Firewall analysis identifies plausible causes and correct diagnostic tools | 10 |
| Static IP hardening steps are complete and accurate with nmcli | 8 |
| Two substantive replies to classmates | 5 |
| **Total** | **50** |

---

### Instructor Notes

Strong responses will demonstrate command-level specificity — not just naming the tool but showing the exact syntax and explaining what output you would look for. The best posts connect the scenario symptoms to the OSI model layer where the failure occurred, demonstrating the layered troubleshooting mindset that separates competent administrators from those who just reboot and hope.

Think about what "169.254.x.x" tells you — this is an APIPA (Automatic Private IP Addressing) address, assigned by the OS when DHCP fails. That single data point tells you exactly which layer failed.
