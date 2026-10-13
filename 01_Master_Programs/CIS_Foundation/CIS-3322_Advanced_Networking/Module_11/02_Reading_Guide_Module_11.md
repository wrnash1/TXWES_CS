# Reading Guide: Module 11 — DHCP and DNS Configuration

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3322 &BULL; ADVANCED NETWORKING & INFRASTRUCTURE</text>
    
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


## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

---

## Overview

DHCP and DNS are IP Services topics tested on the CCNA 200-301 exam. The exam focuses on Cisco IOS DHCP server configuration, DHCP relay (ip helper-address), DHCP snooping, and the DNS resolution process. This guide provides configuration tables, command references, troubleshooting flowcharts, and CCNA exam tips covering all testable concepts.

---

## 1. DHCP Core Concepts

### The DORA Exchange

DHCP uses four messages to assign an IP address. The entire process takes milliseconds on a functioning network.

| Step | Message    | Direction          | Source    | Destination   | Purpose                                             |
|------|------------|--------------------|-----------|---------------|-----------------------------------------------------|
| 1    | Discover   | Client → Server    | 0.0.0.0   | 255.255.255.255 | Client broadcasts to find available DHCP servers  |
| 2    | Offer      | Server → Client    | Server IP | 255.255.255.255 | Server offers an available IP address and params  |
| 3    | Request    | Client → Server    | 0.0.0.0   | 255.255.255.255 | Client requests the offered address (broadcast)   |
| 4    | Acknowledge| Server → Client    | Server IP | Client IP     | Server confirms and delivers full IP configuration  |

### Why Broadcasts Cannot Cross Routers

DHCP Discover and Request messages use Layer 2 and Layer 3 broadcast addresses. Routers do not forward broadcasts by default. This means each subnet needs either a local DHCP server or a relay agent configured on the subnet's gateway router.

### DHCP Lease Lifecycle

A DHCP lease has three timing thresholds. At 50% of lease time (T1), the client attempts to renew directly with the server that issued the lease. At 87.5% of lease time (T2), if renewal failed, the client broadcasts a rebind request to any available DHCP server. At 100% of lease time, if rebind failed, the client releases its address and restarts the DORA process.

---

## 2. Cisco IOS DHCP Server Configuration

### Configuration Order

Always configure excluded addresses before creating pools. The excluded-address command must be in place before the pool starts handing out addresses.

```text
! Step 1: Reserve addresses for static assignment (gateways, servers, printers)
ip dhcp excluded-address <first-ip> <last-ip>

! Step 2: Create pool and define parameters
ip dhcp pool <pool-name>
  network <network-address> <subnet-mask>
  default-router <gateway-ip>
  dns-server <dns-ip1> [dns-ip2]
  domain-name <domain>
  lease <days> [<hours> [<minutes>]]
```

### Full Cisco IOS DHCP Server Example

```text
R1(config)# ip dhcp excluded-address 192.168.10.1 192.168.10.20
R1(config)# ip dhcp pool VLAN10_POOL
R1(dhcp-config)# network 192.168.10.0 255.255.255.0
R1(dhcp-config)# default-router 192.168.10.1
R1(dhcp-config)# dns-server 10.1.1.53 8.8.8.8
R1(dhcp-config)# domain-name corp.local
R1(dhcp-config)# lease 0 12
```

The `lease 0 12` means 0 days and 12 hours. The default lease is 1 day if not specified.

### DHCP Pool Parameter Reference

| Parameter       | Command Syntax                              | Purpose                                          |
|-----------------|---------------------------------------------|--------------------------------------------------|
| Subnet definition| `network <ip> <mask>`                      | Defines which subnet this pool serves            |
| Default gateway | `default-router <ip>`                       | Sent to clients as the default gateway           |
| DNS server(s)   | `dns-server <ip1> [ip2]`                    | Up to 8 DNS server addresses in order            |
| Domain name     | `domain-name <name>`                        | Appended to unqualified hostnames by client      |
| Lease time      | `lease <days> [hours] [minutes]`            | Duration of the IP address assignment            |
| WINS server     | `netbios-name-server <ip>`                  | Windows name service server (legacy)             |
| NTP server      | `option 42 ip <ip>`                         | NTP server address via DHCP option               |

---

## 3. DHCP Relay Agent — ip helper-address

### When a Relay Agent Is Needed

A relay agent is needed whenever the DHCP server and the DHCP clients are on different subnets separated by a router. Because DHCP broadcasts do not cross routers, the relay converts the broadcast to a unicast and forwards it.

### Configuration

Apply `ip helper-address` on the router interface facing the client subnet — not the server-facing interface:

```text
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip helper-address <dhcp-server-ip>
```

Multiple `ip helper-address` statements can be added to the same interface to specify multiple DHCP servers for redundancy.

### How the Relay Works

When a DHCP Discover broadcast arrives on the interface with `ip helper-address` configured:

1. The router copies the broadcast packet and converts the destination from 255.255.255.255 to the DHCP server's unicast IP
2. The router populates the `giaddr` (gateway IP address) field in the DHCP packet with the receiving interface's IP address
3. The DHCP server uses the `giaddr` field to determine which pool to use for the response
4. The server sends the Offer/Acknowledge directly to the relay agent's `giaddr` address
5. The relay agent forwards the response to the client subnet

### Default UDP Services Forwarded by ip helper-address

| Port | Service                |
|------|------------------------|
| 67   | DHCP (BootP server)    |
| 68   | DHCP (BootP client)    |
| 69   | TFTP                   |
| 37   | Time protocol          |
| 137  | NetBIOS Name Service   |
| 138  | NetBIOS Datagram       |
| 49   | TACACS                 |
| 53   | DNS                    |

---

## 4. DHCP Snooping

### What DHCP Snooping Prevents

Without DHCP snooping, any host on the network can run a rogue DHCP server. A rogue server can:

- Hand out incorrect default gateways (redirecting traffic to an attacker's machine)
- Hand out incorrect DNS servers (enabling DNS hijacking)
- Exhaust the legitimate DHCP pool (denial of service)

### Trusted vs Untrusted Ports

| Port Type | Connected To                              | Behavior                                       |
|-----------|-------------------------------------------|------------------------------------------------|
| Trusted   | Legitimate DHCP server, uplink to switch  | All DHCP messages (including Offers) allowed   |
| Untrusted | End-user client devices (default)         | DHCP Offer and ACK messages are dropped        |

All ports are untrusted by default when DHCP snooping is enabled. Only explicitly trusted ports allow DHCP server traffic.

### DHCP Snooping Configuration

```text
! Enable DHCP snooping globally
Switch(config)# ip dhcp snooping

! Enable for specific VLAN(s)
Switch(config)# ip dhcp snooping vlan 10
Switch(config)# ip dhcp snooping vlan 20

! Trust the uplink port facing the legitimate DHCP server
Switch(config)# interface GigabitEthernet0/24
Switch(config-if)# ip dhcp snooping trust

! Verification
Switch# show ip dhcp snooping
Switch# show ip dhcp snooping binding
```

### DHCP Snooping Binding Table

The snooping binding table maps: client MAC → assigned IP → VLAN → switch port → lease time. This table feeds into:

- Dynamic ARP Inspection (DAI): validates ARP packets against the binding table
- IP Source Guard: filters packets by source IP and MAC against the binding table

---

## 5. DNS Resolution Process

### Full Resolution Sequence

```text
Client query: www.example.com (no cache hit)
    |
    v
1. Client → Recursive Resolver
   Query: "What is the IP of www.example.com?" (recursive query)
    |
    v
2. Recursive Resolver → Root Name Server
   Query: "Who handles .com?" (iterative query)
   Response: "Ask the .com TLD server at 192.5.6.30"
    |
    v
3. Recursive Resolver → .com TLD Server
   Query: "Who handles example.com?"
   Response: "Ask ns1.example.com at 205.251.196.1"
    |
    v
4. Recursive Resolver → Authoritative Server for example.com
   Query: "What is the IP of www.example.com?"
   Response: A record = 93.184.216.34  (TTL: 3600)
    |
    v
5. Recursive Resolver caches result and returns to client
6. Client connects to 93.184.216.34
```

### Recursive vs Iterative Queries

| Query Type | Who Does the Work       | Used Between                        |
|------------|-------------------------|-------------------------------------|
| Recursive  | Resolver does all work  | Client and recursive resolver       |
| Iterative  | Resolver follows referrals | Recursive resolver and root/TLD/auth servers |

### DNS Record Types

| Record | Full Name              | Maps                                     | Example                            |
|--------|------------------------|------------------------------------------|------------------------------------|
| A      | Address                | Hostname → IPv4 address                  | www.example.com → 93.184.216.34    |
| AAAA   | IPv6 Address           | Hostname → IPv6 address                  | www.example.com → 2606:2800::/32   |
| CNAME  | Canonical Name         | Alias hostname → real hostname           | ftp.example.com → www.example.com  |
| MX     | Mail Exchanger         | Domain → mail server hostname            | example.com → mail.example.com     |
| PTR    | Pointer (reverse)      | IP address → hostname                    | 34.216.184.93.in-addr.arpa → www   |
| NS     | Name Server            | Domain → authoritative DNS server        | example.com → ns1.example.com      |
| SOA    | Start of Authority     | Zone metadata (primary NS, serial, TTL)  | example.com SOA ns1.example.com    |

---

## 6. Split-Horizon DNS

### The Problem Split-Horizon Solves

An organization publishes `app.corp.com` in public DNS as 203.0.113.50 (the public IP). Internal users querying public DNS get 203.0.113.50, which routes to the outside of the firewall. Traffic must transit NAT to reach the internal server at 10.5.1.50. This is inefficient and can fail in environments where hairpin NAT is not supported.

### The Solution

Run two authoritative DNS zones for the same domain name:

- External DNS zone for `corp.com`: returns 203.0.113.50 for `app.corp.com`
- Internal DNS zone for `corp.com`: returns 10.5.1.50 for `app.corp.com`

Internal clients query the internal DNS server and receive the internal IP. External clients query public DNS and receive the public IP.

### Cisco IOS DNS Configuration

To configure a Cisco router for DNS resolution:

```text
Router(config)# ip domain-lookup
Router(config)# ip name-server 8.8.8.8 8.8.4.4
Router(config)# ip domain-name corp.local
```

To disable DNS lookup on a router (reduces response time when mistyping commands):

```text
Router(config)# no ip domain-lookup
```

---

## 7. DHCP and DNS Command Reference

| Task                                  | Command                                          | Mode            |
|---------------------------------------|--------------------------------------------------|-----------------|
| Exclude addresses from DHCP pool      | `ip dhcp excluded-address <first> <last>`        | Global config   |
| Create DHCP pool                      | `ip dhcp pool <name>`                            | Global config   |
| Define pool subnet                    | `network <ip> <mask>`                            | DHCP pool       |
| Set default gateway for clients       | `default-router <ip>`                            | DHCP pool       |
| Set DNS server for clients            | `dns-server <ip1> [ip2]`                         | DHCP pool       |
| Set lease duration                    | `lease <days> [hours] [minutes]`                 | DHCP pool       |
| Configure DHCP relay                  | `ip helper-address <server-ip>`                  | Interface       |
| Enable DHCP snooping globally         | `ip dhcp snooping`                               | Global config   |
| Enable snooping on VLAN               | `ip dhcp snooping vlan <vlan-id>`                | Global config   |
| Trust a switch port for snooping      | `ip dhcp snooping trust`                         | Interface       |
| View active DHCP leases               | `show ip dhcp binding`                           | Privileged EXEC |
| View DHCP pool usage statistics       | `show ip dhcp pool`                              | Privileged EXEC |
| View address conflicts                | `show ip dhcp conflict`                          | Privileged EXEC |
| View DHCP server statistics           | `show ip dhcp server statistics`                 | Privileged EXEC |
| Debug DHCP events                     | `debug ip dhcp server events`                    | Privileged EXEC |
| View snooping binding table           | `show ip dhcp snooping binding`                  | Privileged EXEC |
| Configure router DNS server(s)        | `ip name-server <ip1> [ip2]`                     | Global config   |
| Enable DNS lookup on router           | `ip domain-lookup`                               | Global config   |
| Set default domain name               | `ip domain-name <name>`                          | Global config   |

---

## 8. DHCP Troubleshooting Flowchart

```text
SYMPTOM: Client not receiving an IP address via DHCP
         |
         v
Is the DHCP server on the same subnet as the client?
  YES --> Check: show ip dhcp pool — is the pool configured for that subnet?
       --> Check: show ip dhcp binding — is the client getting an IP?
       --> Check: show ip dhcp conflict — are there conflicts in the pool?
  NO  --> Continue (relay agent required)
         |
         v
Is ip helper-address configured on the gateway interface facing the client?
  NO  --> Add ip helper-address <server-ip> to the interface
  YES --> Continue
         |
         v
Can the relay router reach the DHCP server?
  Run: ping <dhcp-server-ip> from the relay router
  NO  --> Fix routing to DHCP server
  YES --> Continue
         |
         v
Is DHCP snooping blocking the Offer on a switch between client and router?
  Run: show ip dhcp snooping — is snooping enabled?
  Is the uplink port trusted?
  NO  --> Add ip dhcp snooping trust to the uplink port
         |
         v
Run: debug ip dhcp server events on the DHCP server
Are Discover messages arriving?
  NO  --> Relay or routing issue
  YES but no Offer --> Pool exhausted or wrong scope; check show ip dhcp pool
         |
         v
Issue resolved — verify with ipconfig /renew or dhclient
```

---

## 9. CCNA Exam Tips

**Tip 1 — DORA sequence.** The CCNA tests DORA in multiple question formats: identifying message types, explaining why Discover uses broadcast, and describing what happens when the server is on a different subnet. Know all four messages and their source/destination addresses.

**Tip 2 — ip helper-address placement.** The relay command goes on the interface facing the client subnet — the interface that receives the DHCP broadcast. It does NOT go on the server-facing interface. This is a frequently missed question.

**Tip 3 — DHCP snooping default.** All ports are untrusted by default when DHCP snooping is enabled. You must explicitly trust uplink ports and the port facing the DHCP server. Forgetting to trust the uplink is the most common snooping misconfiguration.

**Tip 4 — Recursive vs iterative.** The client sends a recursive query to its resolver. The resolver sends iterative queries to root, TLD, and authoritative servers. The resolver does all the heavy lifting — the client just waits for the final answer.

**Tip 5 — show ip dhcp binding.** This command is the primary verification tool for DHCP. It shows every active lease, the MAC address of each client, and the lease expiration time. If a client claims it is not getting an IP, check this output first.

**Tip 6 — Split-horizon use case.** When a question describes internal users getting routed to an external IP for an internal resource, split-horizon DNS is the solution. It ensures internal clients receive the internal IP directly rather than the public-facing IP.

**Tip 7 — ip domain-lookup.** On routers, `no ip domain-lookup` disables DNS resolution for the router itself. This is a best practice in labs to prevent the router from trying to resolve typos as DNS names. On the exam, if a question says the router attempts DNS resolution for every mistyped command, the fix is `no ip domain-lookup`.

---

## 10. Study Checklist

Work through each item before taking the Module 11 quiz.

- [ ] Write the Cisco IOS DHCP server configuration from memory for a /24 pool with exclusions
- [ ] Explain where `ip helper-address` is placed and why
- [ ] Describe the DORA process including source and destination addresses for each message
- [ ] Explain the difference between trusted and untrusted ports in DHCP snooping
- [ ] Draw the DNS resolution sequence for a fresh query from a client (no cache)
- [ ] Explain the difference between recursive and iterative DNS queries
- [ ] Describe a scenario where split-horizon DNS is necessary and how it resolves the problem
- [ ] Identify four DHCP troubleshooting commands and what each shows
- [ ] Complete the Module 11 Packet Tracer lab
- [ ] Post your Module 11 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and practice questions: professormesser.com
- Cisco DHCP configuration guide: cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/15-mt/dhcp-15-mt-book.html

---

## 11. Supplemental Resources

The following open educational resources extend DHCP and DNS concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Enterprise Networking, Security, and Automation, Chapter 7 (DHCP)** (skillsforall.com): Free chapter covering IOS DHCP server configuration, the relay agent (`ip helper-address`), DHCP snooping, and verification commands with interactive Packet Tracer activities that build multi-VLAN DHCP topologies.

2. **Jeremy's IT Lab — DHCP (Day 38) and DNS (Day 53)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): Video lessons covering the DORA process, IOS DHCP configuration, relay agent placement, DNS record types, recursive vs. iterative resolution, and exam-style scenario walkthroughs. Jeremy's DHCP video includes a Packet Tracer follow-along with troubleshooting.

3. **Cisco Learning Network — DHCP and DNS Study Group** (learningnetwork.cisco.com): Community discussion threads on DHCP relay troubleshooting, DHCP snooping trust port misconfigurations, split-horizon DNS scenarios, and CCNA exam question patterns for IP Services topics.

4. **Cisco IOS DHCP Snooping Configuration Guide** (cisco.com): Cisco's official guide covering DHCP snooping configuration, trust port designation, Option 82, the snooping binding database, and integration with Dynamic ARP Inspection (DAI). Includes CLI examples for multi-VLAN deployments.

5. **RFC 2131 — Dynamic Host Configuration Protocol** (rfc-editor.org/rfc/rfc2131): The authoritative IETF specification for DHCPv4, including the full DORA message exchange, relay agent behavior, `giaddr` field definition, and lease lifecycle management. The message format section is particularly useful for understanding what each DHCP packet field contains.
