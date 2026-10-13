# Discussion Forum: Module 05 - VPC: Subnets, Route Tables, Security Groups, NACLs

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Instructions

Read all three scenarios below and select one to address in your initial post. Your initial post must be 175-225 words, technically precise, and reference specific VPC components, routing, or security controls from this module. Respond to at least two classmates who chose different scenarios from yours.

Initial post due: Wednesday at 11:59 PM
Peer responses due: Sunday at 11:59 PM

---

## Scenario A - Connectivity Troubleshooting

A developer reports that their EC2 instance in a private subnet cannot connect to the internet to download software updates. They confirm the instance is running and the security group allows all outbound traffic. You review the VPC configuration and find: the private subnet route table has a route `0.0.0.0/0` pointing to an Internet Gateway; the instance has no public IP address; no NAT Gateway exists in the VPC. Identify every configuration error contributing to the connectivity failure, explain specifically what each error means for network behavior, and describe the corrected architecture. Your response should identify at least three distinct issues and explain the correct role of each routing component involved.

---

## Scenario B - Security Group vs. NACL Decision

A security engineer at a healthcare company receives a threat intelligence feed indicating that a specific IP range (198.51.100.0/22) has been identified as a source of credential stuffing attacks. The company wants to block all traffic from this range from reaching their web application servers immediately. Separately, the company wants to ensure that only the Application Load Balancer can send traffic to the EC2 web servers — no other sources should be able to reach the servers directly even if they have the server's private IP address. Explain which security control (Security Group, NACL, or both) you would use for each requirement, why the other control is insufficient for that requirement, and what specific rule or rules you would configure in each case.

---

## Scenario C - Multi-VPC Architecture Decision

A company currently operates three VPCs: a Production VPC running customer-facing applications, a Development VPC for engineering, and a Shared Services VPC running internal tools (Active Directory, monitoring, CI/CD). The Operations team manually configured VPC peering between Production-Shared and Development-Shared. Now engineering wants Production and Development to be able to share test data. The network team proposes adding a Production-Development peering connection. The CTO asks: "If we keep growing and add a Staging VPC and a Data VPC, is peering still the right long-term approach?" Evaluate the peering proposal for the immediate need. Then address the CTO's question directly: at what scale does peering become unmanageable, what problem does it hit that peering cannot solve, and what architecture would you recommend for the five-VPC state and beyond?

---

## Discussion Rubric

| Criteria | Points | Description |
|---|---|---|
| Initial post — technical accuracy | 3 | Correctly identifies VPC components, routing behavior, or security control capabilities; no factual errors |
| Initial post — depth and completeness | 2 | Addresses all parts of the chosen scenario; 175-225 words; uses specific AWS service names and configuration details |
| Initial post — clarity | 1 | Well-organized, professional tone, correct AWS networking terminology |
| Peer response 1 — substantive engagement | 2 | Adds an alternative approach, identifies a missed issue, or extends the scenario; minimum 50 words |
| Peer response 2 — substantive engagement | 2 | Adds an alternative approach, identifies a missed issue, or extends the scenario; minimum 50 words |
| **Total** | **10** | |

---

## Professor Nash Note

Scenario A requires you to know the exact three-component requirement for internet connectivity and identify which one is wrong for each issue. Scenario B requires you to know the rule types each control supports — a response that uses the wrong control for either requirement will not earn full credit. Scenario C should demonstrate that you understand not just when peering works, but when it fundamentally cannot work due to transitivity — that distinction is what the CTO needs to hear.
