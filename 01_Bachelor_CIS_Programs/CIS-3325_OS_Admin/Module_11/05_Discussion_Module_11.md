# Discussion Forum: Module 11 - Firewall Management

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

### Scenario A - Web Server Firewall Hardening

You are hardening the firewall on an Ubuntu 22.04 production web server. The server currently
runs nginx (HTTP/HTTPS), has SSH for administrative access from a management network
(10.100.0.0/24), and receives NTP synchronization. The ufw is currently inactive. The server
has a public IP and receives internet traffic on ports 80 and 443.

1. Write the complete ufw command sequence in the correct order to implement the following
   policy: SSH allowed only from 10.100.0.0/24, HTTP and HTTPS allowed from any source,
   all other inbound traffic denied, and ufw enabled. Explain why order matters for the
   SSH source restriction.
2. After implementing the rules, a developer reports they cannot access a staging application
   on port 8080 from their workstation (192.168.1.50). The developer has legitimate access.
   Write the ufw command to allow this access, and explain the trade-off between a specific
   source-based rule versus an open port 8080 rule.
3. A week later, the security team reports that a previous developer's IP (192.168.1.75) is
   making unauthorized connection attempts to port 8080. Write the ufw rule to block this IP
   entirely and explain whether the deny rule must be added before or after the existing
   allow rule for 192.168.1.50.

---

### Scenario B - firewalld on a New RHEL Server

Your organization is deploying a new RHEL 9 database server. The server should accept MySQL
connections (port 3306) only from the application servers in the 10.50.0.0/16 subnet. SSH
should only be accessible from the management network (10.100.0.0/24). All other inbound
traffic should be dropped. The server is using firewalld.

1. Write the complete firewall-cmd command sequence to configure this policy. Use zones
   appropriately — assign the management subnet to a trusted or specific zone, restrict MySQL
   to the app server subnet, and ensure all changes are permanent and active immediately after
   configuration. Show your work with the reload command included.
2. An application team member tests the connection and reports that they can connect on port
   3306 from 10.50.1.100 but not from 10.50.2.50. Your firewall rules appear correct.
   Describe two possible non-firewall causes and the diagnostic commands you would run to
   investigate each.
3. Six months later, the database is migrated to a different server and MySQL access is no
   longer needed. Write the firewall-cmd commands to remove the MySQL rules from all zones
   where they were added, including both the port and zone-based rules, and verify that the
   removal was successful.

---

### Scenario C - Firewall Recovery from a Lockout

A junior administrator was tasked with hardening a production server's firewall using iptables.
They ran the following commands in order: iptables -P INPUT DROP, then iptables -F. All SSH
connections dropped immediately and the server became unreachable via the network.

1. Explain step by step why this command sequence caused a complete lockout. What is the
   state of the firewall after these commands execute? Why did the problem not occur when
   just iptables -P INPUT DROP was run without flushing first (assume ACCEPT rules existed)?
2. The server is in a remote data center with no local console access. Describe at least two
   recovery options that the organization might have available for this situation. Explain
   which of these could have been prevented by a proper testing procedure before applying
   firewall changes.
3. Write the safe procedure an administrator should follow when changing iptables default
   policies and rules on a remote server. Include the concept of a scheduled rule revert
   (using at or cron) that automatically removes blocking rules if the administrator does
   not actively cancel it, and explain why this safety mechanism matters for remote administration.

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 11 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

---

### Professor Nash's Closing Note

Firewalls are often treated as set-and-forget infrastructure, but firewall management is
an ongoing operational discipline. Rules accumulate over time. Old rules for deprecated
services are never removed. Conflicting rules create unexpected behavior. The administrator
who cannot enumerate their firewall's current state — without looking at documentation —
cannot guarantee the server's security posture. Make it a habit to run firewall-cmd --list-all
or ufw status numbered regularly, just as you would check df -h for disk space. Your firewall
should reflect your current security policy, not a historical record of every change anyone
ever made.
