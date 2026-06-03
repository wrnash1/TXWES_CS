# Lab: Module 15 — Network Documentation and Policies

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Lab Overview

This lab is a documentation and policy creation exercise. Rather than configuring network devices, you will produce the actual documentation artifacts that professional network administrators create and maintain: a network diagram, an IPAM spreadsheet, a change request, and a basic DR plan outline. These deliverables mirror real-world work products.

**Estimated Time:** 90–120 minutes

**Required Tools:**

- draw.io (free — diagrams.net) or Microsoft Visio for diagrams
- Microsoft Excel, Google Sheets, or any spreadsheet application for IPAM
- Microsoft Word, Google Docs, or any word processor for policy documents

---

## Scenario

You have been hired as the network administrator for Lone Star Community Credit Union, a regional credit union with two locations:

- Main Branch — Fort Worth, TX: 45 staff workstations, 3 servers, 1 VoIP gateway, 10 IP phones, 2 wireless APs
- Branch Office — Arlington, TX: 12 staff workstations, 1 server, 5 IP phones, 1 wireless AP

The network uses the following address space:

- Main Branch LAN: 192.168.1.0/24 — Staff VLAN 10
- Main Branch Voice: 192.168.2.0/24 — Voice VLAN 20
- Main Branch Servers: 192.168.3.0/24 — Server VLAN 30
- Main Branch Management: 192.168.99.0/24 — Management VLAN 99
- Arlington Branch LAN: 172.16.10.0/24 — Staff VLAN 10
- Arlington Branch Voice: 172.16.20.0/24 — Voice VLAN 20
- WAN Link (MPLS): 10.0.0.0/30 — Main to MPLS PE
- WAN Link (MPLS): 10.0.0.4/30 — Arlington to MPLS PE

The two branches are connected via a 10 Mbps MPLS circuit. Main Branch has a 100 Mbps fiber internet connection.

---

## Part 1: Network Diagram

### Part 1 Objective

Create a logical network diagram for Lone Star Community Credit Union using draw.io or Visio.

### Step 1: Set Up Your Diagram

Open draw.io (diagrams.net) in your browser. Create a new diagram.

From the shape library, enable "Network" shapes. You will need: router, switch, firewall, server, PC, IP phone, wireless AP, and cloud shapes.

### Step 2: Build the Logical Diagram

Include the following elements:

Internet cloud (top of diagram):

- Represents public internet
- Connected to Main Branch firewall via 100 Mbps fiber

Main Branch (center-left area):

- Firewall (label: FW-Main, Management IP: 192.168.99.2)
- Core switch (label: SW-CORE-01, Management IP: 192.168.99.10)
- Access switch for staff floor (label: SW-ACCESS-01, Management IP: 192.168.99.11)
- VoIP Gateway (label: VGW-01, IP: 192.168.2.2)
- Three servers in Server VLAN 30: DC01 (192.168.3.10), FILE01 (192.168.3.11), PRINT01 (192.168.3.12)
- Label each VLAN boundary with VLAN ID and subnet

MPLS cloud (center of diagram):

- Represents carrier MPLS network
- Connected to both branch routers
- Label with bandwidth: 10 Mbps

Arlington Branch (right area):

- Router (label: RTR-ARLINGTON, WAN IP: 10.0.0.6, LAN: 172.16.10.1)
- Access switch (label: SW-ARLINGTON-01, Management IP: 172.16.10.250)
- File server (label: FILE-ARL-01, IP: 172.16.10.10)

Label all subnets on the diagram. Use consistent notation (e.g., 192.168.1.0/24 written next to each segment).

### Step 3: Add a Title Block

Add a title block to your diagram containing:

- Organization name: Lone Star Community Credit Union
- Diagram title: Logical Network Diagram
- Author: Your name
- Date: Today's date
- Version: 1.0

### Checkpoint 1

Export the diagram as a PNG or PDF. Submit with the lab report.

---

## Part 2: IPAM Spreadsheet

### Part 2 Objective

Create an IP Address Management spreadsheet for the Main Branch network.

### Step 4: Create Subnet Tab

Create a spreadsheet with two tabs: "Subnets" and "Static Assignments."

On the Subnets tab, create columns and fill in a row for each subnet:

Columns: Subnet | Prefix Length | VLAN | Purpose | Gateway | DHCP Start | DHCP End | DHCP Exclusions | Notes

Fill in rows for all four Main Branch subnets:

- 192.168.1.0 / 24 / VLAN 10 / Staff Workstations / 192.168.1.1 / 192.168.1.100 / 192.168.1.200 / 192.168.1.1–99 reserved for static
- 192.168.2.0 / 24 / VLAN 20 / Voice (VoIP Phones) / 192.168.2.1 / 192.168.2.100 / 192.168.2.200 / 192.168.2.1–99 reserved
- 192.168.3.0 / 24 / VLAN 30 / Servers / 192.168.3.1 / (No DHCP — all static) / — / — / All addresses statically assigned
- 192.168.99.0 / 24 / VLAN 99 / Network Management / 192.168.99.1 / (No DHCP — all static) / — / — / Admin access only

### Step 5: Create Static Assignments Tab

On the Static Assignments tab, create columns:

IP Address | Hostname | MAC Address | Device Type | VLAN | Location | Owner | Notes | Date Assigned

Add entries for all static devices:

- 192.168.3.10 — DC01 — AA:BB:CC:DD:EE:01 — Windows Server (Domain Controller) — VLAN 30 — Server Room Rack 1 U10 — IT — Primary DC — 2024-01-15
- 192.168.3.11 — FILE01 — AA:BB:CC:DD:EE:02 — Windows Server (File Server) — VLAN 30 — Server Room Rack 1 U12 — IT — Primary File Server — 2024-01-15
- 192.168.3.12 — PRINT01 — AA:BB:CC:DD:EE:03 — Windows Server (Print Server) — VLAN 30 — Server Room Rack 1 U14 — IT — Print Server — 2024-01-15
- 192.168.2.2 — VGW-01 — AA:BB:CC:DD:EE:10 — Cisco VoIP Gateway — VLAN 20 — Server Room — IT — VoIP Gateway — 2024-01-20
- 192.168.99.2 — FW-Main — AA:BB:CC:DD:EE:20 — Fortinet Firewall — VLAN 99 — Server Room Rack 2 U1 — IT — Main Firewall — 2024-01-15

Add at least three more entries for network devices of your choice (switches, management addresses, etc.).

### Checkpoint 2

Submit the completed IPAM spreadsheet (both tabs populated) as part of the lab report.

---

## Part 3: Change Request Document

### Part 3 Objective

Complete a formal Change Request for a planned network change.

### Step 6: Write the Change Request

The following change is proposed: The credit union's compliance officer has requested that the server VLAN (VLAN 30) be isolated from the staff VLAN (VLAN 10) by adding a firewall rule that blocks all direct communication from VLAN 10 to VLAN 30. Staff will be required to use application-layer services (File Server share access on TCP 445) — direct ping and other protocols will be blocked. The change is scheduled for Saturday at 2:00 AM.

Complete a Change Request document with the following sections:

- Change title and reference number (assign CR-2024-001)
- Change type (Standard / Normal / Emergency — select and justify)
- Submitter name and date
- Proposed implementation date and maintenance window
- Description of the change (specific ACL or firewall rule changes)
- Business justification
- Systems affected
- Risk rating and rationale
- Rollback plan (exactly how to undo the change)
- Test plan (what tests confirm success)
- Required approvals (list the roles that should approve)

### Checkpoint 3

Submit the completed Change Request document.

---

## Part 4: DR Plan Outline

### Part 4 Objective

Create a basic DR plan outline for the credit union's most critical system: the Domain Controller (DC01 at 192.168.3.10).

### Step 7: Write the DR Plan Section for DC01

Create a document with the following sections for DC01:

System name and description:

- Name: DC01
- Description: Windows Server 2022 Domain Controller — provides authentication, DNS, and Group Policy for all Main Branch staff

Recovery objectives:

- RTO: 4 hours (credit union can operate for 4 hours using cached credentials)
- RPO: 1 hour (AD changes must not be lost more than 1 hour of changes)

Recovery team:

- Primary: [Your name] — Network/Systems Administrator — [phone placeholder]
- Secondary: [Backup contact] — IT Manager — [phone placeholder]

Backup strategy:

- Full system backup via Windows Server Backup daily at midnight to NAS device
- Active Directory replication to a second DC (DC02 at 192.168.3.13) every 15 minutes
- Backup retention: 30 days

Activation criteria:

- DC01 unresponsive for more than 30 minutes
- Hardware failure confirmed; no expected recovery within 4 hours

Recovery procedures (numbered steps):

1. Confirm DC01 failure — ping, RDP attempt, physical console check.
2. Verify DC02 is responding to authentication requests — test workstation login.
3. If DC02 is handling authentication, user impact is minimal — update DNS to ensure DC02 is primary DNS.
4. Order replacement hardware or request loaner server from vendor.
5. Restore DC01 from most recent backup once hardware is available.
6. Verify AD replication between DC01 and DC02 after restoration.
7. Notify IT Manager and branch manager of restoration.
8. Document incident and update change log.

Vendor contacts:

- Server hardware vendor: [Placeholder — Dell/HP/Lenovo support number]
- Microsoft support: 1-800-642-7676

### Checkpoint 4

Submit the completed DR plan section document.

---

## Lab Report Requirements

Submit a single PDF containing all of the following:

1. Checkpoint 1: Exported network diagram PNG or PDF.
2. Checkpoint 2: IPAM spreadsheet (submitted as Excel/Sheets attachment or embedded screenshots).
3. Checkpoint 3: Completed Change Request document.
4. Checkpoint 4: DR plan outline for DC01.
5. Reflection (150–200 words): A colleague argues that documentation is a waste of time — "I know this network; I don't need to write it all down." Write a response that uses at least two specific scenarios from Module 15 content to counter this argument.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Network diagram (complete, labeled, correct topology) | 25 |
| Part 2 — IPAM spreadsheet (both tabs, complete entries) | 20 |
| Part 3 — Change Request (all sections complete and appropriate) | 25 |
| Part 4 — DR plan outline (RTO/RPO correct, procedures actionable) | 20 |
| Reflection paragraph | 10 |
| **Total** | **100** |
