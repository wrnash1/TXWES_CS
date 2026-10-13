# Discussion Forum: Module 09 — Access Control Lists (ACLs)

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Identify your chosen scenario (A, B, or C) at the top of your initial post. Your post must address all three sub-questions for the scenario you select.

Initial posts are due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: Hospital Network ACL Policy

A hospital network team is designing ACL policy for a new electronic health record (EHR) server at 10.50.1.100. The policy requirements are: (1) only the clinical workstations subnet (10.20.0.0/24) should reach the EHR server on port 443; (2) the billing subnet (10.30.0.0/24) should reach the EHR server on port 443 and port 80 only; (3) all administrative SSH access to network devices must be restricted to the IT management subnet (10.10.0.0/24).

### Sub-questions for Scenario A

1. The team decides to use a named extended ACL for the EHR server policy. Write the ACL entries that enforce requirements 1 and 2. Include a final entry to deny all other traffic to the EHR server. Explain why a standard ACL cannot implement this policy.

2. The IT manager wants to apply a single ACL to block all Telnet access to the EHR server from outside the clinical and billing subnets. Explain the correct placement decision: which router interface and which direction. Justify your answer using the extended ACL placement rule.

3. Describe the operational risk of misconfiguring entry order in the EHR ACL. Give a specific example where placing a broad permit before a specific deny would cause a security failure, and explain how named ACL sequence numbers help prevent this in production.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Scenario B: Branch Office ACL Troubleshooting

A branch network engineer receives a ticket: users on the sales floor (192.168.10.0/24) cannot reach the corporate file server at 172.16.5.20, but they can reach all other internal destinations. No other subnets are experiencing connectivity issues. The engineer runs `show access-lists` on the branch router and finds:

```text
Standard IP access list 15
    10 deny 192.168.10.0 0.0.0.255 (47 matches)
    20 permit any (0 matches)
```

The ACL is applied inbound on the Gi0/0 interface connected to the internet uplink.

### Sub-questions for Scenario B

1. Analyze the `show access-lists` output. The deny line has 47 matches but the complaint is only about access to one specific server, not all destinations. Identify the two problems in the current ACL design that explain this behavior. Be specific about ACL type and placement.

2. The ticket says users can reach all OTHER internal destinations, but the deny line has 47 matches. Explain how both conditions can be simultaneously true — what does the 47-match count tell you about what the ACL is actually blocking?

3. Write a corrected ACL configuration that blocks only access from the sales floor to the file server at 172.16.5.20 while permitting all other traffic. Identify the ACL type you chose, where you would apply it, and why.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Scenario C: ACL Verification and Security Audit

A security auditor reviews the running configuration of a production router and finds this ACL applied outbound on the WAN interface:

```text
ip access-list extended OUTBOUND_WAN
  10 permit ip 10.0.0.0 0.255.255.255 any
  20 permit ip 172.16.0.0 0.15.255.255 any
  30 permit ip 192.168.0.0 0.0.255.255 any
  40 deny ip any any log
```

The auditor flags this ACL as providing no security value and recommends its removal. The network engineer disagrees, arguing the ACL prevents IP address spoofing.

### Sub-questions for Scenario C

1. Evaluate the auditor's position. Does this ACL provide meaningful security value when applied outbound on the WAN interface? Explain what it does and does not protect against. Use the concept of egress filtering in your answer.

2. The engineer claims the ACL prevents IP spoofing. Explain what specific threat the ACL is mitigating and whether the outbound WAN placement is the correct location for this type of control. Compare outbound WAN placement versus inbound LAN placement for anti-spoofing ACLs.

3. The auditor is also concerned about the logging entry on line 40. Explain what `log` does to denied traffic and identify one operational benefit and one operational risk of enabling ACL logging on a high-traffic WAN interface.

Write an initial post of 175–225 words addressing all three sub-questions.

---

## Sample Peer Response

The following is an example of a substantive peer response that meets the minimum standard. Use it as a quality benchmark, not as a template to copy.

"You made a great point about the implicit deny in your Scenario B answer. I would add that the 47-match count on the deny line actually helps the troubleshooting process — it confirms the ACL is active and processing real traffic. If the count were zero, that would suggest the ACL might not be applied to the right interface or direction. One thing I would add to your corrected ACL: consider using a named extended ACL instead of a numbered one so the team can insert additional entries later without recreating the entire list. In a growing branch environment that flexibility matters."

---

## Discussion Rubric

| Component                       | Points | Criteria                                                                                    |
|---------------------------------|--------|---------------------------------------------------------------------------------------------|
| Initial Post — Technical Accuracy | 3    | All three sub-questions answered with correct ACL terminology and accurate concept application |
| Initial Post — Depth and Analysis | 2    | Responses analyze operational scenarios, evaluate design trade-offs, or diagnose failures     |
| Initial Post — Word Count         | 1    | Post falls within the 175–225 word range                                                      |
| Peer Response 1                   | 2    | Substantive reply (50+ words) that adds a technical detail, corrects an error, or extends the scenario analysis |
| Peer Response 2                   | 2    | Substantive reply (50+ words) meeting the same criteria as Peer Response 1                  |

---

## Professor Nash's Note

ACL placement is the single most misunderstood concept I see on CCNA practice exams and in real network audits. Students memorize the rule — standard close to destination, extended close to source — but many cannot explain why. The why is what sticks. Standard ACLs are blunt instruments: they only see source address. Put one near the source and you block that source from everywhere. Extended ACLs are precise: they see source, destination, protocol, and port. Put them near the source so you drop the unwanted traffic before it wastes bandwidth crossing the network. Once you understand the reasoning, the rule becomes self-evident. If you find yourself second-guessing placement on a question, ask yourself: what information does this ACL type have, and where does that make it most effective?
