# Discussion Forum: Module 11 — DHCP and DNS Configuration

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Multi-Site DHCP Architecture

A university campus has three buildings: Admin, Science, and Dormitory. Each building has its own subnet (10.10.0.0/24, 10.20.0.0/24, 10.30.0.0/24). A central DHCP server at 172.16.0.10 serves all three subnets. The IT team is deciding whether to configure one large DHCP pool or three separate pools.

### Sub-questions for Scenario A

1. Explain why three separate DHCP pools are required rather than one pool that covers all three subnets. Describe specifically how the `giaddr` field in a relayed DHCP packet enables the server to select the correct pool when requests from different subnets arrive at the same server.

2. The Dormitory building's gateway router is configured with `ip helper-address 172.16.0.10` on its LAN interface, but dormitory students are not receiving IP addresses. List three possible root causes in priority order and identify which IOS command you would run first to begin isolating the failure.

3. The IT director proposes enabling DHCP snooping on all access layer switches in the dormitory to prevent students from running unauthorized DHCP servers from their personal devices. Explain which ports must be configured as trusted and which must remain untrusted. Describe the specific attack that DHCP snooping prevents and how the attack would affect dormitory students if snooping were not deployed.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Scenario B: DHCP and DNS Integration Failure

A network engineer at a logistics company receives tickets from users in two different offices. Office A users (192.168.10.0/24) report that they receive IP addresses correctly but cannot resolve internal hostnames like `apps.logistics.local`. Office B users (192.168.20.0/24) report they cannot get IP addresses at all.

The engineer checks the central DHCP server configuration and finds:

```text
ip dhcp excluded-address 192.168.10.1 192.168.10.10
ip dhcp pool OFFICE_A
  network 192.168.10.0 255.255.255.0
  default-router 192.168.10.1
  lease 1
ip dhcp pool OFFICE_B
  network 192.168.20.0 255.255.255.0
  default-router 192.168.20.1
  dns-server 192.168.100.53
  domain-name logistics.local
  lease 1
```

### Sub-questions for Scenario B

1. Identify the specific configuration error in OFFICE_A's pool that explains why Office A users cannot resolve `apps.logistics.local`. Write the corrected pool configuration. Explain what the `domain-name` parameter tells the client's operating system to do with unqualified hostnames.

2. Office B users cannot get IP addresses at all. The pool appears correctly configured. Describe three possible relay agent issues that could prevent DHCP Discover messages from reaching the server, and explain how `debug ip dhcp server events` on the server would help isolate which layer the failure is occurring at.

3. After fixing both issues, users in both offices can now resolve `apps.logistics.local` when querying the internal DNS server at 192.168.100.53. However, users report they cannot reach external internet sites by name. Explain what additional DNS configuration is required on the internal DNS server at 192.168.100.53 to enable external name resolution for internal clients.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Scenario C: Split-Horizon DNS Design

A healthcare company hosts an internal application server (`ehr.healthcorp.com`) that is accessible both internally (private IP 10.50.1.80) and externally (public IP 203.0.113.80 via static NAT). Internal clinicians access the server by name daily. External auditors access it from the internet.

The network team is evaluating whether to deploy split-horizon DNS.

### Sub-questions for Scenario C

1. Describe the specific problem that occurs when internal clinicians query the public DNS server for `ehr.healthcorp.com` and receive 203.0.113.80 as the answer. Include what happens to the clinician's traffic at the firewall and explain why this path may fail or be suboptimal without hairpin NAT.

2. Explain how split-horizon DNS resolves the problem described in sub-question 1. Describe the two DNS zone configurations required — one for internal clients and one for external clients — and identify which DNS server each client type queries.

3. A network administrator argues that split-horizon DNS creates a security risk because internal IP addresses (10.50.1.80) are exposed in the internal DNS zone and could assist an attacker who gains access to the internal network. Evaluate this argument: does split-horizon DNS meaningfully increase the attack surface for an internal threat actor who already has network access? What compensating controls make the internal DNS zone safer?

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Sample Peer Response

The following is an example of a substantive peer response that meets the minimum standard.

"Your answer on split-horizon DNS was clear. I want to add a detail about the DHCP role in making it work: the `dns-server` and `domain-name` parameters in the DHCP pool are what steer internal clients toward the internal DNS server. If those parameters are misconfigured — wrong DNS server IP or wrong domain — clients might send DNS queries to a public resolver even when an internal resolver exists. That is why DHCP pool configuration and DNS infrastructure design have to be planned together. A correct split-horizon DNS deployment breaks if the DHCP pool sends clients to the wrong DNS server."

---

## Discussion Rubric

| Component                         | Points | Criteria                                                                                      |
|-----------------------------------|--------|-----------------------------------------------------------------------------------------------|
| Initial Post — Technical Accuracy | 3      | All three sub-questions answered with correct DHCP/DNS terminology and accurate concepts       |
| Initial Post — Depth and Analysis | 2      | Responses analyze operational scenarios, evaluate design trade-offs, or diagnose failures      |
| Initial Post — Word Count         | 1      | Post falls within the 175–225 word range                                                      |
| Peer Response 1                   | 2      | Substantive reply (50+ words) that adds a technical detail, corrects an error, or extends the scenario analysis |
| Peer Response 2                   | 2      | Substantive reply (50+ words) meeting the same criteria as Peer Response 1                    |

---

## Professor Nash's Note

DHCP is one of those services that engineers often configure once and forget — until it breaks. The two failure patterns I see most in real environments are the missing `ip helper-address` and the pool that works for six months and then suddenly stops assigning addresses because the excluded range was set wrong and the available space is exhausted. Both are entirely preventable with careful initial configuration and periodic verification using `show ip dhcp pool`. For the exam, the relay agent placement question is almost guaranteed to appear. Remember: the helper-address goes on the interface that receives the broadcast from the client side — the gateway facing the subnet, not the server-facing uplink. Get that placement right and half the DHCP troubleshooting questions answer themselves.
