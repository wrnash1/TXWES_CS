# Reading Guide: Module 11 — Networking in Linux

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3325 &BULL; OPERATING SYSTEM ADMINISTRATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3325 OS Administration Linux

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Linux+ (XK0-005)

---

### Overview

This reading guide accompanies the Module 11 video lectures. Use it to reinforce key concepts, locate additional reference material, and prepare for the module quiz and lab. Estimated reading and review time: 90 minutes.

---

### Learning Objectives

After completing this module, you will be able to:

- Use the `ip` command to inspect and configure network interfaces, routes, and the ARP cache
- Create and manage persistent network connections using `nmcli` and NetworkManager
- Interpret and modify `/etc/hosts`, `/etc/resolv.conf`, and `/etc/nsswitch.conf`
- Configure and manage `firewalld` using zones and `firewall-cmd`
- Understand `iptables` chain structure and write basic filtering rules
- Configure the SSH client using `~/.ssh/config` for efficiency and security
- Diagnose network connectivity issues using `ping`, `ss`, `traceroute`, `dig`, `tcpdump`, and `nmap`

---

### Key Terms and Concepts

**Interface**
A network interface is the software representation of a network hardware device (or virtual device). Each interface has a name (e.g., `eth0`, `ens3`, `lo`, `wlan0`), a MAC address, and optionally one or more IP addresses.

**CIDR Notation**
Classless Inter-Domain Routing notation expresses an IP address and its network prefix in one string. Example: `192.168.1.50/24` means the host address is `192.168.1.50` and the subnet mask is `255.255.255.0` (24 bits).

**Default Gateway**
The router that handles traffic destined for networks not explicitly in the routing table. Shown as `default` in `ip route show` output.

**NetworkManager**
A daemon that manages network connections on most modern Linux distributions. It stores connection profiles in `/etc/NetworkManager/system-connections/` and exposes its functionality through `nmcli` and `nmtui`.

**Zone (firewalld)**
A named trust level applied to a network interface or source address. Zones contain collections of allowed services, ports, and rich rules.

**Chain (iptables)**
A sequence of rules that packets traverse. The three built-in chains in the `filter` table are INPUT, OUTPUT, and FORWARD.

**Netfilter**
The kernel subsystem that provides packet filtering, NAT, and connection tracking. Both `iptables` and `nftables` are userspace interfaces to Netfilter.

**Socket**
An endpoint for network communication. The `ss` command displays socket statistics, replacing the older `netstat`.

---

### Section 1: The ip Command — Detailed Reference

The `iproute2` package provides the `ip` command. Its general syntax is:

```
ip [OPTIONS] OBJECT {COMMAND | help}
```

Common objects:

| Object | Description |
|--------|-------------|
| `link` | Network interfaces |
| `addr` | IP addresses |
| `route` | Routing table entries |
| `neigh` | ARP/neighbor cache |
| `rule` | Policy routing rules |

**Viewing All Addresses**

```bash
ip addr show
ip -4 addr show   # IPv4 only
ip -6 addr show   # IPv6 only
```

**Interface Flags**

When you run `ip link show`, look for flags in angle brackets:

- `UP` — interface is administratively up
- `LOWER_UP` — physical link is up (cable connected)
- `BROADCAST` — supports broadcast
- `MULTICAST` — supports multicast
- `LOOPBACK` — loopback interface

**Flushing Addresses**

Remove all IP addresses from an interface:

```bash
sudo ip addr flush dev eth0
```

**Policy Routing**

Linux supports multiple routing tables. View rules with:

```bash
ip rule show
```

This is an advanced topic covered later, but knowing the command exists is useful for exam scenarios.

---

### Section 2: NetworkManager Deep Dive

**Connection Profiles**

NetworkManager stores connection profiles as INI-style files in:

```
/etc/NetworkManager/system-connections/
```

Each file contains sections like `[connection]`, `[ipv4]`, `[ipv6]`, and `[ethernet]`. You can edit these files directly, but using `nmcli` is preferred to avoid syntax errors.

**nmcli Output Fields**

When you run `nmcli connection show`, the columns mean:

- `NAME` — the connection profile name you assigned
- `UUID` — unique identifier for the connection
- `TYPE` — ethernet, wifi, vpn, etc.
- `DEVICE` — which interface it's bound to

**nmtui**

For administrators who prefer a text-based menu interface, `nmtui` provides a curses UI for NetworkManager configuration. It covers most common tasks without requiring memorization of `nmcli` syntax.

**Restarting NetworkManager**

```bash
sudo systemctl restart NetworkManager
```

Restarting NetworkManager briefly interrupts all network connections. Be careful on remote sessions.

---

### Section 3: DNS Resolution Architecture

Understanding how Linux resolves names requires knowing the full resolution stack.

**Resolution Order**

1. Local cache (if systemd-resolved is running)
2. `/etc/hosts` (controlled by `files` in `nsswitch.conf`)
3. DNS servers in `/etc/resolv.conf` or systemd-resolved configuration
4. mDNS/LLMNR if configured

**systemd-resolved**

On Ubuntu and modern RHEL systems, `systemd-resolved` manages DNS caching and stub resolution. The stub resolver listens on `127.0.0.53`.

Check its status:

```bash
resolvectl status
```

View DNS cache statistics:

```bash
resolvectl statistics
```

Flush the DNS cache:

```bash
sudo resolvectl flush-caches
```

**The /etc/resolv.conf Symlink**

When systemd-resolved is active, `/etc/resolv.conf` is typically a symlink to one of:

- `/run/systemd/resolve/stub-resolv.conf` — points to `127.0.0.53` (stub mode)
- `/run/systemd/resolve/resolv.conf` — contains actual upstream DNS servers

Do not break this symlink by replacing the file with a static version unless you disable systemd-resolved.

---

### Section 4: firewalld Architecture

**Zones and Interfaces**

Each network interface belongs to exactly one zone. When firewalld receives a packet, it determines which zone applies to the incoming interface and processes the packet against that zone's rules.

**Runtime vs. Permanent Configuration**

firewalld maintains two sets of rules:

- **Runtime** — active immediately, lost on reload or reboot
- **Permanent** — written to `/etc/firewalld/`, applied on reload or boot

Always use `--permanent` for production changes, then reload:

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

**Custom Services**

You can define custom services in `/etc/firewalld/services/`. Copy an existing service XML as a template:

```bash
sudo cp /usr/lib/firewalld/services/ssh.xml \
  /etc/firewalld/services/myapp.xml
sudo nano /etc/firewalld/services/myapp.xml
sudo firewall-cmd --reload
```

**Direct Rules**

For cases where zones and rich rules are insufficient, firewalld supports direct iptables rules via `--direct`. Use sparingly as they bypass the zone model.

---

### Section 5: iptables — Tables and Targets

**Tables**

iptables organizes rules into tables:

| Table | Purpose |
|-------|---------|
| `filter` | Default; packet filtering (INPUT, OUTPUT, FORWARD) |
| `nat` | Network Address Translation |
| `mangle` | Packet header modification |
| `raw` | Connection tracking bypass |

**Targets**

When a packet matches a rule, the target specifies the action:

| Target | Action |
|--------|--------|
| `ACCEPT` | Allow the packet |
| `DROP` | Silently discard |
| `REJECT` | Discard and send error response |
| `LOG` | Log to kernel log, continue processing |
| `DNAT` | Destination NAT (nat table) |
| `SNAT` | Source NAT (nat table) |
| `MASQUERADE` | Dynamic SNAT for dynamic IPs |

**Rule Order Matters**

iptables processes rules in order within a chain. The first matching rule's target is applied. Place more specific rules before general ones. A common mistake is placing a DROP-all rule before more permissive rules.

**Flushing Rules**

```bash
sudo iptables -F        # Flush all rules in filter table
sudo iptables -F INPUT  # Flush only INPUT chain
```

Be careful — flushing on a remote server can lock you out if the default policy is DROP.

---

### Section 6: SSH Client Security

**Key-Based Authentication**

The `~/.ssh/config` file can enforce key-based authentication by specifying `IdentitiesOnly yes`:

```
Host prodserver
    HostName 10.0.0.5
    User admin
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
```

This prevents SSH from trying other keys or falling back to password authentication.

**Host Key Verification**

Known host keys are stored in `~/.ssh/known_hosts`. On first connection, SSH prompts you to verify the host's fingerprint. After acceptance, it's stored and verified on future connections.

To view a host's key fingerprint:

```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

**SSH Agent**

For working with password-protected private keys:

```bash
eval $(ssh-agent)
ssh-add ~/.ssh/id_ed25519
```

The agent caches the decrypted key in memory for the session duration.

---

### Section 7: Troubleshooting Reference

**Layered Troubleshooting Map**

| Layer | Check | Tool |
|-------|-------|------|
| Physical/Link | Interface UP, cable | `ip link show` |
| Network | IP address, gateway | `ip addr`, `ip route` |
| Routing | Gateway reachable | `ping <gateway>` |
| Internet | External reachable | `ping 8.8.8.8` |
| DNS | Name resolution | `dig`, `nslookup` |
| Transport | Port open | `ss`, `nmap`, `telnet` |
| Application | Service responding | `curl`, `wget` |

**Common ss Flags**

| Flag | Meaning |
|------|---------|
| `-t` | TCP sockets |
| `-u` | UDP sockets |
| `-l` | Listening sockets |
| `-n` | No name resolution |
| `-p` | Show process |
| `-4` | IPv4 only |
| `-6` | IPv6 only |

**tcpdump Filter Syntax**

Basic filter primitives:

- `host 192.168.1.10` — match source or destination IP
- `port 443` — match source or destination port
- `tcp` or `udp` — match protocol
- `net 192.168.1.0/24` — match network
- `and`, `or`, `not` — combine filters

Example — capture only HTTPS traffic to a specific host:

```bash
sudo tcpdump -i eth0 'host 10.0.0.5 and port 443'
```

---

### Practice Review Questions

Answer these before taking the quiz:

1. What is the difference between `ip addr add` and creating a NetworkManager connection with `nmcli`?

2. What is the effect of adding a firewalld rule without `--permanent`?

3. In the `iptables` filter table, packets going to a remote host pass through which chain?

4. What file controls the order of hostname resolution methods?

5. How does `ss -tlnp` differ from `ss -tnp`?

6. What is the purpose of `ServerAliveInterval` in `~/.ssh/config`?

7. A ping to `8.8.8.8` succeeds but `ping google.com` fails. What is the most likely cause?

8. What is the difference between firewalld's runtime and permanent configuration?

---

### Additional Resources

- Red Hat Networking Guide: [access.redhat.com/documentation](https://access.redhat.com/documentation)
- `man ip` — comprehensive manual for the `ip` command
- `man firewall-cmd` — firewalld command reference
- `man 5 ssh_config` — SSH client configuration file reference
- `man tcpdump` — packet capture filter syntax
- CompTIA Linux+ Study Guide, Chapter on Networking (XK0-005 Objective 1.4, 2.3, 4.1)

---

### Key Takeaways

- The `ip` command suite is the modern replacement for `ifconfig`, `route`, and `arp`. Use it.
- NetworkManager with `nmcli` provides persistent network configuration that survives reboots.
- `/etc/hosts` is checked before DNS — it is your first line of local resolution override.
- firewalld zones provide a clean abstraction over iptables; always reload after permanent changes.
- SSH client configuration in `~/.ssh/config` improves both productivity and security posture.
- Systematic layered troubleshooting (physical → application) is the most efficient diagnostic approach.

---

## 9. Supplemental Resources

**1. [Red Hat — Getting Started with NetworkManager and nmcli](https://www.redhat.com/sysadmin/nmcli-linux-networking)**
A practical Red Hat sysadmin article walking through the most common NetworkManager and nmcli workflows: creating and modifying connection profiles, configuring static IPs, adding DNS servers, and managing bonds and VLANs. Directly supports the Module 11 lab tasks and provides the persistent-configuration context that `ip addr add` (temporary) commands cannot.

**2. [Arch Linux Wiki — firewalld](https://wiki.archlinux.org/title/firewalld)**
A comprehensive reference for firewalld zones, services, ports, and rich rules. Covers runtime vs. permanent rule management, the zone-to-interface assignment model, masquerading for NAT, and the `direct` interface for raw iptables rules. The Arch Wiki is distribution-agnostic and explains concepts more deeply than vendor-specific docs — useful for understanding why firewalld is designed the way it is.

**3. [SSH Config File for Client — ssh.com Documentation](https://www.ssh.com/academy/ssh/config)**
A detailed reference for the `~/.ssh/config` and `/etc/ssh/ssh_config` client configuration files. Covers all commonly used directives: `Host`, `HostName`, `User`, `IdentityFile`, `IdentitiesOnly`, `ProxyJump`, `ForwardAgent`, `StrictHostKeyChecking`, and `ServerAliveInterval`. Understanding the SSH config file is essential for both the lab exercises and real-world sysadmin work involving multi-server environments.
