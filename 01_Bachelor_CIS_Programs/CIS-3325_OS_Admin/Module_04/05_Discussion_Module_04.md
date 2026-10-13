# Discussion Forum: Module 04 - User and Group Management

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

### Scenario A - Employee Offboarding Incident

A systems administrator is notified at 4:30 PM on a Friday that a senior developer named
Rodriguez was terminated effective immediately for cause. Rodriguez has admin accounts on 12
Linux servers, belongs to the sudo, docker, and databases groups, and owns several critical
application files in /opt/appdata.

1. What is the exact sequence of steps you take in the first five minutes after receiving this
   notification? List the specific commands for disabling Rodriguez's accounts on Linux systems
   before any further action is taken.
2. After the immediate lockout, you need to audit what Rodriguez did recently. Identify at least
   two command-line approaches to review recent activity by a specific user on a Linux system.
3. Eventually Rodriguez's accounts need to be permanently removed. What factors should you
   consider before running userdel -r, and what is the risk if files owned by Rodriguez's UID
   exist outside the home directory?

---

### Scenario B - Principle of Least Privilege in Practice

Your company is deploying a new web application that will run on five Linux servers. The
application runs as a service account named webapp. The development team is requesting that
webapp be added to the sudo group "just in case" for easier troubleshooting.

1. Explain the principle of least privilege and why adding webapp to the sudo group violates it.
   What specific attack scenario becomes possible if the webapp process is compromised and it has
   sudo access?
2. Instead of sudo access, propose a specific, limited sudoers entry that would allow only the
   specific administrative action the developers actually need, such as restarting only the
   webapp service.
3. The development team argues that managing limited sudo entries is too complex and they just
   want unrestricted access for efficiency. How do you respond? What is the business risk
   argument against their position?

---

### Scenario C - New Employee Onboarding Automation

Your team manages a Linux server environment with 200+ servers. Onboarding new employees
manually takes too long: creating accounts, setting passwords, adding to the right groups,
configuring SSH, and standardizing their shell environment across all servers.

1. Describe the /etc/skel directory and how it can be used to standardize new user environments.
   Give two specific examples of files you would add to /etc/skel for a development team.
2. Write a multi-line bash command sequence (not a full script, just the commands) that creates
   a new developer account named johndoe with: home directory, bash shell, membership in the
   developers and docker groups, a forced password change at first login, and a 90-day maximum
   password age.
3. Beyond the technical account creation, what two organizational processes should surround user
   account provisioning to ensure accountability and compliance?

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 04 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

User management is where Linux administration meets organizational risk management. An unlocked
account belonging to a terminated employee is not just a technical oversight - it is a liability.
A service account with excessive privileges is not just a configuration choice - it is an open
door. The scenarios in this discussion reflect real incidents. Terminated employees who retained
access caused documented data breaches. Overprivileged service accounts enabled major ransomware
campaigns. The commands you learned this week are not abstract exercises. They are the controls
standing between your organization and the next incident headline.
