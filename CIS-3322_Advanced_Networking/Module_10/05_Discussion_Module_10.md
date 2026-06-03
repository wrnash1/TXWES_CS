# Discussion Forum: Module 10 — NAT and PAT

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Small Business NAT Design

A small business has 80 workstations, 3 internal servers (web, mail, and file), and one public IP address assigned by their ISP: 198.51.100.25. The network administrator must design a NAT strategy that allows all workstations to reach the internet and allows external clients to reach the web server and mail server from the internet.

### Sub-questions for Scenario A

1. Identify which NAT type should be used for each of the three servers and explain why. For the web and mail servers, describe the specific configuration command pattern needed on the edge router and explain what the bidirectional nature of static NAT enables that PAT cannot.

2. The administrator proposes using PAT with the single public IP for all 80 workstations. A colleague argues this will not work because only 65,535 ports exist and 80 users will exceed that limit. Evaluate this argument. Explain how PAT actually tracks sessions and why the colleague's concern is or is not valid for this deployment scale.

3. The file server handles only internal traffic and does not need internet access. Should the administrator include the file server's subnet in the PAT ACL? Explain the security implications of including versus excluding internal servers that do not require outbound internet access in the NAT translation pool.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Scenario B: NAT Translation Table Interpretation

A network engineer is troubleshooting internet connectivity complaints at a branch office. The engineer runs `show ip nat translations` and captures the following output:

```text
Pro  Inside global        Inside local         Outside local    Outside global
tcp  198.51.100.1:1024    10.10.5.20:54321     208.67.222.222:53  208.67.222.222:53
tcp  198.51.100.1:1025    10.10.5.21:60112     208.67.222.222:53  208.67.222.222:53
tcp  198.51.100.1:1026    10.10.5.22:44891     172.217.11.46:443  172.217.11.46:443
---  198.51.100.5         10.10.5.100          ---              ---
```

Some users report they cannot browse websites while others can. The engineer also notices the hit counter on the PAT ACL has stopped incrementing for affected users.

### Sub-questions for Scenario B

1. Analyze the translation table output. Identify the NAT type in use, describe what the `---` entry in the last row indicates, and identify the inside local addresses of the three PAT-translated hosts. Explain what the port numbers in the inside global column represent.

2. The affected users' traffic is not creating new entries in the translation table even though the ACL hit counter shows zero new matches. Based on this information, identify the two most likely causes of the failure. Describe specifically what show command output you would examine to confirm each cause.

3. The branch router's outside interface gets its IP address from the ISP via DHCP. The current PAT configuration uses a named pool with a hardcoded IP address. Explain why this creates a potential problem and describe the configuration change that would make the PAT configuration resilient to ISP-assigned IP address changes.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Scenario C: NAT and IPv6 Transition Planning

An enterprise network architect is planning a multi-year IPv6 migration strategy. The current network is IPv4-only with PAT providing internet access for 2,000 internal hosts. The architect must decide how to handle connectivity during the transition period when some internal segments are IPv6 and some remain IPv4.

### Sub-questions for Scenario C

1. The architect proposes deploying NAT64 for the IPv6-only segments during the transition. Explain the specific problem NAT64 solves in this scenario and identify what additional companion technology is needed to support DNS resolution for IPv6 hosts attempting to reach IPv4-only internet destinations. Describe what that companion technology does.

2. Dual-stack deployment (running both IPv4 and IPv6 simultaneously on all devices) is an alternative to NAT64. Identify one operational advantage of dual-stack over NAT64 for this enterprise and one scenario where NAT64 would be preferred over dual-stack during the transition.

3. The architect is concerned that continuing to rely on PAT during the IPv6 migration undermines the long-term goal of end-to-end IPv6 connectivity. Explain the fundamental difference in network addressing philosophy between the IPv4-plus-NAT model and the native IPv6 model. In your answer, address why IPv6 was designed to eliminate the need for NAT in the first place.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Sample Peer Response

The following is an example of a substantive peer response that meets the minimum standard.

"Your point about static NAT being bidirectional is exactly right, and I want to add one nuance: static NAT does not just translate outbound traffic — it also lets the NAT router accept inbound connections from the internet and forward them to the internal server. This is why static NAT is essential for any publicly accessible service. PAT cannot do this because PAT entries are only created when the inside host initiates the connection. If an external client tries to connect to a PAT-translated address with no active session, the router has no entry in the table and drops the packet. That is why web servers need static NAT, not PAT."

---

## Discussion Rubric

| Component                         | Points | Criteria                                                                                    |
|-----------------------------------|--------|---------------------------------------------------------------------------------------------|
| Initial Post — Technical Accuracy | 3      | All three sub-questions answered with correct NAT/PAT terminology and accurate concept application |
| Initial Post — Depth and Analysis | 2      | Responses analyze operational scenarios, evaluate design trade-offs, or diagnose failures    |
| Initial Post — Word Count         | 1      | Post falls within the 175–225 word range                                                    |
| Peer Response 1                   | 2      | Substantive reply (50+ words) that adds a technical detail, corrects an error, or extends the scenario analysis |
| Peer Response 2                   | 2      | Substantive reply (50+ words) meeting the same criteria as Peer Response 1                  |

---

## Professor Nash's Note

The question I hear most often about NAT is: "Why does it matter if IPv6 eliminates it?" It matters because the world is still running IPv4, and you will configure PAT on your first job, your second job, and probably your tenth. NAT also appears in AWS VPCs, Azure virtual networks, and nearly every cloud architecture — the addresses and platforms change but the translation concepts are identical. Understanding how the inside global, inside local, outside local, and outside global relate to each other makes you able to read any NAT translation table on any platform. That fluency is what the CCNA is testing. Learn the four address types until they are automatic.
