# Quiz: Module 05 – QoS, High Availability & Network Automation
## CSC-6361 Advanced Computer Networks | Graduate Level
## 10 Questions | 30-Minute Time Limit | 1 Attempt
## Due: Sunday, November 22, 2026 at 11:59 PM CST

---

### Question 1 (Multiple Choice — 10 pts)
A network engineer configures LLQ (Low Latency Queuing) for VoIP traffic with `priority percent 20` on a 100 Mbps WAN interface. VoIP traffic is currently using 15 Mbps. Data traffic suddenly bursts and tries to use the full 100 Mbps. What happens to VoIP traffic?

- A) VoIP is throttled to 15% of the interface bandwidth. ❌
- B) VoIP is guaranteed its 20 Mbps (20%) allocation — data traffic cannot consume the VoIP portion. The LLQ strict priority queue is serviced first before any other queue. ✅
- C) VoIP and data traffic compete equally for the 100 Mbps. ❌
- D) VoIP is placed in the default queue and data is prioritized. ❌

**Answer:** B — LLQ (implemented via `priority` in a policy map) creates a strict priority queue. VoIP traffic is always serviced first, up to its configured rate (20 Mbps in this case). Other queues only receive service after the priority queue is empty or exhausted. This guarantees the VoIP application never waits behind a file transfer.

---

### Question 2 (Multiple Choice — 10 pts)
What is the key behavioral difference between traffic **policing** and traffic **shaping**?

- A) Policing only works on inbound traffic; shaping only works on outbound. ❌ (both can technically be applied in either direction, though policing inbound and shaping outbound is the common pattern)
- B) Policing drops or re-marks traffic that exceeds the configured rate; shaping buffers excess traffic in a queue and sends it later, introducing delay but not dropping packets. ✅
- C) Policing is a Layer 3 mechanism; shaping operates at Layer 2. ❌
- D) Shaping immediately drops traffic above the committed rate; policing queues it. ❌

**Answer:** B — Policing has no buffer — it acts immediately, either dropping excess packets or remarking their DSCP to a lower value. Shaping maintains a buffer where excess packets wait until the token bucket refills, introducing delay but preventing drops. Shaping is typically preferred for traffic sent toward a carrier circuit where drops would cause TCP retransmissions and application performance problems.

---

### Question 3 (Scenario — 10 pts)
A DSCP marking policy map is applied **inbound** on an access switch port connected to a user's PC. The class-map matches traffic with DSCP value 0 (Best Effort) and sets it to DSCP AF11. A second class-map matches DSCP EF and sets it to DSCP 0. Why would an enterprise deploy this unusual "downgrade" policy for DSCP EF traffic arriving from a PC port?

- A) To comply with RFC 2474 which prohibits EF marking on access layer ports. ❌
- B) To prevent users from marking their own PC traffic as high-priority (DSCP EF) to receive voice-class treatment. EF markings are untrusted from end-user PCs and must be reset to prevent QoS manipulation. ✅
- C) To enable QoS for the PC while conserving EF markings for the IP phone on the same port. ❌
- D) This policy would break the QoS design and should never be deployed. ❌

**Answer:** B — This is a standard **QoS trust boundary** policy. End-user PCs cannot be trusted to mark their own traffic correctly — a user could configure their web browser or BitTorrent client to mark traffic as DSCP EF (voice quality) to gain unfair priority. The enterprise policy strips EF markings from PC ports and re-marks them to lower-priority values, while trusting EF markings only from IP phones (identified by CDP device classification).

---

### Question 4 (Multiple Choice — 10 pts)
HSRP is configured on two distribution switches. DS1 has priority 110 with preempt enabled. DS2 has priority 100. DS1 goes offline for maintenance. DS2 becomes Active. When DS1 comes back online, what happens?

- A) DS2 remains Active because it was promoted during the outage. ❌
- B) DS1 immediately becomes Active again because it has a higher priority AND preempt is enabled. ✅
- C) DS1 becomes Active only if DS2's priority is manually decreased. ❌
- D) Both switches enter the Speak state and re-elect a new Active, which could be either DS1 or DS2. ❌

**Answer:** B — Preemption (`standby X preempt`) causes a router to claim the Active role if its priority is higher than the current Active router. When DS1 comes back with priority 110 and DS2 is Active with priority 100, DS1 sends a coup HSRP message and becomes Active. Without preemption, DS2 would remain Active even after DS1 recovers — which is undesirable in a properly designed HA network.

---

### Question 5 (Multiple Choice — 10 pts)
What is the primary advantage of GLBP over HSRP in an enterprise campus distribution layer?

- A) GLBP supports more FHRP groups per interface. ❌
- B) GLBP allows multiple routers to simultaneously forward traffic for the same virtual IP, providing actual load balancing across redundant uplinks — not just failover. ✅
- C) GLBP uses an open standard (IEEE RFC 5798), while HSRP is Cisco proprietary. ❌
- D) GLBP has faster convergence than HSRP because it uses a different hello mechanism. ❌

**Answer:** B — HSRP and VRRP only allow one Active router at a time — all traffic for a VLAN goes through the Active router, while the Standby router sits idle. GLBP uses multiple **Active Virtual Forwarders (AVFs)** — each AVF responds to ARP with a different virtual MAC address, so different hosts use different physical gateways. Both routers forward traffic simultaneously, effectively doubling the available gateway bandwidth.

---

### Question 6 (Multiple Choice — 10 pts)
A network engineer uses Netmiko to automate configuration changes across 100 routers. The script connects to each router sequentially. After running for 45 minutes, the engineer notices only 30 routers were configured before the script timed out. What is the most efficient improvement to make?

- A) Increase the SSH timeout value in Netmiko's ConnectHandler. ❌
- B) Implement **parallel/concurrent connections** using Python's threading or `concurrent.futures` module so multiple routers are configured simultaneously. ✅
- C) Switch from Netmiko to Ansible, which is always faster. ❌
- D) Use Telnet instead of SSH to reduce connection overhead. ❌

**Answer:** B — Sequential connections mean each router's configuration is blocked by the previous one. Using Python's threading (`ThreadPoolExecutor`) allows 10–20 routers to be configured simultaneously, reducing the total runtime from 45 minutes to a few minutes. Ansible also handles this parallelism natively (via `forks` configuration).

---

### Question 7 (Multiple Choice — 10 pts)
An Ansible playbook uses the `cisco.ios.ios_ntp_global` module with `state: merged`. What does `merged` mean in the context of Ansible's network automation?

- A) The playbook will first delete all existing NTP configuration, then apply the new configuration. ❌
- B) The playbook adds the specified configuration to the existing configuration without removing unrelated settings that already exist on the device. ✅
- C) The playbook merges configurations from two different inventory files. ❌
- D) `merged` is the same as `replaced` in Ansible network modules. ❌

**Answer:** B — Ansible network modules support several state values: `merged` (add specified config to existing), `replaced` (replace the entire resource with the specified config), `deleted` (remove the specified config), `overridden` (replace all global configuration for that resource), and `gathered` (read from device into Ansible facts). Using `merged` is safe for pushing new NTP servers without accidentally removing other existing NTP settings.

---

### Question 8 (Scenario — 10 pts)
A RESTCONF GET request is sent to a Cisco IOS-XE router:
`GET https://192.168.1.1/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1`
The request returns HTTP 401. What is the most likely cause?

- A) RESTCONF is not enabled on the router. (This would return 404 or connection refused) ❌
- B) The authentication credentials provided in the HTTP Basic Auth header are incorrect or the user does not have the required privilege level. ✅
- C) The interface GigabitEthernet1 does not exist on the router. (This would return 404 Not Found) ❌
- D) The JSON content-type header is missing. (This would return 415 Unsupported Media Type for PUT/POST, not GET) ❌

**Answer:** B — HTTP 401 (Unauthorized) means the server received the request but rejected it due to authentication failure. For RESTCONF, this typically means the HTTP Basic Auth username/password is wrong, or the user account does not have privilege level 15. Verify credentials and that the user is configured with: `username admin privilege 15 secret [password]`.

---

### Question 9 (Short Answer — 10 pts)
Explain the difference between Expedited Forwarding (EF) and Assured Forwarding (AF) per-hop behaviors in DiffServ. For each, describe what specific traffic types it is designed for and how the network treats packets marked with each PHB. (3–4 sentences)

**Model Answer:** **Expedited Forwarding (DSCP 46)** provides the lowest possible latency, jitter, and packet loss — it is implemented as a strict priority queue (LLQ) that is always serviced before other queues. EF is designed for real-time traffic like VoIP RTP and is typically rate-limited (policed) to prevent it from starving other queues. **Assured Forwarding (AF)** provides multiple classes (AF11-AF43) with different drop precedences — each AF class guarantees a minimum bandwidth allocation via CBWFQ, and within each class, packets marked with higher drop precedence (e.g., AF13 vs. AF11) are dropped first during congestion, using **WRED (Weighted Random Early Detection)**. AF is designed for business-critical applications (SAP, databases) and interactive video that can tolerate slightly more delay than voice but still need priority over best-effort traffic.

---

### Question 10 (Short Answer — 10 pts)
What is BFD (Bidirectional Forwarding Detection), and why would a network engineer configure it alongside HSRP in an enterprise distribution layer? What failure scenario does BFD detect that HSRP alone would be slow to respond to? (3–4 sentences)

**Model Answer:** **BFD** is a lightweight, sub-second failure detection protocol that continuously sends short "hello" packets between two network devices on a specific path. When configured with HSRP (`standby 1 bfd`), BFD notifies HSRP immediately if the forwarding path to the Active router fails — triggering a near-instant failover rather than waiting for the HSRP dead timer to expire (default: 10 seconds). The critical scenario BFD catches that HSRP alone misses is a **unidirectional forwarding failure**: if the physical link is still up (so HSRP still receives hellos) but the forwarding path has broken at the data plane level (e.g., a hardware ASIC failure that stops forwarding packets but keeps the interface "up"), BFD detects that data plane traffic is no longer getting through and triggers the failover, while HSRP without BFD would never detect the problem and traffic would continue to be blackholed.
