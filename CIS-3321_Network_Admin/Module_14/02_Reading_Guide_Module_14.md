# Reading Guide: Module 14 — Network Troubleshooting Methodology

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Overview

This reading guide supports Module 14 video lectures and prepares you for the quiz and the CompTIA Network+ N10-008 exam. Network troubleshooting and tools make up a significant portion of Domain 5 (Network Troubleshooting and Tools) — one of the exam's largest domains. The seven-step methodology and scenario-based reasoning are directly tested.

**Estimated Reading Time:** 55–70 minutes

---

## Part 1: The CompTIA Seven-Step Troubleshooting Model

### 1.1 Step-by-Step Reference

The seven steps must be memorized in order. The exam presents scenarios that ask which step should be performed next, or which step was skipped.

| Step | Name | Key Activities |
|---|---|---|
| 1 | Identify the Problem | Gather information, duplicate the problem, identify symptoms, question users |
| 2 | Establish a Theory of Probable Cause | Consider common causes, use OSI model, consult documentation |
| 3 | Test the Theory | Run diagnostics, verify one hypothesis at a time |
| 4 | Establish a Plan of Action | Define the fix, assess impact, schedule if needed |
| 5 | Implement the Solution or Escalate | Apply the fix or escalate appropriately |
| 6 | Verify Full System Functionality | Confirm resolution, test related systems, check for new problems |
| 7 | Document Findings, Actions, and Outcomes | Update knowledge base, file change records, post-incident review |

### 1.2 Step 1 — Identify the Problem in Detail

Effective information gathering uses open-ended questions:

- "What is not working?" (not "Is the network down?" — yes/no answers are less informative)
- "When did the problem start?"
- "What changed recently? New hardware? Software update? Configuration change?"
- "Who else is affected? Just you, your floor, or the whole building?"
- "What error messages are you seeing?"

Duplicate the problem yourself if possible. You need firsthand observation, not just a user's description.

### 1.3 Step 2 — OSI Model as a Troubleshooting Framework

The OSI model organizes symptoms by layer. When building your theory, identify the lowest OSI layer at which a problem could explain all observed symptoms.

| OSI Layer | Common Problem Types |
|---|---|
| Layer 1 — Physical | No link, broken cable, port failure, duplex mismatch from auto-negotiation, NIC failure |
| Layer 2 — Data Link | Wrong VLAN, STP blocking, MAC table issue, duplex mismatch |
| Layer 3 — Network | Wrong IP, wrong subnet, missing route, wrong gateway, ARP failure |
| Layer 4 — Transport | Firewall blocking port, application not listening, NAT/PAT issue |
| Layer 5-7 — Session/Presentation/Application | DNS failure, authentication error, SSL certificate error, application crash |

### 1.4 Step 3 — Diagnostic Testing Principles

When testing theories:

- Change one variable at a time.
- Test the most likely cause first.
- Test the least disruptive option before the most disruptive.
- Use known-good substitutes when possible (test with a known-good cable before blaming the switch).
- Roll back changes that do not fix the problem — do not leave unrelated changes in place.

### 1.5 Step 5 — Escalation Guidelines

Escalation is appropriate when:

- The issue is beyond your skill level or authority
- The problem requires vendor support (hardware warranty, carrier circuit fault)
- The fix requires change management approval
- Resolution requires access or resources you do not have

Escalation tiers:

- Tier 1: Help desk / frontline support
- Tier 2: Network engineers, system administrators
- Tier 3: Senior engineers, vendor TAC (Technical Assistance Center)

Always provide complete documentation when escalating — what you observed, what you tested, what the results were.

### 1.6 Step 7 — Documentation Value

Documentation after every incident provides:

- Incident record for audit and compliance purposes
- Knowledge base entry for faster future resolution
- Pattern data — if the same problem recurs monthly, there is an underlying design flaw
- Protection for the administrator — documented actions show professional practice
- Input for change management — repeated incidents may trigger a formal change proposal

---

## Part 2: Troubleshooting Approaches

### 2.1 Bottom-Up

Start at Layer 1 (Physical) and verify each layer before moving up. Best when:

- The problem could be at any layer
- Physical layer has not been verified
- No prior knowledge about the affected system

Steps: Verify cable/port → Verify Layer 2 (VLAN, STP) → Verify Layer 3 (IP, routing) → Verify Layer 4 (firewall, NAT) → Verify DNS and application.

### 2.2 Top-Down

Start at Layer 7 (Application) and work down. Best when:

- Users can access some services but not a specific application
- Physical and network layers are known to be working for other traffic

### 2.3 Divide and Conquer

Start at Layer 3 and test bidirectionally. If ping works (Layer 3 OK), move up. If ping fails, move down to Layer 2 and 1. Best for experienced troubleshooters who want to quickly narrow the search space.

### 2.4 Follow the Path

Trace the traffic path from source to destination, verifying at each hop. Useful for routing and WAN problems. `traceroute` / `tracert` implements this approach automatically.

### 2.5 Swap the Component

Replace a suspected component with a known-good unit. If the problem goes away, the original component was faulty. If not, the component was not the cause.

---

## Part 3: Diagnostic Commands Reference

### 3.1 Windows / Linux Command Comparison

| Function | Windows | Linux/macOS |
|---|---|---|
| View IP configuration | `ipconfig /all` | `ip addr show` / `ifconfig` |
| Ping | `ping <host>` | `ping <host>` |
| Trace route | `tracert <host>` | `traceroute <host>` |
| DNS query | `nslookup <host>` | `nslookup <host>` / `dig <host>` |
| View ARP cache | `arp -a` | `arp -a` / `ip neigh` |
| View routing table | `route print` / `netstat -r` | `ip route` / `route -n` |
| View open connections | `netstat -an` | `netstat -an` / `ss -an` |
| Path MTU discovery | `ping -l 1472 -f <host>` | `ping -s 1472 -M do <host>` |

### 3.2 Command Deep Dives

#### ipconfig /all (Windows)

Key fields to check:

- IPv4 Address — should match expected subnet
- Subnet Mask — verify correct length for the network
- Default Gateway — must be reachable for off-subnet connectivity
- DNS Servers — must be reachable and contain correct records
- DHCP Server — shows which server issued the address
- IPv4 Address in 169.254.0.0/16 range = APIPA — DHCP failed

#### ping

Options:

- `ping -t <host>` (Windows): Continuous ping — useful for monitoring during changes
- `ping -n 100 <host>` (Windows): Send 100 pings — better sample for packet loss measurement
- Result analysis: Successful = Layer 1-3 reachable. TTL Exceeded = routing loop. Destination Unreachable = no route or firewall. Request Timeout = packet filtered or host down.

#### traceroute / tracert

Each line shows one router hop, with round-trip time to that hop. Three asterisks (***) mean the router did not respond to the probe — may be firewall-filtered, not necessarily a problem. Loss at a hop with successful replies at later hops indicates ICMP rate-limiting, not an actual break.

#### nslookup

Usage patterns:

- `nslookup hostname` — forward lookup
- `nslookup -type=MX domain.com` — query mail records
- `nslookup hostname <DNS server IP>` — query a specific server directly
- Identifies whether DNS failure is at the client DNS server or authoritative server level

---

## Part 4: Physical Layer and Hardware Troubleshooting

### 4.1 Copper Cable Faults

| Fault Type | Description | Detectable With |
|---|---|---|
| Open circuit | Wire completely broken | Basic cable tester, TDR |
| Short circuit | Two wires touching | Basic cable tester |
| Crossed pair (transposed) | Two pairs swapped end-to-end | Basic cable tester |
| Reversed pair | Wire pair polarity flipped | Basic cable tester |
| Split pair | Pair formed from wrong wires | Advanced tester (NEXT measurement) |
| Excessive crosstalk (NEXT) | Adjacent pair interference | Cable certifier |
| Attenuation | Signal loss over distance | Cable certifier |

### 4.2 Cable Testing Tools

#### Basic Cable Tester

- Tests continuity of all eight conductors
- Detects: opens, shorts, crossed pairs, reversed pairs, split pairs
- Does not measure performance (attenuation, NEXT)
- Inexpensive — suitable for basic field troubleshooting

#### Cable Certifier (e.g., Fluke DSX)

- Measures all TIA/EIA performance parameters
- Certifies cable as Cat5e, Cat6, Cat6a
- Includes TDR — locates faults by distance
- Required for formal structured cabling certification
- Expensive — typically $5,000–$15,000

#### Time Domain Reflectometer (TDR)

- Sends signal pulse down cable; measures reflected signal
- Calculates distance to any impedance discontinuity (break, short, connector)
- Available standalone or integrated in cable certifiers

#### Tone Generator and Inductive Probe

- Tone generator (transmitter) injects a tone signal onto the cable
- Probe detects the tone inductively through insulation and walls
- Used to trace cables from one end to the other through conduit, walls, and patch panels
- Also called a "toner" or "fox and hound" tool

### 4.3 Fiber Optic Testing Tools

| Tool | Purpose |
|---|---|
| Optical power meter | Measures signal strength (dBm) — detects attenuation |
| OTDR (Optical TDR) | Locates faults and measures attenuation per segment |
| Visual fault locator (VFL) | Red laser light visible at faults and tight bends |
| Fiber inspection microscope | Inspects connector end-face for contamination |
| Fiber cleaning kit | Removes contamination from connectors |

Most common fiber problem: dirty connectors. Clean before testing. Always.

### 4.4 Common Hardware Failure Symptoms

| Hardware | Failure Symptom | Diagnosis |
|---|---|---|
| NIC | No link light, 169.254 APIPA, wrong speed | Test with known-good cable; check device manager |
| Switch port | Dark LED, no link | Move device to different port; check `show interfaces` |
| PoE port | Device not powering | Check PoE budget; check PoE standard match |
| SFP/transceiver | No link on fiber port | Replace SFP; check fiber polarity; clean connectors |
| Switch PSU | Switch powers off or reboots | Check redundant PSU status; replace failed unit |
| Router WAN module | WAN interface down | Check CSU/DSU; contact carrier for circuit status |

---

## Part 5: Common Troubleshooting Scenarios

### 5.1 APIPA Address (169.254.x.x)

Symptom: Client has 169.254.x.x address.

Cause: DHCP request failed — client assigned itself an APIPA address per RFC 3927.

Diagnosis: Can the client reach the DHCP server? Is the DHCP server running? Is the helper-address (DHCP relay) configured on the router interface?

### 5.2 Duplicate IP Address

Symptom: Intermittent connectivity, ARP conflicts in logs, IP conflict notification.

Cause: Two devices configured with the same IP address.

Diagnosis: `arp -a` on other devices — which MAC addresses are associated with the IP? Use `ping -n 100` and observe which device responds.

### 5.3 Duplex Mismatch

Symptom: Slow throughput on a Gigabit link; late collisions in switch statistics.

Cause: One side set to full-duplex (or auto-negotiated); other set to half-duplex.

Diagnosis: `show interfaces` on the switch — look for "Half-duplex" or high collision counts.

Fix: Set both sides to the same explicit duplex and speed (full/1000), or both to auto-negotiation.

### 5.4 Incorrect DNS Configuration

Symptom: Can ping by IP, cannot connect by name.

Cause: DNS server unreachable, wrong DNS server configured, or missing DNS record.

Diagnosis: `nslookup` to test name resolution. `ipconfig /all` to verify DNS server addresses. Check if DNS server is reachable via ping.

---

## Key Terms Glossary

- **APIPA**: Automatic Private IP Addressing — 169.254.0.0/16 range; assigned when DHCP fails.
- **Cable certifier**: Advanced tool measuring cable performance and certifying compliance.
- **Divide and conquer**: Troubleshooting approach starting at Layer 3.
- **Duplex mismatch**: Mismatched full/half duplex settings causing slow performance and collisions.
- **Escalation**: Transferring a problem to a higher support tier.
- **NEXT**: Near End Crosstalk — interference between adjacent pairs measured at the same end.
- **OTDR**: Optical Time Domain Reflectometer — locates fiber faults by distance.
- **Split pair**: Wiring error using wires from different pairs — passes continuity but fails performance.
- **TDR**: Time Domain Reflectometer — locates cable faults by measuring signal reflection.
- **Tone generator**: Injects audible tone into cable for tracing.
- **VFL**: Visual Fault Locator — red laser reveals fiber breaks and tight bends.

---

## Review Questions

1. List the seven steps of the CompTIA troubleshooting methodology in order.

2. A user can ping a server by IP address but cannot connect to it by hostname. Which OSI layer is likely at fault? What command would you use to diagnose this?

3. A new workstation receives a 169.254.47.23 IP address. What does this indicate and what is the likely cause?

4. Describe three types of cable faults that a basic cable tester can detect but a TDR can additionally locate by distance.

5. What is a duplex mismatch? What symptom would you see in switch interface statistics?

6. A fiber link shows no light and the optical power meter reads no signal. List three possible causes in order from most to least common.

7. When should you escalate a problem rather than continue troubleshooting independently?

8. What is the purpose of Step 6 (Verify Full System Functionality) and why should it not be skipped?

9. Describe the divide-and-conquer troubleshooting approach and when it is most effective.

10. A switch port shows the following: Speed 10Mb/s, Duplex Half, Input errors: 45,000, CRC: 12,000. What are the likely causes?
