# Video Script: Module 11 - Firewall Management (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 11. A firewall is a policy enforcement point that decides which network
traffic is allowed and which is dropped. On Linux, firewalls are implemented in the kernel
using netfilter, and there are three main tools to manage them: iptables (direct kernel rules),
firewalld (zone-based, used on RHEL/CentOS), and ufw (Uncomplicated Firewall, used on Ubuntu).
By the end of both parts you will be able to configure host-based firewalls on both Ubuntu
and RHEL, understand the iptables chain model, and create persistent rules.

---

### Section 1: How Linux Firewalls Work

[SHOW TERMINAL]

All three tools (iptables, firewalld, ufw) ultimately configure netfilter rules in the Linux
kernel. Packets pass through a series of chains and tables as they traverse the network stack:

Tables contain chains. The default table for filtering is the filter table. The filter table
has three built-in chains:

INPUT: Traffic destined for this system.
OUTPUT: Traffic originating from this system.
FORWARD: Traffic passing through this system (for routers/gateways).

Each chain has a default policy (ACCEPT or DROP) and a list of rules. Rules are evaluated
top to bottom. The first matching rule wins. If no rule matches, the default policy applies.

Actions (targets):
- ACCEPT: Allow the packet
- DROP: Silently discard the packet
- REJECT: Discard and send an ICMP error back to the sender
- LOG: Log the packet (and continue to next rule)

```bash
sudo iptables -L -n -v
```

Lists all rules in all chains, numeric IPs, with packet and byte counters.

---

### Section 2: iptables Fundamentals

[SHOW TERMINAL]

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

-A INPUT: Append a rule to the INPUT chain
-p tcp: Match TCP protocol
--dport 22: Match destination port 22
-j ACCEPT: Action is ACCEPT

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

Allow HTTP and HTTPS.

```bash
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

Allow established connections and related traffic (like ICMP error replies for active connections).
This is essential — without it, responses to outbound connections would be dropped.

```bash
sudo iptables -P INPUT DROP
```

Set the default policy for INPUT to DROP. Now any traffic not matched by an ACCEPT rule is
dropped. This is the "default deny" model. Only do this after you have added ACCEPT rules for
the traffic you need, including SSH.

```bash
sudo iptables -A INPUT -i lo -j ACCEPT
```

Always allow loopback traffic. Many local services communicate through lo and breaking
this will cause application failures.

```bash
sudo iptables -I INPUT 1 -i lo -j ACCEPT
```

-I inserts at position 1 (the top of the chain). Use this to ensure the loopback rule
is evaluated first.

---

### Section 3: iptables Rule Management

[SHOW TERMINAL]

```bash
sudo iptables -L INPUT -n -v --line-numbers
```

Shows rules with line numbers. The --line-numbers flag makes it easy to reference rules
for insertion or deletion.

```bash
sudo iptables -D INPUT 3
```

Delete rule number 3 from the INPUT chain.

```bash
sudo iptables -D INPUT -p tcp --dport 8080 -j ACCEPT
```

Delete a rule by specifying its exact parameters.

```bash
sudo iptables -F INPUT
```

Flush (delete) all rules in the INPUT chain. Dangerous on a remote server if the default
policy is DROP — this will allow all traffic, or block all traffic depending on the policy.

```bash
sudo iptables -F
```

Flush all rules in all chains. Combined with a DROP default policy, this locks you out.
Always reset the policy to ACCEPT before flushing.

Saving iptables rules (Ubuntu):

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

iptables rules are lost on reboot unless saved. iptables-persistent loads saved rules
at boot. The rules are stored in /etc/iptables/rules.v4.

---

### Section 4: ufw (Uncomplicated Firewall) on Ubuntu

[SHOW TERMINAL]

ufw is the recommended firewall tool on Ubuntu. It provides a simpler interface on top of
iptables.

```bash
sudo ufw status
```

Shows whether ufw is active and lists all rules.

```bash
sudo ufw enable
```

Enables ufw. Note: if you enable ufw on an SSH session without first allowing SSH,
you will be locked out.

```bash
sudo ufw allow ssh
```

Allow SSH by service name. Equivalent to allowing TCP port 22.

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

Allow specific ports.

```bash
sudo ufw allow from 192.168.1.0/24 to any port 22
```

Allow SSH only from a specific subnet.

```bash
sudo ufw deny 23/tcp
```

Explicitly deny a port.

```bash
sudo ufw delete allow 80/tcp
```

Remove a rule.

```bash
sudo ufw status numbered
```

Show rules with line numbers for deletion by number.

```bash
sudo ufw delete 3
```

Delete rule number 3.

ufw rules are automatically persistent — they survive reboots without additional configuration.

---

### Section 5: ufw Logging

[SHOW TERMINAL]

```bash
sudo ufw logging on
```

Enable logging for denied packets.

```bash
sudo ufw logging medium
```

Logging levels: off, low, medium, high, full.

```bash
sudo journalctl | grep UFW
```

View ufw log entries via the systemd journal.

Logs show: UFW BLOCK or UFW ALLOW, the interface, source/destination IP, and port.

---

### Certification Connection

Firewall management maps to Linux+ Domain 2.0 (Security). Key exam objectives:

Know iptables chains: INPUT (inbound), OUTPUT (outbound), FORWARD (routing).

Know iptables targets: ACCEPT, DROP, REJECT, LOG.

Know the difference between -A (append) and -I (insert at position).

Know ufw enable, allow, deny, status, and delete.

Know the firewalld workflow: --add-service/--add-port with --permanent plus --reload.

Know that ufw rules are persistent by default; iptables rules are not.

---

### Transition to Part 2

In Part 2 we cover firewalld (used on RHEL/CentOS), zones, services, and the permanent
versus runtime configuration model. We also cover connection tracking and common firewall
policy patterns.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
