# Discussion Forum: Module 01 - Linux Installation and VM Setup

## CIS-3325 OS Administration | Texas Wesleyan University

**Certification Alignment:** CompTIA Linux+ (XK0-005)
**Total Points:** 10
**Initial Post Due:** Wednesday at 11:59 PM
**Peer Responses Due:** Sunday at 11:59 PM

---

### Instructions

Choose one of the three scenarios below. Write an initial post of 175 to 225 words that addresses
all three sub-questions for your chosen scenario. After posting, respond to at least two classmates
who chose different scenarios. Each response should be at least 75 words and add substantive
technical content, not just agreement.

---

### Scenario A - Enterprise Server Deployment Decision

Your company is deploying twenty new Linux servers to host an internal web application. A junior
engineer suggests installing Ubuntu Desktop on each server because "it is easier to manage with
a GUI." You need to push back on this recommendation.

1. Explain the security argument against installing a desktop environment on a production server,
   using the term attack surface in your response.
2. Describe at least two specific types of unnecessary software or services that a desktop install
   adds to a server that a minimal install avoids.
3. If a new administrator truly needs a graphical view of server metrics, what approach would you
   recommend that does not require installing a full desktop on the server itself?

---

### Scenario B - Hypervisor Selection for a New Data Center

Your organization is building a new data center with forty physical servers. The IT director asks
you to recommend a hypervisor strategy. You must choose between Type 1 and Type 2 hypervisors.

1. Explain the fundamental technical difference between a Type 1 and Type 2 hypervisor, using
   at least one real product name as an example of each type.
2. Describe two specific performance or management advantages that Type 1 hypervisors provide
   in a production data center compared to Type 2.
3. Is there any legitimate use case where a Type 2 hypervisor would be preferable over Type 1
   even in a professional setting? Explain your reasoning.

---

### Scenario C - Disk Corruption Recovery Planning

A Linux server you manage suddenly fails to boot. The GRUB menu appears but selecting the default
kernel leads to a kernel panic. You need to understand what happened and how to recover.

1. Identify at least two components that could cause this symptom: GRUB loads but the kernel
   fails to start. Explain what each component does in the boot process.
2. Linux systems commonly use separate partitions for /boot, /, /home, and /var. Explain how
   having /boot on a separate partition might help or complicate recovery in this scenario.
3. How does taking regular VM snapshots in VirtualBox prevent this type of scenario from becoming
   a data loss event in a lab or development environment?

---

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Initial Post (6 points total) | |
| Addresses all three sub-questions with technical accuracy | 3 |
| Demonstrates understanding of Module 01 concepts | 2 |
| Meets the 175-225 word requirement | 1 |
| Peer Responses (4 points total) | |
| Response 1: substantive, at least 75 words, adds technical content | 2 |
| Response 2: substantive, at least 75 words, adds technical content | 2 |

A grade of 0 is recorded for any of the following: no initial post submitted, initial post
is less than 100 words, peer responses are fewer than 50 words or say only "great post" without
technical substance.

---

### Professor Nash's Closing Note

The decision of which OS to install, which hypervisor to use, and how to partition a disk are
not just textbook concepts. Every system you build for the rest of your career starts with these
choices. Getting them right means less rework, fewer vulnerabilities, and easier recovery when
something goes wrong. Think carefully about the scenarios above and back up your reasoning with
the technical vocabulary you are learning. I am looking forward to reading your perspectives.
