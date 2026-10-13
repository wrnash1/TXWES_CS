# Discussion Board: Module 02 – Campus Network Design: VLANs, STP & EtherChannel
## CSC-6361 Advanced Computer Networks | Graduate Level
## Due: Sunday, November 1, 2026 at 11:59 PM CST

---

## Graduate Discussion Instructions
Initial post: **400+ words**, all prompt components addressed, at least **1 credible technical citation**.
Peer responses: **Substantive replies to 2+ classmates** — add new information, challenge assumptions, or present an alternative architectural approach.

---

## Discussion Prompt: Enterprise Campus Refresh — L2 vs. L3 Access Debate

**Scenario:**
You are the lead network architect at a regional university that is refreshing its entire campus network. The current infrastructure uses a flat Layer 2 design: all access switches trunk directly to a single pair of core switches, with one giant STP domain spanning the entire campus. There are 120 access switches, ~8,000 connected devices, and 40 active VLANs. The network experiences frequent STP topology changes, occasional broadcast storms, and slow convergence after any switch failure.

The CTO wants to modernize the campus. She has received two competing proposals from vendor teams:

**Proposal A — "Modern Flat Access with Rapid PVST+":**
Replace all access switches with new hardware running Rapid PVST+ with tuned bridge priorities. Keep the flat L2 design but add proper STP hierarchy (core = root, distribution = secondary root, access = leaf). Maintain the single STP domain. Cost: $800K.

**Proposal B — "Routed Access Layer (L3 to the Edge)":**
Deploy multilayer switches at both the distribution AND access layers. Run OSPF from access to core. Each access switch is a Layer 3 boundary — there is no spanning tree between switches at all. VLANs are local to each access switch. Cost: $1.4M.

**Your Task (400+ words, addressing ALL of the following):**

1. **Root Cause Analysis:** Given the existing symptoms (frequent TCs, broadcast storms, slow convergence), identify the specific STP and network design failures causing them. Be specific — what STP events cause topology change flooding? What causes a broadcast storm in a flat L2 domain?

2. **Evaluate Proposal A:** Would Rapid PVST+ with tuned priorities actually solve the root causes you identified? What are the practical limits of PVST+ at 120-switch/40-VLAN scale in a single STP domain?

3. **Evaluate Proposal B:** What are the specific technical advantages of a routed access design? What are the trade-offs — what does a network engineer give up by eliminating L2 between access switches? (Think about: seamless guest mobility, VM vMotion, wireless roaming, legacy applications that require L2 adjacency.)

4. **Your Recommendation:** Which proposal would you recommend, or would you propose a hybrid approach (e.g., routed uplinks to distribution + L2 access with MST)? Justify your recommendation with specific technical reasoning.

5. **Cost Justification:** The CTO is asking whether the $600K cost difference between Proposal A and B is justified. What business and operational factors would you include in that justification?

**Citation Requirement:** Cite at least one of:
- Cisco Validated Design Guide: Campus LAN (free at cisco.com)
- IEEE 802.1W or 802.1S standard documentation
- A peer-reviewed paper on large-scale campus STP design (available via TXWES West Library → IEEE Xplore)

---

## Peer Response Guidance
After posting your initial recommendation, respond to two classmates whose recommendation **differs from yours**. Address the specific technical trade-offs they raised and either acknowledge their point or present a counterargument with evidence. Strong responses will advance the technical analysis, not just restate agreement or disagreement.

---

## Grading Rubric (100 Points)
| Component | Points |
|---|---|
| Root cause analysis — specific and technically accurate | 15 |
| Proposal A evaluation — limitations of flat PVST+ at scale | 15 |
| Proposal B evaluation — trade-offs of routed access | 15 |
| Recommendation — justified with specific technical reasoning | 25 |
| Cost justification — business factors addressed | 10 |
| External citation — credible, properly integrated | 10 |
| Peer responses — substantive, advances discussion | 10 |
| **Total** | **100** |
