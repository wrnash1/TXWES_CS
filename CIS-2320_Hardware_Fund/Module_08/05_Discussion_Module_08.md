# Discussion Forum: Module 08 - Custom PC Configurations

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.4
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

## Overview

This week's discussion moves beyond memorizing component names and asks you to reason about real-world build decisions the way a working technician would. You will choose one scenario below, analyze it using the concepts from Module 08, and engage with your classmates' reasoning in your peer responses.

Choose one scenario (A, B, or C). Read it carefully, then write your initial post addressing all three sub-questions for that scenario. Your response should be 175-225 words total.

---

## Scenario A — The Mixed-Use Workstation Decision

A mid-sized engineering firm is purchasing new workstations for a team of structural engineers. The IT manager proposes buying high-end consumer gaming PCs (GeForce RTX 4070 Ti, Core i7, 32 GB DDR5) because they are significantly cheaper than professional workstations and benchmarks show the gaming GPUs outperform the Quadro-class options in raw rendering speed tests. Several engineers have pushed back, saying they need "certified hardware" for their software.

Address all three of the following:

1. Explain what "certified hardware" means in the context of professional CAD GPUs and why it matters for the engineers' actual software stability — not just benchmark performance. What specific risk does using a consumer gaming GPU introduce in a professional design environment?

2. The IT manager argues that benchmark tests prove the gaming GPU is faster. Is this argument valid for a professional workstation purchasing decision? Explain why raw benchmark scores do not fully capture the requirements of this build type.

3. If budget is genuinely constrained, what compromise approach could the IT manager take — and what should they verify before finalizing the purchase?

---

## Scenario B — The Virtualization Host Upgrade

A small university IT department runs a virtualization host that currently has 16 cores and 64 GB of RAM running VMware ESXi. The host supports 12 virtual machines for student development environments, but students are reporting that VMs are extremely slow during midterms when all 12 are active simultaneously. The department chair suggests upgrading the GPU to a high-end gaming card to improve performance, having read that "gaming GPUs accelerate compute workloads."

Address all three of the following:

1. Explain why upgrading the GPU is unlikely to solve the performance problem for this specific virtualization workload. What resource is most likely the actual bottleneck, and how would you confirm your diagnosis?

2. What specific hardware upgrade(s) would you recommend, and how would you calculate the minimum resources needed to support 12 simultaneous VMs if each VM is allocated 2 vCPUs and 8 GB of RAM?

3. Under what circumstances would a GPU upgrade actually be appropriate for a virtualization host? Describe a specific use case that would justify adding a high-performance GPU to this system.

---

## Scenario C — The Home NAS Design Debate

Two friends are building a home NAS for a small family photography business. They plan to use four 6 TB drives. Friend A insists on RAID 0 because "you get the full 24 TB of storage and the transfers are fastest." Friend B argues for RAID 5. A third option they are considering is RAID 10. The NAS will store original RAW photo files that cannot be re-shot — client wedding photos going back several years.

Address all three of the following:

1. Evaluate Friend A's RAID 0 argument. What is the critical flaw in this recommendation for this specific use case, and what failure scenario makes RAID 0 particularly dangerous for irreplaceable data?

2. Compare RAID 5 and RAID 10 for this four-drive, four-6-TB-drive scenario. Calculate the usable capacity of each, identify the fault tolerance of each, and explain which you would recommend given the irreplaceable nature of the data.

3. The friends are also deciding between standard DDR4 RAM and ECC DDR4 RAM for the NAS motherboard. The NAS will run TrueNAS with ZFS. Explain the specific risk of using non-ECC RAM with ZFS and whether the cost difference is justified for this use case.

---

## Discussion Rubric (10 Points Total)

**Initial Post — 6 Points (due Wednesday at 11:59 PM)**

- 5-6 pts: All three sub-questions answered with technical accuracy. Response demonstrates understanding of the specific hardware principle at stake, not just general definitions. Stays within 175-225 words. Uses correct terminology (RAID levels, GPU types, vCPU, ECC, etc.).
- 3-4 pts: Two of three sub-questions adequately addressed, or all three addressed with surface-level explanations that lack technical specificity.
- 1-2 pts: One sub-question addressed, or response is off-topic or demonstrates significant technical inaccuracies.
- 0 pts: No initial post submitted.

**Peer Responses — 4 Points (due Sunday at 11:59 PM)**

Respond to at least two classmates who chose different scenarios from yours. Each response must be at least 75 words and do one of the following: correct a technical inaccuracy respectfully, add a detail or nuance they did not mention, describe how you would apply their reasoning differently in a real-world context, or challenge one of their conclusions with a counterargument supported by module content.

- 4 pts: Two substantive responses meeting the criteria above, each at least 75 words.
- 2 pts: One substantive response, or two responses that are generic ("Good post, I agree") without added technical content.
- 0 pts: No peer responses submitted.

---

*Professor Nash — Texas Wesleyan University*
*These scenarios are designed to reflect real decisions technicians face in the field. There is often more than one defensible answer — what matters is the quality of your reasoning and your ability to connect module concepts to practical outcomes.*
