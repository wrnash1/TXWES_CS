# Video Script: Module 09 - Networking Configuration (Part 1 of 2)

## CIS-3325 OS Administration | Texas Wesleyan University

**Recorded by:** Professor Nash | Texas Wesleyan University
**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Estimated Duration:** 13 minutes
**Part:** 1 of 2 - Conceptual Foundation

---

### Opening

Welcome to Module 09. Networking is how your server communicates with everything else —
other servers, users, the internet, and your management infrastructure. Every service you
have configured so far depends on networking to be useful. In this module we cover the ip
command suite, NetworkManager, /etc/hosts, DNS resolution, and network troubleshooting tools.
By the end you will be able to configure an interface, verify connectivity, diagnose failures,
and understand the resolution chain from hostname to IP address.

---

### Section 1: Network Interface Fundamentals

[SHOW TERMINAL]

```bash
ip addr show
```

This is the primary command for viewing network interface information. ip replaced ifconfig,
which is deprecated. The output shows:

- Interface name (lo = loopback, eth0 or ens33 = first Ethernet)
- link/ether: MAC address
- inet: IPv4 address with CIDR prefix length (e.g., 192.168.1.100/24)
- inet6: IPv6 address
- state UP or DOWN

```bash
ip addr show ens33
```

Show information for a specific interface.

```bash
ip link show
```

Shows link-layer (Layer 2) status for all interfaces. Useful for checking whether an
interface is UP or DOWN at the physical layer before looking at IP addressing.

Interface naming conventions:

- eth0: Traditional naming. Still seen in older systems and some VMs.
- ens33: Predictable network interface naming. ens = Ethernet slot. The number derives
  from PCI slot or connection order.
- enp2s0: en=Ethernet, p=PCI bus 2, s=slot 0.
- lo: Loopback interface. Always 127.0.0.1/8. Used for local process communication.

---

### Section 2: Temporary vs Persistent Configuration

[SHOW TERMINAL]

```bash
sudo ip addr add 192.168.1.200/24 dev ens33
```

This adds an IP address temporarily. It is gone after a reboot or when NetworkManager
resets the interface. Use this only for testing.

```bash
sudo ip addr del 192.168.1.200/24 dev ens33
```

Remove a temporary address.

```bash
sudo ip link set ens33 up
sudo ip link set ens33 down
```

Bring an interface up or down. Again, temporary — use NetworkManager for persistence.

For persistent configuration, use nmcli (NetworkManager CLI).

```bash
nmcli con show
```

List all NetworkManager connection profiles. Each connection has a name, UUID, type, and
the device it is bound to.

```bash
nmcli dev status
```

Shows the state of each network device.

---

### Section 3: Static IP with nmcli

[SHOW TERMINAL]

```bash
nmcli con mod "ens33" \
    ipv4.addresses 192.168.1.100/24 \
    ipv4.gateway 192.168.1.1 \
    ipv4.dns 8.8.8.8 \
    ipv4.method manual
```

This modifies the existing connection profile. The method manual means static (not DHCP).

```bash
nmcli con up "ens33"
```

Apply the changes by bringing the connection up (or use nmcli con reload).

```bash
ip addr show ens33
```

Verify the new address.

```bash
nmcli con show "ens33"
```

Shows all settings for the connection profile, including the saved IP configuration.

To switch back to DHCP:

```bash
nmcli con mod "ens33" ipv4.method auto ipv4.addresses "" ipv4.gateway "" ipv4.dns ""
nmcli con up "ens33"
```

---

### Section 4: Routing

[SHOW TERMINAL]

```bash
ip route show
```

Shows the kernel routing table. The default route (0.0.0.0/0) points to the default gateway.

```bash
ip route add 10.10.0.0/16 via 192.168.1.254
```

Add a static route. Temporary — use nmcli for persistence.

```bash
nmcli con mod "ens33" +ipv4.routes "10.10.0.0/16 192.168.1.254"
nmcli con up "ens33"
```

Add a persistent static route through NetworkManager.

```bash
ip route get 8.8.8.8
```

Shows which route the kernel would use to reach a specific address. Useful for verifying
that routing is configured correctly for a specific destination.

---

### Section 5: DNS Resolution

[SHOW TERMINAL]

DNS resolution follows a chain determined by /etc/nsswitch.conf.

```bash
cat /etc/nsswitch.conf | grep hosts
```

The hosts: line typically shows: files dns. This means:
1. Check /etc/hosts first
2. Then query DNS servers

```bash
cat /etc/hosts
```

Static name-to-IP mappings. Checked before DNS. Useful for:
- Mapping a loopback alias to the local hostname
- Overriding DNS for testing
- Adding entries for hosts on local networks with no DNS

Format:
```
IP_ADDRESS    HOSTNAME    [ALIASES...]
127.0.0.1     localhost
192.168.1.10  webserver01  webserver01.example.com
```

```bash
cat /etc/resolv.conf
```

Lists the nameservers the system queries. On systems managed by systemd-resolved,
this file is a symlink to a managed file. The nameserver lines point to DNS servers.

```bash
resolvectl status
```

On modern Ubuntu systems, resolvectl shows DNS configuration managed by
systemd-resolved, including per-interface DNS servers.

---

### Section 6: DNS Query Tools

[SHOW TERMINAL]

```bash
nslookup google.com
```

Legacy DNS query tool. Shows the server queried and the answer. Still useful for
quick checks.

```bash
dig google.com
```

More detailed DNS query tool. Shows the full DNS response including query time, server
used, and all answer sections.

```bash
dig google.com MX
```

Query for MX (mail exchanger) records.

```bash
dig @8.8.8.8 google.com
```

Query a specific DNS server (bypassing /etc/resolv.conf). Useful for testing whether
the problem is your DNS server or the authoritative server.

```bash
dig -x 8.8.8.8
```

Reverse DNS lookup: resolve an IP address to a hostname.

```bash
host google.com
```

Simpler output than dig. Returns IP addresses for a hostname.

---

### Certification Connection

Networking maps to Linux+ Domain 2.0 (Security) and Domain 1.0 (System Management).
Key exam objectives:

Know ip addr show, ip link show, ip route show. These replace ifconfig, route, and netstat.

Know nmcli con mod for persistent changes versus ip addr add for temporary changes.

Know the /etc/hosts and /etc/nsswitch.conf roles in name resolution.

Know dig, nslookup, and host for DNS queries.

Know ss -tuln for listing listening ports (replaces netstat -tuln).

---

### Transition to Part 2

In Part 2 we cover network diagnostic tools (ping, traceroute, ss, tcpdump), common
troubleshooting scenarios, hostname configuration, and network bonding concepts.

---

### Additional Resources

- professormesser.com - CompTIA Linux+ study materials and practice exams
- comptia.org/certifications/linux - Official Linux+ exam objectives (XK0-005)
