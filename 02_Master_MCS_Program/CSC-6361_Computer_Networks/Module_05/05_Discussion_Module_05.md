# Discussion Board: Module 05 – QoS, High Availability & Network Automation
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, November 22, 2026 at 11:59 PM CST

---

## Graduate Discussion Instructions
Initial post: **400+ words**, all prompt components addressed, at least **1 credible technical citation**.
Peer responses: **Substantive replies to 2+ classmates** — challenge design decisions with technical specifics.

---

## Discussion Prompt: QoS for a Hybrid Work Enterprise

**Scenario:**
You are the network architect for a 3,000-employee technology company that shifted to permanent hybrid work (50% in-office, 50% remote). The company's network includes:
- A 1 Gbps campus WAN uplink to the internet (shared by all office traffic).
- 1,500 simultaneous Microsoft Teams video calls at peak hours (both in-office and remote users).
- A real-time trading platform used by 200 financial analysts (latency-critical, max 5ms end-to-end within the campus).
- File backup and replication running continuously to cloud storage (large, non-time-sensitive).
- General web browsing and SaaS application traffic from all 3,000 employees.

At peak hours, the WAN link is saturated and Teams video quality drops dramatically. The trading platform users complain of intermittent latency spikes. Engineering leadership wants to solve both problems simultaneously.

**Write a graduate-level post (400+ words) addressing ALL of the following:**

1. **QoS Classification & Marking Strategy:** Define your DSCP marking policy for each traffic type in this environment. Which device in the network marks each type (access switch, router, or endpoint)? Justify your trust boundary decision for Teams traffic vs. trading platform traffic.

2. **Queuing Design on the WAN Uplink:** Design a specific MQC policy for the 1 Gbps WAN uplink. Assign percentage allocations to each traffic class. Calculate whether your policy can support 1,500 simultaneous Teams video sessions at 2 Mbps each. Show your math — does 1 Gbps accommodate this? If not, what is the realistic limit and how should you communicate this to leadership?

3. **High Availability for the Trading Platform:** The trading platform gateway is a single multilayer switch. An HA engineer proposes HSRP with BFD using 300ms intervals (multiplier 3 = 900ms total detection). A junior engineer argues this is unnecessary because "the building has redundant power." Evaluate this argument and defend (or reject) the HA engineer's proposal with technical reasoning.

4. **Automation for QoS Consistency:** You need to deploy this QoS policy to 45 access switches and 8 distribution switches simultaneously. Which automation approach would you use — Python/Netmiko or Ansible — and why? Write a pseudo-code outline of the automation solution.

**Citation:** Cite RFC 2474 (DiffServ), RFC 2475 (DiffServ Architecture), or the Cisco QoS Design Guide.

---

## Grading Rubric (100 Points)
| Component | Points |
|---|---|
| DSCP marking strategy with trust boundary justification | 25 |
| MQC policy design with bandwidth math | 25 |
| HSRP/BFD HA analysis — technically justified | 20 |
| Automation recommendation with pseudo-code | 20 |
| Citation — credible, properly integrated | 5 |
| Peer responses — substantive | 5 |
| **Total** | **100** |


---

### Comprehensive SACSCOC RSI Grading Rubric (100 Points Total)

Your colloquium submission and peer critiques will be evaluated according to the following doctoral criteria:

| Evaluation Dimension | Exemplary (90–100%) | Proficient (80–89%) | Developing (<80%) | Points |
|---|---|---|---|:---:|
| **1. Theoretical Grounding & Scholarly Rigor** | Explicitly cites peer-reviewed literature (IEEE, ACM, AIS) and national regulatory frameworks (NIST, ISO) with flawless contextual application. | Cites literature and industry standards with minor gaps in theoretical synthesis. | Relies on informal or unreferenced assertions; lacks rigorous academic grounding. | **25 pts** |
| **2. Technical Precision & Architecture** | Demonstrates deep mastery of underlying protocols, data flows, and hardware/software constraints with zero conceptual errors. | Technically accurate with minor omissions in protocol-level execution or edge-case handling. | Superficial technical depth; treats core concepts as black-box abstractions. | **25 pts** |
| **3. Fiduciary & Governance Analysis** | Thoroughly quantifies operational risk, ROI impact, executive KPIs, and regulatory liability across enterprise failure domains. | Addresses business impact and governance, but lacks specific quantitative metrics or KPI alignment. | Ignores business risk, regulatory compliance, or fiduciary considerations. | **25 pts** |
| **4. Substantive Peer Critiques (2 required)** | Critically challenges colleagues using concrete counter-examples, empirical failure modes, and architectural trade-offs; drives intellectual debate. | Provides constructive feedback, but largely agrees without rigorous technical critique. | Superficial comments (e.g., "Good post, I agree") that fail federal RSI standards. | **25 pts** |
