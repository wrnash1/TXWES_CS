# Lab Activity — Module 07: Network Security Architecture Analysis

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment | Authorized Educational Use Only

---

## Lab Overview

**Lab Title:** Network Security Architecture Design and Analysis

**Estimated Completion Time:** 90 minutes

**Submission:** Upload your completed deliverables to Canvas before the module deadline.

**Learning Objectives:**

- Analyze firewall rule sets and identify policy gaps.

- Design a DMZ architecture that meets stated security requirements.

- Evaluate a network topology for segmentation weaknesses.

- Apply zero-trust principles to a network redesign scenario.

- Interpret IDS/IPS alert data and classify detection events.

---

## Background

This lab uses scenario-based network analysis. No tools are installed, no systems are accessed, and no traffic is generated. All analysis is document-based, consistent with Security+ performance-based questions that test architecture reasoning skills.

---

## Part 1 — Firewall Rule Analysis (25 minutes)

### Part 1 Background

You are reviewing a firewall rule set for a small financial services company. The company has an internet-facing web server, an internal database server, and workstation users on the internal network. The firewall sits between the internet and the internal network (no DMZ is present — that is addressed in Part 2).

The current rule set (rules evaluated top to bottom):

| Rule | Source | Destination | Port/Protocol | Action |
|---|---|---|---|---|
| 1 | ANY | Web Server (203.0.113.10) | TCP 80 | PERMIT |
| 2 | ANY | Web Server (203.0.113.10) | TCP 443 | PERMIT |
| 3 | Internal Network | ANY | ANY | PERMIT |
| 4 | ANY | ANY | ANY | DENY |

### Part 1 Tasks

1. Rule 3 permits all traffic from the internal network to any destination on any port. What security risk does this create? Which type of malicious activity does it most directly enable?

2. A user on the internal network attempts to connect outbound on TCP 80 and TCP 443 to browse the internet. Which rule matches their traffic, and is this appropriate?

3. An attacker has compromised a workstation on the internal network and is attempting to exfiltrate data to an external server on TCP 4444. Which rule applies? Does the current configuration allow or block this?

4. The web server is directly on the internal network alongside the database server and workstations. Identify the security risk of this architecture compared to a DMZ design. What attack path does this create if the web server is compromised?

5. Rewrite the rule set with the following requirements: (a) permit inbound HTTP and HTTPS to the web server; (b) permit DNS and HTTPS outbound for internal workstations only; (c) deny all other traffic; (d) add an explicit rule to block RFC 1918 private addresses from appearing as source IPs on inbound internet traffic. Present your revised rule set in the same table format.

### Part 1 Deliverable

Written answers for tasks 1–4 and a revised firewall rule table for task 5.

---

## Part 2 — DMZ Architecture Design (20 minutes)

### Part 2 Background

The financial services company from Part 1 wants to implement a proper DMZ. They have the following infrastructure:

- One public-facing web server (serves the company's customer portal).

- One SMTP relay server (receives and forwards external email).

- One internal mail server (employees' mailboxes).

- One internal database server (stores customer financial data).

- User workstations on the internal network.

### Part 2 Tasks

1. Design a dual-firewall DMZ architecture for this company. Identify which systems belong in the DMZ and which belong on the internal network. Justify each placement decision.

2. Draw a simple text-based topology diagram showing: Internet, Outer Firewall, DMZ, Inner Firewall, Internal Network, and the placement of each server.

3. Write the key firewall rules for both the outer firewall and the inner firewall:
  - Outer firewall rules must define what traffic is permitted from the internet to the DMZ.
  - Inner firewall rules must define what traffic is permitted from the DMZ to the internal network and vice versa.

4. The internal database server needs to receive queries from the web server in the DMZ. How would you configure the inner firewall rule for this connection? Specify source, destination, port, and protocol. Apply least privilege to this rule.

5. An attacker compromises the SMTP relay server in the DMZ. What can the attacker reach from that position given your firewall design? What controls prevent them from reaching the internal database?

### Part 2 Deliverable

Written answers for tasks 1 and 5, a text-format topology diagram for task 2, outer and inner firewall rule tables for task 3, and the specific inner firewall rule for task 4.

---

## Part 3 — Zero Trust Architecture Evaluation (20 minutes)

### Part 3 Background

A technology company is evaluating a migration from their traditional perimeter-based network to a zero-trust architecture. Their current state is:

- All employees connect to a corporate VPN when working remotely.

- Once on VPN, employees have broad access to all corporate subnets.

- Office-based users connect directly to the flat internal network.

- Applications are hosted on-premises and in AWS.

- There is no device compliance checking before granting network access.

- User authentication for most applications is username and password only.

### Part 3 Tasks

1. Identify three specific security weaknesses in the current architecture that zero-trust principles would address. For each weakness, name the zero-trust principle or pillar that applies.

2. Using the CISA Zero Trust Maturity Model pillars (Identity, Devices, Networks, Applications/Workloads, Data), propose one specific improvement for each pillar that would advance this organization from "Traditional" toward "Initial" maturity. Be specific — name the control or technology, not just the concept.

3. The engineering team argues that zero trust will make it harder for developers to quickly access systems they need for incident response. How would you address this concern using PAM concepts from Module 06 and zero-trust principles from Module 07?

4. The company's CISO asks: "If we implement ZTNA to replace the VPN, what happens to our internal network monitoring visibility?" Explain what visibility is gained and what visibility may be reduced with a ZTNA model, and what compensating controls maintain monitoring capability.

### Part 3 Deliverable

Written answers to all four tasks (approximately 150 words each).

---

## Part 4 — IDS Alert Analysis (25 minutes)

### Part 4 Background

You are a SOC analyst. The IDS has generated the following four alerts. For each alert, classify it as a true positive, false positive, or unknown (requiring further investigation), and provide your reasoning.

### Alert 1

```text
ALERT: Potential SQL Injection attempt
Source: 198.51.100.45 (external)
Destination: 203.0.113.10:443 (web server)
Payload snippet: GET /search?q=1'+OR+'1'='1
Signature: SQL_INJECT_OR_TAUTOLOGY
Time: 2024-11-14 14:22:31
```

### Alert 2

```text
ALERT: Internal host scanning multiple ports
Source: 10.0.1.55 (internal workstation)
Destination: 10.0.2.0/24 (server subnet)
Activity: TCP SYN to 10.0.2.1-254 on port 22, 80, 443, 3389
Count: 254 targets in 30 seconds
Time: 2024-11-14 02:47:15
```

### Alert 3

```text
ALERT: DNS query for algorithmically generated domain
Source: 10.0.1.77 (internal workstation)
Destination: 8.8.8.8:53
Query: mxpqrlzabcdef1234.example-updates.com
Signature: DGA_DOMAIN_PATTERN
Time: 2024-11-14 09:05:02
```

### Alert 4

```text
ALERT: Large outbound data transfer
Source: 10.0.1.12 (internal workstation, Finance dept)
Destination: 52.31.199.148 (AWS us-east-1 IP range)
Volume: 4.2 GB transferred over 6 hours
Protocol: HTTPS (TCP 443)
Time: 2024-11-14 08:00:00 - 14:00:00
```

### Part 4 Tasks

1. For each alert, state your initial classification (true positive, false positive, or unknown) and your reasoning.

2. For each alert classified as "unknown," describe the specific additional information you would investigate to reach a definitive conclusion.

3. Alert 4 involves encrypted HTTPS traffic. The IDS cannot inspect the payload. What controls or additional data sources would help you determine whether this is legitimate business activity or data exfiltration?

4. Alert 2 occurs at 2:47 AM. How does the timing affect your assessment? What other contextual information would be relevant?

### Part 4 Deliverable

A four-row alert analysis table with columns for Alert, Classification, Reasoning, and Next Steps. Plus written answers to tasks 3 and 4.

---

## Lab Submission Checklist

Before submitting, verify:

- Part 1: Written answers for tasks 1–4 and revised rule table for task 5.

- Part 2: Written answers for tasks 1 and 5, topology diagram, firewall rule tables for task 3, and specific rule for task 4.

- Part 3: Written answers to all four tasks.

- Part 4: Four-row alert analysis table and written answers to tasks 3 and 4.

---

## Part 9 — Challenge Exercise

### Challenge 1: Firewall Rule Audit and Zero Trust Gap Analysis

A mid-size e-commerce company has engaged you for a network security assessment. Their network has a single perimeter firewall, a flat internal network with no segmentation, and a remote access SSL VPN. All 200 employees use the VPN when working remotely and gain full subnet access upon connection. The following policy gaps have been documented by a junior analyst.

1. The perimeter firewall has no egress filtering rules. Any internal host can initiate outbound connections to any destination on any port. Explain the three specific attack scenarios this enables — command-and-control beaconing, data exfiltration, and lateral movement facilitation — and write three specific egress rules (in table format) that would reduce risk while permitting normal business operations such as web browsing, email, and DNS resolution.

2. The company's VPN grants full network access to all subnets upon authentication. A developer account is compromised, and the attacker uses the VPN to scan and access the finance database server. Trace the attack path step by step: initial compromise → VPN authentication → network access → database reconnaissance → data extraction. For each step, identify which zero-trust principle would have broken the attack chain and what specific control implements that principle.

3. The company wants to prioritize their security improvements using a risk-tiered approach. Using the CISA Zero Trust Maturity Model pillars (Identity, Devices, Networks, Applications/Workloads, Data), assign each of the following gaps to the appropriate pillar and rank all five by risk priority (1 = highest). Justify each ranking with a specific threat scenario. The gaps are: no MFA on VPN; no device compliance checking; no internal VLAN segmentation; no application-level access control (all apps accessible once on VPN); no data classification labels on file shares.

4. After reviewing the network, you recommend replacing the SSL VPN with a ZTNA solution. The CIO asks: "What does ZTNA actually verify before granting access that our current VPN does not?" Write a concise comparison (in table format) covering: what is verified at access time, granularity of access granted, visibility into access events, and how a compromised account is contained under each model.

### Challenge 2: Network Segmentation Design and IDS Tuning

A regional bank with 300 employees operates the following infrastructure: branch teller workstations, ATM network, back-office servers (loan processing, HR, finance), a public-facing web portal, an internal development environment, and a data center with core banking systems. The current network is entirely flat — all systems share a single subnet.

1. Design a segmented network architecture for this bank. Define at least six network zones, identify which systems belong in each zone, and for each zone boundary specify whether you would implement a firewall, VLAN-only segmentation, or microsegmentation — and justify each choice based on the risk profile of the systems in adjacent zones.

2. The bank's compliance team reports that PCI DSS requires the cardholder data environment (CDE) to be isolated from all other networks with access controls and monitoring. Identify which of your proposed zones would be classified as the CDE, describe the specific firewall rules required at the CDE boundary (in table format, at least four rules), and explain why a flat network architecture fails PCI DSS Section 1.3 requirements.

3. The bank's IDS generates an average of 800 alerts per day. The SOC has two analysts and can investigate approximately 40 alerts per day thoroughly. Describe three specific IDS tuning strategies that would reduce alert volume without increasing the false negative rate. For each strategy, explain: what change is made, why it reduces volume, and what residual risk it introduces.

4. After implementing VLAN segmentation, the bank's security team discovers that the ATM network and the teller workstation network are in different VLANs but an attacker who compromises a teller workstation can still reach ATM management interfaces. Explain two specific techniques an attacker could use to cross VLAN boundaries despite segmentation, and for each technique identify the specific control that prevents it.

### Reflection Questions

1. After completing both challenges, explain why network segmentation alone is insufficient to achieve zero trust, even when every department has its own VLAN with firewall rules between them. Address the specific gap that microsegmentation fills, the specific gap that identity-aware access control fills, and why the combination of all three layers (VLAN segmentation + microsegmentation + identity verification) is required to satisfy the zero-trust principle of "never trust, always verify."

2. In Challenge 1, you analyzed egress filtering as a control against command-and-control beaconing and data exfiltration. A network engineer argues that since all C2 traffic now uses HTTPS on port 443, egress filtering is ineffective because you cannot block port 443 without breaking all web traffic. Identify two specific controls beyond port-based egress filtering that address HTTPS-based C2 and exfiltration, explain the mechanism by which each control detects or blocks the malicious traffic despite it using standard HTTPS, and describe the operational tradeoffs each control introduces.

---

Module 07 Lab — End
