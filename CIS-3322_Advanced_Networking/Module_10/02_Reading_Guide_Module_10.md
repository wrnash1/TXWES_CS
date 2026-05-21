# Reading Guide: Module 10 - Access Control Lists (ACLs)
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 10 - Access Control Lists (ACLs)**! This week's study material focuses on the core foundations and configuration mechanics of **Access Control Lists (ACLs)** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Standard vs Extended ACLs**: Standard ACLs (numbered 1–99, 1300–1999) filter traffic based **only on source IP address** and should be placed as close to the destination as possible to avoid blocking legitimate traffic to other destinations. Extended ACLs (numbered 100–199, 2000–2699) filter on source IP, destination IP, protocol (TCP/UDP/ICMP), and port numbers — they should be placed as close to the source to stop unwanted traffic early.
*   **Numbering schemes**: Standard numbered ACLs use ranges 1–99 and 1300–1999. Extended numbered ACLs use 100–199 and 2000–2699. Named ACLs (both standard and extended) allow descriptive names instead of numbers and are easier to edit — individual entries can be inserted or deleted using sequence numbers. The CCNA exam tests whether a student can identify an ACL type from its number.
*   **Wildcard filtering**: ACL wildcard masks specify which bits of an address to match. A 0 bit means "must match," a 1 bit means "don't care." The `host` keyword is equivalent to wildcard 0.0.0.0 (match exact IP). The `any` keyword is equivalent to wildcard 255.255.255.255 (match all IPs). Example: `10.1.0.0 0.0.255.255` matches all addresses in the 10.1.0.0/16 range.
*   **Implicit deny**: Every ACL ends with an invisible `deny any any` entry that drops all traffic not explicitly permitted. This means an ACL with only `permit` statements will still block everything not listed. A common mistake is forgetting to add `permit ip any any` at the end of an ACL that is intended to allow most traffic while blocking only specific entries.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** ACLs fall under **Security Fundamentals (15%)** and **IP Services (10%)** of the CCNA 200-301 exam. Expect 3–5 ACL questions including reading ACL output from `show access-lists` and identifying placement.
*   **Placement rule — memorize this:** Standard ACLs = close to destination. Extended ACLs = close to source. The exam frequently asks "where should this ACL be applied?" given a topology diagram.
*   **Inbound vs outbound:** `ip access-group [name/number] in` filters packets arriving on the interface before routing. `ip access-group [name/number] out` filters packets leaving after routing. Getting direction wrong is a common exam and real-world mistake.
*   **Named ACL advantage:** You can add or delete specific lines using sequence numbers (e.g., `no 10` removes line 10 from a named ACL). Numbered ACLs require deletion and recreation of the entire ACL to make changes.
*   **Study Resource:** Watch the ACL episodes in the Jeremy's IT Lab CCNA free playlist, which cover standard vs extended ACL configuration, wildcard mask calculation, and interface application direction: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for the multi-part "Standard ACLs" and "Extended ACLs" episodes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Access Control Lists** in the Cisco Skills for All CCNA course. The content includes Packet Tracer labs where you configure and verify standard and extended ACLs on router interfaces: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Enterprise Networking, Security, and Automation" — the ACL chapter.
*   **Required Video:** Watch the ACL episodes in the Jeremy's IT Lab CCNA complete playlist. These videos cover ACL syntax, wildcard masks, placement best practices, and `show access-lists` output interpretation: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create extended ACL: `access-list 101 permit tcp any host 10.1.1.5 eq 80`**: This entry permits TCP traffic from any source to host 10.1.1.5 on port 80 (HTTP). The implicit deny at the end blocks all other traffic. Test by pinging and telnetting from different sources to verify matching behavior.
*   **Apply ACL to interface: `ip access-group 101 in`**: Apply the ACL to an interface in the inbound or outbound direction. Verify the application with `show ip interface [id]` which lists any ACL applied in each direction.
*   **Verify matches: `show access-lists`**: This command shows each ACL entry along with a match counter showing how many packets have matched that specific entry. Use this to confirm your ACL is working as intended.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Access Control Lists** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the ACL episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
