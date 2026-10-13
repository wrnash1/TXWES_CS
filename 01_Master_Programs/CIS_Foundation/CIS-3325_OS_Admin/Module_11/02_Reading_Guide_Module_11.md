# Reading Guide: Module 11 - Firewall Management

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


## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Exam Domain:** Domain 2.0 - Security

---

### Glossary

**netfilter** - The Linux kernel framework that implements packet filtering. All Linux firewall tools (iptables, firewalld, ufw, nftables) configure netfilter rules.

**iptables** - A command-line tool for configuring netfilter rules directly. Rules exist in tables (filter, nat, mangle). The filter table has INPUT, OUTPUT, and FORWARD chains.

**Chain** - A list of rules in iptables. Built-in chains: INPUT (inbound), OUTPUT (outbound), FORWARD (routing between interfaces).

**Default Policy** - The action taken when a packet matches no rule in a chain. ACCEPT or DROP.

**ufw (Uncomplicated Firewall)** - Ubuntu's simplified firewall management tool. Persistent by default. Frontend for iptables.

**firewalld** - A zone-based firewall management daemon used on RHEL, CentOS, Fedora, and Rocky Linux. Separates runtime (active) and permanent (saved) configurations.

**Zone** - A named firewall policy in firewalld that is assigned to a network interface or source address range. Each zone has its own allowed services and ports.

**Runtime Configuration** - firewalld rules that are currently active but not saved. Lost when firewalld is reloaded or the system reboots.

**Permanent Configuration** - firewalld rules written to configuration files. Not active until firewalld is reloaded.

**Rich Rule** - An advanced firewalld rule type that allows complex matching conditions including source address, destination, rate limiting, and logging.

---

### iptables Filter Table Chain Model

```
INBOUND PACKETS  →  INPUT chain  →  local process
                                      ↓
LOCAL PROCESS    →  OUTPUT chain →  network

ROUTED PACKETS   →  FORWARD chain → network
```

Rule evaluation: top to bottom. First match wins. If no match, the default policy applies.

Targets:

| Target | Effect |
|--------|--------|
| ACCEPT | Allow the packet |
| DROP | Silently discard (no response to sender) |
| REJECT | Discard and send ICMP error to sender |
| LOG | Log packet details; continue to next rule |

---

### iptables Command Reference

| Command | Purpose |
|---------|---------|
| iptables -L -n -v | List all rules, numeric IPs, with counters |
| iptables -L INPUT -n -v --line-numbers | List INPUT chain with line numbers |
| iptables -A CHAIN RULE | Append a rule to a chain |
| iptables -I CHAIN N RULE | Insert a rule at position N |
| iptables -D CHAIN N | Delete rule at line number N |
| iptables -D CHAIN RULE | Delete a rule by specification |
| iptables -F CHAIN | Flush (delete all) rules in a chain |
| iptables -F | Flush all rules in all chains |
| iptables -P CHAIN POLICY | Set the default policy for a chain |
| iptables -S CHAIN | Print rules in save/restore format |

Common rule components:

| Component | Meaning |
|-----------|---------|
| -p tcp | Match TCP protocol |
| -p udp | Match UDP protocol |
| --dport N | Match destination port N |
| --sport N | Match source port N |
| -s IP/CIDR | Match source address |
| -d IP/CIDR | Match destination address |
| -i IFACE | Match input interface |
| -o IFACE | Match output interface |
| -m state --state ESTABLISHED,RELATED | Match established connections |

---

### ufw Command Reference

| Command | Purpose |
|---------|---------|
| ufw status | Show status and all rules |
| ufw status numbered | Show rules with line numbers |
| ufw enable | Enable ufw (takes effect immediately) |
| ufw disable | Disable ufw |
| ufw allow ssh | Allow by service name |
| ufw allow 80/tcp | Allow specific port/protocol |
| ufw allow from IP to any port N | Allow from specific source to port |
| ufw deny PORT/PROTO | Explicitly deny a port |
| ufw delete allow PORT/PROTO | Remove a rule |
| ufw delete N | Remove rule by number |
| ufw logging on | Enable logging |
| ufw reset | Remove all rules and disable ufw |

ufw rules are persistent automatically. No reload command is needed.

---

### firewalld Command Reference

| Command | Purpose |
|---------|---------|
| firewall-cmd --get-zones | List all available zones |
| firewall-cmd --get-default-zone | Show the default zone |
| firewall-cmd --get-active-zones | Show active zones and their interfaces |
| firewall-cmd --list-all | Show rules in the default zone |
| firewall-cmd --list-all-zones | Show all zones and their rules |
| firewall-cmd --list-services | List allowed services in active zone |
| firewall-cmd --list-ports | List explicitly opened ports |
| firewall-cmd --add-service=NAME | Allow service (runtime) |
| firewall-cmd --add-service=NAME --permanent | Allow service (permanent) |
| firewall-cmd --remove-service=NAME --permanent | Remove service (permanent) |
| firewall-cmd --add-port=N/tcp --permanent | Allow port (permanent) |
| firewall-cmd --remove-port=N/tcp --permanent | Remove port (permanent) |
| firewall-cmd --reload | Load permanent config into runtime |
| firewall-cmd --runtime-to-permanent | Copy runtime rules to permanent |
| firewall-cmd --query-service=NAME | Returns yes/no if service is active |

---

### firewalld Runtime vs Permanent

| Action | Command | Active now? | Survives reload? |
|--------|---------|------------|-----------------|
| Add runtime rule | --add-service=X | Yes | No |
| Add permanent rule | --add-service=X --permanent | No | Yes |
| Add both | Both commands above | Yes | Yes |
| Add permanent + reload | --permanent then --reload | Yes | Yes |

The most common mistake: adding a rule with --permanent but forgetting --reload, leaving
the rule in config files but not active in the running firewall.

---

### firewalld Zones Reference

| Zone | Default Allowed Services | Use Case |
|------|--------------------------|---------|
| drop | None (all inbound dropped silently) | Maximum restriction |
| block | None (inbound rejected with ICMP) | Block with notification |
| public | ssh, dhcpv6-client | Internet-facing servers |
| home | ssh, mdns, samba-client, dhcpv6-client | Home networks |
| trusted | All | Fully trusted networks |
| dmz | ssh only | DMZ servers |

---

### iptables Persistence (Ubuntu)

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

Rules saved to:
- /etc/iptables/rules.v4 (IPv4)
- /etc/iptables/rules.v6 (IPv6)

Manual save: sudo iptables-save > /etc/iptables/rules.v4
Manual restore: sudo iptables-restore < /etc/iptables/rules.v4

---

### Exam Tips

1. iptables rules are not persistent by default. ufw rules are persistent. firewalld permanent rules are persistent.

2. firewalld --permanent writes to config but does NOT activate. --reload activates the permanent config. Both steps are required for a rule to be active AND persistent.

3. iptables -F flushes all rules. If the default policy is DROP, flushing locks you out. Always change the policy to ACCEPT before flushing, or ensure you have console access.

4. ufw enable on a remote server without first allowing SSH will lock you out. Always allow SSH before enabling ufw.

5. iptables -I inserts at the top; -A appends to the bottom. Loopback rules and ESTABLISHED,RELATED rules should be inserted at the top to evaluate first.

6. DROP silently discards packets. REJECT sends an ICMP error. Drop is less informative to attackers; Reject is more useful for debugging.

7. firewall-cmd --list-all shows the current zone's active runtime rules. Add --permanent to list the saved permanent rules.

8. Zone drop versus block: drop silently discards, block sends an ICMP rejection message. Use drop for maximum stealth.

---

### Study Checklist

Before the quiz and lab, confirm you can do all of the following without looking them up:

- Describe the iptables filter table chains and default policies
- Add, insert, and delete iptables rules
- Set the default policy for an iptables chain
- Save and restore iptables rules on Ubuntu
- Enable ufw and add basic allow/deny rules
- Remove ufw rules by rule specification and by number
- List all ufw rules with and without line numbers
- Explain the difference between firewalld runtime and permanent configuration
- Add a permanent firewalld service rule and reload it
- List active services and ports in the default firewalld zone
- Move a network interface to a specific firewalld zone
- Add a source address to a trusted zone in firewalld
- Explain the firewalld zones and their default trust levels

---

## 9. Supplemental Resources

**1. iptables(8) and ip6tables(8) Man Pages — man7.org**
URL: https://man7.org/linux/man-pages/man8/iptables.8.html
Coverage: The authoritative iptables reference covering all tables (filter, nat, mangle,
raw), built-in chains (INPUT, OUTPUT, FORWARD, PREROUTING, POSTROUTING), match extensions
(-m conntrack, -m state, -m limit, -m multiport), and targets (ACCEPT, DROP, REJECT, LOG,
RETURN). The iptables-extensions(8) man page documents all match and target modules.
Essential for understanding the rules used in Part 4 of the lab.

**2. ufw — Uncomplicated Firewall Documentation (Ubuntu)**
URL: https://help.ubuntu.com/community/UFW
Coverage: Ubuntu's official ufw guide covering basic allow/deny rules, application profiles,
logging levels, rule deletion by number and specification, IPv6 handling, and integration
with Docker. Includes a troubleshooting section for common issues including rules that appear
correct but do not take effect. Directly maps to all ufw commands in this module.

**3. firewalld Documentation — firewalld.org**
URL: https://firewalld.org/documentation/
Coverage: The official firewalld documentation covering zones, services, ports, rich rules,
direct rules, runtime versus permanent configuration, and the --reload workflow. The zone
concept documentation explains source-based versus interface-based zone assignment priority.
The firewall-cmd man page section covers all subcommands used in this module.

**4. nftables — The Successor to iptables (Red Hat)**
URL: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_firewalls_and_packet_filters/getting-started-with-nftables_firewall-packet-filters
Coverage: On RHEL 9 and newer Ubuntu releases, nftables is the underlying kernel framework
replacing iptables. This guide introduces nft syntax, tables, chains, and rules. Understanding
nftables is increasingly important as iptables is deprecated. The iptables-nft compatibility
layer (iptables commands that internally use nftables) is also explained.

**5. Arch Wiki — iptables and ufw**
URL: https://wiki.archlinux.org/title/Iptables
Coverage: The Arch Wiki iptables article provides a practical introduction to the filter
table, chain traversal, stateful matching, logging, and saving rules. The companion ufw
article covers the complete ufw workflow including application profiles and integration
with other services. Both articles include worked examples and common configuration patterns
not found in the official man pages.
