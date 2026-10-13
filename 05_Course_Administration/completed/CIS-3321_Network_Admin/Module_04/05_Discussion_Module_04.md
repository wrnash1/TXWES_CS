# Discussion Forum: Module 04 – IPv6 Addressing and Transition Technologies
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion connects IPv6 addressing and transition technology concepts to real-world network engineering decisions. You will choose one of three scenarios below and respond with a substantive initial post of 175–225 words. After posting, respond to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: IPv6 Rollout Planning at a University

The IT department at a mid-sized university is planning to enable IPv6 across the campus network. Currently, all 15,000 devices use IPv4 with DHCP. The network team is debating between three approaches: configuring SLAAC on all subnets, deploying stateful DHCPv6, or using a combination of SLAAC with stateless DHCPv6 for DNS configuration.

Respond to all three questions:

1. Compare SLAAC and stateful DHCPv6 in the context of a university campus with 15,000 devices. What are the operational advantages and limitations of each approach for an institution that needs to track which device has which address (e.g., for security investigations)?
2. What is stateless DHCPv6, and why might the university choose to use it alongside SLAAC rather than deploying full stateful DHCPv6? What specific configuration information does stateless DHCPv6 provide that SLAAC cannot provide by default?
3. The network engineer recommends dual stack as the transition strategy rather than going IPv6-only immediately. Explain why dual stack is considered the most practical transition strategy and describe one scenario where the university would still rely on IPv4 even after dual stack is deployed.

---

#### Scenario B: IPv6 Address Type Identification and Security

A security analyst at a financial services company is reviewing firewall rules for the company's IPv6 deployment. She has a list of source IPv6 addresses from a network log and needs to categorize each one to determine the appropriate security treatment. She also notices that some hosts appear to be generating multiple IPv6 addresses on the same interface, which she does not understand.

Respond to all three questions:

1. The analyst sees the following source addresses in the log. Identify the address type for each and explain whether traffic from that address type should be permitted to cross a routed firewall to the internet: fe80::1a2b:3c00:1, 2001:db8:1234::50, fd00:a:b:c::1, ff02::1. Include the prefix that identifies each type.
2. Explain why hosts may have multiple IPv6 addresses on the same interface. What is the difference between a link-local address and a global unicast address, and why does the operating system generate both?
3. Some modern operating systems use IPv6 privacy extensions (RFC 4941) instead of EUI-64 to generate temporary interface identifiers. Explain why privacy extensions were developed and what security or privacy concern they address compared to EUI-64-derived addresses.

---

#### Scenario C: Troubleshooting an IPv6-Only Network Connectivity Issue

A network engineer at a service provider is deploying a new IPv6-only network segment for IoT devices. After configuration, the IoT devices can communicate with each other on the local segment but cannot reach the company's IPv4-only backend server infrastructure. The engineer's initial test shows that pinging an IPv4 address from an IoT device times out, but pinging another IoT device's link-local address succeeds.

Respond to all three questions:

1. Based on the test results, diagnose the connectivity problem. The IoT devices can communicate locally but cannot reach IPv4 servers. Which specific transition technology should the engineer implement at the network border, and how does it work?
2. The engineer also notices that the IoT devices have link-local addresses but no global unicast addresses. What must be configured on the router to enable the devices to receive global unicast addresses via SLAAC? What specific router message carries the network prefix to the devices?
3. NDP performs address resolution on the IPv6 segment. Explain how NDP's Duplicate Address Detection (DAD) process works, and describe what would happen if two IoT devices on the same segment were accidentally configured with the same IPv6 address. Which NDP process would detect this, and what would happen to the device that detected the conflict?

---

### Response Requirements

**Initial Post (due Wednesday at 11:59 PM):**

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct IPv6 terminology (prefix notation, address type names, protocol names)

**Peer Responses (due Sunday at 11:59 PM):**

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Offer a specific technical addition, correction, or alternative perspective

---

### Grading Rubric (10 Points Total)

**Initial Post — 6 Points:**

- 5–6 points: All three sub-questions answered with accurate IPv6 address type identification, correct prefix notation, appropriate terminology, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but contains a prefix error or lacks technical depth.
- 1–2 points: Post is incomplete, off-topic, or contains significant IPv6 inaccuracies.
- 0 points: No initial post submitted.

**Peer Responses — 4 Points:**

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding technical value.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

IPv6 is not something that will arrive someday — it is here now, running on most operating systems alongside IPv4 whether you have configured it or not. The scenarios this week reflect the kinds of decisions network engineers are making right now in enterprise environments. The transition from IPv4 to IPv6 is not a single event; it is a multi-year process that requires careful planning, and the choices between SLAAC, DHCPv6, dual stack, and NAT64 are made based on the specific requirements of the organization. Understanding these trade-offs is a core competency for any network administrator, and it is tested directly on the Network+ exam.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
