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

---

**Question 11**

An administrator runs `ufw status` and sees the following output:

```
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
443/tcp                    ALLOW       Anywhere
22/tcp (v6)                ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
443/tcp (v6)               ALLOW       Anywhere (v6)
```

The server should only accept SSH from the management network 10.0.0.0/24. Which command
sequence correctly restricts SSH while leaving web traffic unrestricted?

- A) ufw delete allow 22/tcp && ufw allow from 10.0.0.0/24 to any port 22
- B) ufw insert 1 deny 22/tcp && ufw allow from 10.0.0.0/24 to any port 22
- C) ufw allow from 10.0.0.0/24 to any port 22 && ufw deny 22/tcp
- D) ufw limit 22/tcp from 10.0.0.0/24

Correct Answer: A) ufw delete allow 22/tcp && ufw allow from 10.0.0.0/24 to any port 22

Distractor Analysis:

- Why B is incorrect: Inserting a deny rule at position 1 before adding the allow rule would cause all SSH to be denied immediately, including from the management network. The specific allow rule must come before the broad deny rule.
- Why C is incorrect: This appears correct in order (allow specific source first, then deny all others), but ufw does not guarantee that previously existing rules are evaluated after newly added rules. The existing "ALLOW Anywhere" rule for 22/tcp would match before the new deny rule. The correct approach is to first delete the broad allow rule, then add the restricted one.
- Why D is incorrect: ufw limit enables rate limiting (connection throttling to prevent brute force), not source IP restriction. The from 10.0.0.0/24 syntax is not valid with the limit subcommand in standard ufw.

---

**Question 12**

Which `iptables` command inserts a rule at the **beginning** of the INPUT chain to accept
established and related connections (required for stateful firewall operation)?

- A) iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
- B) iptables -I INPUT 1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
- C) iptables -R INPUT 1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
- D) iptables -P INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

Correct Answer: B) iptables -I INPUT 1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

Distractor Analysis:

- Why A is incorrect: The -A flag appends the rule to the end of the chain. On a chain with existing rules, an appended rule may never be reached if earlier rules match first. For a stateful connection rule that must always be evaluated early, insertion at position 1 is required.
- Why C is incorrect: The -R flag replaces an existing rule at a specified position. If the INPUT chain is empty or has different rules at position 1, this would either fail or overwrite an important existing rule. For adding a new rule at position 1, the -I (insert) flag is correct.
- Why D is incorrect: The -P flag sets the default policy for a chain (e.g., ACCEPT or DROP). It does not accept match expressions or jump targets in the same syntax as a rule. Default policies apply only when no rule in the chain matches.

---

**Question 13**

An administrator wants to log and drop all packets from a specific IP address 203.0.113.50
using iptables. They need two rules. Which pair accomplishes this correctly?

- A) iptables -A INPUT -s 203.0.113.50 -j LOG --log-prefix "BLOCKED: " && iptables -A INPUT -s 203.0.113.50 -j DROP
- B) iptables -A INPUT -s 203.0.113.50 -j DROP && iptables -A INPUT -s 203.0.113.50 -j LOG
- C) iptables -A INPUT -s 203.0.113.50 -j LOG,DROP
- D) iptables -A INPUT -s 203.0.113.50 -j LOG --log-prefix "BLOCKED: " -j DROP

Correct Answer: A) iptables -A INPUT -s 203.0.113.50 -j LOG --log-prefix "BLOCKED: " && iptables -A INPUT -s 203.0.113.50 -j DROP

Distractor Analysis:

- Why B is incorrect: Rules are evaluated in order. If the DROP rule comes first, the packet is immediately discarded and the LOG rule is never reached. For log-and-drop, the LOG rule must always precede the DROP rule.
- Why C is incorrect: iptables does not support comma-separated targets in a single -j flag. Each rule has exactly one target (LOG, DROP, ACCEPT, REJECT, etc.). Logging and dropping are always implemented as two separate sequential rules.
- Why D is incorrect: A single iptables rule can only have one -j (jump) target. Specifying -j twice in the same rule is invalid syntax; the second -j would either be ignored or cause a parse error. This is a common misconception about iptables syntax.

---

**Question 14**

An administrator successfully adds a firewalld rule to open port 8080 with:

```
firewall-cmd --add-port=8080/tcp
```

After rebooting the server, port 8080 is blocked again. What was missing from the command?

- A) The --zone flag was not specified; firewalld discards rules without an explicit zone.
- B) The --permanent flag was not used; without it, the rule is added only to the runtime configuration and is lost on reboot or reload.
- C) The --reload flag must be run immediately after adding any rule to save it.
- D) Port rules require the service name instead of the port number to persist.

Correct Answer: B) The --permanent flag was not used; without it, the rule is added only to the runtime configuration and is lost on reboot or reload.

Distractor Analysis:

- Why A is incorrect: If no --zone flag is specified, firewalld applies the rule to the default zone. The rule does take effect — it simply does not persist. The missing element is --permanent, not --zone.
- Why C is incorrect: firewall-cmd --reload applies permanent configuration to the runtime. It does not save runtime rules to the permanent configuration. Running --reload after a runtime rule would actually remove that runtime rule, not save it.
- Why D is incorrect: firewalld supports both service names (--add-service=http) and port numbers (--add-port=8080/tcp) for permanent rules. There is no requirement to use service names for persistence.

---

**Question 15**

What is the functional difference between iptables `-j DROP` and `-j REJECT` when applied
to an incoming packet?

- A) DROP silently discards the packet; the sender receives no response. REJECT discards the packet and sends an ICMP error (port-unreachable by default) back to the sender.
- B) DROP sends a TCP RST to the sender. REJECT sends an ICMP unreachable message.
- C) DROP applies to UDP traffic only. REJECT applies to TCP traffic only.
- D) There is no functional difference; both discard the packet silently.

Correct Answer: A) DROP silently discards the packet; the sender receives no response. REJECT discards the packet and sends an ICMP error (port-unreachable by default) back to the sender.

Distractor Analysis:

- Why B is incorrect: DROP does not send any response. It discards the packet with no notification. A TCP RST response is sent by REJECT with the --reject-with tcp-reset option, not by DROP.
- Why C is incorrect: Both DROP and REJECT apply to all IP traffic regardless of transport protocol (TCP, UDP, ICMP). The choice between them is about response behavior, not protocol applicability.
- Why D is incorrect: There is a significant functional difference. DROP causes the sender's connection to time out silently (which takes longer to detect and can slow down legitimate error handling). REJECT gives the sender an immediate error, which speeds up failure detection. The operational security preference for DROP is to avoid revealing firewall presence to attackers.

---

**Question 16**

An administrator runs `iptables-save > /etc/iptables/rules.v4` after configuring their
firewall rules. After a reboot, all rules are gone. What additional step is required on
Ubuntu to restore rules automatically at boot?

- A) Add iptables-restore < /etc/iptables/rules.v4 to /etc/rc.local.
- B) Install the netfilter-persistent package and run systemctl enable netfilter-persistent. The saved rules in /etc/iptables/rules.v4 are automatically restored at boot.
- C) Set the IPTABLES_SAVE_ON_STOP variable in /etc/default/iptables.
- D) Create a systemd timer that runs iptables-restore every 5 minutes.

Correct Answer: B) Install the netfilter-persistent package and run systemctl enable netfilter-persistent. The saved rules in /etc/iptables/rules.v4 are automatically restored at boot.

Distractor Analysis:

- Why A is incorrect: While /etc/rc.local would technically work, it is a legacy mechanism and is not the correct approach on modern Ubuntu systems using systemd. The netfilter-persistent service is the correct and supported method.
- Why C is incorrect: /etc/default/iptables is not a standard Ubuntu configuration file. This setting exists on some RHEL/CentOS distributions (in /etc/sysconfig/iptables-config) but is not applicable to Ubuntu's netfilter-persistent mechanism.
- Why D is incorrect: A timer running iptables-restore every 5 minutes would apply the saved rules repeatedly, which is inefficient and unnecessary. Rules should be restored once at boot, not on a recurring timer.

---

**Question 17**

An administrator runs `firewall-cmd --list-all` and sees:

```
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: ens33
  sources:
  services: cockpit dhcpv6-client ssh
  ports:
  ...
```

They want to add a permanent rule to allow HTTP and HTTPS, then apply it immediately without
rebooting. Which command sequence is correct?

- A) firewall-cmd --permanent --add-service=http --add-service=https && firewall-cmd --reload
- B) firewall-cmd --add-service=http --add-service=https && firewall-cmd --permanent --reload
- C) firewall-cmd --permanent --add-service={http,https} && systemctl restart firewalld
- D) firewall-cmd --zone=public --add-service=http && firewall-cmd --zone=public --add-service=https

Correct Answer: A) firewall-cmd --permanent --add-service=http --add-service=https && firewall-cmd --reload

Distractor Analysis:

- Why B is incorrect: Adding the service without --permanent applies only to the runtime. The subsequent --permanent --reload is not valid syntax (--reload does not take --permanent). The rules would not be saved persistently.
- Why C is incorrect: systemctl restart firewalld reloads the firewall service entirely, which is more disruptive than --reload. More importantly, brace expansion {http,https} is a shell feature that is not supported by firewall-cmd itself. The --add-service flag must be specified twice or used as two separate commands.
- Why D is incorrect: Without --permanent, these rules apply only to the runtime configuration and will be lost on the next reload or reboot. Runtime-only rules are useful for testing but not for permanent service exposure.

---

**Question 18**

A Linux server runs both a web application on port 8443 and an SSH service. The security
team requires that port 8443 be accessible only from the corporate network 192.168.100.0/22.
Using `ufw`, which pair of commands implements this requirement?

- A) ufw allow 8443/tcp && ufw deny from 0.0.0.0/0 to any port 8443
- B) ufw allow from 192.168.100.0/22 to any port 8443 && ufw deny 8443/tcp
- C) ufw allow proto tcp from 192.168.100.0/22 port 8443
- D) ufw allow 8443/tcp from 192.168.100.0/22

Correct Answer: B) ufw allow from 192.168.100.0/22 to any port 8443 && ufw deny 8443/tcp

Distractor Analysis:

- Why A is incorrect: Adding a broad allow rule first and then a deny rule after it does not work. ufw processes rules in order and would match the first ALLOW rule before reaching the DENY rule, allowing all connections.
- Why C is incorrect: The ufw allow proto syntax specifies the source port, not the destination port. The correct syntax for destination port restriction uses the to any port form: ufw allow proto tcp from 192.168.100.0/22 to any port 8443.
- Why D is incorrect: ufw does not support the allow PORT from SOURCE syntax in that order. The correct syntax for source-restricted rules is: ufw allow from SOURCE to any port PORT.

---

**Question 19**

An administrator wants all outgoing traffic from the server to be allowed by default in
iptables but all incoming traffic to be dropped by default unless explicitly permitted.
Which commands set the correct default policies?

- A) iptables -P INPUT DROP && iptables -P OUTPUT ACCEPT && iptables -P FORWARD DROP
- B) iptables -P INPUT DENY && iptables -P OUTPUT ALLOW
- C) iptables -D INPUT DROP && iptables -D OUTPUT ACCEPT
- D) iptables --default INPUT DROP && iptables --default OUTPUT ACCEPT

Correct Answer: A) iptables -P INPUT DROP && iptables -P OUTPUT ACCEPT && iptables -P FORWARD DROP

Distractor Analysis:

- Why B is incorrect: The valid iptables default policy targets are ACCEPT and DROP. DENY and ALLOW are not valid iptables policy targets. This syntax would produce an error.
- Why C is incorrect: The -D flag deletes a specific rule from a chain. It is not used to set default policies. Attempting to delete a rule named "DROP" would fail because that is a target value, not a rule specification.
- Why D is incorrect: There is no --default flag in iptables. The correct flag for setting chain default policies is -P (policy). This tests whether students know the correct flag syntax versus a logical-sounding but non-existent alternative.

---

**Question 20**

An administrator configures ufw on a server that also has Docker installed. After enabling
ufw with default deny incoming, containers can still receive incoming connections from the
internet. What is the most likely explanation?

- A) ufw rules do not apply to IPv6 traffic, and Docker uses IPv6 by default.
- B) Docker modifies iptables directly to create ACCEPT rules in the DOCKER chain, bypassing ufw's rules in the INPUT chain.
- C) Container traffic is encrypted and ufw cannot inspect it.
- D) ufw only filters traffic on the loopback interface; physical interface traffic bypasses ufw.

Correct Answer: B) Docker modifies iptables directly to create ACCEPT rules in the DOCKER chain, bypassing ufw's rules in the INPUT chain.

Distractor Analysis:

- Why A is incorrect: ufw manages both IPv4 (iptables) and IPv6 (ip6tables) rules. Default deny policies apply to both protocol families when ufw is enabled with the default configuration.
- Why C is incorrect: ufw and iptables filter at the network layer (Layer 3/4) based on IP addresses and ports. Container traffic is not inherently encrypted at the network layer, and iptables can filter it regardless of application-layer protocols.
- Why D is incorrect: ufw manages rules for all network interfaces, not just the loopback. The INPUT chain applies to all incoming traffic. The specific issue with Docker is that it bypasses the INPUT chain by inserting rules in the DOCKER and FORWARD chains with direct iptables calls, not that ufw filters the wrong interface.
