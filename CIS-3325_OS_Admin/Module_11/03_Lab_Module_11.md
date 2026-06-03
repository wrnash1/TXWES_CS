# Lab 11: Firewall Management

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 75-90 minutes

---

### Overview

In this lab you will configure the Linux firewall using ufw (Ubuntu's firewall) and examine
iptables rules directly. You will practice adding and removing rules, verifying connectivity,
and understanding the persistence model.

**What you will practice:**

- ufw enable, allow, deny, status, and delete
- ufw logging and log inspection
- iptables -L, -A, -I, -D, and default policy management
- iptables persistence with netfilter-persistent
- Understanding DROP versus REJECT
- Testing firewall rules with ss and connection tests

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running
- You are logged in as labadmin with an active SSH or console session
- You have watched both parts of the Module 11 video lecture
- WARNING: Before enabling any firewall rules, ensure SSH is allowed. Follow steps in order.

---

### Part 1 - Baseline Survey

**Step 1.1 - Check current firewall state**

```bash
sudo ufw status
```

If ufw is inactive, no rules are currently enforced.

**Step 1.2 - Check iptables rules**

```bash
sudo iptables -L -n -v
```

Note the default policies for INPUT, OUTPUT, and FORWARD chains. On a fresh Ubuntu system
with ufw inactive, all three default to ACCEPT.

**Step 1.3 - Verify SSH is currently accessible**

```bash
sudo ss -tulnp | grep :22
```

Confirm sshd is listening on port 22 before enabling any firewall rules.

---

### Part 2 - ufw Configuration

**Step 2.1 - Allow SSH before enabling ufw**

```bash
sudo ufw allow ssh
sudo ufw status
```

The rule is added but ufw is still inactive. Verify the rule appears:

```bash
sudo ufw show added
```

**Step 2.2 - Enable ufw**

```bash
sudo ufw enable
```

Type y when prompted. The firewall is now active and the SSH rule takes effect.

```bash
sudo ufw status
```

Status should show active. SSH should be listed as ALLOW.

**Step 2.3 - Verify SSH access is still working**

Open a new terminal or SSH session to confirm access is not broken.

**Step 2.4 - Add service and port rules**

```bash
sudo ufw allow http
sudo ufw allow 443/tcp
sudo ufw status
```

Both HTTP (port 80) and HTTPS (port 443) are now allowed.

**Step 2.5 - Allow from a specific source**

```bash
sudo ufw allow from 127.0.0.1 to any port 8080
sudo ufw status
```

Port 8080 is only accessible from the loopback interface.

**Step 2.6 - Deny a specific port**

```bash
sudo ufw deny 23/tcp
sudo ufw status
```

Telnet (port 23) is explicitly denied.

---

### Part 3 - ufw Rule Management

**Step 3.1 - View rules with line numbers**

```bash
sudo ufw status numbered
```

Record the line numbers for each rule.

**Step 3.2 - Delete a rule by specification**

```bash
sudo ufw delete allow http
sudo ufw status
```

The HTTP rule is removed.

**Step 3.3 - Delete a rule by number**

```bash
sudo ufw status numbered
```

Note the line number of the deny 23/tcp rule.

```bash
sudo ufw delete LINENUMBER
```

Replace LINENUMBER with the actual number. Type y to confirm.

```bash
sudo ufw status
```

Verify the rule is removed.

**Step 3.4 - Re-add HTTP**

```bash
sudo ufw allow http
```

---

### Part 4 - ufw Logging

**Step 4.1 - Enable logging**

```bash
sudo ufw logging on
sudo ufw logging medium
```

**Step 4.2 - View log output**

```bash
sudo journalctl -k | grep UFW | tail -20
```

Firewall log entries appear in the kernel journal.

**Step 4.3 - Generate a denied connection attempt**

In a separate terminal, try to connect to a blocked port:

```bash
nc -zv localhost 23
```

Expected: connection refused. Back in the first terminal, check for a UFW BLOCK entry:

```bash
sudo journalctl -k | grep "UFW BLOCK" | tail -5
```

---

### Part 5 - iptables Direct Access

**Step 5.1 - View the current iptables state with ufw active**

```bash
sudo iptables -L -n -v
```

Note that ufw has added chains (ufw-user-input, ufw-before-input, etc.) to manage its rules.

**Step 5.2 - View only the custom ufw user rules**

```bash
sudo iptables -L ufw-user-input -n -v
```

**Step 5.3 - Understanding rule order and line numbers**

```bash
sudo iptables -L INPUT -n -v --line-numbers
```

**Step 5.4 - Add a direct iptables rule**

```bash
sudo iptables -A INPUT -p tcp --dport 9999 -j DROP
sudo iptables -L INPUT -n -v --line-numbers | tail -5
```

The DROP rule for port 9999 is appended to the INPUT chain.

**Step 5.5 - Test the iptables rule**

```bash
nc -zv localhost 9999
```

Connection attempt is dropped (timeout, not connection refused). This demonstrates the
difference between DROP and REJECT.

**Step 5.6 - Delete the direct iptables rule**

```bash
sudo iptables -D INPUT -p tcp --dport 9999 -j DROP
sudo iptables -L INPUT -n -v --line-numbers | tail -5
```

The rule is removed.

---

### Part 6 - iptables Persistence

**Step 6.1 - Install iptables-persistent**

```bash
sudo apt install -y iptables-persistent
```

During installation, you may be prompted to save current rules. Select Yes.

**Step 6.2 - View saved rules**

```bash
sudo cat /etc/iptables/rules.v4
```

**Step 6.3 - Add a rule and save**

```bash
sudo iptables -A INPUT -p icmp -j ACCEPT
sudo netfilter-persistent save
sudo cat /etc/iptables/rules.v4 | grep icmp
```

The ICMP rule is now saved.

**Step 6.4 - Demonstrate persistence**

```bash
sudo iptables -D INPUT -p icmp -j ACCEPT
sudo iptables -L INPUT -n | grep icmp
```

The rule is gone from the running state.

```bash
sudo netfilter-persistent reload
sudo iptables -L INPUT -n | grep icmp
```

After reload, the saved ICMP rule is restored.

---

### Part 7 - Reset to Clean State

```bash
sudo ufw disable
sudo ufw reset
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow 443/tcp
```

---

### Part 8 - Analysis Questions

**Question 1:** Explain why running sudo ufw enable without first running sudo ufw allow ssh on a server you are managing via SSH would lock you out. Describe the exact mechanism: what happens to existing SSH connections versus new connections when ufw is enabled with its default policy?

**Question 2:** An administrator adds the following iptables rule: iptables -A INPUT -p tcp --dport 22 -j ACCEPT. After a reboot, the rule is gone and SSH is still accessible. Explain: why is SSH accessible even without the rule, and how is the system's current firewall state (no explicit rules, default ACCEPT) different from a hardened firewall configuration?

**Question 3:** Explain the difference between DROP and REJECT as iptables targets. From a security perspective, why would you prefer DROP for internet-facing rules? From an operational perspective, why might you use REJECT on internal networks? Write the iptables rule to REJECT all traffic on port 23 with an ICMP port-unreachable response.

**Question 4:** An administrator configures a firewalld rule with firewall-cmd --add-service=mysql --permanent but after testing notes that MySQL connections are not being allowed. They run firewall-cmd --list-services and see mysql is not in the list. What step was missed? Write the complete two-command sequence that would have correctly added the rule and made it immediately active.

**Question 5:** Your company's security policy requires that a web server only accept HTTP traffic from specific partner IP ranges (10.20.0.0/16 and 10.30.0.0/16) and block all other HTTP traffic. Write the complete ufw rule sequence to implement this policy, including rules for HTTPS if the same restriction applies, and explain why rule order matters for this configuration.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 2, Step 2.2 showing ufw enable and the resulting status
2. Screenshot of Part 2, Step 2.6 showing all rules including the deny 23/tcp rule
3. Screenshot of Part 4, Step 4.3 showing the UFW BLOCK log entry for the denied connection
4. Screenshot of Part 5, Step 5.4 showing the direct iptables rule appended to INPUT
5. Screenshot of Part 6, Step 6.3 showing the saved iptables rules with the ICMP entry
6. Screenshot of Part 6, Step 6.4 showing the rule restored after netfilter-persistent reload
7. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| ufw enable and status screenshot | 10 |
| Rules including deny 23/tcp screenshot | 10 |
| UFW BLOCK log entry screenshot | 10 |
| Direct iptables rule screenshot | 10 |
| Saved iptables rules screenshot | 10 |
| netfilter-persistent reload screenshot | 10 |
| Analysis Question 1 (ufw lockout) | 5 |
| Analysis Question 2 (default ACCEPT vs hardened) | 5 |
| Analysis Question 3 (DROP vs REJECT) | 5 |
| Analysis Question 4 (firewalld --reload) | 10 |
| Analysis Question 5 (source-restricted rules) | 15 |
| **Total** | **100** |
