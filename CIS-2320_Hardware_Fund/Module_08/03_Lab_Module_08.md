# Lab Activity: Module 08 - Custom PC Configurations

## Course: CIS-2320 Hardware Fundamentals | Texas Wesleyan University

**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 3.4
**Total Points:** 100
**Submission:** Upload your completed lab document to the Canvas assignment portal before the due date.

---

## Overview

In this lab you will apply the component selection principles from Module 08 to five real-world workload scenarios. For each scenario you will identify the correct build type, select appropriate components from a provided list, complete a bill-of-materials table, and justify your choices in writing.

This lab does not require physical hardware. All work is completed as written analysis and table completion. Your grade is based on the accuracy of your component selections and the quality of your written justifications — not just the final answers.

**Tools needed:** This Reading Guide, your notes, and access to professormesser.com for reference. No additional software required.

---

## Part 1 — Build Type Identification and Component Matching (40 points)

### Instructions

Read each workload scenario below. In the table that follows each scenario, complete the three columns: Build Type, Primary Hardware Priority, and Component Justification. Use the Reading Guide and your lecture notes to support your answers.

---

### Scenario A — The Architecture Firm

A regional architecture firm hires a new junior technician. The firm's architects use Autodesk Revit and AutoCAD daily to create large building information models. The models can contain hundreds of components and take 20-45 minutes to fully render. The firm's current workstations have consumer gaming GPUs (NVIDIA GeForce RTX 3060) and 16 GB of RAM. Architects are reporting rendering errors and occasional application crashes during complex renders.

**Question A1:** What is the correct build type for this workload?

Your answer: ___________________________________________________________

**Question A2:** What is the most likely root cause of the rendering errors and crashes?

Your answer: ___________________________________________________________

**Question A3:** Complete the component selection table for one upgraded architect workstation:

| Component | Your Selection | Justification (1-2 sentences) |
|---|---|---|
| GPU | | |
| CPU core count | | |
| RAM capacity and type | | |
| Primary storage type | | |
| PSU wattage estimate | | |

---

### Scenario B — The Growing Startup Development Team

A software startup wants to consolidate their 6 physical developer workstations into virtual machines running on a single powerful host server. Each VM will be allocated 4 vCPUs and 16 GB of RAM. The host must support all 6 VMs running simultaneously plus the hypervisor's own overhead (estimated at 4 cores and 16 GB RAM for the host OS and VMware ESXi).

**Question B1:** What is the correct build type for this workload?

Your answer: ___________________________________________________________

**Question B2:** Calculate the minimum physical RAM the host server needs. Show your work.

| Calculation Step | Your Answer |
|---|---|
| Total VM RAM (6 VMs x 16 GB each) | |
| Host OS and hypervisor overhead | |
| Minimum total RAM required | |
| RAM capacity you would recommend (next standard size up) | |

**Question B3:** Calculate the minimum logical CPU thread count required. Show your work.

| Calculation Step | Your Answer |
|---|---|
| Total vCPUs needed by VMs (6 VMs x 4 vCPUs each) | |
| Host overhead cores | |
| Minimum physical threads required | |
| Processor recommendation (core count and why) | |

**Question B4:** Should this host server include a high-end gaming GPU? Explain why or why not in 2-3 sentences.

Your answer: ___________________________________________________________

---

### Scenario C — The Competitive Gamer

A college student wants to build a gaming PC to play modern AAA titles at 1440p resolution and a target of 144 frames per second. Their budget prioritizes performance over aesthetics. They currently have a 1440p 144Hz monitor with DisplayPort input.

**Question C1:** What is the correct build type for this workload?

Your answer: ___________________________________________________________

**Question C2:** Complete the component selection table:

| Component | Your Selection | Justification (1-2 sentences) |
|---|---|---|
| GPU tier (high/mid/entry and why) | | |
| CPU priority (cores vs. clock speed) | | |
| RAM capacity and speed | | |
| Storage type and minimum capacity | | |

**Question C3:** The student's friend recommends they buy a professional NVIDIA RTX A4000 workstation GPU instead of a gaming card, arguing it is "more powerful." Write a 3-4 sentence response explaining why this advice is incorrect for a gaming build.

Your answer: ___________________________________________________________

---

### Scenario D — The Home Media Server

A family wants to set up a home NAS to store 10 years of family photos and videos (currently 3 TB and growing), stream media to TVs, and back up all household computers automatically. They want to survive at least one drive failure without losing any data.

**Question D1:** What is the correct build type for this workload?

Your answer: ___________________________________________________________

**Question D2:** They are considering a 4-drive array using 4 TB drives. Complete the RAID comparison table:

| RAID Level | Usable Capacity from 4x 4TB Drives | Fault Tolerance | Appropriate for This Scenario? (Yes/No/Why) |
|---|---|---|---|
| RAID 0 | | | |
| RAID 1 | | | |
| RAID 5 | | | |
| RAID 10 | | | |

**Question D3:** Which RAID level do you recommend for this family, and why? Write 3-4 sentences addressing both the storage capacity requirement and the data protection requirement.

Your answer: ___________________________________________________________

**Question D4:** The family's NAS will run TrueNAS with ZFS. A component vendor offers a lower price on non-ECC RAM. Should they use non-ECC RAM to save money? Explain the specific risk in 2-3 sentences.

Your answer: ___________________________________________________________

---

## Part 2 — Mixed-Scenario Component Matching Exercise (30 points)

### Part 2 Directions

The table below lists 10 components or features. For each item, identify which build type(s) it is most appropriate for. Some items may apply to more than one build type. In the "Reasoning" column, explain in one sentence why that component is or is not appropriate for each build type.

Use these build type codes: W = CAD/Professional Workstation, V = Virtualization Host, G = Gaming PC, N = NAS/Home Server

| Component or Feature | Most Appropriate Build Type(s) | Reasoning |
|---|---|---|
| NVIDIA RTX A5000 (Radeon Pro-class GPU) | | |
| 128 GB DDR4 ECC Registered RAM | | |
| 4x 4TB NAS-rated 3.5-inch HDDs in RAID 5 | | |
| AMD Ryzen 9 7950X (16 cores, 32 threads) | | |
| NVIDIA GeForce RTX 4080 (consumer gaming GPU) | | |
| 1 TB NVMe SSD (boot + primary OS drive) | | |
| Low-TDP ARM-based or Atom-class processor | | |
| 1440p 144Hz monitor with DisplayPort | | |
| Integrated graphics only (no discrete GPU) | | |
| 10 GbE network interface card | | |

---

## Part 3 — Scenario Analysis and Written Justification (30 points)

### Part 3 Directions

Answer both questions below. Each response should be 150-200 words and demonstrate your understanding of the component selection reasoning, not just the final choice.

### Question 3A — The Mismatched Build

A technician is asked to upgrade a 3D animation studio's rendering workstation. The current machine has an Intel Core i9 processor (24 cores), 128 GB of ECC RAM, and a fast NVMe SSD — but the GPU is a high-end consumer gaming card (NVIDIA GeForce RTX 4090). The artists are reporting that their renders complete correctly in most scenes, but they see occasional shading artifacts in complex transparency calculations, and the rendering software occasionally crashes without warning during long overnight batch renders.

In 150-200 words, explain what component should be replaced, why the symptoms point specifically to that component, and what the replacement should be. Reference the specific technical distinction between the two GPU types that explains the observed symptoms.

Your response: ___________________________________________________________

### Question 3B — Advising a First-Time Builder

A friend asks you to help them build a PC. They say they want to "do everything" — run a few virtual machines for development, play games on weekends, and eventually set up a home server for backups. They have a moderate budget and want one machine.

In 150-200 words, explain the challenge with designing a single PC for all three of these workloads simultaneously. Identify the primary hardware conflict between the gaming build priorities and the virtualization host priorities, and suggest a realistic compromise configuration that reasonably addresses each workload without extreme cost. You may also recommend splitting the workloads across two machines if that is the better technical answer — just justify your recommendation.

Your response: ___________________________________________________________

---

## Deliverables and Submission

Submit one document containing all of the following:

1. Part 1 — All four scenario response tables and written answers (A1-A3, B1-B4, C1-C3, D1-D4)
2. Part 2 — Completed component matching table with reasoning column filled in
3. Part 3 — Both written responses (3A and 3B), each 150-200 words

Accepted formats: PDF, DOCX, or Google Docs link with comment access enabled.

---

## Grading Rubric

| Section | Points Possible | Criteria |
|---|---|---|
| Part 1 — Scenario A (Architecture Firm) | 10 | Correct build type identification; accurate component selections; written justifications reference professional GPU vs. consumer GPU distinction |
| Part 1 — Scenario B (Virtualization Host) | 10 | Correct RAM and CPU math with work shown; correct conclusion about GPU; clear explanation of why virtualization does not need gaming GPU |
| Part 1 — Scenario C (Gaming PC) | 10 | Correct GPU tier selection with resolution/frame rate reasoning; accurate CPU priority explanation; correct response to the workstation GPU advice |
| Part 1 — Scenario D (NAS) | 10 | RAID comparison table fully and accurately completed; sound RAID recommendation with justification; correct explanation of ECC RAM and ZFS risk |
| Part 2 — Component Matching | 30 | Each of the 10 components correctly assigned to appropriate build type(s) with accurate one-sentence reasoning (3 points each) |
| Part 3 — Written Responses | 30 | Each response 150-200 words; demonstrates technical accuracy; correctly identifies the core hardware principle at issue; references specific component properties (15 points each) |
| **Total** | **100** | |

---

## Troubleshooting Notes

If you are unsure about a component recommendation, the Reading Guide Section 2-5 specification tables provide specific guidance for each build type. Professor Messer's free study notes at professormesser.com (220-1101, Domain 3.4) include additional use-case comparisons.

Do not use fabricated URLs or cite product reviews for component justifications. Base your answers on the technical principles covered in this module.
