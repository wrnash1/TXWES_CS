# Discussion Forum: Module 08 — Azure Networking

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 10 | Initial Post Due: Wednesday 11:59 PM | Peer Responses Due: Sunday 11:59 PM

---

## Instructions

Read all three scenarios below. Choose **one** scenario that interests you most and write your initial post responding to that scenario. Your initial post must be 175–225 words. Then respond to **two classmates** who chose different scenarios. Each peer response must be at least 75 words and add substantive insight beyond simple agreement.

---

## Scenario 1: Retail Company Hybrid Connectivity Decision

A mid-size retail company is expanding its e-commerce platform to Azure. Its primary data center is in Dallas, Texas, where it runs inventory management, order processing, and warehouse management software. The cloud team needs to connect the Dallas data center to Azure so that Azure-based applications can read and write to on-premises databases in real time. The connection must be reliable, secure, and capable of handling up to 2 Gbps of sustained data transfer during peak shopping seasons (Black Friday, Cyber Monday). The CTO is concerned about internet-routed traffic appearing on security audit logs and wants to avoid sending sensitive customer data over the public internet.

**Discussion Prompt:** Which hybrid connectivity option would you recommend — VPN Gateway or ExpressRoute — and which specific tier or SKU? What is the strongest argument for your recommendation? What are the cost and setup time tradeoffs your team would need to prepare the CTO for? If the budget was strictly limited to $500/month for connectivity, would your recommendation change?

---

## Scenario 2: Multi-Tier Application Network Design

A software team is deploying a three-tier web application to Azure: a public-facing web tier (nginx), a middle application tier (Node.js API), and a back-end database tier (PostgreSQL). The security architect requires that the database tier must be completely inaccessible from the public internet and must only accept connections from the application tier on port 5432. The web tier must accept HTTP (port 80) and HTTPS (port 443) from any internet source. The application tier must only accept traffic from the web tier.

**Discussion Prompt:** Design the subnet and NSG architecture for this three-tier application. How many subnets would you create? What NSG rules would you define for each subnet — be specific about priority, direction, source, destination, port, and action for at least four rules. Would you also deploy an Azure Application Gateway in front of the web tier? Why or why not?

---

## Scenario 3: Web Application Firewall Evaluation

A healthcare organization is moving its patient portal to Azure. The portal is a web application that handles PHI (protected health information) and must comply with HIPAA security requirements. The security team has identified that previous versions of the portal were vulnerable to SQL injection attacks in its login form and a reflected XSS vulnerability in its search feature. The team is evaluating whether to use Azure Application Gateway with WAF or to implement all security controls at the application code level only, arguing that WAF adds cost and complexity without guaranteed protection.

**Discussion Prompt:** Do you agree or disagree with the security team's argument against WAF? What specific OWASP Top 10 protections does Azure Application Gateway WAF provide that are relevant to the SQL injection and XSS vulnerabilities described? Is a WAF a replacement for secure coding practices, or a complement to them? How does HIPAA compliance factor into this decision? Reference at least one specific WAF rule set or feature in your response.

---

## Peer Response Guidelines

When responding to a classmate:

- Reference a specific Azure networking feature, SKU, or SLA that supports or challenges their recommendation
- Add at least one consideration they did not address — cost, latency, compliance, failover, or operational complexity
- If you would make a different architectural decision, explain it constructively with specific reasoning
- Responses that simply restate the original post or say "I agree" will not earn full credit

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post demonstrates clear understanding of the scenario and relevant Azure networking services | 4 |
| Initial post references specific Azure features, SKUs, SLA figures, or technical details | 2 |
| Peer response 1: substantive, adds new insight, 75+ words | 2 |
| Peer response 2: substantive, adds new insight, 75+ words | 2 |
| **Total** | **10** |

---

## Professor Nash Note

Networking is where cloud architecture theory meets real-world trade-offs. The scenarios in this forum reflect decisions that cloud architects, network engineers, and security teams debate every day. Notice that each scenario involves competing constraints: cost vs. security, simplicity vs. control, speed to deploy vs. long-term maintainability. There is no single correct answer — but there are well-reasoned answers supported by evidence and poorly-reasoned answers that ignore constraints. I am looking for the former. When you respond to your classmates, challenge them to sharpen their reasoning with specific technical details, not just agreement.

---

*Discussion 08 — Module 08: Azure Networking | CIS-4331 | Texas Wesleyan University*
