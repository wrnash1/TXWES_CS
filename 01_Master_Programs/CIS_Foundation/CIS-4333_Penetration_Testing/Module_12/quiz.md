# Quiz: Module 12 — Physical Security Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Time limit: 20 minutes.

---

## Questions

**Question 1**

An organization uses HID Prox 125 kHz cards for building access. A penetration tester with a concealed Proxmark3 reads an employee's card from 4 inches while standing in an elevator. Which characteristic of the card technology makes this attack possible?

A. The card uses RC4 encryption that has known weaknesses.

B. The card transmits a fixed ID without authentication when energized by a reader.

C. The card stores credentials in writable flash memory accessible at range.

D. The HID Prox protocol requires proximity but uses no signal shielding.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. HID Prox 125 kHz cards do not use RC4 or any encryption. They broadcast a fixed facility code and card number in cleartext whenever energized by an RF field.
- B is correct. 125 kHz proximity cards are passive devices that broadcast a fixed ID when energized by the reader's RF field. There is no authentication challenge, no encryption, and no mechanism to detect unauthorized reads.
- C is incorrect. HID Prox cards do not use writable flash memory for credential storage. The card ID is encoded in read-only memory (ROM or laser-fused links).
- D is incorrect. While proximity is required, the vulnerability is not about signal shielding. The fundamental issue is the absence of any authentication or encryption, not physical shielding of the RF field.

---

**Question 2**

During a physical penetration test, a tester successfully enters a building's server room by following an employee through the card-controlled door when the employee holds the door open. The employee was unaware the person behind them was unauthorized. This is an example of:

A. Piggybacking

B. Tailgating

C. Shoulder surfing

D. Loiding

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Piggybacking occurs when the authorized person is aware (and passively or actively allows) the unauthorized person to enter. In this scenario, the employee held the door without knowing the tester was unauthorized — that is tailgating.
- B is correct. Tailgating occurs when an unauthorized person follows an authorized person through a controlled entry without the authorized person's knowledge. The employee holding the door was acting from social politeness, not deliberate permission.
- C is incorrect. Shoulder surfing involves observing sensitive information visually. It does not involve physical entry.
- D is incorrect. Loiding involves using a flexible tool to retract a spring latch. It does not involve a social interaction.

---

**Question 3**

A physical penetration tester is challenged by a security guard who demands identification and explanation. The tester provides a business card but does not have the get-out-of-jail letter on their person. What is the BEST course of action?

A. Explain the penetration testing engagement verbally and provide the client contact's phone number from memory.

B. Cooperate fully, present whatever identification is available, and call the designated client emergency contact to have them speak with the guard.

C. Invoke attorney-client privilege and decline to answer questions until legal counsel is present.

D. Abandon the test immediately and leave the premises to avoid further confrontation.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Verbal explanation alone is insufficient. Without the get-out-of-jail letter as physical evidence, the guard has no way to verify the claim. Verbal information from the person being challenged is not credible confirmation.
- B is correct. Cooperating fully, presenting available identification, and enabling the guard to speak directly with the authorized client contact resolves the situation through legitimate verification. This is why an accessible emergency contact is a required element of physical test authorization.
- C is incorrect. Attorney-client privilege applies to communications between an attorney and their client. It has no application here. Invoking it would be misleading and would likely escalate the situation unnecessarily.
- D is incorrect. Abandoning the test does not resolve the situation — the guard has already observed the tester and the encounter is documented. Leaving without resolving the situation may prompt the guard to call law enforcement. Staying to cooperate is the correct approach.

---

**Question 4**

A physical security assessment of a corporate campus finds that dumpsters containing unshredded documents are located inside a fenced perimeter that requires a badge scan to enter. The scope of work authorizes "all physical security testing of Meridian Financial Group facilities." Does the tester have authorization to access the dumpster area?

A. Yes, because the scope covers all facilities and the dumpster is on company property.

B. No, because dumpster diving must be explicitly named in the scope of work.

C. Yes, because waste materials have no legal protection once discarded.

D. No, because the dumpster area requires badge access, and entry without a badge constitutes unauthorized access outside the test's scope.

**Correct Answer:** A

**Distractor Analysis:**

- A is correct. The scope of work authorizes all physical security testing of company facilities. The dumpster area is within the company's physical perimeter and is a legitimate assessment target. Accessing it is within scope. The badge access to reach the dumpster is itself a physical control being tested.
- B is incorrect. While explicit naming is a best practice, "all physical security testing" is broad authorization. A well-scoped engagement would list specific techniques, but the broad authorization here is sufficient.
- C is incorrect. While there is a legal principle that discarded materials in public spaces lack privacy protection, this reasoning misses the point. The authorization comes from the scope of work, not from legal disposals principles. This answer uses a real legal principle in the wrong context.
- D is incorrect. If the scope authorizes all physical security testing of the facility, overcoming physical access controls (including badge-controlled gates) is within that authorization. The badge access to the dumpster area is a control being assessed, not a boundary excluding that area from scope.

---

**Question 5**

Which physical security control would MOST effectively prevent the badge cloning attack described in Question 1?

A. Reducing the operating range of the badge reader from 4 inches to 2 inches.

B. Replacing HID Prox cards with a 13.56 MHz smart card system using mutual authentication.

C. Installing CCTV cameras at the badge reader to detect unauthorized reading attempts.

D. Training employees to hold their badge wallet against their body to prevent proximity reads.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Reducing reader range to 2 inches does not eliminate the vulnerability — it only requires the attacker to position their concealed reader slightly closer. The fundamental issue (unauthenticated broadcast ID) remains.
- B is correct. Upgrading to a 13.56 MHz smart card system with mutual authentication (such as MIFARE DESFire EV2, HID iCLASS SE, or SEOS) requires both the card and reader to authenticate to each other. The card will not respond to an unauthorized reader, eliminating the cloning attack path.
- C is incorrect. CCTV cameras provide forensic evidence but do not prevent the attack. An attacker with a concealed reader can operate within camera coverage areas without being immediately identified as performing an attack.
- D is incorrect. Faraday shielding in badge wallets is a partial mitigation but is not an organizational control. Employees routinely remove cards from wallets to badge in, creating the attack window. Training is not a substitute for technical controls.

---

**Question 6**

During a physical pen test, a tester finds a door with a lever handle secured by an electromagnetic lock. The door has a 1.5-inch gap at the bottom. Which tool would MOST likely enable opening this door from the outside?

A. Pick gun

B. Bump key

C. Under-door tool with hook

D. Loid/shim

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. A pick gun attacks the pin tumbler lock mechanism. An electromagnetic lock does not have pins — it is secured by magnetic holding force, not a mechanical lock. Picking is irrelevant.
- B is incorrect. A bump key also attacks the pin tumbler mechanism. Same reasoning as A — the electromagnetic lock has no pins.
- C is correct. An under-door tool is a flexible rod with a hook attachment that can be inserted under the door gap and manipulated to push down the lever handle from the inside, releasing the door without engaging any lock mechanism.
- D is incorrect. A loid/shim attacks spring latches (the angled bolt in a standard doorknob). An electromagnetic lock does not use a spring latch — it uses magnetic force to hold the door closed. A loid would not engage the magnetic holding force.

---

**Question 7**

A company uses keypad locks for server room access. After observing the keypad, a tester notices heavy wear on the keys 2, 5, and 8. What does this indicate and what attack is most directly suggested?

A. The PIN is exactly 2-5-8 in that order.

B. The PIN consists of some combination of 2, 5, and 8, substantially narrowing brute-force attempts.

C. The keypad has been used primarily for employee training and the PIN has not been updated.

D. The keypad requires regular maintenance — worn keys indicate need for replacement, not a security risk.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Worn keys reveal which digits are used but not their order, repetition, or exact sequence. The PIN could be 258, 285, 528, 582, 825, 852, 2258, 5882, or any other combination.
- B is correct. Three worn keys reveal which three digits are used in the PIN. A 4-digit PIN using only those three digits has a maximum of 3^4 = 81 possibilities (or 4! = 24 if non-repeating) rather than 10^4 = 10,000. This substantially reduces brute-force complexity.
- C is incorrect. The wear pattern reveals user behavior, not training activity. There is no basis to conclude the PIN has not been updated based on wear alone.
- D is incorrect. Key wear is a well-documented physical security vulnerability called "key wear analysis." It is directly relevant to security assessment, not merely a maintenance issue.

---

**Question 8**

A penetration tester completes a physical assessment and discovers that the CFO's office was unlocked and unoccupied for 45 minutes. The tester entered and found physical stock certificates and a handwritten note containing the acquisition target name. Which is the MOST appropriate action during the test?

A. Photograph all documents as evidence and remove the stock certificates to demonstrate they were unprotected.

B. Document the unlocked office and visible documents in notes (without photographing or removing anything), then report the finding immediately to the client emergency contact.

C. Lock the office door from the inside and wait for the CFO to return to demonstrate physical access was obtained.

D. Ignore the finding since the office is inside the secured building perimeter and physical assets were not a named target.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Photographing sensitive documents requires explicit authorization in the scope of work. Removing physical property — even temporarily — constitutes theft and violates the scope of virtually all physical assessments. The goal is to document access, not to acquire assets.
- B is correct. Documenting the finding with notes (and authorized photography if pre-approved) and immediately notifying the client contact allows the client to secure the sensitive materials. Physical pen tests routinely require real-time notification when highly sensitive materials are discovered.
- C is incorrect. Remaining hidden in a secured space extends the unauthorized presence beyond what is needed to document the finding. It also risks a confrontation that cannot be quickly resolved with the get-out-of-jail letter.
- D is incorrect. Physical assets discovered in unlocked, accessible spaces are always within scope when the assessment authorizes physical security testing of the building. Finding sensitive materials in an unoccupied, unlocked executive office is a high-value finding.

---

**Question 9**

Which standard provides the most specific requirements for physical access control, visitor management, and media disposal for organizations handling payment card data?

A. ISO/IEC 27001 Annex A Control 7

B. NIST SP 800-53 PE controls

C. PCI DSS Requirement 9

D. HIPAA 45 CFR § 164.310

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect. ISO/IEC 27001 Annex A Control 7 addresses physical security but provides a general framework rather than specific prescriptive requirements for payment card environments.
- B is incorrect. NIST SP 800-53 PE controls are comprehensive and broadly applicable but are aimed at federal systems. They do not specifically address payment card data handling environments.
- C is correct. PCI DSS Requirement 9 specifically addresses physical access to cardholder data environments, including access control mechanisms, visitor logs, badge requirements, and media handling/destruction procedures for organizations in the payment card industry.
- D is incorrect. HIPAA 45 CFR § 164.310 addresses physical safeguards for protected health information. It applies to healthcare organizations, not to payment card data.

---

**Question 10**

A physical penetration test report includes a finding that a server room door can be bypassed by inserting a flexible tool under a 2-inch door gap to depress the internal push bar. The finding is rated High. The client disputes the rating, arguing that the server room is inside a secured building that already requires badge access. How should the tester respond?

A. Accept the downgrade since defense in depth means any single finding is mitigated by surrounding controls.

B. Explain that the rating reflects the potential impact of bypassing the control, independent of the controls that precede it, because each layer must be independently defensible.

C. Upgrade the finding to Critical to emphasize the seriousness and prevent the client from downplaying it.

D. Remove the finding from the report since the client disagrees with the assessment.

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect. Defense in depth requires each layer to independently resist attack. If an attacker has already compromised or bypassed outer layers (or has authorized access as a contractor), the server room door must hold independently. Relying entirely on preceding layers is not a sound security posture.
- B is correct. The finding's risk rating reflects the impact achievable by bypassing that specific control. Each physical control should be evaluated on its own merits. A server room door that can be bypassed with a simple tool is a High finding regardless of what controls precede it, because contractors, cleaning staff, and social engineers may already be inside the secured building.
- C is incorrect. Artificially upgrading a finding to intimidate the client into accepting it is dishonest and damages professional credibility. Ratings must be evidence-based.
- D is incorrect. Removing a finding because the client disagrees with the rating is a serious professional integrity violation. The tester's obligation is accurate, evidence-based reporting. If the client wishes to accept the risk, they document that in the report's risk acceptance section — but the finding remains.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | A |
| 5 | B |
| 6 | C |
| 7 | B |
| 8 | B |
| 9 | C |
| 10 | B |
