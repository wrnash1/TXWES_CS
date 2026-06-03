# Video Script: Module 11 — Networking in Linux (Part 1 of 2)

## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Introduction

Welcome back to CIS-3325. I'm Professor Nash, and this is Module 11, Part 1: Networking in Linux.

Networking is the backbone of every modern Linux deployment. Whether you're administering a single server or a fleet of cloud instances, understanding how Linux manages network interfaces, IP addressing, and name resolution is non-negotiable. The CompTIA Linux+ exam dedicates a significant portion of its objectives to networking, and today we're going to cover the foundational tools that every Linux administrator uses daily.

By the end of Part 1, you'll be comfortable with the `ip` command suite, NetworkManager's command-line interface `nmcli`, and the critical configuration files that control hostname resolution. In Part 2, we'll move into firewall management, SSH client configuration, and network troubleshooting tools.

Let's get started.

---

### Section 1: The ip Command Suite

The `ip` command replaced the older `ifconfig`, `route`, and `arp` commands. If you're still using `ifconfig` in production, it's time to migrate. The `ip` command is part of the `iproute2` package and is present on virtually every modern Linux distribution.

**Viewing Network Interfaces**

To list all network interfaces and their current state, run:

```bash
ip link show
```

This shows each interface, its MAC address, and whether it is UP or DOWN. You'll typically see `lo` (loopback), `eth0` or `ens3` (Ethernet), and possibly `wlan0` (wireless).

To see IP address assignments:

```bash
ip addr show
```

Or the shorthand:

```bash
ip a
```

Pay attention to the `inet` line — that's your IPv4 address and prefix length. The `inet6` line shows your IPv6 address.

**Assigning IP Addresses**

To assign a temporary IP address to an interface:

```bash
sudo ip addr add 192.168.1.50/24 dev eth0
```

Note the word "temporary" — this does not survive a reboot. For persistent configuration, we use NetworkManager, which we'll cover shortly.

To bring an interface up or down:

```bash
sudo ip link set eth0 up
sudo ip link set eth0 down
```

**Routing Tables**

The routing table tells the kernel where to send packets. To view it:

```bash
ip route show
```

Or:

```bash
ip r
```

You'll see entries like:

```
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.50
```

The `default` entry is your default gateway. To add a static route:

```bash
sudo ip route add 10.0.0.0/8 via 192.168.1.254 dev eth0
```

To delete a route:

```bash
sudo ip route del 10.0.0.0/8
```

**ARP Cache**

To view the ARP cache — the table mapping IP addresses to MAC addresses on your local network:

```bash
ip neigh show
```

This is useful when troubleshooting Layer 2 connectivity issues.

---

### Section 2: NetworkManager and nmcli

Most modern Linux distributions use NetworkManager to manage network connections persistently. The command-line interface to NetworkManager is `nmcli`. This is the tool you'll use to create, modify, and activate connections that survive reboots.

**Checking Status**

```bash
nmcli general status
```

This shows whether NetworkManager is running and connected.

To list all connections:

```bash
nmcli connection show
```

To list only active connections:

```bash
nmcli connection show --active
```

**Viewing Device Information**

```bash
nmcli device status
```

This shows each network device, its type, state, and which connection profile is associated with it.

For detailed information about a specific device:

```bash
nmcli device show eth0
```

**Creating a Static IP Connection**

Here's a real-world scenario: you need to configure a server with a static IP. Here's the full command sequence:

```bash
sudo nmcli connection add \
  type ethernet \
  con-name "static-eth0" \
  ifname eth0 \
  ipv4.addresses 192.168.1.100/24 \
  ipv4.gateway 192.168.1.1 \
  ipv4.dns "8.8.8.8 8.8.4.4" \
  ipv4.method manual
```

Then activate it:

```bash
sudo nmcli connection up static-eth0
```

**Modifying an Existing Connection**

To change the DNS server on an existing connection:

```bash
sudo nmcli connection modify static-eth0 ipv4.dns "1.1.1.1 1.0.0.1"
sudo nmcli connection reload
```

**DHCP Connection**

For a DHCP-configured interface:

```bash
sudo nmcli connection add \
  type ethernet \
  con-name "dhcp-eth0" \
  ifname eth0 \
  ipv4.method auto
```

**Wi-Fi Connection**

On a workstation:

```bash
sudo nmcli device wifi connect "MyNetwork" password "MyPassword"
```

---

### Section 3: /etc/hosts and /etc/resolv.conf

Before DNS queries leave your system, Linux checks two local files. Understanding these files is critical for troubleshooting resolution failures.

**The /etc/hosts File**

This file maps hostnames to IP addresses locally, bypassing DNS entirely for listed entries.

```
127.0.0.1   localhost
127.0.1.1   myhostname
192.168.1.10  webserver01 web01
192.168.1.20  dbserver01
```

The format is: `IP_ADDRESS  FQDN  aliases`

Common use cases include:

- Blocking domains by pointing them to 127.0.0.1 or 0.0.0.0
- Mapping internal hostnames that aren't in DNS
- Testing application behavior before DNS changes propagate

**The NSSwitch Configuration**

The file `/etc/nsswitch.conf` controls the order of name resolution. Look for the `hosts:` line:

```
hosts: files dns myhostname
```

This means: check `/etc/hosts` first (`files`), then DNS, then the local hostname. This is why `/etc/hosts` entries override DNS.

**The /etc/resolv.conf File**

This file configures DNS resolution:

```
nameserver 8.8.8.8
nameserver 8.8.4.4
search example.com internal.example.com
domain example.com
```

- `nameserver` — IP of your DNS resolver (up to three entries)
- `search` — domain suffixes appended to unqualified hostnames
- `domain` — the local domain name

**Important Warning**: On systems using NetworkManager or systemd-resolved, `/etc/resolv.conf` may be a symlink or managed file. Editing it directly will cause your changes to be overwritten. Use `nmcli` or `/etc/systemd/resolved.conf` instead.

To check if it's a symlink:

```bash
ls -la /etc/resolv.conf
```

If it points to `/run/systemd/resolve/stub-resolv.conf`, you're using systemd-resolved.

---

### Section 4: Hostname Management

Your server's hostname is referenced in logs, SSL certificates, and Kerberos tickets. Managing it correctly matters.

**Viewing the Hostname**

```bash
hostname
hostnamectl status
```

`hostnamectl` shows three hostname types:

- **Static**: persisted across reboots, stored in `/etc/hostname`
- **Transient**: set at runtime by DHCP or another service
- **Pretty**: a human-readable label with spaces and special characters allowed

**Setting the Hostname**

```bash
sudo hostnamectl set-hostname webserver01.example.com
```

This updates `/etc/hostname` and takes effect immediately.

---

### Summary — Part 1

Let's review what we covered:

- The `ip` command suite for viewing and modifying interfaces, routes, and the ARP cache
- `nmcli` for creating persistent NetworkManager connection profiles
- `/etc/hosts` for local hostname resolution and `/etc/resolv.conf` for DNS configuration
- Hostname management with `hostnamectl`

In Part 2, we'll cover firewalld and iptables basics, SSH client configuration, and the essential troubleshooting tools: `ping`, `traceroute`, `ss`, `nmap`, and `tcpdump`.

See you in Part 2.
