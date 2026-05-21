# Quiz: Module 08 - Security Architecture and Design
## Course: CIS-4315_Cyber_Governance_Risk_Compliance (ISACA Certified Information Security Manager (CISM))

---

**Question 1**
Which recovery site type is fully operational, contains real-time mirrored datasets, and can take over production workflows within minutes?
*   A) Cold Site
*   B) Warm Site
*   C) Hot Site
*   D) Mirror Store
*   **Correct Answer:** C) Hot sites are equipped with matching hardware, network connectivity, power, and synchronized datasets that enable rapid, near-immediate failover.
*   **Distractor Analysis:**
    *   *Why C is correct:* Hot sites maintain real-time or near-real-time data replication and fully provisioned infrastructure, enabling activation within minutes or hours.
    *   *Why A is incorrect:* Cold sites provide physical space and power only — no hardware or pre-loaded data; recovery takes days to weeks.
    *   *Why B is incorrect:* Warm sites have infrastructure but require configuration and data restoration; recovery typically takes hours to days.
    *   *Why D is incorrect:* "Mirror Store" is not a standard recovery site classification in BCP/DRP terminology.

---

**Question 2**
Which of the following most accurately describes a **tabletop exercise** as a DRP testing method?
*   A) A live failover test in which production systems are actually switched to the alternate recovery site to verify full operational capability
*   B) A discussion-based review exercise where team members verbally walk through their assigned roles and responses to a hypothetical disaster scenario
*   C) An automated penetration test that simulates a ransomware attack against the organization's disaster recovery infrastructure
*   D) A parallel processing test in which both primary and alternate systems run simultaneously to verify data consistency
*   **Correct Answer:** B) Tabletop exercises are the least disruptive testing method — they validate plan knowledge and identify gaps through discussion without activating actual recovery systems.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Switching production to an alternate site is a full interruption test — the most comprehensive and most disruptive testing method.
    *   *Why B is correct:* Tabletop exercises are scenario-based discussions that identify procedural gaps and test participant awareness without operational disruption.
    *   *Why C is incorrect:* Automated penetration testing is a security assessment activity, not a DRP test method.
    *   *Why D is incorrect:* Running primary and alternate systems simultaneously is parallel testing — a higher-maturity testing method that follows tabletop exercises.

---

**Question 3**
An organization has an RTO of 30 minutes for its online trading platform. Which recovery site strategy is most appropriate?
*   A) Cold site with media backups stored offsite
*   B) Warm site with 4-hour hardware pre-staging capability
*   C) Hot site with real-time data replication and automated failover capability
*   D) Mobile recovery unit deployed from regional headquarters within 24 hours
*   **Correct Answer:** C) A 30-minute RTO requires a hot site — only a fully provisioned, real-time synchronized facility can achieve recovery within this timeframe.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cold sites require days to deploy hardware and restore from media; they cannot support a 30-minute RTO.
    *   *Why B is incorrect:* A 4-hour warm site capability far exceeds the 30-minute RTO requirement.
    *   *Why C is correct:* Only hot sites with automated failover can achieve sub-hour RTOs; the investment is justified by the business-critical nature of a trading platform.
    *   *Why D is incorrect:* A 24-hour mobile deployment is far outside any aggressive RTO and is only suitable for non-critical functions.

---

**Question 4**
What is the key distinction between a Business Continuity Plan (BCP) and a Disaster Recovery Plan (DRP)?
*   A) BCPs are required by law; DRPs are optional for organizations below a certain revenue threshold
*   B) BCPs address the full scope of maintaining business operations during a disruption; DRPs specifically address the restoration of IT systems and data
*   C) BCPs apply to natural disasters only; DRPs apply to cyber incidents only
*   D) BCPs are created by business units; DRPs are created by IT vendors under contract
*   **Correct Answer:** B) BCP and DRP address different scopes — BCP maintains the broader business; DRP is the IT-specific recovery component within the BCP framework.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Legal requirements for BCP/DRP vary by industry and jurisdiction; the distinction is not a legal mandate threshold.
    *   *Why B is correct:* This is the standard CISM definition — DRP is a subset of BCP focused specifically on technology recovery.
    *   *Why C is incorrect:* Both plans address all types of disruptive events, not segmented by disaster type.
    *   *Why D is incorrect:* Both plans are created by the organization; DRP is not an externally contracted vendor document.

---

**Question 5**
After a major ransomware attack, an organization activates its DRP and successfully restores systems within the defined RTO. During the post-incident review, the team notes that the DRP had never been tested before the actual incident. What governance lesson does this scenario illustrate?
*   A) The DRP was clearly effective since recovery succeeded within the RTO, so testing is unnecessary
*   B) Post-incident reviews should focus only on technical improvements to backup and recovery systems
*   C) Untested DRPs may succeed by luck but cannot be relied upon; regular structured testing is essential to identify and correct gaps before an actual disaster
*   D) DRP testing should only be conducted when a new threat category emerges
*   **Correct Answer:** C) Successful recovery from an untested plan is a near-miss event — the organization got lucky, but gaps that could have caused failure were never identified through controlled exercises.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* One successful unplanned recovery does not validate a plan; conditions will differ in future incidents and untested gaps may be catastrophic.
    *   *Why B is incorrect:* Post-incident reviews should also address governance, training, and plan testing gaps — not only technical improvements.
    *   *Why C is correct:* CISM emphasizes that plan testing is a governance requirement, not optional; untested plans represent unquantified risk.
    *   *Why D is incorrect:* DRP testing should occur on a scheduled basis (at minimum annually) regardless of emerging threats, and should be updated after any significant organizational or technology change.
