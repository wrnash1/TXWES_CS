# Video Script: Module 11 — Networking in Linux (Part 2 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome back. This is Part 2 of Module 11: Networking in Linux.

In Part 1, we configured network interfaces with `ip` and `nmcli`, and explored hostname resolution files. Now we'll tackle firewall management with `firewalld` and `iptables`, configure the SSH client, and work through the network troubleshooting toolkit that every Linux administrator needs to know cold for both real work and the Linux+ exam.

---

### Section 5: Firewall Management — firewalld

`firewalld` is the default firewall management layer on Red Hat-based distributions (RHEL, CentOS, Fedora, Rocky Linux, AlmaLinux). It provides a dynamic firewall with the concept of **zones** — trust levels assigned to network interfaces or source addresses.

**Understanding Zones**

Common zones include:

- **public** — for use in public areas; only selected connections are accepted
- **trusted** — all network connections are accepted
- **home** — for home networks; most connections are trusted
- **drop** — all incoming connections are dropped without reply
- **block** — incoming connections are rejected with an ICMP message

**Basic firewall-cmd Commands**

Check the firewall status:

```bash
sudo firewall-cmd --state
```

List all rules in the active zone:

```bash
sudo firewall-cmd --list-all
```

List available zones:

```bash
sudo firewall-cmd --get-zones
```

Get the default zone:

```bash
sudo firewall-cmd --get-default-zone
```

**Opening a Port**

Allow HTTP (port 80) in the public zone:

```bash
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --reload
```

The `--permanent` flag writes the rule to disk. Without it, the rule applies only until the next reload or reboot. Always reload after adding permanent rules.

**Opening a Service by Name**

firewalld includes predefined service definitions:

```bash
sudo firewall-cmd --zone=public --add-service=https --permanent
sudo firewall-cmd --reload
```

To list available predefined services:

```bash
sudo firewall-cmd --get-services
```

**Removing a Rule**

```bash
sudo firewall-cmd --zone=public --remove-port=80/tcp --permanent
sudo firewall-cmd --reload
```

**Rich Rules**

For more complex scenarios, firewalld supports rich rules. For example, allow SSH only from a specific subnet:

```bash
sudo firewall-cmd --zone=public \
  --add-rich-rule='rule family="ipv4" source address="10.0.1.0/24" service name="ssh" accept' \
  --permanent
sudo firewall-cmd --reload
```

---

### Section 6: iptables Basics

While `firewalld` is the modern abstraction, the Linux+ exam still tests `iptables` knowledge, and some environments (especially older or minimal installations) still use it directly.

**Understanding Chains**

iptables processes packets through chains:

- **INPUT** — packets destined for the local system
- **OUTPUT** — packets originating from the local system
- **FORWARD** — packets being routed through the system

**Viewing Current Rules**

```bash
sudo iptables -L -n -v
```

- `-L` — list rules
- `-n` — numeric output (no DNS lookups)
- `-v` — verbose (shows packet/byte counts)

**Adding Rules**

Allow established connections (required to not break existing sessions):

```bash
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

Allow SSH:

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

Drop all other incoming traffic:

```bash
sudo iptables -A INPUT -j DROP
```

**Saving iptables Rules**

On RHEL/CentOS:

```bash
sudo service iptables save
```

On Debian/Ubuntu:

```bash
sudo netfilter-persistent save
```

**Note on nftables**

Modern kernels have largely replaced iptables with `nftables`. The `iptables` commands on recent systems are often compatibility shims. The Linux+ exam covers this transition, so know that `nft list ruleset` is the equivalent command under nftables.

---

### Section 7: SSH Client Configuration

SSH (Secure Shell) is your primary tool for remote administration. The client-side configuration file is `~/.ssh/config` and it can dramatically simplify your workflow.

**Basic SSH Usage**

Connect to a remote host:

```bash
ssh user@hostname
ssh -p 2222 user@hostname
```

**The ~/.ssh/config File**

Instead of remembering IP addresses, ports, and usernames, define host aliases:

```
Host webprod
    HostName 192.168.1.100
    User deploy
    Port 22
    IdentityFile ~/.ssh/id_ed25519_prod
    ServerAliveInterval 60

Host jump-bastion
    HostName bastion.example.com
    User admin
    IdentityFile ~/.ssh/id_ed25519
```

Now connect with:

```bash
ssh webprod
```

**Key Configuration Directives**

- `HostName` — actual hostname or IP
- `User` — remote username
- `Port` — SSH port (default 22)
- `IdentityFile` — path to private key
- `ServerAliveInterval` — sends keepalive packets every N seconds
- `ProxyJump` — route connection through a bastion host
- `StrictHostKeyChecking` — whether to verify host keys (keep `yes` in production)

**Jump Hosts (Bastion)**

```
Host internal-server
    HostName 10.10.10.50
    User admin
    ProxyJump jump-bastion
```

This connects through the bastion host transparently.

---

### Section 8: Network Troubleshooting Tools

A strong troubleshooting methodology moves through the OSI model from Layer 1 up. Here are the tools for each stage.

**ping — Layer 3 Connectivity**

```bash
ping -c 4 8.8.8.8
ping -c 4 google.com
```

- `-c 4` sends exactly 4 packets
- If IP ping works but hostname ping fails, the problem is DNS, not routing

**traceroute / tracepath**

```bash
traceroute 8.8.8.8
tracepath 8.8.8.8
```

Shows each hop between your host and the destination. Useful for identifying where packets are being dropped or delayed.

**ss — Socket Statistics (replaces netstat)**

List all listening TCP ports:

```bash
ss -tlnp
```

- `-t` — TCP
- `-l` — listening sockets
- `-n` — numeric (no service name resolution)
- `-p` — show process name and PID

List all established connections:

```bash
ss -tnp
```

**nmap — Network Mapper**

Scan a host for open ports:

```bash
nmap -sV 192.168.1.1
```

Scan a subnet:

```bash
nmap -sn 192.168.1.0/24
```

The `-sn` flag (ping scan) discovers live hosts without port scanning. Use `nmap` carefully — unauthorized scans can trigger security alerts.

**tcpdump — Packet Capture**

Capture all traffic on eth0:

```bash
sudo tcpdump -i eth0
```

Filter by host:

```bash
sudo tcpdump -i eth0 host 192.168.1.10
```

Filter by port:

```bash
sudo tcpdump -i eth0 port 80
```

Save to a file for analysis in Wireshark:

```bash
sudo tcpdump -i eth0 -w /tmp/capture.pcap
```

**dig and nslookup — DNS Queries**

Query a specific DNS server:

```bash
dig @8.8.8.8 example.com
dig example.com MX
dig -x 8.8.8.8
```

- The last command performs a reverse DNS lookup

`nslookup` is the older equivalent still common in exam questions:

```bash
nslookup example.com
nslookup example.com 8.8.8.8
```

**curl and wget — HTTP Testing**

Test HTTP response headers:

```bash
curl -I https://example.com
```

Follow redirects and show response body:

```bash
curl -L https://example.com
```

Download a file:

```bash
wget https://example.com/file.tar.gz
```

---

### Troubleshooting Methodology

When a network problem is reported, work through this sequence:

1. Is the interface up? (`ip link show`)
2. Does the interface have an IP address? (`ip addr show`)
3. Is the default gateway reachable? (`ping <gateway IP>`)
4. Is external routing working? (`ping 8.8.8.8`)
5. Is DNS resolving? (`ping google.com`, `dig google.com`)
6. Is the specific service reachable? (`ss -tlnp`, `telnet host port`, `curl`)
7. Is a firewall blocking traffic? (`firewall-cmd --list-all`, `iptables -L`)

This systematic approach isolates the failure layer quickly and is exactly the kind of thinking Linux+ tests in its troubleshooting scenario questions.

---

### Summary — Module 11

Module 11 covered the complete Linux networking stack from an administrator's perspective:

- `ip` command for interface, routing, and ARP management
- `nmcli` for persistent NetworkManager connections
- `/etc/hosts` and `/etc/resolv.conf` for name resolution
- `firewalld` zones and `firewall-cmd` for modern firewall management
- `iptables` chains and rules for legacy/exam scenarios
- SSH client configuration with `~/.ssh/config`
- Troubleshooting tools: `ping`, `traceroute`, `ss`, `nmap`, `tcpdump`, `dig`

Networking knowledge is tested heavily on the Linux+ exam and used every single day in production. Practice each command in your lab environment before moving to Module 12.

Next module: System Services and Daemons — where we dive deep into systemd.
