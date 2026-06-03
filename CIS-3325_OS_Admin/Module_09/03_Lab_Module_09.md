# Lab 09: Networking Configuration

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Points:** 100
**Estimated Time:** 75-90 minutes

---

### Overview

In this lab you will inspect and configure network interfaces using the ip command suite,
use nmcli for persistent configuration, explore DNS resolution files, and use diagnostic
tools to test and troubleshoot network connectivity.

**What you will practice:**

- ip addr show, ip link show, ip route show
- Temporary ip addr add versus persistent nmcli con mod
- /etc/hosts, /etc/resolv.conf, and /etc/nsswitch.conf
- dig and nslookup for DNS queries
- ping and traceroute for connectivity testing
- ss for listening port inspection

---

### Prerequisites

- Ubuntu Server VM from Lab 01 is running and has internet access
- You are logged in as labadmin
- The VM has an active network connection (can ping 8.8.8.8)
- You have watched both parts of the Module 09 video lecture

---

### Part 1 - Interface Inspection

**Step 1.1 - View all interfaces**

```bash
ip addr show
```

Record:
- The loopback interface (lo) IP address
- The main interface name (eth0, ens33, etc.)
- The main interface IPv4 address and subnet prefix

**Step 1.2 - View link-layer status**

```bash
ip link show
```

Note the state: UP or DOWN for each interface.

**Step 1.3 - View the routing table**

```bash
ip route show
```

Identify:
- The default route (0.0.0.0/0)
- The gateway IP address
- Any directly connected network routes

**Step 1.4 - Test a route lookup**

```bash
ip route get 8.8.8.8
```

This shows which interface and gateway would be used to reach 8.8.8.8.

---

### Part 2 - Temporary IP Configuration

**Step 2.1 - Add a temporary IP address**

```bash
ip addr show
sudo ip addr add 192.168.100.200/24 dev lo
ip addr show lo
```

The loopback interface now has a second address. This is a temporary change.

**Step 2.2 - Test connectivity to the temporary address**

```bash
ping -c 2 192.168.100.200
```

The ping succeeds because the address is assigned locally.

**Step 2.3 - Remove the temporary address**

```bash
sudo ip addr del 192.168.100.200/24 dev lo
ip addr show lo
```

The address is removed.

**Step 2.4 - Confirm temporary changes do not persist**

```bash
sudo ip addr add 10.99.99.1/24 dev lo
ip addr show lo
```

Note that the address appears. Now simulate what happens at a network reset:

```bash
sudo ip addr del 10.99.99.1/24 dev lo
```

This demonstrates why temporary changes must not be relied on for production.

---

### Part 3 - Persistent Configuration with nmcli

**Step 3.1 - View connection profiles**

```bash
nmcli con show
```

Record the NAME and DEVICE columns. The NAME is the profile name used in subsequent commands.

**Step 3.2 - View current connection details**

```bash
nmcli con show "$(nmcli -t -f NAME con show | head -1)"
```

This shows all settings for the first connection profile.

**Step 3.3 - Check current DNS configuration**

```bash
nmcli con show "$(nmcli -t -f NAME con show | head -1)" | grep dns
```

**Step 3.4 - Add a secondary DNS server (persistent)**

Store the connection name in a variable for reuse:

```bash
CONN=$(nmcli -t -f NAME con show | head -1)
echo "Connection name: $CONN"
```

Add a secondary DNS server:

```bash
nmcli con mod "$CONN" ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con show "$CONN" | grep dns
```

Apply the change:

```bash
nmcli con up "$CONN"
```

**Step 3.5 - Verify the DNS change took effect**

```bash
cat /etc/resolv.conf
```

The DNS servers from the NetworkManager profile should appear in resolv.conf.

---

### Part 4 - DNS Resolution

**Step 4.1 - Examine resolution configuration files**

```bash
cat /etc/nsswitch.conf | grep hosts
```

Record the hosts: line and the order of resolution methods.

```bash
cat /etc/resolv.conf
```

Record the nameserver IP addresses.

```bash
cat /etc/hosts
```

Record all non-comment entries.

**Step 4.2 - Add a local hosts entry**

```bash
echo "127.0.0.1  lab09test.local" | sudo tee -a /etc/hosts
```

**Step 4.3 - Test local hosts resolution**

```bash
ping -c 2 lab09test.local
nslookup lab09test.local
```

ping and nslookup should both resolve lab09test.local to 127.0.0.1 from /etc/hosts.

**Step 4.4 - DNS queries with dig**

```bash
dig google.com
```

Record: the ANSWER SECTION IP address, the SERVER line (which DNS server answered), and
the query time.

```bash
dig google.com MX
```

Shows the mail exchanger records for google.com.

```bash
dig @8.8.8.8 google.com
```

Query Google's public DNS directly, bypassing the system default.

```bash
dig @1.1.1.1 google.com
```

Query Cloudflare's DNS. Compare the results and query times.

**Step 4.5 - Reverse DNS lookup**

```bash
dig -x 8.8.8.8
```

Resolves an IP address to its hostname.

**Step 4.6 - Clean up the hosts entry**

```bash
sudo sed -i '/lab09test.local/d' /etc/hosts
cat /etc/hosts
```

---

### Part 5 - Connectivity Testing

**Step 5.1 - Systematic ping test**

```bash
ping -c 2 127.0.0.1
```

Loopback test.

```bash
ping -c 2 $(ip addr show | awk '/inet / && !/127/ {print $2}' | head -1 | cut -d/ -f1)
```

Ping the local interface IP.

```bash
GATEWAY=$(ip route show default | awk '{print $3}')
echo "Gateway: $GATEWAY"
ping -c 2 $GATEWAY
```

Ping the default gateway.

```bash
ping -c 2 8.8.8.8
```

Ping a public IP.

```bash
ping -c 2 google.com
```

Ping using a hostname (tests DNS resolution).

**Step 5.2 - Traceroute**

```bash
sudo apt install -y traceroute
traceroute -n 8.8.8.8
```

Record the number of hops and identify any hops that time out (* * *).

---

### Part 6 - Port and Service Inspection

**Step 6.1 - List listening ports**

```bash
ss -tuln
```

Record which ports are listening on the system.

**Step 6.2 - Show processes with ports**

```bash
sudo ss -tulnp
```

Identify the process listening on port 22 (sshd).

**Step 6.3 - Filter for a specific port**

```bash
ss -tulnp | grep :22
```

**Step 6.4 - Show all TCP connections**

```bash
ss -tan
```

The ESTABLISHED connections show your current SSH session. TIME-WAIT connections are
recently closed connections that the kernel is cleaning up.

**Step 6.5 - Check a service port**

```bash
sudo systemctl start ssh
ss -tulnp | grep sshd
```

Verify that sshd is listening.

```bash
sudo systemctl stop ssh
ss -tulnp | grep sshd
```

After stopping, no sshd entry appears in ss output.

```bash
sudo systemctl start ssh
```

Restart ssh before ending the lab.

---

### Part 7 - Hostname Configuration

**Step 7.1 - View current hostname**

```bash
hostname
hostnamectl
```

**Step 7.2 - Set hostname**

```bash
sudo hostnamectl set-hostname lab09server.example.local
hostname
```

**Step 7.3 - Verify persistence**

```bash
cat /etc/hostname
```

The hostname is stored in /etc/hostname.

**Step 7.4 - Restore original hostname**

```bash
sudo hostnamectl set-hostname ubuntu-server
```

---

### Part 8 - Analysis Questions

**Question 1:** Explain the technical difference between running ip addr add 10.0.0.1/24 dev ens33 and running nmcli con mod "ens33" ipv4.addresses 10.0.0.1/24 ipv4.method manual followed by nmcli con up "ens33". When would you use each approach?

**Question 2:** A server can ping 8.8.8.8 successfully but cannot connect to google.com by hostname. Identify the layer where the failure is occurring and write the exact diagnostic commands you would run to determine whether the problem is in /etc/resolv.conf, /etc/nsswitch.conf, or the DNS servers themselves.

**Question 3:** You run ss -tulnp and see that nginx is listening on 0.0.0.0:80 but not on 0.0.0.0:443. Explain what this means in terms of service availability, and write the command you would use to verify that the service is also failing to respond to HTTPS requests from a client perspective.

**Question 4:** An administrator adds the line 192.168.1.50 dbserver01 to /etc/hosts on a web server. The web application uses dbserver01 as its database hostname. Later, the database server is moved to 192.168.1.75 and the DNS record is updated. The web application still connects to the old IP. Explain why, what the resolution order problem is, and how to fix it.

**Question 5:** Describe the complete seven-layer troubleshooting methodology for diagnosing why a server cannot reach a remote service on port 443. Write the specific command for each layer (physical through application) in the correct diagnostic sequence.

---

### Deliverables

Submit all of the following through the course LMS:

1. Screenshot of Part 1, Step 1.3 showing ip route show output with the default route identified
2. Screenshot of Part 2, Step 2.1 showing the temporary address added to lo
3. Screenshot of Part 3, Step 3.5 showing the updated /etc/resolv.conf after nmcli change
4. Screenshot of Part 4, Step 4.3 showing ping and nslookup resolving lab09test.local
5. Screenshot of Part 5, Step 5.1 showing all four ping steps (loopback through hostname)
6. Screenshot of Part 6, Step 6.2 showing sudo ss -tulnp with sshd process identified
7. Written answers to all five analysis questions

---

### Grading Rubric

| Component | Points |
|-----------|--------|
| ip route show screenshot | 10 |
| Temporary address on lo screenshot | 10 |
| /etc/resolv.conf update screenshot | 10 |
| /etc/hosts resolution screenshot | 10 |
| Systematic ping test screenshot | 10 |
| ss -tulnp with sshd screenshot | 10 |
| Analysis Question 1 (temporary vs persistent) | 5 |
| Analysis Question 2 (DNS diagnosis) | 5 |
| Analysis Question 3 (ss and port 443) | 5 |
| Analysis Question 4 (/etc/hosts override) | 10 |
| Analysis Question 5 (seven-layer methodology) | 15 |
| **Total** | **100** |
