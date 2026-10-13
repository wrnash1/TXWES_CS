# Video Script: Module 15 — Network Documentation and Policies (Part 1 of 2)

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Network+ (N10-008)

---

## Introduction

Welcome to Module 15 of CIS-3321 Network Administration. I am Professor Nash. This module covers network documentation and organizational policies — topics that might seem less exciting than configuring routers and troubleshooting switches, but are absolutely essential for running a professional network environment.

Here is the reality: the best-designed network in the world is only as manageable as its documentation. When a critical link fails at 2 AM, the on-call technician needs to know exactly what is connected where, what the IP addressing scheme is, and what the change history looks like. Without documentation, that technician is guessing in the dark.

Documentation and policies also make up a measurable portion of the CompTIA Network+ N10-008 exam — specifically Domain 3 (Network Operations) and Domain 5 (Network Troubleshooting).

Part 1 covers network diagrams, IP address management, and change management. Part 2 covers acceptable use policies, service level agreements, and disaster recovery documentation.

---

## Section 1: Network Diagrams

Network diagrams are the foundation of network documentation. They provide a visual representation of the network's physical and logical structure.

### Logical Diagrams

A logical diagram shows how devices communicate at the network layer — IP addressing, routing, VLANs, and logical traffic flows — without necessarily showing the physical location of devices or the actual cable paths.

What a logical diagram includes:

- Device names (hostnames) and device types (shown with standard icons)
- IP address assignments (network addresses and individual interface addresses)
- VLAN IDs and names
- Routing protocols and major routes
- WAN connections with bandwidth and circuit IDs
- Network boundaries (internet, DMZ, internal, cloud)

Logical diagrams are used for:

- Planning network changes — visualizing the impact before making changes
- Troubleshooting — understanding traffic paths
- Onboarding new staff — orienting them to the network architecture
- Security reviews — identifying trust boundaries and exposure points

### Physical Diagrams

A physical diagram shows the actual physical connections and locations:

- Which device connects to which other device and via what port
- Rack locations and physical hardware layout
- Cable types and patch panel connections
- Building floors, server rooms, and wiring closets

Physical diagrams are used for:

- Cable plant management
- Hardware replacement planning
- Physical security assessments
- Data center and rack layout planning

### Standard Diagram Symbols

Network diagrams use standardized icons to represent device types. While not legally required, using standard icons makes diagrams universally readable. Common standards come from Cisco, Microsoft Visio, and network diagram software like Lucidchart, draw.io, and NetBox.

Standard device representations:

- Router: Cylinder with an arrow circle
- Switch: Rectangle with arrows pointing in multiple directions
- Firewall: Brick wall symbol or flame icon
- Server: Tower or rack-mount box
- Cloud: Cloud shape (internet or provider cloud services)
- Workstation: Desktop or laptop icon
- Wireless AP: Antenna with wave lines

### Diagram Maintenance

Diagrams that are not kept current become liabilities — they mislead troubleshooters and planners. Best practices:

- Update diagrams whenever a physical change is made (new device, cable move, configuration change).
- Version-control diagrams — keep change history.
- Store diagrams in a shared location accessible to the team.
- Review diagrams at regular intervals — quarterly or annually — to catch undocumented drift.

---

## Section 2: IP Address Management

### Why IP Address Management Matters

IP address management, commonly called IPAM, is the process of planning, tracking, and managing IP address space within a network. Without IPAM, organizations experience:

- IP address conflicts (two devices with the same IP)
- Accidental overlap of subnets during network expansion
- Unknown device counts leading to subnet exhaustion
- Inability to troubleshoot because no one knows what has what IP

### Manual IPAM — Spreadsheets

The simplest IPAM approach is a spreadsheet. A well-maintained IP address spreadsheet documents:

- Subnet address and mask (e.g., 192.168.10.0/24)
- Subnet purpose (e.g., "Marketing floor, VLAN 10")
- Gateway address
- DHCP range (start and end)
- Static assignments — hostname, IP, MAC, device type, location
- Date last updated

Limitations of spreadsheets:

- Manual — easily becomes out of date
- No automated discovery or conflict detection
- No integration with DNS or DHCP
- Does not scale well beyond a few hundred addresses

### IPAM Software

Enterprise organizations use dedicated IPAM software that integrates DNS, DHCP, and IP management — called DDI (DNS, DHCP, IPAM). Examples: Infoblox, SolarWinds IPAM, phpIPAM (open source), NetBox (open source).

IPAM software features:

- Automated discovery of active addresses on the network
- Conflict detection and alerts
- DHCP server integration — automatically records leases
- DNS integration — automatically creates/removes DNS records
- Subnet utilization reporting — shows percentage of subnets in use
- Audit trail — records who made what change when

### Subnetting Documentation

Document every subnet with:

- Network address and prefix length
- Usable host range
- Broadcast address
- VLAN association
- Physical location (building, floor, rack)
- Purpose (server farm, user access, management, DMZ)
- DHCP configuration (yes/no, server address, scope range, exclusions)

This documentation is critical when expanding the network — you need to know which address space is available for new subnets.

---

## Section 3: Change Management

Change management is the formal process for requesting, reviewing, approving, implementing, and documenting changes to a production network. It is one of the most important operational disciplines in enterprise networking.

### Why Change Management Is Critical

The majority of network outages are caused by changes — configuration modifications, software updates, hardware replacements. Change management does not prevent changes; it makes changes safer by requiring planning, peer review, and rollback preparation.

### Change Management Components

#### Change Request (CR)

A Change Request is the formal document initiating a change. It includes:

- Description of the proposed change
- Business justification (why is this change needed?)
- Systems affected
- Risk assessment (low/medium/high risk)
- Rollback plan (how to undo the change if it fails)
- Implementation steps
- Test plan (how to verify success)
- Maintenance window (when the change will be made)
- Required approvals

#### Change Advisory Board (CAB)

The Change Advisory Board is a group that reviews and approves change requests. Typically includes representatives from IT operations, security, application teams, and business stakeholders. The CAB meets regularly — often weekly — to review pending changes.

#### Change Types

- **Standard change**: Pre-approved, routine, low-risk change. Follows an established procedure. Examples: adding a user account, rebooting a server per scheduled maintenance. Does not require CAB approval each time.
- **Normal change**: Requires CAB review and approval. Scheduled in advance. Examples: VLAN configuration change, router upgrade, firewall rule modification.
- **Emergency change**: Urgent fix required immediately due to a major outage or security incident. Expedited approval process. Must still be documented after implementation.

#### Rollback Plan

Every normal and emergency change must have a documented rollback plan — the specific steps to restore the previous configuration if the change causes problems. This is not optional. A change without a rollback plan should not be approved.

### Change Management Best Practices

- Never make changes to production without a change record.
- Implement changes during maintenance windows (typically nights or weekends when traffic is lowest).
- Test changes in a lab or staging environment before production when possible.
- Communicate planned changes to stakeholders in advance.
- Document what actually happened — not just what was planned.

---

## Section 4: Configuration Management

Related to change management is configuration management — the ongoing documentation of device configurations.

### Device Configuration Backups

Every network device configuration should be backed up regularly and after every change. Methods:

- Manual: Copy running-config to a file — simple but prone to being skipped.
- TFTP: Device pushes config to a TFTP server — can be automated.
- Network configuration management tools: RANCID, Oxidized, SolarWinds Network Configuration Manager — automatically back up device configs on a schedule and detect changes.

### Configuration Baseline

A baseline configuration is the known-good, approved starting state for a device type or network segment. Deviations from the baseline indicate unauthorized changes or drift.

Change detection tools alert administrators when a running configuration differs from the last-approved baseline. This is particularly important for security compliance — detecting unauthorized access or configuration modifications.

### Configuration Documentation

Document for each network device:

- Hostname and management IP address
- Device type and model
- Firmware/OS version
- Physical location (building, room, rack, unit)
- Interface assignments (what is connected to each port)
- VLAN assignments
- Routing protocols configured
- Access control lists applied
- Date of last configuration change and who made it

---

## Summary of Part 1

Key points from Part 1:

- Network diagrams include logical (IP addressing, VLANs, routing) and physical (connections, locations, ports) types. Both must be maintained.
- IP Address Management (IPAM) tracks subnet allocation and individual IP assignments. Enterprise IPAM integrates DNS, DHCP, and IP tracking.
- Change management requires formal Change Requests, CAB review, rollback plans, and documentation for every production change.
- Configuration management includes regular backups, baseline comparison, and per-device documentation.

In Part 2, we will cover acceptable use policies, service level agreements, disaster recovery documentation, and other policies that network administrators must understand and implement.
