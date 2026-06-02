# Reading Guide: Module 09 - Networking Configuration

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 2.0 - Security and Domain 1.0 - System Management

---

### Glossary

**Network Interface** - A hardware or virtual device that connects a system to a network. Named eth0 (legacy), ens33, enp2s0 (predictable naming), or lo (loopback).

**CIDR Notation** - A way of expressing an IP address and subnet mask together, such as 192.168.1.100/24 where /24 indicates the first 24 bits are the network portion.

**Default Gateway** - The router that a system sends traffic to when the destination IP is not on any locally connected network.

**NetworkManager** - A Linux service that manages network connections. Controlled with nmcli (CLI) or nmtui (text UI). Stores persistent configuration in connection profiles.

**nmcli** - The command-line interface for NetworkManager. Used for making persistent network configuration changes.

**Loopback Interface** - The lo interface, always 127.0.0.1/8. Used by applications to communicate with other processes on the same system without using the network.

**/etc/hosts** - A local file mapping hostnames to IP addresses. Checked before DNS when the nsswitch.conf hosts: line starts with files.

**/etc/resolv.conf** - Contains the IP addresses of DNS servers the system queries. Managed by NetworkManager or systemd-resolved on modern systems.

**/etc/nsswitch.conf** - The Name Service Switch configuration file. The hosts: line controls the order in which /etc/hosts (files) and DNS (dns) are consulted for hostname resolution.

**ss** - The socket statistics command. Modern replacement for netstat. Shows listening ports and active connections.

**dig** - A DNS query tool that returns detailed DNS responses including query time and the nameserver consulted.

---

### ip Command Reference

| Command | Purpose |
|---------|---------|
| ip addr show | Show all interfaces with IP addresses |
| ip addr show IFACE | Show a specific interface |
| ip addr add IP/PREFIX dev IFACE | Add an IP address (temporary) |
| ip addr del IP/PREFIX dev IFACE | Remove an IP address (temporary) |
| ip link show | Show link-layer status of all interfaces |
| ip link set IFACE up | Bring an interface up (temporary) |
| ip link set IFACE down | Bring an interface down (temporary) |
| ip route show | Show the routing table |
| ip route add NETWORK via GATEWAY | Add a static route (temporary) |
| ip route del NETWORK | Remove a static route (temporary) |
| ip route get IP | Show which route is used to reach a specific IP |

---

### nmcli Command Reference

| Command | Purpose |
|---------|---------|
| nmcli con show | List all connection profiles |
| nmcli dev status | Show device state and connected profile |
| nmcli con show NAME | Show all settings for a connection profile |
| nmcli con mod NAME ipv4.addresses IP/PREFIX | Set a static IP |
| nmcli con mod NAME ipv4.gateway IP | Set the default gateway |
| nmcli con mod NAME ipv4.dns IP | Set DNS server |
| nmcli con mod NAME ipv4.method manual | Set static (non-DHCP) mode |
| nmcli con mod NAME ipv4.method auto | Set DHCP mode |
| nmcli con up NAME | Apply connection profile changes |
| nmcli con reload | Reload all connection profiles |
| nmcli con mod NAME +ipv4.routes "NET via GW" | Add a persistent static route |

---

### DNS Resolution Chain

When an application resolves a hostname, the system follows the order in /etc/nsswitch.conf:

```
hosts: files dns
```

This means:
1. Check /etc/hosts for a matching entry
2. If not found, query the DNS servers in /etc/resolv.conf

If the line read hosts: dns files, DNS would be queried first and /etc/hosts would only be
consulted as a fallback.

Key DNS configuration files:

| File | Purpose |
|------|---------|
| /etc/hosts | Static hostname-to-IP mappings |
| /etc/resolv.conf | DNS server IP addresses |
| /etc/nsswitch.conf | Resolution order (files, dns) |
| /etc/hostname | Persistent system hostname |

---

### DNS Query Tools

| Command | Use Case |
|---------|---------|
| dig HOSTNAME | Full DNS query with detailed output |
| dig HOSTNAME TYPE | Query a specific record type (A, MX, NS, TXT) |
| dig @SERVER HOSTNAME | Query a specific DNS server directly |
| dig -x IP | Reverse DNS lookup (IP to hostname) |
| nslookup HOSTNAME | Legacy DNS query tool, simpler output |
| host HOSTNAME | Simple forward and reverse DNS lookups |
| resolvectl status | Show DNS configuration managed by systemd-resolved |

---

### Network Diagnostic Tools

| Command | Purpose |
|---------|---------|
| ping -c N IP | Send N ICMP packets; test basic connectivity |
| traceroute -n IP | Show path hops to destination (-n = no DNS) |
| ss -tuln | List listening TCP/UDP ports (numeric) |
| ss -tulnp | Same, with process name and PID (requires root) |
| ss -tan | All TCP connections in all states |
| tcpdump -i IFACE -n | Capture packets on interface (numeric IPs) |
| tcpdump -i IFACE port N | Capture packets for a specific port |
| tcpdump -i IFACE host IP | Capture packets for a specific host |
| tcpdump -i IFACE -w FILE | Save capture to file |

---

### ss Output Interpretation

The ss -tulnp command produces columns:

| Column | Meaning |
|--------|---------|
| Netid | tcp or udp |
| State | LISTEN, ESTAB, TIME-WAIT, etc. |
| Recv-Q | Bytes in receive queue |
| Send-Q | Bytes in send queue |
| Local Address:Port | Interface IP and port on this system |
| Peer Address:Port | Remote IP and port (0.0.0.0:* for listeners) |
| Process | Command name and PID (with -p) |

An entry with Local Address 0.0.0.0:22 means sshd is listening on all interfaces.
An entry with 127.0.0.1:PORT means the service is only accessible locally.

---

### Troubleshooting Methodology

Test layer by layer from the bottom up:

1. Physical layer: ip link show — is the interface state UP?
2. IP layer: ip addr show — is an IP address assigned?
3. Routing: ip route show — is there a default route?
4. Gateway: ping GATEWAY_IP — can you reach the local gateway?
5. Internet: ping 8.8.8.8 — can you reach a public IP?
6. DNS: dig google.com — does hostname resolution work?
7. Service: ss -tulnp | grep PORT — is the service listening?

If step 5 works but step 6 fails, the problem is DNS.
If step 4 fails, the problem is on the local network.
If step 3 shows no default route, run ip route add default via GATEWAY.

---

### Hostname Configuration

| Command | Purpose |
|---------|---------|
| hostname | Show current hostname |
| hostnamectl | Show detailed hostname information |
| sudo hostnamectl set-hostname NAME | Set hostname persistently |
| cat /etc/hostname | View the stored hostname file |

The hostname in /etc/hosts should match /etc/hostname. On Ubuntu, the convention is:

```
127.0.1.1   hostname.domain.example.com  hostname
```

This entry is separate from the 127.0.0.1 localhost entry.

---

### Exam Tips

1. ip replaces ifconfig. ip addr show, ip link show, ip route show are the exam-current commands.

2. nmcli con mod makes persistent changes; ip addr add makes temporary (lost at reboot) changes. This distinction is a common exam scenario.

3. /etc/nsswitch.conf hosts: line controls resolution order. files = /etc/hosts, dns = DNS servers. The default is files dns (local file first).

4. /etc/hosts is checked before DNS when nsswitch.conf has files before dns. A wrong entry in /etc/hosts can override DNS and cause connection failures.

5. ss -tuln shows listening ports. ss -tulnp adds process names. Both require the -n flag to suppress slow DNS lookups.

6. dig @IP HOSTNAME queries a specific DNS server, bypassing /etc/resolv.conf. Use this to isolate whether the problem is your DNS server or the authoritative server.

7. ping the gateway first, then 8.8.8.8, then a hostname. This three-step test isolates physical, routing, and DNS issues.

8. traceroute * * * at a hop means the router does not respond to TTL-exceeded messages. This does not necessarily mean the network path is broken.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

- Show interface IP addresses with ip addr show
- Show the routing table with ip route show
- Add a temporary IP address with ip addr add
- Add a persistent static IP with nmcli con mod and nmcli con up
- Explain the difference between ipv4.method manual and auto in nmcli
- Explain the purpose of /etc/hosts, /etc/resolv.conf, and /etc/nsswitch.conf
- Describe the DNS resolution chain and how to change it
- Query a specific DNS server with dig @IP hostname
- List listening ports with ss -tuln
- Identify which process is listening on a port with ss -tulnp
- Use ping to test connectivity at each layer (loopback, gateway, internet, DNS)
- Use traceroute to identify where a network path fails
- Set a hostname persistently with hostnamectl
