# Quiz: Module 11 - Firewall Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Questions:** 10
**Points:** 10 (1 point per question)

---

**Question 1**

An administrator on a RHEL 9 server runs firewall-cmd --add-service=https to allow HTTPS
traffic. After a reboot, HTTPS is blocked again. What was the cause?

- A) The firewalld service was not running when the command was executed.
- B) The --permanent flag was omitted, so the rule was added only to the runtime configuration and not saved persistently.
- C) HTTPS requires a separate --add-port=443/tcp command in addition to --add-service=https.
- D) firewall-cmd changes require a subsequent systemctl restart firewalld to take effect.

Correct Answer: B) The --permanent flag was omitted, so the rule was added only to the runtime configuration and not saved persistently.

Distractor Analysis:

- Why A is incorrect: If firewalld were not running, the command itself would have failed with an error. The fact that HTTPS worked until the reboot confirms firewalld was active and the rule was applied — just not persistently.
- Why C is incorrect: --add-service=https already includes port 443/tcp as part of the service definition in firewalld's service library. A separate --add-port is not needed when using a named service.
- Why D is incorrect: systemctl restart firewalld would wipe the non-permanent runtime rule. The correct workflow is to use --permanent when adding the rule, then run firewall-cmd --reload to apply the permanent config to the running state.

---

**Question 2**

A security administrator needs to allow TCP port 8443 through the firewall on an Ubuntu 22.04
server using ufw. After running ufw allow 8443/tcp, traffic on port 8443 is still blocked.
What is the most likely cause?

- A) ufw rules require a reboot to take effect after being added.
- B) Port 8443 is reserved and cannot be opened with ufw.
- C) ufw was never enabled with ufw enable and is still inactive.
- D) The rule must be added to both the INPUT and OUTPUT chains separately using ufw allow in 8443/tcp and ufw allow out 8443/tcp.

Correct Answer: C) ufw was never enabled with ufw enable and is still inactive.

Distractor Analysis:

- Why A is incorrect: ufw rules take effect immediately when ufw is active — no reboot is required. Rules are also automatically persistent across reboots.
- Why B is incorrect: Port 8443 is a common HTTPS alternate port and is not reserved or restricted. ufw has no list of forbidden ports; any valid port number from 1-65535 can be allowed or denied.
- Why D is incorrect: ufw allow 8443/tcp without a direction flag allows inbound traffic on that port, which is the typical requirement for a server service. Separate in/out rules are not required for standard service exposure.

---

**Question 3**

An administrator wants to list all current iptables rules in the INPUT chain with packet counts
and without DNS resolution of IP addresses. Which command is correct?

- A) iptables --show INPUT -v
- B) iptables -L INPUT -n -v
- C) iptables -S INPUT
- D) iptables -F INPUT

Correct Answer: B) iptables -L INPUT -n -v

Distractor Analysis:

- Why A is incorrect: --show is not a valid iptables flag. The correct flag for listing rules is -L. This command would produce an error.
- Why C is incorrect: iptables -S INPUT prints rules in iptables-restore format (the save/restore syntax). It does not show packet/byte counts and is used for exporting rules, not for human-readable inspection.
- Why D is incorrect: iptables -F INPUT flushes (deletes) all rules in the INPUT chain. Running this on a production system would remove all inbound filtering rules, not display them.

---

**Question 4**

A Linux administrator needs to block all inbound TCP traffic on port 23 (Telnet) using iptables
directly. The server's INPUT chain default policy is ACCEPT. Which command correctly adds the
blocking rule?

- A) iptables -A INPUT -p tcp --dport 23 -j DROP
- B) iptables -D INPUT -p tcp --dport 23 -j ACCEPT
- C) iptables -P INPUT DROP
- D) iptables -A OUTPUT -p tcp --sport 23 -j DROP

Correct Answer: A) iptables -A INPUT -p tcp --dport 23 -j DROP

Distractor Analysis:

- Why B is incorrect: The -D flag deletes an existing rule. This command would attempt to delete an ACCEPT rule for port 23 — which likely does not exist — and would fail or have no effect on blocking inbound Telnet.
- Why C is incorrect: iptables -P INPUT DROP sets the default policy for the entire INPUT chain to DROP, blocking all inbound traffic that does not match an explicit ACCEPT rule. This is far broader than blocking a single port and would disrupt all inbound connections including SSH.
- Why D is incorrect: The OUTPUT chain applies to traffic originating from the local host. Blocking port 23 on OUTPUT would prevent the server from initiating outbound Telnet connections — it would not block inbound Telnet connections from external clients.

---

**Question 5**

An administrator adds a firewalld rule with --permanent but notices it is not currently active.
What additional step is required to make the permanent rule take effect without rebooting?

- A) Run systemctl restart firewalld to restart the daemon and load permanent rules.
- B) Run firewall-cmd --reload to apply the permanent configuration to the running firewall state.
- C) Run firewall-cmd --complete-reload to flush all active connections and load the permanent rules.
- D) Log out and back in so the shell session picks up the new firewall rules.

Correct Answer: B) Run firewall-cmd --reload to apply the permanent configuration to the running firewall state.

Distractor Analysis:

- Why A is incorrect: systemctl restart firewalld restarts the entire daemon, which also loads permanent rules, but it briefly interrupts the firewall service. firewall-cmd --reload is the preferred method because it applies permanent rules without a service interruption.
- Why C is incorrect: firewall-cmd --complete-reload drops all active network connections and reloads the kernel modules. This is disruptive and reserved for situations requiring a full module reset. --reload is the correct non-disruptive option.
- Why D is incorrect: Firewall rules are kernel-level configuration managed by firewalld — they have no relationship to user shell sessions. Logging out and back in has no effect on firewall rule activation.

---

**Question 6**

An administrator needs to view all currently active services and ports allowed in the default
firewalld zone. Which command provides this information?

- A) firewall-cmd --status
- B) firewall-cmd --list-all
- C) firewall-cmd --get-zones
- D) firewall-cmd --show-permanent

Correct Answer: B) firewall-cmd --list-all

Distractor Analysis:

- Why A is incorrect: --status is not a valid firewall-cmd flag. The service status is checked with systemctl status firewalld. The active rule set is shown with --list-all.
- Why C is incorrect: --get-zones lists all available zone names but does not show the rules or services in any zone. It simply outputs a space-separated list of zone names.
- Why D is incorrect: --show-permanent is not a valid firewall-cmd flag. To view permanent rules for a zone, use --list-all --permanent.

---

**Question 7**

An administrator runs iptables -F on a production server that has a default INPUT chain policy
of DROP. What is the immediate effect on inbound connectivity?

- A) All inbound connections are allowed because flushing removes the restrictive rules.
- B) All inbound connections are dropped because the default DROP policy now applies to all packets with no rules to match.
- C) Only SSH connections are maintained because -F preserves established connections.
- D) The -F command fails because flushing rules when the default policy is DROP is not permitted.

Correct Answer: B) All inbound connections are dropped because the default DROP policy now applies to all packets with no rules to match.

Distractor Analysis:

- Why A is incorrect: iptables -F removes all rules from all chains, but the default policy remains unchanged. With a DROP policy and no ACCEPT rules, all traffic that was previously allowed by rules is now dropped.
- Why C is incorrect: iptables -F does not distinguish between new and established connections. Without the ESTABLISHED,RELATED ACCEPT rule that was just flushed, even responses to outbound connections will be dropped.
- Why D is incorrect: iptables -F works regardless of the default policy. There is no built-in protection against flushing rules on a system with a DROP policy — this is a dangerous but valid operation that the administrator must guard against.

---

**Question 8**

A security team requires that all denied inbound connection attempts to a production web server
be logged for security analysis. Which ufw command sequence correctly enables logging at an
appropriate level and where can the log entries be found?

- A) ufw log on && cat /var/log/ufw.log
- B) ufw logging medium; logs appear via journalctl with kernel UFW entries
- C) ufw enable-logging full && ls /etc/ufw/logs/
- D) iptables -A INPUT -j LOG --log-prefix "BLOCKED: "; logs appear in /var/log/iptables.log

Correct Answer: B) ufw logging medium; logs appear via journalctl with kernel UFW entries

Distractor Analysis:

- Why A is incorrect: The correct ufw logging command is ufw logging on (or ufw logging LEVEL), not ufw log on. Also, ufw log entries appear in the kernel journal (journalctl -k) and /var/log/kern.log, not in /var/log/ufw.log.
- Why C is incorrect: enable-logging is not a valid ufw command. There is no /etc/ufw/logs/ directory — ufw logs go through the kernel logging facility.
- Why D is incorrect: While adding LOG rules to iptables is technically valid, it is not the standard approach when using ufw. The ufw logging command is the correct tool for enabling ufw-level logging. Additionally, iptables LOG entries go to the kernel log (syslog), not to a dedicated /var/log/iptables.log file by default.

---

**Question 9**

An administrator needs to allow SSH access only from the management subnet 10.10.10.0/24 on
a ufw-managed Ubuntu server. All other SSH access should be denied. Which command sequence
correctly implements this policy?

- A) ufw allow ssh && ufw deny from 0.0.0.0/0 to any port 22
- B) ufw allow from 10.10.10.0/24 to any port 22 && ufw deny 22/tcp
- C) ufw allow from 10.10.10.0/24 to any port 22 (ufw's default deny handles the rest)
- D) ufw allow 22/tcp && ufw deny from !10.10.10.0/24 to any port 22

Correct Answer: B) ufw allow from 10.10.10.0/24 to any port 22 && ufw deny 22/tcp

Distractor Analysis:

- Why A is incorrect: This adds a broad allow-ssh rule first, then a deny rule after it. Because ufw evaluates rules in order and the ALLOW rule comes first, all SSH connections would be allowed before reaching the DENY rule.
- Why C is incorrect: This depends on ufw's default deny policy being set. If the default policy is ALLOW (the default for a freshly enabled ufw), then SSH from all sources would be allowed and only the subnet-specific rule would exist with no effect on other sources. An explicit deny rule is needed for clarity and correctness.
- Why D is incorrect: The ! (negation) syntax for source address exclusions is not supported in standard ufw command syntax. The correct approach is to add the specific allow rule and a broad deny rule in that order.

---

**Question 10**

An administrator examines a firewalld configuration and sees that the public zone has the ssh
service listed under services. They also notice that a source address 10.1.1.0/24 is assigned
to the trusted zone. How does firewalld determine which zone rules apply to a packet from
10.1.1.50 on port 22?

- A) The packet matches both zones; firewalld applies the most restrictive rules from both zones.
- B) Source-based zone assignments take priority over interface-based assignments. The packet from 10.1.1.50 is processed by the trusted zone rules, not the public zone.
- C) The packet is processed by the public zone because SSH is explicitly allowed there.
- D) firewalld queries DNS to resolve 10.1.1.50 and assigns it to a zone based on its hostname.

Correct Answer: B) Source-based zone assignments take priority over interface-based assignments. The packet from 10.1.1.50 is processed by the trusted zone rules, not the public zone.

Distractor Analysis:

- Why A is incorrect: firewalld does not combine rules from multiple zones for a single packet. Each packet is processed by exactly one zone — the most specific match (source address before interface assignment).
- Why C is incorrect: While SSH is allowed in the public zone, the source-based zone assignment overrides the interface-based zone. The packet from 10.1.1.50 goes to the trusted zone, where all traffic is permitted regardless of the public zone's SSH rule.
- Why D is incorrect: firewalld uses IP address-based matching, not DNS resolution, for zone assignment. DNS lookups would be too slow and unreliable for firewall packet classification.
