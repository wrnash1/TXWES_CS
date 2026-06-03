# Discussion Forum: Module 07 — Amazon EC2 and Auto Scaling

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

**Instructions:** Choose ONE of the three scenarios below. Write an initial post of 175–225 words responding to the scenario. Then write a substantive reply (75–100 words) to at least one classmate who chose a different scenario. Use specific AWS service names and feature names in your response.

---

## Scenario A — The Pricing Model Dilemma

A regional healthcare analytics company currently runs 50 EC2 M6i.xlarge instances 24 hours a day, 7 days a week, processing patient data. They pay On-Demand pricing. The CTO asks the architecture team to reduce compute costs without changing the workload. A junior engineer suggests switching everything to Spot Instances because "they're 90% cheaper." A senior engineer disagrees and recommends Compute Savings Plans instead.

Explain who is right and why. In your response, address whether Spot Instances are appropriate for this workload and what the actual risk would be if the company followed the junior engineer's advice. Describe the correct pricing strategy in detail, including whether you would recommend Savings Plans, Reserved Instances, or a combination, and explain your reasoning. Consider whether any portion of the workload could reasonably use Spot Instances.

---

## Scenario B — The Auto Scaling Incident

A social media startup launched a new feature last Tuesday. Within 30 minutes of launch, the application became unresponsive. Investigation showed that the Auto Scaling group had launched many new instances in response to CPU alarms, but the new instances were immediately marked unhealthy by the load balancer and terminated before they could serve traffic. The cycle repeated continuously, consuming budget and providing no relief.

Diagnose the root cause of this Auto Scaling failure. Explain what configuration was likely missing or incorrect that caused new instances to be marked unhealthy immediately. Describe at least two configuration changes that would prevent this scenario in the future, referencing specific Auto Scaling and EC2 features. Also explain how lifecycle hooks could have helped detect the problem earlier in the deployment process.

---

## Scenario C — Placement Group Trade-offs

A financial trading firm is deploying a new algorithmic trading system on AWS EC2. The system has two tiers: a market data processing tier (8 instances that exchange data at extremely high frequency with microsecond latency requirements) and a risk management tier (3 instances, each running independently — if one fails the others must continue operating without interruption). Both tiers are in us-east-1.

Design the placement group strategy for each tier and justify your choices. Explain the trade-offs you are accepting with each choice. For the market data tier, address what happens to the entire tier if the underlying hardware fails. For the risk management tier, explain how your choice guarantees fault isolation. Would you put both tiers in the same placement group? Why or why not?

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
| Technical Accuracy | 3 | AWS service names, feature names, and behavior described correctly |
| Depth of Analysis | 2 | Response goes beyond surface-level description to explain trade-offs and reasoning |
| Word Count (Initial) | 1 | Initial post is between 175 and 225 words |
| Use of Module Concepts | 2 | Response explicitly references concepts from Module 07 video and reading guide |
| Peer Reply Quality | 2 | Reply is substantive (75–100 words), identifies a specific point of agreement, and asks a meaningful follow-up question |
| **Total** | **10** | |

---

**Professor Nash Note:** The pricing model question (Scenario A) is one of the most common mistakes I see from candidates on the actual SAA-C03 exam. Many people see "90% discount" and immediately think Spot is always the answer. Understanding when Spot is and is not appropriate — and being able to articulate the difference between Savings Plans and Reserved Instances — is something you will absolutely need on exam day and in your career. Push yourself to be specific in your response: name the pricing model, the discount percentage range, and the specific risk you are managing.

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*
