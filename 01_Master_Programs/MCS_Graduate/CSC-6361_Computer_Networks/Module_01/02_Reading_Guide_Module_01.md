# Reading Guide: Module 01 – Advanced IP Routing: Multi-Area OSPF & EIGRP

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CSC-6361 &BULL; ADVANCED COMPUTER NETWORKS (GRADUATE LEVEL)</text>
    
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

## CSC-6361 Advanced Computer Networks | Graduate Level
## Week 1: October 19–25, 2026

---

## Learning Objectives
By completing this reading guide, you will be able to:
1. Explain the hierarchical architecture of multi-area OSPF, including the role of Area 0, ABRs, and ASBRs.
2. Differentiate LSA Types 1–5 and 7, specifying which cross area boundaries and which do not.
3. Compare and contrast Stub, Totally Stubby, NSSA, and Totally NSSA area types.
4. Describe the EIGRP DUAL algorithm, defining Feasible Distance, Reported Distance, Successor, and Feasible Successor.
5. Configure EIGRP Named Mode and explain its advantages over Classic mode.
6. Design and implement mutual redistribution between OSPF and EIGRP with route-tag loop prevention.

---

## Required Free Readings

### 1. IETF RFC 2328 — OSPF Version 2 (Sections 1–4 and 10–12)
**URL:** https://datatracker.ietf.org/doc/html/rfc2328
**Focus sections:**
- Section 1: Overview of OSPF
- Section 3.3: The Areas of an Autonomous System
- Section 10: The Flooding Procedure (LSA types)
- Section 12.1: The LSA Header

**Graduate Reading Note:** RFCs are the authoritative source for protocol behavior. Read these sections critically — note where the RFC says "MUST", "SHOULD", and "MAY". These are normative requirement levels (RFC 2119) that define what is mandatory behavior vs. recommended behavior.

### 2. IETF RFC 7868 — Cisco EIGRP (Sections 1–5)
**URL:** https://datatracker.ietf.org/doc/html/rfc7868
**Focus sections:**
- Section 1: Introduction
- Section 2: EIGRP Architecture
- Section 3: DUAL Algorithm Overview

### 3. Cisco OSPF Design Guide (Free)
**URL:** https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7039-1.html
**Focus:** Multi-area OSPF design best practices, stub area configuration, ABR summarization commands

### 4. Cisco EIGRP Named Mode Configuration Guide (Free)
**URL:** https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_eigrp/configuration/xe-16/ire-xe-16-book/ire-named-md.html
**Focus:** Address-family configuration, per-interface settings, topology base commands

### 5. Cisco Learning Network — CCNP ENCOR Study Hub
**URL:** https://learningnetwork.cisco.com/s/encor-study-materials
**Focus:** Review the OSPF and EIGRP sections of the official CCNP ENCOR study materials

---

## Key Concepts to Master

### OSPF Area Design Rules (Graduate-Level)
1. **All non-backbone areas must connect to Area 0** — this is an absolute design requirement.
2. **Virtual links** can extend Area 0 connectivity through non-backbone areas in legacy designs, but this is considered a workaround, not best practice.
3. **ABRs maintain separate LSDBs** for each area they participate in — they do not share the full LSDB between areas.
4. **Summarization suppresses specific routes** in the summarizing area's LSDB — there is a trade-off between summarization efficiency and routing detail for troubleshooting.

### EIGRP DUAL Reference Card
| Term | Definition |
|---|---|
| FD | Feasible Distance — total metric from local router to destination via Successor |
| RD / AD | Reported/Advertised Distance — neighbor's metric to the destination |
| Successor | Primary best path — appears in routing table |
| Feasible Successor | Backup path where RD < FD (Feasibility Condition) |
| Active State | EIGRP is querying for a new path (no FS available) |
| SIA | Stuck-in-Active — neighbor failed to reply to Query (relationship torn down) |

### Redistribution Route Tag Loop Prevention Pattern
```
! On the redistribution router — tag OSPF routes being sent into EIGRP
route-map OSPF-TO-EIGRP permit 10
 match tag 100
 ! deny routes that were already tagged as coming from EIGRP
route-map OSPF-TO-EIGRP deny 5
 match tag 200

route-map EIGRP-TO-OSPF permit 10
 match tag 200
route-map EIGRP-TO-OSPF deny 5
 match tag 100

router ospf 1
 redistribute eigrp 100 subnets route-map EIGRP-TO-OSPF tag 200

router eigrp ENTERPRISE
 address-family ipv4 unicast autonomous-system 100
  topology base
   redistribute ospf 1 metric 10000 100 255 1 1500 route-map OSPF-TO-EIGRP tag 100
```
This pattern ensures that routes redistributed from OSPF into EIGRP are tagged `100`, and when those routes attempt to be redistributed back into OSPF, they are denied by the `deny 5` statement matching tag `100`.

---

## Verification Commands Reference
Practice these commands until they are second nature:

**OSPF Verification:**
```
show ip ospf neighbor                  ! Verify neighbor relationships
show ip ospf database                  ! View the LSDB
show ip ospf database summary          ! View Type 3 LSAs
show ip ospf interface                 ! Verify area assignments, DR/BDR status
show ip route ospf                     ! View OSPF routes in routing table
```

**EIGRP Verification:**
```
show ip eigrp neighbors                ! Verify neighbor relationships
show ip eigrp topology                 ! View topology table (all paths)
show ip eigrp topology all-links       ! View all paths including non-FS
show ip route eigrp                    ! View EIGRP routes in routing table
debug ip eigrp                         ! Real-time EIGRP updates (use with caution)
```

---

## Graduate Discussion Prompt (Due Sunday, October 25, 11:59 PM CST)

**Prompt:** A senior network engineer at your company has proposed migrating a 50-router single-area OSPF network to a multi-area design. A junior engineer objects, arguing that the reconfiguration risk and downtime outweigh the benefits because "OSPF is already working fine." Write a substantive response (400+ words) from the perspective of the senior engineer. Address: (1) the specific technical limitations of a 50-router single-area OSPF network, (2) the concrete benefits of multi-area design in terms of convergence and scalability, and (3) a brief migration strategy that minimizes risk. Cite at least one RFC or Cisco design guide in your argument.

**Peer Response:** After posting your initial response, provide substantive replies to at least two classmates. Challenge their migration strategy or add a complicating scenario (e.g., "What if some of the 50 routers are in a remote data center with limited maintenance windows?").

---

## 9. Supplemental Resources

**1. Cisco OSPF Troubleshooting Guide — "OSPF Neighbor Problems Explained"**
https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13733-26.html
Authoritative Cisco troubleshooting reference covering all OSPF neighbor state failures (EXSTART, EXCHANGE, LOADING). Essential reading for understanding why adjacencies fail and how to diagnose them from `show ip ospf neighbor` output.

**2. IETF RFC 4750 — OSPF MIB (OSPF Version 2 Management Information Base)**
https://datatracker.ietf.org/doc/html/rfc4750
Defines the SNMP MIB objects for OSPF v2. Useful for understanding what operational data OSPF exposes for monitoring — directly relevant to production network management and the CCNP ENCOR network management domain.

**3. Cisco EIGRP Technology White Paper — "Introduction to EIGRP"**
https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html
Comprehensive Cisco white paper covering DUAL algorithm internals, metric calculation, Named Mode, and redistribution — written at CCNP depth and freely available without registration.
