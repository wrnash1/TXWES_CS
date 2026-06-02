# Discussion Forum: Module 01 - Windows Server Installation and Editions

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion connects the installation and edition decisions from the video lecture and reading guide to real-world enterprise scenarios. Choose one scenario below, respond to all three sub-questions in your initial post, and engage meaningfully with at least two classmates.

---

### Scenario A — Branch Office Deployment Decision

Your company is opening a new branch office that requires a single server to run DNS, DHCP, and file sharing for 30 local users. The branch has no on-site IT staff. Management asks you to minimize ongoing maintenance overhead while keeping the server secure. A junior colleague suggests installing Desktop Experience so the occasional visiting technician can manage it locally with a familiar GUI.

1. Which Windows Server edition and installation option would you recommend, and why does the junior colleague's reasoning not outweigh the security trade-offs?
2. How would a visiting technician manage this Server Core installation without a local GUI? Name at least two remote management tools and explain how each works.
3. What post-installation configuration steps are most critical for a branch office server that has no on-site administrator, and which step would you automate first if you were scripting the deployment?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario B — Licensing Cost Optimization

A mid-size company plans to consolidate its 14 departmental servers onto two physical Hyper-V hosts. Each host will run 7 Windows Server virtual machines. The IT director asks you to determine the most cost-effective licensing approach and justify the recommendation with specific edition rules.

1. Explain the per-VM licensing rule for Standard edition and calculate how many Standard licenses would be needed for both hosts combined.
2. Compare the cost-effectiveness of your Standard calculation against purchasing one Datacenter license per host. What is the break-even point in VM count?
3. Storage Spaces Direct is on the company's roadmap for 18 months from now. How does this planned feature affect your edition recommendation today, and what is the cost of choosing the wrong edition now?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario C — Activation Strategy for a Secure Facility

A government contractor is deploying 8 Windows Server machines in a classified facility with no internet access and no connection to the corporate network. The machines must be activated before going into production. A colleague suggests using KMS because it is the enterprise standard.

1. Explain why KMS is not the right choice for this deployment and what activation method should be used instead.
2. Describe the key limitation of the alternative activation method you chose and how the administrator should plan around it before the deployment begins.
3. If one of the 8 servers needs to be replaced two years from now and the original activation key pool is exhausted, what process should the administrator follow to obtain additional activations?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario, answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates who chose different scenarios if possible; minimum 60 words each
- In peer replies: evaluate the technical accuracy of their answer to sub-question 1, and add one point they did not mention

---

### Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

### Professor Nash's Note

The Server Core versus Desktop Experience decision is one that every Windows Server administrator faces repeatedly throughout their career. The temptation to install Desktop Experience because it is familiar is understandable, but in professional environments the expectation is that you can manage servers remotely without needing a GUI on the box. Practice your PowerShell and Windows Admin Center skills in the lab — the administrators who master remote management tools are the ones who stand out. I look forward to reading your scenario responses this week.
