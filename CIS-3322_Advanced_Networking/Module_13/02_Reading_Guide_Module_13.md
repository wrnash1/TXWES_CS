# Reading Guide: Module 13 - Quality of Service (QoS) Fundamentals
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 13 - Quality of Service (QoS) Fundamentals**! This week's study material focuses on the core foundations and configuration mechanics of **Quality of Service (QoS) Fundamentals** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Traffic classification and marking (CoS, DSCP)**: QoS classification identifies traffic types (voice, video, data) and marking assigns a priority value to packets so network devices can treat them appropriately. **CoS (Class of Service)** is a 3-bit field in the 802.1Q header (Layer 2), supporting 8 priority values (0–7). **DSCP (Differentiated Services Code Point)** is a 6-bit field in the IPv4 ToS byte (Layer 3), supporting 64 values including standard PHBs like EF (Expedited Forwarding, value 46) for voice and AF (Assured Forwarding) classes for data.
*   **Queuing mechanisms (FIFO, WFQ)**: When congestion occurs, routers use queuing to manage which packets are sent next. **FIFO (First-In, First-Out)** is the default — no prioritization, packets are sent in arrival order. **WFQ (Weighted Fair Queuing)** automatically classifies traffic into flows and gives lower-bandwidth flows proportionally more bandwidth to prevent starvation. **LLQ (Low Latency Queuing)** adds a strict-priority queue for voice traffic on top of WFQ, ensuring real-time traffic is never delayed.
*   **Congestion avoidance**: Mechanisms that proactively drop packets before a queue fills completely, preventing TCP synchronization (where all TCP flows simultaneously slow down). **WRED (Weighted Random Early Detection)** monitors queue depth and randomly drops lower-priority packets when thresholds are crossed, triggering TCP senders to reduce their transmission rate gradually and smoothly.

---

### 2. Certification Exam Tips
*   **CCNA Domain:** QoS falls under **IP Services (10%)** of the CCNA 200-301 exam. Expect 2–3 conceptual QoS questions. The exam does not require you to configure full MQC QoS policies, but you must understand the concepts.
*   **Layer 2 vs Layer 3 marking:** CoS = Layer 2 (802.1Q tag), DSCP = Layer 3 (IP header). The exam will ask which field is used at each layer. Note that CoS markings are lost when a frame is de-tagged — only DSCP survives end-to-end across routed hops.
*   **Voice QoS requirements:** Voice traffic requires low latency (under 150ms one-way), low jitter (under 30ms), and low packet loss (under 1%). It is typically marked DSCP EF (46) and placed in a priority queue. The CCNA exam tests whether students know these thresholds.
*   **MQC structure:** Cisco's Modular QoS CLI (MQC) uses three elements: `class-map` (classify traffic), `policy-map` (define actions per class), `service-policy` (apply policy to interface). The exam expects awareness of this three-step structure.
*   **Study Resource:** Watch the QoS episodes in the Jeremy's IT Lab CCNA free playlist, which cover classification, marking, queuing, and the MQC configuration model: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for the "Quality of Service" episodes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Quality of Service** in the Cisco Skills for All CCNA course. The content includes QoS model comparisons (IntServ vs DiffServ), DSCP value tables, and queuing algorithm descriptions: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Enterprise Networking, Security, and Automation" — the QoS chapter.
*   **Required Video:** Watch the QoS episodes in the Jeremy's IT Lab CCNA complete playlist. The videos clearly explain CoS vs DSCP, voice requirements, queuing types, and the MQC configuration structure with Packet Tracer: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a class-map to match VoIP traffic**: Use `class-map match-all VOIP` with `match ip dscp ef` to classify packets marked with DSCP EF (46). Alternatively, match by access group or protocol using `match protocol rtp`.
*   **Define a policy-map prioritizing VoIP to high priority queue**: Create `policy-map QoS-Policy` and assign the VOIP class to `priority [bandwidth-kbps]` for LLQ (strict priority). Assign remaining classes to `bandwidth [kbps]` or `fair-queue` for WFQ treatment.
*   **Apply policy-map to interface: `service-policy output QoS-Policy`**: Apply the policy in the outbound direction on the WAN or congestion-prone interface. Verify with `show policy-map interface [id]` to see queue statistics and drop counters.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Quality of Service** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the QoS episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
