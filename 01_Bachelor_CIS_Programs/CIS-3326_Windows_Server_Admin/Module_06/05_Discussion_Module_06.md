# Discussion Forum: Module 06 - DNS and DHCP Server Roles

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion applies DNS and DHCP concepts to real-world enterprise design and troubleshooting scenarios. Choose one scenario below, answer all three sub-questions, and engage substantively with at least two classmates.

---

### Scenario A — DNS Zone Design for a Multi-Site Organization

A manufacturing company operates two Active Directory forests: `corp.local` for corporate users and `plant.local` for the production floor network. The two forests have a two-way forest trust. Users in `corp.local` frequently access a shared resource hosted in `plant.local`, but name resolution for `plant.local` hostnames fails when queried from the `corp.local` DNS servers.

1. Explain which DNS feature resolves this cross-forest name resolution failure and describe exactly how it is configured on the `corp.local` DNS servers. What information about the `plant.local` DNS infrastructure is required before you can complete this configuration?

2. The company also wants all `corp.local` workstations to be able to resolve internet hostnames (e.g., `microsoft.com`) without the internal DNS servers needing to query internet root servers directly. What DNS feature provides this, where should it point, and why is this better than relying on Root Hints in a corporate environment?

3. A junior administrator enables "Nonsecure and Secure" dynamic updates on the `corp.local` forward lookup zone to simplify registration for a new batch of contractor laptops. What specific security risk does this create, and what is the correct configuration change to restore secure registration while still allowing contractors to register records?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario B — DHCP Scope Design and Failover Planning

A retail company has a single building with 300 client workstations on the `10.10.20.0/24` subnet. The IT manager asks you to design the DHCP infrastructure. The current setup uses a single DHCP server with no failover. Two incidents last year caused IP address outages of several hours each when that server was taken offline for maintenance.

1. Design the address pool for the `10.10.20.0/24` scope. The building has 12 network printers, 4 IP phones, and 6 APs — all of which need consistent addressing. Explain which DHCP feature you would use for each device category (reservation vs. exclusion) and justify the choice based on how each feature works.

2. The IT manager wants to eliminate the single point of failure. Compare the DHCP Failover Hot Standby and Load Balance modes. Which mode is appropriate for this scenario given a 300-client workload, and what are the specific advantages over the old "split scope" approach?

3. After configuring DHCP Failover, the administrator notices that clients occasionally receive addresses from the old scope range after the failover configuration is applied. Walk through the two most likely causes and the PowerShell commands used to verify each one.

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario C — DHCP and DNS Troubleshooting

A domain administrator reports that after promoting a second Domain Controller (DC2) and installing the DHCP role on it, clients on the `192.168.50.0/24` subnet are receiving APIPA addresses (`169.254.x.x`). The existing DHCP server on DC1 is also still running and its scope is active. Additionally, several workstations that recently changed subnets still resolve to their old IP addresses in DNS.

1. Identify the two most likely causes of APIPA addresses in this scenario — one related to DHCP authorization and one related to potential scope configuration — and describe the PowerShell command that would diagnose each cause.

2. The DNS stale record issue is occurring on an AD-integrated zone with dynamic updates set to Secure Only. Explain how DNS aging and scavenging should be configured to prevent this problem, including the two interval values and their purpose. What happens if aging is enabled on the server but not on the zone (or vice versa)?

3. A junior administrator wants to verify that clients on `192.168.50.0/24` are receiving the correct default gateway and DNS server addresses from DHCP. Without accessing the clients directly, which PowerShell command on DC2 would show what scope options are being delivered, and what would a missing Option 003 cause for client connectivity?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario, answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates; minimum 60 words each
- In peer replies: evaluate the accuracy of their DNS or DHCP design decision, and add one consideration they did not mention

---

### Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

### Professor Nash's Note

DNS and DHCP feel straightforward until you have to troubleshoot them under pressure at 2 AM because nobody can log in or reach the internet. The two most common real-world DNS mistakes I have seen are: one, forgetting that DNS TTL caching means clients hold stale records even after a correct update is made, and two, confusing Conditional Forwarders with regular Forwarders in a multi-forest environment. For DHCP, the mistake I see most often is installing a DHCP server on a new domain server and forgetting to authorize it in AD — then spending an hour wondering why clients are getting APIPA addresses. Scenario C is based directly on a support call I fielded early in my career. Looking forward to your analysis.
