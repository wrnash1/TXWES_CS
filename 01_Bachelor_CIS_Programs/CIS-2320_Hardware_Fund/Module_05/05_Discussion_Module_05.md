# Discussion Forum: Module 05 - Storage Devices

## Course: CIS-2320 Hardware Fundamentals (CompTIA A+ Core 1, 220-1101)

---

### Overview

This discussion asks you to apply what you learned in Module 05 to realistic workplace scenarios. Choose one of the three scenarios below and respond to all three sub-questions within it. Your initial post should be 175–225 words and must demonstrate accurate technical terminology from the module. You are not required to respond to the same scenario as your peers — reading across scenarios is encouraged.

---

### Scenario A — The Small Business Server Upgrade

A local law firm currently stores all client case files on a single 4 TB desktop HDD attached to their file server. The office manager reports that file access is slow and the IT manager is concerned about data loss if the drive fails. The firm has a budget to purchase three identical 4 TB drives and wants to maximize both storage capacity and resilience with a single-drive fault tolerance.

Respond to all three of the following:

1. Which RAID level would you recommend for this firm's three-drive scenario, and what usable storage capacity would result? Show your calculation.
2. The IT manager asks whether they should use a SATA SSD or an HDD for the array drives. Explain the trade-offs between the two options for a file server used primarily for sequential document reads and writes.
3. A year after deployment, one drive in the array fails. Describe the steps the technician should take and explain what state the array is in during the period between the failure and the replacement drive rebuild completing.

---

### Scenario B — The Gaming PC Build Dilemma

A customer comes to your shop with two questions about a new gaming PC build. First, they want to know whether they should install a 2.5-inch SATA SSD or an M.2 NVMe SSD as their boot drive. Second, they have heard that "M.2 means fast" and want to buy the cheapest M.2 drive they can find, assuming all M.2 drives perform the same.

Respond to all three of the following:

1. Explain the performance difference between a SATA SSD (whether 2.5-inch or M.2 SATA) and an M.2 NVMe SSD. Use specific speed figures from the module in your response.
2. The customer finds an M.2 drive listed as "M.2 2280, B+M key, SATA." Their new motherboard's M.2 slot is labeled "PCIe 4.0 x4, NVMe only." Will this drive work in that slot? Explain why or why not in terms the customer can understand.
3. The customer ultimately installs an NVMe drive and later reports it is not detected in BIOS. The drive is physically seated and the retaining screw is installed. List two diagnostic steps the technician should take before concluding the drive is defective.

---

### Scenario C — The RAID Misconception

A classmate tells you they set up a two-drive RAID 0 array on their home PC for "extra protection" because RAID means redundancy. They stored their entire college project archive on the array and have no other backup. They also mention they were unable to add a third drive to make it RAID 5 and gave up.

Respond to all three of the following:

1. Correct your classmate's misunderstanding about RAID 0. Explain clearly what RAID 0 actually does, what the real data-loss risk is, and why calling it a protection strategy is incorrect.
2. Explain why adding a third drive and switching from RAID 0 to RAID 5 is not a simple add-on operation. What would the classmate actually need to do to safely migrate to a RAID 5 array?
3. Your classmate asks which RAID level would give them the best combination of redundancy and usable capacity if they buy two additional 1 TB drives (bringing their total to four drives of equal size). Compare RAID 5 and RAID 10 for this four-drive scenario, including usable capacity for each.

---

### Grading Rubric — 10 Points Total

Initial Post — 6 Points (due Wednesday at 11:59 PM):

- 5–6 pts: Addresses all three sub-questions with technical accuracy, uses correct terminology from the module (RAID level names, drive types, speed figures, connector names), and meets the 175–225 word count.
- 3–4 pts: Addresses most sub-questions but lacks technical detail, misuses terminology, or falls short of the word count.
- 0–2 pts: Post is missing, addresses fewer than two sub-questions, or contains significant factual errors.

Peer Responses — 4 Points (due Sunday at 11:59 PM):

- 4 pts: Replies to at least two classmates with substantive technical additions — for example, pointing out a consideration the peer missed, offering an alternative RAID choice with justification, or expanding on a connector or drive type comparison.
- 2 pts: Replies to only one peer, or responses are brief and non-technical (e.g., "Great post, I agree!").
- 0 pts: No peer responses submitted.

Peer responses must be at least 50 words each and must add new technical content, not simply restate the peer's answer.

---

### Professor Nash's Note

RAID is one of the topics where I consistently see students lose points on the A+ exam because they memorize the name of a level without understanding what happens when a drive actually fails. As you write your post, ask yourself: if a drive failed in the RAID configuration you are describing, what would a technician see? What would they do next? That kind of thinking — working through the failure scenario — is exactly what the exam tests and exactly what separates a prepared technician from one who only memorized a chart. Good luck, and I look forward to reading your posts.
