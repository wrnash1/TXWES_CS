# Discussion Forum: Module 09 — DNS and DHCP Services in Windows Server

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

This week's discussion applies DNS and DHCP concepts to real-world design and
troubleshooting scenarios. Choose one scenario below, answer all three
sub-questions, and engage substantively with at least two classmates.

---

## Scenario A — DNS Design for a Multi-Site Organization

A regional university has two campuses: Main (192.168.10.0/24) and North
(192.168.20.0/24). Each campus has a domain controller running DNS. The domain
is `txwes.edu`. A partner organization uses the domain `partner.edu` and
maintains its own DNS server at `10.200.1.10`. The IT director wants all DNS
changes to replicate automatically without configuring zone transfers, and
wants stale records cleaned up automatically.

1. Describe the DNS zone configuration you would deploy on both domain
   controllers. Identify the zone type, dynamic update setting, and replication
   scope. Explain why AD-Integrated zones eliminate the need for manual zone
   transfer configuration between the two DCs.

2. Explain how you would configure DNS so that queries for `*.partner.edu`
   resolve correctly without exposing internal DNS records to the partner
   organization. Identify the specific DNS feature you would use, the PowerShell
   cmdlet to configure it, and the parameter that stores the configuration in
   Active Directory so both DCs receive it automatically.

3. After enabling DNS scavenging on both servers and both zones, the IT director
   reports that stale records are still present two weeks after decommissioning
   workstations. Describe the full scavenging timeline using default intervals,
   identify when records become eligible for deletion, and explain what condition
   could cause records to persist beyond the expected 21-day window.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Scenario B — DHCP Scope Planning and Failover

A community college is expanding its network. The main building uses subnet
192.168.10.0/24. Network printers and servers in the range .1–.50 are
statically assigned. Faculty workstations (.51–.99) are statically assigned.
The DHCP scope should serve student devices and guest devices only. There are
15 network printers in the student labs that must always receive the same IP
from DHCP. Two DHCP servers (DC1 and DC2) are available. During normal operation
both servers should handle lease requests, with the pool split equally.

1. Design the DHCP scope: define the start range, end range, exclusion ranges,
   and lease duration. Justify each decision. Identify which PowerShell cmdlets
   you would use to create the scope and configure the exclusion.

2. Explain how you would configure DHCP reservations for the 15 printers.
   Identify the information you need from each printer and the PowerShell cmdlet
   to create each reservation. Describe the difference between a reservation and
   an exclusion range, and explain why a reservation is the correct choice here
   rather than a static assignment with an exclusion.

3. Configure DHCP failover between DC1 and DC2 to meet the equal-load
   requirement. Identify the failover mode, the PowerShell cmdlet, and the
   key parameter that controls the address pool split. Explain what happens to
   client leases if one server becomes unavailable while using this mode.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Scenario C — DNS and DHCP Troubleshooting

A new technician is setting up a branch office for the first time. The branch
subnet is 192.168.30.0/24. A domain controller (BDC1) has been promoted and is
running DNS and DHCP. After completing setup, the technician reports three
problems: (1) Client computers receive APIPA addresses. (2) After manually
assigning an IP and DNS server, clients can ping `8.8.8.8` but cannot resolve
`google.com`. (3) After adding a standard forwarder, clients can resolve
external names but cannot log on to the domain; `Resolve-DnsName
_ldap._tcp.dc._msdcs.txwes.edu` returns no results.

1. Diagnose and resolve Problem 1. Identify the two most likely causes for
   APIPA addresses in a domain environment and the specific PowerShell cmdlets
   or commands you would run to check each cause.

2. Diagnose and resolve Problem 2. Explain why a client can reach an external
   IP address but cannot resolve external hostnames, and identify the missing
   configuration on BDC1.

3. Diagnose and resolve Problem 3. Explain what the missing SRV record means
   for Active Directory, identify the service responsible for registering it,
   and describe the steps you would take to force re-registration without
   restarting the domain controller.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

## Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario,
  answer all three sub-questions.

- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates;
  minimum 60 words each.

- In peer replies: evaluate the accuracy of their DNS or DHCP design or
  troubleshooting approach, and add one consideration or edge case they did
  not mention.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

## Professor Nash's Note

DNS and DHCP troubleshooting separates administrators who understand the
architecture from those who do not. Scenario C is based on a real-world
commissioning exercise. The three problems appear to be unrelated, but they
all trace back to setup steps performed out of order or skipped entirely.
Problem 3 is the most commonly missed: many administrators never check SRV
records because everything looks correct until someone tries to log on. If
you have never run `Resolve-DnsName -Name "_ldap._tcp.dc._msdcs.<domain>"
-Type SRV`, add it to your AD health-check routine now. For Scenario B, pay
close attention to the distinction between exclusion ranges and reservations —
the exam will test this difference, and the practical implication is significant
in real environments where IP conflicts cause hard-to-diagnose outages.
