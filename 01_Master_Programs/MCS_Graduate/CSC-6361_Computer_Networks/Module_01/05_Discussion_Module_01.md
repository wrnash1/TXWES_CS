# Discussion Board: Module 01 – Advanced IP Routing: Multi-Area OSPF & EIGRP
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, October 25, 2026 at 11:59 PM CST

---

## Graduate Discussion Instructions
Your initial post must be **400 words or more**, address the specific prompt, include at least **one citation** from a credible technical source (RFC, Cisco documentation, peer-reviewed article, or IEEE/ACM paper), and demonstrate connection between the week's lecture content and your own lab experience.

After posting your initial response, provide **substantive replies to at least two classmates**. A substantive reply adds new information, poses a challenging follow-up question, or offers an alternative technical perspective. "Great post, I agree!" is not a substantive reply.

---

## Discussion Prompt: Routing Protocol Selection for a Multi-Site Enterprise

**Scenario:**
You are a senior network architect at a mid-sized financial services company. The company currently runs a flat single-area OSPF network across all 12 locations (headquarters + 11 branches). Each location has 2–8 routers. The CTO has tasked you with redesigning the routing architecture before the company acquires a competitor that runs EIGRP throughout its network.

**Your Task:**
Write a substantive initial post (400+ words) that addresses ALL of the following:

1. **Multi-Area OSPF Redesign Justification:** Given the current 12-location, ~50-router scale, explain specifically *why* a multi-area OSPF design is warranted. Reference at least one concrete technical consequence of leaving the network as a single flat area (e.g., SPF recalculation impact, LSDB size, convergence time).

2. **Area Design Recommendation:** Propose a specific area design for this company. Which locations should share areas? What area type (normal, stub, totally stubby, NSSA) would you recommend for branch offices that have no direct internet connections? Justify your choices.

3. **Post-Acquisition EIGRP Integration:** Once the acquisition is complete, you will have EIGRP routers that need to communicate with your OSPF domain. Describe your redistribution strategy, including how you would prevent routing loops. Would you consider migrating the acquired EIGRP domain to OSPF, or keeping the two protocols permanently? Justify your answer.

4. **Real-World Trade-offs:** Identify at least one practical trade-off or risk in your proposed design that you would need to communicate to the CTO. (Example trade-offs: impact of summarization on troubleshooting visibility, redistribution complexity, migration downtime window.)

**Citation Requirement:** Cite at least one of the following (or a comparable credible source):
- IETF RFC 2328 (OSPF v2)
- IETF RFC 7868 (EIGRP)
- A Cisco OSPF or EIGRP design guide (free at cisco.com)
- A peer-reviewed networking paper from IEEE Xplore or ACM Digital Library (accessible via TXWES West Library)

---

## Peer Response Guidance
When responding to classmates, choose posts that made a design recommendation **different from yours** and engage with the difference. Consider:
- "You recommended Totally Stubby areas for all branches. What about a branch that has a local internet breakout — would you still use Totally Stubby, and if so, how would you handle the local default route?"
- "You proposed keeping EIGRP and OSPF permanently separate. What would change if the company planned to migrate to SD-WAN within 3 years?"

---

## Grading Rubric (100 Points)
| Component | Points |
|---|---|
| Substantive Content — all 4 prompt points addressed, 400+ words | 40 |
| External Citation — credible technical source, properly integrated | 30 |
| Peer Engagement — meaningful replies to 2+ classmates | 30 |
| **Total** | **100** |
