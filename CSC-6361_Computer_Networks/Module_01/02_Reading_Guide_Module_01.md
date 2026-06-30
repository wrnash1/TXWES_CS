# Reading Guide: Module 01 – Advanced IP Routing: Multi-Area OSPF & EIGRP
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
