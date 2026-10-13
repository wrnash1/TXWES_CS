# Video Script: Module 11 - Firewall Management (Part 2 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 11 minutes
**Part:** 2 of 2 - firewalld and Production Patterns

---

### Opening

Welcome back to Part 2 of Module 11. In Part 1 we covered the iptables chain model, iptables
commands, and ufw for Ubuntu. In Part 2 we cover firewalld — the zone-based firewall used on
RHEL, CentOS, Fedora, and Rocky Linux. We also cover the permanent versus runtime configuration
model, common production firewall patterns, and how to save and restore rules.

---

### Section 1: firewalld Architecture

firewalld uses a zone model. A zone is a named set of rules that applies to a network interface
or source address range.

[SHOW TERMINAL]

```bash
sudo systemctl status firewalld
```

```bash
sudo firewall-cmd --get-zones
```

Lists all available zones. Common zones:

- public: Used for interfaces exposed to untrusted networks (the internet). Minimum services permitted.
- trusted: All connections are accepted. Used for internal trusted networks.
- home: Allows ssh, dhcpv6-client, and a few others. For home networks.
- dmz: Allows ssh only. For servers in a DMZ.
- drop: All incoming connections are dropped silently. Maximum restriction.
- block: Incoming connections are rejected (ICMP error sent back).

```bash
sudo firewall-cmd --get-default-zone
```

Shows which zone applies to interfaces that do not have an explicit zone assignment.

```bash
sudo firewall-cmd --get-active-zones
```

Shows which zones are currently active and which interfaces are in each zone.

---

### Section 2: firewalld Runtime vs Permanent

[SHOW TERMINAL]

This is the most important concept in firewalld. Every rule change can be either:

Runtime: Applied immediately to the running firewall. Lost when firewalld is reloaded or
the system reboots.

Permanent: Written to configuration files. Does not take effect until firewalld is reloaded.

```bash
sudo firewall-cmd --add-service=https
```

Runtime only — active now, gone after reload.

```bash
sudo firewall-cmd --add-service=https --permanent
```

Permanent only — written to config, not active yet.

```bash
sudo firewall-cmd --reload
```

Loads the permanent configuration into the running state. Clears all non-permanent runtime
rules and applies the permanent ones.

Best practice for adding a rule that is both active now and permanent:

Option 1: Add it twice:
```bash
sudo firewall-cmd --add-service=https
sudo firewall-cmd --add-service=https --permanent
```

Option 2: Add it permanently and reload:
```bash
sudo firewall-cmd --add-service=https --permanent
sudo firewall-cmd --reload
```

---

### Section 3: Managing Services and Ports

[SHOW TERMINAL]

```bash
sudo firewall-cmd --list-all
```

Shows all rules for the default zone: services, ports, sources, rich rules.

```bash
sudo firewall-cmd --list-services
```

Lists services currently allowed in the active zone.

```bash
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent
sudo firewall-cmd --reload
```

Allow HTTP and HTTPS persistently.

```bash
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```

Allow a specific port number. Use this when there is no named service definition.

```bash
sudo firewall-cmd --remove-service=http --permanent
sudo firewall-cmd --reload
```

Remove a service rule.

```bash
sudo firewall-cmd --list-ports
```

Lists ports explicitly added (not via service definitions).

---

### Section 4: firewalld Zones and Source-Based Rules

[SHOW TERMINAL]

```bash
sudo firewall-cmd --zone=public --add-service=ssh --permanent
sudo firewall-cmd --zone=trusted --add-source=192.168.1.0/24 --permanent
sudo firewall-cmd --reload
```

This configuration:
- Allows SSH in the public zone (accessible from anywhere)
- Allows all traffic from the 192.168.1.0/24 subnet in the trusted zone

Any traffic from 192.168.1.x is now fully trusted. Traffic from other sources is subject
to the public zone rules.

```bash
sudo firewall-cmd --zone=drop --change-interface=eth1 --permanent
```

Move eth1 to the drop zone — silently drops all inbound traffic on that interface.

```bash
sudo firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="203.0.113.0/24" drop' --permanent
```

Rich rules allow more complex conditions: source address blocking, rate limiting, logging.
The example blocks all traffic from a specific IP range.

---

### Section 5: Viewing and Testing Firewall Rules

[SHOW TERMINAL]

```bash
sudo firewall-cmd --list-all --zone=public
```

Shows the full configuration for the public zone.

```bash
sudo firewall-cmd --list-all-zones
```

Shows all zones and their rules.

```bash
sudo firewall-cmd --query-service=ssh
```

Returns yes if ssh is currently allowed in the default zone. Returns no if not.

```bash
sudo firewall-cmd --runtime-to-permanent
```

Copies all current runtime rules to the permanent configuration. Useful when you have
been testing rules interactively and want to save the current state permanently.

---

### Section 6: iptables Persistence (Saving Rules)

[SHOW TERMINAL]

Unlike firewalld and ufw, raw iptables rules are not persistent. They must be saved manually.

Ubuntu:

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

Rules are saved to /etc/iptables/rules.v4 (IPv4) and /etc/iptables/rules.v6 (IPv6).
The iptables-persistent service loads them at boot.

To reload saved rules:

```bash
sudo netfilter-persistent reload
```

Manually saving current rules:

```bash
sudo iptables-save > /etc/iptables/rules.v4
```

Restoring rules from a file:

```bash
sudo iptables-restore < /etc/iptables/rules.v4
```

---

### Section 7: Exam Tips for Module 11

iptables default policy DROP versus rules: default policy applies to all packets that do
not match any rule. Adding ACCEPT rules before setting DROP policy is essential to avoid
lockouts.

ufw is Ubuntu; firewalld is RHEL/CentOS. Know which commands belong to which.

firewalld --permanent: written to config but not active. --reload: loads permanent into runtime.
Missing --permanent means the rule is lost on reboot. Missing --reload means the permanent
rule is not yet active.

ufw rules are persistent by default. No separate save step needed.

iptables -F flushes all rules. Combined with a DROP default policy, this blocks all traffic.
Always change the default policy to ACCEPT before flushing.

firewall-cmd --list-all shows the current zone's active rules. firewall-cmd --list-all-zones
shows all zones.

Rich rules in firewalld allow source IP blocking and rate limiting beyond simple
service/port rules.

---

### Summary

Module 11 covers the three Linux firewall tools: iptables (direct kernel rule manipulation),
ufw (Ubuntu's simplified wrapper), and firewalld (RHEL/CentOS zone-based management). The
underlying engine is the same — netfilter — but the management layer differs between
distributions.

Module 12 covers system logging and monitoring: syslog, journald, logrotate, and log analysis.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
