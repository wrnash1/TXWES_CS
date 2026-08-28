# Reading Guide: Module 10 — NAT and PAT

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

Network Address Translation (NAT) and Port Address Translation (PAT) are IP Services topics on the CCNA 200-301 exam. The exam tests your ability to distinguish NAT types, interpret translation table output, configure static NAT and PAT, and troubleshoot common failures. This guide covers all testable NAT concepts with configuration tables, command references, and a troubleshooting flowchart.

---

## 1. Core NAT Concepts

### Why NAT Exists

IPv4 has approximately 4.3 billion addresses. The internet ran out of globally routable IPv4 space in 2011. NAT allows organizations to use private RFC 1918 addresses internally (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) while sharing a small number of public IP addresses for outbound internet access.

### How NAT Works

A NAT-capable router sits at the boundary between the internal (inside) network and the external (outside) network. When a packet crosses this boundary, the router rewrites the source or destination IP address (and in the case of PAT, the port number) to perform the translation.

### NAT Direction Awareness

- Traffic flowing from inside to outside: source address is translated
- Traffic flowing from outside to inside (replies or static NAT): destination address is translated

---

## 2. NAT Address Terminology

The four NAT address types appear in `show ip nat translations` output and are tested heavily on the CCNA exam.

| Term           | Definition                                                                                       | Example         |
|----------------|--------------------------------------------------------------------------------------------------|-----------------|
| Inside local   | Private IP address of the internal host as seen from inside the network                          | 192.168.1.10    |
| Inside global  | Public IP address representing the internal host as seen from outside (internet side)            | 203.0.113.5     |
| Outside global | Public IP address of the external destination as seen from outside                              | 8.8.8.8         |
| Outside local  | IP address of the external destination as seen from inside (usually equals outside global)       | 8.8.8.8         |

### Memory Tip

Inside = your network. Outside = internet. Local = address as seen from the local perspective. Global = address as seen from the global (internet) perspective.

---

## 3. NAT Type Comparison

| NAT Type     | Mapping Ratio | Addresses Used            | Keyword     | Primary Use Case                       |
|--------------|---------------|---------------------------|-------------|----------------------------------------|
| Static NAT   | 1:1           | One public per one private | (none)      | Hosting servers accessible from internet |
| Dynamic NAT  | Many:pool     | Pool of public addresses  | (none)      | Controlled outbound with pool          |
| PAT (overload) | Many:1      | Single public IP          | `overload`  | Internet access for large networks     |

---

## 4. Static NAT Configuration

Static NAT creates a permanent bidirectional mapping. Internet hosts can initiate connections to the inside global address.

### Configuration Steps

```text
! Step 1: Create the static translation
Router(config)# ip nat inside source static <inside-local> <inside-global>

! Step 2: Mark the inside interface
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip nat inside

! Step 3: Mark the outside interface
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip nat outside
```

### Static NAT Example

Internal web server at 10.1.1.50 mapped to public IP 203.0.113.50:

```text
Router(config)# ip nat inside source static 10.1.1.50 203.0.113.50
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip nat inside
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip nat outside
```

Internet users connecting to 203.0.113.50 are transparently forwarded to 10.1.1.50.

---

## 5. Dynamic NAT Configuration

Dynamic NAT maps inside hosts to addresses from a named pool. Translations are temporary and expire when idle.

### Configuration Steps

```text
! Step 1: Define the public address pool
Router(config)# ip nat pool <name> <start-ip> <end-ip> netmask <mask>

! Step 2: Create ACL to identify inside hosts to translate
Router(config)# access-list <number> permit <network> <wildcard>

! Step 3: Link the ACL to the pool
Router(config)# ip nat inside source list <acl-number> pool <name>

! Step 4: Mark inside and outside interfaces
```

### Dynamic NAT Example

```text
Router(config)# ip nat pool CORP_POOL 203.0.113.10 203.0.113.20 netmask 255.255.255.0
Router(config)# access-list 10 permit 10.0.0.0 0.255.255.255
Router(config)# ip nat inside source list 10 pool CORP_POOL
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip nat inside
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip nat outside
```

---

## 6. PAT Configuration

PAT adds the `overload` keyword to allow many-to-one translation using port tracking.

### PAT Using Interface Address (Most Common)

```text
Router(config)# access-list 1 permit 192.168.0.0 0.0.255.255
Router(config)# ip nat inside source list 1 interface GigabitEthernet0/1 overload
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip nat inside
Router(config)# interface GigabitEthernet0/1
Router(config-if)# ip nat outside
```

The public IP is dynamically pulled from the `GigabitEthernet0/1` interface. If that interface IP changes (e.g., via DHCP from ISP), PAT automatically uses the new address.

### PAT Using a Named Pool

```text
Router(config)# ip nat pool PAT_POOL 203.0.113.1 203.0.113.1 netmask 255.255.255.0
Router(config)# ip nat inside source list 1 pool PAT_POOL overload
```

Using a pool with a single address in the pool range achieves the same PAT behavior with a static public IP.

---

## 7. NAT Command Reference

| Task                                    | Command                                                               | Mode            |
|-----------------------------------------|-----------------------------------------------------------------------|-----------------|
| Create static NAT mapping               | `ip nat inside source static <local> <global>`                        | Global config   |
| Define dynamic NAT pool                 | `ip nat pool <name> <start> <end> netmask <mask>`                    | Global config   |
| Link ACL to pool (dynamic)              | `ip nat inside source list <acl> pool <name>`                         | Global config   |
| Enable PAT with interface address       | `ip nat inside source list <acl> interface <int> overload`            | Global config   |
| Mark interface as NAT inside            | `ip nat inside`                                                       | Interface       |
| Mark interface as NAT outside           | `ip nat outside`                                                      | Interface       |
| View translation table                  | `show ip nat translations`                                            | Privileged EXEC |
| View detailed translation table         | `show ip nat translations verbose`                                    | Privileged EXEC |
| View NAT statistics and interface roles | `show ip nat statistics`                                              | Privileged EXEC |
| Clear all dynamic translations          | `clear ip nat translation *`                                          | Privileged EXEC |
| Clear specific translation              | `clear ip nat translation inside <local> <global>`                    | Privileged EXEC |
| Enable real-time NAT debugging          | `debug ip nat`                                                        | Privileged EXEC |
| Disable NAT debugging                   | `no debug ip nat`                                                     | Privileged EXEC |

---

## 8. Interpreting show ip nat translations Output

### Sample PAT Translation Table

```text
Router# show ip nat translations
Pro  Inside global       Inside local        Outside local       Outside global
tcp  203.0.113.1:1024    192.168.1.10:55321  8.8.8.8:443         8.8.8.8:443
tcp  203.0.113.1:1025    192.168.1.20:48210  8.8.8.8:443         8.8.8.8:443
icmp 203.0.113.1:512     192.168.1.30:512    8.8.4.4:512         8.8.4.4:512
---  203.0.113.50        10.1.1.50           ---                 ---
```

Reading the columns left to right:

- Pro: protocol (tcp, udp, icmp, or --- for static)
- Inside global: translated public address and port
- Inside local: original private address and port
- Outside local: destination as seen from inside (usually same as outside global)
- Outside global: destination public address

The last row (Pro = ---) is a static NAT entry with no protocol or port, confirming the permanent mapping.

---

## 9. NAT Troubleshooting Flowchart

```text
SYMPTOM: Internal hosts cannot reach internet / NAT not translating
         |
         v
Are inside and outside interfaces marked correctly?
  Run: show ip nat statistics
  Look for: "Inside interfaces" and "Outside interfaces" lists
  NO interfaces listed --> Apply ip nat inside / ip nat outside to correct interfaces
         |
         v
Is the ACL matching internal host traffic?
  Run: show access-lists <acl-number>
  Look for: hit counts on permit statements
  Zero matches --> ACL subnet/wildcard does not match source addresses; correct the ACL
         |
         v
Are translations appearing in the table?
  Run: show ip nat translations
  Empty table --> Translation not triggering; verify ACL match and interface markings
         |
         v
Is there a default route to the internet?
  Run: show ip route
  Look for: gateway of last resort (S* 0.0.0.0/0)
  Missing --> Add: ip route 0.0.0.0 0.0.0.0 <ISP-gateway>
         |
         v
Are translations present but traffic still not reaching internet?
  The inside global address must be routable by the ISP
  Confirm public IP is registered/assigned by the provider
         |
         v
Issue resolved — verify with ping from inside host to 8.8.8.8
```

---

## 10. NAT64 Concepts

NAT64 translates between IPv6 and IPv4 to support IPv6-only hosts communicating with IPv4-only internet services. Key concepts for the CCNA exam:

- NAT64 is a stateful translation mechanism similar to PAT
- DNS64 works alongside NAT64 to synthesize AAAA (IPv6) records for IPv4-only hosts so IPv6 clients can resolve them
- NAT64 is one of several IPv6 transition strategies alongside dual-stack and tunneling
- The CCNA tests understanding of the purpose of NAT64, not detailed configuration syntax

---

## 11. CCNA Exam Tips

**Tip 1 — Identify PAT by the overload keyword.** The `overload` keyword on the `ip nat inside source` command is what distinguishes PAT from dynamic NAT. Any question showing `overload` in the configuration is describing PAT.

**Tip 2 — Know the four address types cold.** The CCNA regularly shows `show ip nat translations` output and asks you to identify which address type is displayed in a specific column. Inside local = private address of the host. Inside global = public address of the host.

**Tip 3 — Static NAT is bidirectional.** Unlike dynamic NAT and PAT, static NAT allows external hosts to initiate connections to the internal server using the public IP address. This makes it suitable for web, mail, and other servers.

**Tip 4 — Pool exhaustion in dynamic NAT.** If the pool is full, new inside hosts cannot get a translation and their connections drop. PAT avoids this by supporting thousands of connections on a single IP using port tracking.

**Tip 5 — Interface marking is mandatory.** NAT does not function unless you apply `ip nat inside` to the inside-facing interface and `ip nat outside` to the outside-facing interface. Forgetting either one is the most common lab configuration error.

**Tip 6 — clear ip nat translation.** The `clear ip nat translation *` command removes all dynamic entries. It does not remove static entries. To test a configuration after fixing it, clear translations and then generate new traffic.

**Tip 7 — debug ip nat is high impact.** On production routers with heavy traffic, `debug ip nat` generates enormous output and can impair router performance. Always use `no debug all` or `undebug all` to stop debugging.

**Tip 8 — ACL in NAT identifies hosts, not destinations.** The ACL used in `ip nat inside source list` identifies which inside hosts should be translated. It is not a security ACL and should not have deny entries for destinations. A permit-only ACL matching the inside networks is the correct pattern.

---

## 12. Study Checklist

Work through each item before taking the Module 10 quiz.

- [ ] Write the three-step static NAT configuration from memory including interface marking
- [ ] Write the four-step dynamic NAT configuration from memory
- [ ] Write the PAT configuration using both interface and pool methods
- [ ] Define all four NAT address terms and identify each in sample show output
- [ ] Explain why PAT uses port numbers to track multiple simultaneous connections
- [ ] Trace the NAT troubleshooting flowchart through a sample missing-translation scenario
- [ ] Explain the purpose of NAT64 in an IPv6 transition context
- [ ] Complete the Module 10 Packet Tracer lab
- [ ] Post your Module 10 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and practice questions: professormesser.com
- Cisco IOS NAT configuration guide: cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/13772-12.html

---

## 13. Supplemental Resources

The following open educational resources extend NAT and PAT concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Enterprise Networking, Security, and Automation, Chapter 6 (NAT for IPv4)** (skillsforall.com): This free chapter covers static NAT, dynamic NAT, and PAT configuration with Packet Tracer activities, translation table interpretation, and troubleshooting using `show ip nat translations` and `show ip nat statistics`.

2. **Jeremy's IT Lab — NAT (Day 44)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): A comprehensive video covering all four NAT address types, static NAT, dynamic NAT, PAT with interface and pool methods, and translation table analysis. Jeremy's walkthrough includes exam-style scenarios for identifying the inside local and inside global addresses.

3. **Cisco Learning Network — NAT/PAT Study Group** (learningnetwork.cisco.com): Community threads on NAT troubleshooting scenarios, pool exhaustion behavior, ACL-in-NAT configuration pitfalls, and CCNA exam question patterns. The interface marking requirement (`ip nat inside`/`ip nat outside`) is a frequently discussed topic with multiple scenario examples.

4. **Cisco IOS IP Addressing Services Configuration Guide — NAT** (cisco.com): Cisco's official configuration guide covering static NAT, dynamic NAT with pools, PAT, hairpinning, NAT virtual interface, and `debug ip nat` output interpretation with full CLI examples.

5. **Packet Tracer Skills Integration Challenge — NAT** (Cisco Networking Academy): Free Packet Tracer activity files from the Networking Academy that include pre-built NAT topologies for configuring static NAT for a DMZ server, PAT for LAN users, and verifying connectivity from a simulated internet host.
