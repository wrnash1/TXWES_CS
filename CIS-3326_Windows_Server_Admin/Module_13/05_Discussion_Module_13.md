# Discussion Forum: Module 13 — Storage Spaces and Advanced Storage

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Microsoft Windows Server Administration

---

## Discussion Prompt

Storage decisions have long-term consequences — the wrong resiliency choice, a missing backup, or unencrypted drives can mean catastrophic data loss or a compliance violation. This discussion asks you to apply the module's storage concepts to realistic scenarios requiring trade-off analysis and design justification.

---

## Primary Post (Due by Thursday)

Respond to **one** of the following prompts in 200–300 words. Clearly state which prompt you are answering at the top of your post.

---

### Prompt A — Storage Spaces Design for a Small Business

A small manufacturing company has asked you to design a storage solution for their new Windows Server 2022 file server. Their requirements are:

- Store 2 TB of active production data (CAD files, project documents)
- Store 8 TB of archive data (completed project files accessed rarely)
- Budget is limited — they cannot afford enterprise SAN hardware
- They need to survive at least one disk failure without data loss

Address the following in your post:

- Which Storage Spaces resiliency type would you recommend for each data category, and why?
- How many physical disks would your design require at minimum?
- Would you use NTFS or ReFS for these volumes, and why?
- What limitations should you explain to the client about Storage Spaces compared to enterprise SAN storage?

---

### Prompt B — iSCSI vs. Fibre Channel in the Enterprise

Your organization is building a new server infrastructure for a SQL Server cluster. The storage team is debating between using iSCSI and traditional Fibre Channel (FC) for the shared storage. You have been asked to present both sides.

Address the following in your post:

- What are the key technical advantages of iSCSI over Fibre Channel (cost, infrastructure, management)?
- What are the scenarios where Fibre Channel is still the superior choice (latency, throughput, isolation)?
- How would you secure an iSCSI storage network in a production environment (VLAN isolation, CHAP, MPIO)?
- What is your recommendation for a 10-node SQL Server cluster, and why?

---

### Prompt C — BitLocker Strategy for a Healthcare Organization

A regional healthcare organization must comply with HIPAA, which requires encryption of data at rest on all servers storing Protected Health Information (PHI). They have 40 Windows Servers across three data centers. Some servers reboot overnight for patching; others run 24/7.

Address the following in your post:

- What BitLocker configuration would you recommend for servers that reboot automatically overnight?
- What configuration would you recommend for servers in a remote data center where no staff are present to enter a PIN?
- How should recovery keys be stored and managed at this scale (40 servers)?
- What is the difference between BitLocker protecting data from physical theft versus protecting it from unauthorized OS-level access?

---

## Reply Posts (Due by Sunday)

Write substantive replies to **two** classmates. Each reply should be 100–150 words and do at least one of the following:

- Identify a risk or edge case in the original recommendation that was not addressed
- Propose an alternative design with technical justification
- Connect the storage topic to a related concept from Module 12 (Hyper-V) or Module 14 (Security)
- Ask a specific follow-up question that would require the classmate to extend their technical analysis

---

## Grading Criteria

Grades are based on the following point distribution:

- Primary post addresses all prompt sub-questions: 40 points
- Technical accuracy and correct use of module terminology: 25 points
- Analytical depth — design justification, not just description: 15 points
- Two substantive reply posts: 20 points
- Total: 100 points

---

## Tips for a Strong Post

Storage discussions are strengthened by specific numbers and comparisons. Instead of saying "mirror is better for important data," say "a two-way mirror requires at least two disks and stores one redundant copy, surviving one disk failure — sufficient for this workload's RTO requirements."

If you are answering Prompt C, research HIPAA's specific language around encryption — it is an "addressable" rather than "required" implementation specification, which creates an interesting compliance nuance worth discussing.

---

## Looking Ahead

Module 14 covers Windows Server Security in depth — Windows Defender, Windows Firewall with Advanced Security, Just Enough Administration, Credential Guard, and LAPS. Note that BitLocker from this module overlaps with Module 14's security theme. As you write your discussion, consider how storage encryption fits into a broader layered security strategy.
