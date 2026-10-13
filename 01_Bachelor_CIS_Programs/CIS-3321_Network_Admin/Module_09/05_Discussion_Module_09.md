# Discussion Forum: Module 09 — Network Services: DNS, DHCP, and NTP

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

### Overview

This week's discussion applies DNS, DHCP, and NTP concepts to real-world incident and design scenarios. You will select one of three scenarios and write a substantive initial post of 175–225 words. After posting, reply to at least two classmates who chose different scenarios.

---

### Choose One Scenario

#### Scenario A: University DNS Outage

A university's IT team receives a flood of help desk tickets at 8:00 AM on a Monday morning. Students and faculty report that websites are unreachable, email is not working, and the learning management system (Canvas) cannot be accessed. One IT technician notices that machines can still reach destinations by IP address. The DNS infrastructure consists of two authoritative name servers for the university's domain and one internal recursive resolver that all campus clients use. Investigation reveals the internal resolver has not responded to queries since 2:00 AM.

Respond to all three questions:

1. Explain the full DNS resolution path that a campus client follows when resolving a hostname for the first time. Identify each DNS component involved, what question each component answers, and where the process fails given the scenario description.

2. The outage affects the entire campus but clients can still reach IPs directly. Identify the specific DNS component that has failed and explain why a failure of that single component would cause campus-wide name resolution failure even though the two authoritative name servers are still running.

3. While troubleshooting, the IT team runs nslookup from an affected workstation and receives a "non-authoritative answer." A junior technician interprets this as meaning the DNS data is unreliable or expired. Correct this misunderstanding: explain what a non-authoritative answer actually means, whether it indicates a problem in this context, and what specific nslookup response would confirm the resolver is down.

---

#### Scenario B: DHCP Scope Exhaustion at a Conference Center

A conference center's network administrator receives calls from guests reporting that they cannot connect to the Wi-Fi. The wireless network is operational and clients are associating to access points successfully. When a guest opens their device network settings, the IP address shows 169.254.x.x. The DHCP server log shows the scope for the conference VLAN (192.168.100.0/24) has 0 addresses available. The scope was configured with a 1-hour lease time and 200 available addresses. The conference today has 180 attendees, but the room has hosted three back-to-back events over the past six hours. Staff workstations on a separate VLAN are unaffected.

Respond to all three questions:

1. Explain what the 169.254.x.x address indicates, what process a Windows client follows when it cannot receive a DHCP response, and why this address range prevents network communication with other devices on the conference VLAN.

2. Analyze why the scope is exhausted despite only 180 current attendees. Your explanation must reference DHCP lease time, the DORA process, and what happens to leases when clients from previous events disconnected without formally releasing their addresses.

3. Propose two configuration changes the administrator could make to prevent this from recurring at future events. For each change, identify the specific DHCP parameter being modified, explain what the change does technically, and describe any trade-off the administrator should be aware of.

---

#### Scenario C: NTP Drift and Kerberos Authentication Failures

A financial services firm's IT security team receives escalating alerts at 6:30 AM: users across three branch offices cannot log into workstations. The error message displayed is "There are currently no logon servers available to service the logon request." Investigation reveals the branch offices connect to a central domain controller via VPN. The central data center's NTP infrastructure relies on a GPS-synchronized primary time server (stratum 1). Overnight, the fiber path to the data center experienced a brief outage lasting 45 minutes, during which the stratum 1 server was unreachable by branch office NTP clients. Branch office clocks drifted during this window.

Respond to all three questions:

1. Explain the NTP stratum hierarchy: what is a stratum 0 reference clock, what is a stratum 1 server, and how does stratum number relate to accuracy and proximity to the time source? Where do the branch office NTP clients fit in this hierarchy, and why did a 45-minute NTP outage cause clock drift rather than immediate failure?

2. Kerberos authentication is described as having a maximum clock skew tolerance. Explain what clock skew is, what the standard maximum tolerance is, and exactly what happens at the Kerberos level when a workstation's clock exceeds that threshold. Why is clock synchronization a security requirement rather than just an operational convenience?

3. Propose a resilient NTP architecture for this firm that would have prevented the authentication failure. Identify at least two specific design changes, explain which NTP stratum tier each change addresses, and explain how the design prevents branch office clock drift during a data center connectivity outage.

---

### Response Requirements

Initial Post (due Wednesday at 11:59 PM):

- Choose exactly one scenario (A, B, or C)
- Write 175–225 words
- Identify which scenario you chose in your first sentence
- Answer all three sub-questions for your chosen scenario
- Use correct terminology: DNS resolver, authoritative name server, root server, TLD server, DORA, DHCP relay agent, APIPA, lease time, scope, NTP stratum, clock skew, Kerberos, TTL, non-authoritative answer, giaddr, DHCP snooping

Peer Responses (due Sunday at 11:59 PM):

- Reply to at least two classmates who chose different scenarios than you
- Each reply must be at least 60 words
- Provide a specific technical addition, correction, or alternative design consideration — do not simply agree or summarize

---

### Grading Rubric (10 Points Total)

Initial Post — 6 Points:

- 5–6 points: All three sub-questions answered with accurate technical terminology, correct protocol concept application, and meets the 175–225 word count.
- 3–4 points: Addresses most sub-questions but lacks technical depth or contains a specification error (such as incorrect port numbers or stratum values).
- 1–2 points: Post is incomplete, off-topic, or contains significant inaccuracies.
- 0 points: No initial post submitted.

Peer Responses — 4 Points:

- 4 points: Substantive responses to two classmates who chose different scenarios, each at least 60 words, adding genuine technical value.
- 2 points: Only one peer response, or both responses lack technical substance.
- 0 points: No peer responses submitted.

---

### Professor Nash's Note

DNS, DHCP, and NTP are the invisible backbone of every network. When any one of them fails, the symptoms look like something else entirely — "the network is down," "I can't log in," "websites don't work." The ability to trace those symptoms back to the correct root cause is the difference between an hour-long outage and a day-long one. Notice that all three scenarios this week involve a single point of failure cascading into something much larger. Your reading covered redundancy designs for each of these services. As you write your posts, think not just about what went wrong but what architecture would have prevented the impact. That's the design thinking Network+ and real-world engineering both require.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash
