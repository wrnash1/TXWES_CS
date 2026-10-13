# Discussion Forum: Module 07 — Network Monitoring and Troubleshooting Tools

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

### Overview

This week's discussion connects network monitoring and troubleshooting tools to real-world decision scenarios. You will select one of three scenarios below and respond with a substantive initial post of 175–225 words. After posting, reply to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: Diagnosing Intermittent Connectivity in a Branch Office

A branch office of 40 employees reports intermittent internet connectivity — about once per hour, all users lose internet access for 30–90 seconds, then it restores on its own. Internal file server access is never interrupted. The branch connects to the internet through a single edge router. The ISP claims their link is healthy.

Respond to all three questions:

1. List three specific diagnostic tools you would run from the branch edge router or a workstation during or after one of the outage windows. For each tool, explain what specific information it provides and what failure condition it would confirm or eliminate.

2. The problem only affects internet access, not internal traffic. Using the divide-and-conquer troubleshooting approach, describe the sequence of ping tests you would run and what each result — success or failure — would tell you about where the fault lies.

3. You decide to implement proactive monitoring so the next occurrence is captured automatically rather than relying on user reports. Which protocol would you configure on the edge router to forward log messages to a central server during outage events, and which protocol would you configure to alert the monitoring system when the WAN interface goes down? Specify the port numbers involved for each.

---

#### Scenario B: Wireshark Analysis of a Security Incident

A security alert fires on a workstation showing unusual outbound traffic volume to an external IP address at 2:00 AM. The workstation belongs to an accountant who does not work night shifts. You have a 30-minute Wireshark PCAP file captured during the event.

Respond to all three questions:

1. Write four specific Wireshark display filters you would apply to investigate this capture. For each filter, explain what you are looking for and what it would reveal if packets matching the filter are present.

2. In your Wireshark capture, you observe multiple TCP SYN packets from the workstation to the external IP on port 443, but no SYN-ACK responses are visible. Then, 15 minutes into the capture, you see a successful three-way handshake to the same destination. Describe what the initial SYN-without-SYN-ACK pattern suggests, and what the eventual successful handshake means in the context of this incident.

3. After analysis, you determine the workstation was communicating with a command-and-control server. You want to implement ongoing detection for this type of communication across the entire network without capturing full packet contents. Which monitoring technology would you deploy, what data does it collect, and why is it more scalable than running Wireshark on every network segment?

---

#### Scenario C: Building a Monitoring Architecture for a New Campus

You are the lead network administrator for a new 500-person corporate campus. Leadership asks you to design a monitoring architecture that provides three capabilities: (1) automated alerting when any network device exceeds 80% CPU or interface utilization, (2) the ability to identify which users and applications are driving WAN bandwidth consumption at any given time, and (3) centralized storage of all device log messages for 90-day compliance retention.

Respond to all three questions:

1. Map each of the three monitoring requirements to a specific protocol or technology. For each, identify the protocol name, the UDP/TCP port it uses, and whether the data flows from devices to a collector (push) or from a collector to devices (poll/pull).

2. For the automated alerting requirement, you must choose between SNMPv2c and SNMPv3. The campus management network is shared with guest wireless traffic on a separate VLAN but traverses the same physical switches. Explain which SNMP version you would choose and why, specifically addressing what an attacker on the guest VLAN could do if they captured SNMPv2c traffic.

3. The network baseline you collect during the first month of operation shows that WAN utilization averages 45% during business hours and peaks at 78% on Tuesday afternoons. Three months later, Tuesday peaks are regularly hitting 95%. Describe how you would use the baseline data to make a data-driven case to leadership for a WAN capacity upgrade, and identify which monitoring technology would provide the specific application-level evidence needed to justify the upgrade.

---

### Response Requirements

Initial Post (due Wednesday at 11:59 PM):

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct terminology: ping, traceroute, nslookup, netstat, Wireshark, SNMP, SNMPv3, NetFlow, syslog, TCP three-way handshake, display filter, baseline, divide-and-conquer

Peer Responses (due Sunday at 11:59 PM):

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Offer a specific technical addition, correction, or alternative approach — do not simply agree or summarize

---

### Grading Rubric (10 Points Total)

Initial Post — 6 Points:

- 5–6 points: All three sub-questions answered with accurate technical detail, correct tool and protocol terminology, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but lacks technical depth or contains a specification error.
- 1–2 points: Post is incomplete, off-topic, or contains significant inaccuracies.
- 0 points: No initial post submitted.

Peer Responses — 4 Points:

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding genuine technical value.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

The tools covered in this module are not just exam topics — they are the first tools you reach for every single time something breaks. Ping, traceroute, nslookup, and netstat are available on virtually every operating system without any installation. Wireshark, SNMP, NetFlow, and syslog are the tools that separate administrators who react to problems after users complain from those who detect and resolve issues before users notice. The monitoring architecture question in Scenario C is exactly the kind of design decision you will be asked to make as a senior network engineer. Think through the tool-to-requirement mapping carefully — each tool answers a different question about the network.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
