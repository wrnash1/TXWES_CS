# Discussion Forum: Module 10 — AWS Networking and VPC Design

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Choose ONE of the three scenarios below. Write an initial post of 175–225 words responding to the scenario. Then write a substantive reply (75–100 words) to at least one classmate who chose a different scenario. Use specific AWS service names and feature names in your response.

---

## Scenario A — The Security Breach Investigation

A company's security team receives an alert that an EC2 instance in their production VPC made outbound connections to a known malicious IP address at 3:00 AM. The VPC has no centralized logging configured. The security team needs to determine: what IP addresses the instance communicated with, on what ports, and whether the connections were accepted or rejected by network controls.

Describe the AWS feature that should have been enabled to provide this visibility. Explain what information it captures and where it can be published for analysis. Describe the specific information in a flow log record that would allow the security team to answer their questions. Then explain how the team would use this information going forward to prevent recurrence — specifically which network control (Security Group or NACL) could block future outbound connections to specific malicious IPs, and why the other control cannot accomplish this.

---

## Scenario B — The VPC Connectivity Redesign

A company currently has 8 AWS VPCs connected via VPC Peering. Each VPC is peered with every other VPC. They are about to add 4 more VPCs, and the networking team is dreading the route table management and new peering connections required. A cloud architect proposes replacing the entire mesh with AWS Transit Gateway.

Calculate the total number of existing peering connections (for 8 VPCs in a full mesh) and the number that would be required after adding 4 more VPCs (for 12 VPCs). Then explain how Transit Gateway eliminates this scaling problem, describing the hub-and-spoke model and how TGW route tables can enforce routing restrictions between VPCs. Address one trade-off of the Transit Gateway approach versus keeping VPC Peering for smaller deployments.

---

## Scenario C — The Route 53 Architecture Decision

A fintech company is planning their global DNS and routing strategy for a new payments application. They have three requirements: (1) users in Europe should be served by their eu-west-1 infrastructure due to GDPR data residency rules, (2) users everywhere else should be served by the lowest-latency region between us-east-1 and ap-southeast-1, and (3) if the primary endpoint for any region fails, traffic should automatically fail over to a backup endpoint in the same region.

Design the Route 53 routing strategy that meets all three requirements. Describe which routing policies you would use and how they would be layered or combined to satisfy all three requirements simultaneously. Explain what health check configuration is required and what happens when an endpoint fails.

---

## Peer Response Instructions

After posting your initial response, read your classmates' posts and reply to at least one person who chose a different scenario than you. Your reply should:

- Identify one point in their response you agree with and explain why
- Identify one consideration they may have missed or could strengthen
- Ask a follow-up question that extends the discussion

---

## 10-Point Grading Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical Accuracy | 3 | AWS service names, features, and routing behaviors described correctly |
| Depth of Analysis | 2 | Response addresses the specific scenario rather than providing generic networking advice |
| Word Count (Initial) | 1 | Initial post is between 175 and 225 words |
| Use of Module Concepts | 2 | Response explicitly references concepts from Module 10 video and reading guide |
| Peer Reply Quality | 2 | Reply is substantive (75–100 words), identifies a specific point, and asks a meaningful follow-up question |
| **Total** | **10** | |

---

**Professor Nash Note:** Scenario C is the one that most directly prepares you for the SAA-C03 routing policy questions. The exam often combines multiple routing requirements in a single scenario, and students who memorize routing policies in isolation struggle to compose them. The key insight is that Route 53 routing policies can be layered — you can use records with different policies in combination to achieve complex behavior. Think carefully about which requirement is best handled by which policy type and whether they can coexist in the same hosted zone.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
