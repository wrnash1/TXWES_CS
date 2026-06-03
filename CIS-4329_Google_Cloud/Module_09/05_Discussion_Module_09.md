# Discussion: Module 09 — Cloud Load Balancing and CDN

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This discussion asks you to apply the load balancer selection framework from Module 09
to an architecture design scenario. You will practice choosing the right GCP load balancer
and justify your design decisions — the same reasoning pattern used on the ACE exam.

**Initial post due**: Thursday at 11:59 PM Central

**Peer responses due**: Sunday at 11:59 PM Central

---

### Scenario

A company called ShipTrack is launching a logistics platform on GCP. The platform has
four components that all need load balancing:

**Component 1 — Public Website**: A global e-commerce website served to customers
worldwide. It uses HTTPS, needs the lowest possible latency for international users, and
serves many static assets (images, CSS, JavaScript) that rarely change. High-profile
launch means DDoS protection is required from day one.

**Component 2 — Internal Order Processing API**: A REST API that only internal backend
services call within the company's GCP VPC. It uses HTTP and needs to route traffic to
different backend services based on the URL path (`/orders/*` vs. `/inventory/*`). No
public internet access should ever be possible.

**Component 3 — Custom Game Server (UDP)**: An internal team runs a corporate gaming
competition on a UDP-based game server hosted on GCP VMs. Participants connect from the
office network. The game requires preserving the source IP address so the server can
track player sessions.

**Component 4 — Partner API Gateway (TCP/SSL)**: A B2B integration point for logistics
partners. It accepts raw TLS connections (not HTTP) on port 8443 and requires global
distribution to serve partners across North America and Europe.

---

### Response Requirements

#### Part 1: Load Balancer Selection

For each component, identify the correct GCP load balancer type. For each answer,
provide a 2–3 sentence justification that references the specific technical requirements
(protocol, scope, routing capability, IP preservation, or public/internal access) that
drove your decision.

#### Part 2: CDN and Armor Integration

For Component 1, describe how you would integrate Cloud CDN and Cloud Armor into the
architecture. In 3–4 sentences explain which specific CDN cache mode you would choose
and why, and what type of Cloud Armor rules you would configure for DDoS protection at
launch.

#### Part 3: Reflection

Identify one load balancer choice in this scenario that you found non-obvious or
surprising. Explain in 2–3 sentences what initially confused you and how you reasoned
through to the correct answer.

---

### Grading Criteria

| Criterion | Points |
|---|---|
| Part 1: Correct LB type for all 4 components with valid justification | 50 |
| Part 2: CDN and Armor integration for Component 1 | 25 |
| Part 3: Reflection on non-obvious choice | 10 |
| Peer response 1: Substantive technical engagement | 7 |
| Peer response 2: Substantive technical engagement | 8 |
| **Total** | **100** |

---

### Peer Response Guidelines

A substantive peer response does at least one of the following:

- Challenges a load balancer choice with a specific technical counter-argument
- Points out a technical requirement in the scenario that the original poster missed
- Suggests an additional configuration detail (e.g., health check settings, SSL cert
  type, Cloud Armor rule priority) that improves the design
- Asks a clarifying question about how a specific component would fail over

Responses limited to agreement without technical content will not receive full credit.

---

### Discussion Hints

The load balancer selection table from the Reading Guide is your primary reference. As
you read each component description, isolate these four questions:

- Is traffic public (internet-facing) or internal (VPC-only)?
- What protocol — HTTP/HTTPS, TCP, UDP, or raw TLS?
- Is global scope needed, or is regional acceptable?
- Does the backend need to see the original client IP address?

Each component in this scenario has a unique combination that maps to a distinct GCP load
balancer type. There are no duplicates — each component uses a different load balancer.
