# Discussion Forum: Module 05 - Package Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Points:** 10
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

### Instructions

Choose one of the three scenarios below. Write an initial post of 175 to 225 words that addresses
all three sub-questions for your chosen scenario. After posting, respond to at least two classmates
who chose different scenarios. Each response should be at least 75 words and add substantive
technical content.

---

### Scenario A - Supply Chain Attack via Package Repository

Your security team issues an alert that a popular open-source package used in your environment
has been compromised. Attackers replaced the legitimate package binary on the package maintainer's
servers with a modified version containing malware. Some of your servers may have already
installed the compromised version.

1. Explain how GPG signing of packages and repositories is supposed to protect against this type
   of attack. What would need to have happened for the malicious package to pass GPG verification?
2. Write the exact commands you would use on both an Ubuntu server and a RHEL server to determine
   whether the suspicious package is installed and, if so, to verify whether its files have been
   tampered with compared to the package database.
3. Beyond verification, what is your remediation strategy if verification shows the installed
   files match the (malicious) package exactly? In other words, what do you do when the package
   itself was compromised at the source?

---

### Scenario B - Unplanned Package Dependency Removal

A junior administrator runs sudo apt remove libssl-dev on a production web server, intending
to remove a development library. apt reports that this will also remove 12 other packages
including nginx, php, and apache2. The junior administrator accepts the removal. Services go
down. You receive the alert.

1. Explain why apt remove libssl-dev triggered a cascade of package removals. What is the
   dependency relationship that caused this? How does apt evaluate whether a package can be
   safely removed?
2. Describe the specific apt command you can run to see what packages would be removed BEFORE
   actually running an uninstall, allowing the administrator to review the impact without
   making changes.
3. On RHEL systems, dnf history provides transaction rollback capability. Write the sequence of
   dnf commands to undo the last transaction that removed the affected packages. Does apt provide
   an equivalent rollback mechanism?

---

### Scenario C - Security Patching Policy for Production Servers

Your company's security policy requires all Linux servers to receive security patches within
48 hours of a critical CVE being published. You manage 50 Ubuntu servers and 30 RHEL servers.
Manual patching is taking too long and delays are creating compliance failures.

1. Describe the apt command and the dnf command for applying only security updates (not all
   available updates) on their respective platforms. Explain why applying only security patches
   rather than all updates is often preferred in production environments.
2. A critical patch for the Linux kernel requires a reboot to take effect. What mechanism does
   Ubuntu provide to apply kernel patches without an immediate reboot, and what is the trade-off
   of using it? How do you verify the currently running kernel versus the installed kernel?
3. Propose a three-step approach to automate and audit the patching process across all 80 servers
   that provides both automation and accountability. Consider scheduling, logging, and verification.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 05 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Package management is infrastructure policy made executable. When you update a package, you are
making a security decision. When you add a third-party repository, you are making a trust decision.
When you leave a package unverified, you are making an implicit risk decision. The scenarios here
reflect the reality that package management is not just a chore - it is one of the primary ways
organizations either prevent attacks or become complicit in them through negligence. Know your
package tools well enough to automate them safely and audit them accurately.
