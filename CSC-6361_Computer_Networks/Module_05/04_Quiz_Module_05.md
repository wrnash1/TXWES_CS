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

---

> **Instructor Note — Questions 11–20:** These 10 questions are worth **5 pts each** (50 pts total). Enter as a separate quiz section or append to the existing quiz. Same format rules apply.

---

### Question 11 (Multiple Choice — 5 pts)
A network engineer configures the following MQC policy on a WAN interface:
```
class-map match-any VOICE
 match dscp ef
policy-map WAN-QOS
 class VOICE
  priority percent 20
 class class-default
  fair-queue
```
VoIP calls are working correctly, but users report that large file transfers are causing video conferencing to freeze intermittently. Video conferencing traffic is DSCP AF41. What is the most likely cause and fix?

- A) EF marking on VoIP is consuming too much bandwidth — reduce `priority percent` to 10. ❌
- B) Video conferencing traffic (DSCP AF41) is falling into `class-default` and competing equally with bulk file transfers. Add a dedicated class for AF41 with a `bandwidth percent` guarantee to protect it from best-effort traffic. ✅
- C) `fair-queue` in `class-default` is broken and must be replaced with `queue-limit`. ❌
- D) Video conferencing requires LLQ (`priority`) — assign AF41 to the priority queue alongside EF. ❌

**Answer:** B — The policy only defines two classes: VOICE (EF) and class-default. AF41 video traffic has no dedicated class and falls into class-default where it competes equally with bulk file transfers (which are typically higher volume). The fix is to add a class for AF41 video with a minimum bandwidth guarantee:
```
class VIDEO
 bandwidth percent 30
```
This ensures video gets a minimum allocation even during congestion. Adding AF41 to the priority queue (option D) would be incorrect — the LLQ is designed for voice-quality traffic with strict rate bounds, not burst-tolerant video.

**Distractor Analysis:**
- A: Reducing VoIP allocation would not fix the video problem; they are in separate queues.
- C: `fair-queue` (WFQ) is functional — the problem is classification, not queuing algorithm.
- D: Mixing video into the LLQ strict priority queue risks starving data traffic and violates QoS design principles.

---

### Question 12 (Multiple Choice — 5 pts)
What does DSCP AF32 mean, and how does it compare to AF31 in terms of drop probability during congestion?

- A) AF32 and AF31 are in different Assured Forwarding classes and are treated completely independently by the network. ❌
- B) AF32 and AF31 are both in AF class 3, but AF32 has a **medium drop probability** compared to AF31's **low drop probability** — meaning AF32 packets are more likely to be dropped first when the queue becomes congested. ✅
- C) AF32 has a higher priority than AF31 — packets marked AF32 are forwarded before AF31 packets. ❌
- D) The number after AF3 indicates bandwidth allocation — AF32 gets twice the bandwidth of AF31. ❌

**Answer:** B — In the Assured Forwarding PHB (RFC 2597), the naming convention is AFxy where x is the class (1–4) and y is the drop precedence (1=low, 2=medium, 3=high). AF31 and AF32 are both in class 3, meaning they share the same bandwidth allocation. However, during congestion, WRED (Weighted Random Early Detection) is configured to start dropping AF32 packets at lower queue depths than AF31, protecting the more important AF31 traffic. This allows differentiation within a traffic class — e.g., transactional database traffic (AF31) is protected over batch database replication (AF32).

**Distractor Analysis:**
- A: AF31 and AF32 are in the same class (class 3) and share the same bandwidth guarantee.
- C: AF PHBs do not create strict priority relationships between drop precedence levels — they influence WRED drop thresholds.
- D: The digit after the class number indicates drop precedence, not bandwidth multiplier.

---

### Question 13 (Multiple Choice — 5 pts)
VRRP is configured on two routers. Router A has priority 120 and Router B has priority 100. Both are in the same VRRP group with virtual IP 10.1.1.1. Router A fails. Which statement about VRRP behavior is correct when Router A recovers?

- A) Router B remains Master indefinitely because it was promoted — VRRP does not support preemption. ❌
- B) Router A immediately becomes Master again upon recovery because VRRP enables preemption by default — unlike HSRP, which requires explicit preempt configuration. ✅
- C) A new VRRP election occurs but either router can become Master — priority is only used for the initial election. ❌
- D) Both routers enter backup state and a new Master is elected via multicast advertisement. ❌

**Answer:** B — A key behavioral difference between VRRP (RFC 5798) and HSRP is that VRRP enables preemption **by default** — a higher-priority router that recovers will automatically reclaim the Master role. HSRP requires explicit `standby X preempt` configuration to achieve the same behavior. This is a common exam trap: in VRRP, do not configure `preempt` (it is the default), while in HSRP, forgetting `preempt` means the higher-priority router never reclaims Active after recovery.

**Distractor Analysis:**
- A: VRRP does support preemption — it is enabled by default, unlike HSRP.
- C: Priority matters throughout VRRP's lifetime, not just the initial election.
- D: VRRP uses multicast advertisements on 224.0.0.18, but the election does not restart from scratch — the higher-priority preempting router sends a higher-priority advertisement and claims Master immediately.

---

### Question 14 (Scenario — 5 pts)
A network engineer runs `show standby brief` and sees:
```
Interface  Grp  Pri P State   Active          Standby         Virtual IP
Gi0/0      1    100   Standby  172.16.1.2      local           172.16.1.1
```
The router's priority is 100. The Active router at 172.16.1.2 has priority 90. Why is this router NOT becoming Active despite having a higher priority?

- A) The interface Gi0/0 is in err-disabled state and cannot assume the Active role. ❌
- B) Preemption is not enabled (`P` flag is absent) on this router — it will not claim the Active role even though its priority is higher than the current Active router's priority. ✅
- C) The HSRP version is mismatched between the two routers. ❌
- D) The virtual IP 172.16.1.1 is conflicting with a real interface IP on the network. ❌

**Answer:** B — The `P` flag in `show standby brief` indicates preemption is enabled. Its absence here means this router will not preempt the current Active router even though it has a higher priority (100 > 90). This is the most common HSRP misconfiguration in production: engineers configure higher priorities on the preferred router but forget to add `standby 1 preempt`. The fix is: `interface Gi0/0` → `standby 1 preempt`.

**Distractor Analysis:**
- A: The interface is clearly operational — it has an Active and Standby relationship established.
- C: HSRP version mismatch would prevent the routers from seeing each other's hellos at all.
- D: The virtual IP must not be the same as any real interface IP — if it were, the gateway would be broken, not just passive.

---

### Question 15 (Multiple Choice — 5 pts)
In NETCONF, what is the purpose of the `<candidate>` datastore, and how does it differ from `<running>`?

- A) `<candidate>` stores the startup configuration loaded at boot; `<running>` stores the active configuration. ❌
- B) `<candidate>` is a staging area where configuration changes can be built and validated before being committed to `<running>` — changes in `<candidate>` do not affect the device until a `<commit>` operation is issued. ✅
- C) `<candidate>` and `<running>` are identical — the distinction only applies to RESTCONF. ❌
- D) `<candidate>` is used only for rollback operations; `<running>` is the only writable datastore. ❌

**Answer:** B — NETCONF (RFC 6241) defines three standard datastores: `<running>` (currently active config), `<candidate>` (staging area for uncommitted changes), and `<startup>` (config loaded at boot). The `<candidate>` datastore enables a transactional workflow: make all changes to `<candidate>`, validate them with `<validate>`, then atomically apply them with `<commit>`. If validation fails, the `<running>` configuration is unchanged. This is fundamentally safer than traditional CLI where each command is applied immediately and a partially entered configuration can leave the device in a broken state.

**Distractor Analysis:**
- A: The startup configuration is in the `<startup>` datastore.
- C: NETCONF datastores are defined in RFC 6241 and are specific to NETCONF; RESTCONF uses a similar but slightly different model.
- D: `<candidate>` is actively written to and is the primary writable datastore in NETCONF-enabled configurations.

---

### Question 16 (Multiple Choice — 5 pts)
A YANG model defines a leaf node with `type uint32` and `range "0..1000"`. A NETCONF `<edit-config>` operation attempts to set the value to `2000`. What happens?

- A) The NETCONF agent silently truncates the value to 1000 and applies the configuration. ❌
- B) The NETCONF agent returns an `<rpc-error>` with error-type `application` and error-tag `invalid-value`, rejecting the operation without changing the running configuration. ✅
- C) The NETCONF agent applies the value but logs a warning to syslog. ❌
- D) The YANG model constraint is advisory only — IOS-XE applies values outside the defined range without error. ❌

**Answer:** B — YANG data models provide strict type validation enforced by the NETCONF agent. When an `<edit-config>` operation violates a `range` constraint, the server rejects the entire RPC and returns a structured `<rpc-error>` element containing the error details. The `<running>` or `<candidate>` datastore is not modified. This model-driven validation is one of the key advantages of NETCONF/YANG over traditional CLI scripting — constraint violations are caught before being applied, preventing misconfigurations that might only fail at runtime.

**Distractor Analysis:**
- A: NETCONF does not silently truncate values — it rejects non-conforming data.
- C: NETCONF error handling is via structured RPC errors, not syslog warnings.
- D: YANG constraints in IOS-XE are enforced by the NETCONF/RESTCONF stack, not advisory.

---

### Question 17 (Multiple Choice — 5 pts)
An Ansible playbook using `cisco.ios.ios_config` is run twice against the same router with the same configuration lines. On the second run, what behavior demonstrates Ansible's **idempotency** for this module?

- A) The second run fails because the configuration already exists and `ios_config` refuses to overwrite. ❌
- B) The second run succeeds and reports `changed: false` — Ansible compares the desired state against the current device configuration and makes no changes since they are already identical. ✅
- C) Ansible always pushes the configuration on every run regardless of current device state. ❌
- D) The second run requires `--force` flag to re-apply existing configurations. ❌

**Answer:** B — Idempotency means that running the same operation multiple times produces the same result as running it once. The `cisco.ios.ios_config` module achieves this by first checking whether the configuration lines already exist in the running configuration. If they do, Ansible marks the task as `ok` (not `changed`) and skips the SSH configuration push. This is critical for automation at scale — playbooks can run repeatedly via scheduled jobs without fear of causing unintended side effects or duplicate configuration entries.

**Distractor Analysis:**
- A: `ios_config` does not fail on pre-existing config — it simply reports no change.
- C: Some tools do re-push every time regardless; Ansible's resource modules are specifically designed to avoid this.
- D: No `--force` flag is needed or relevant to idempotent behavior in Ansible.

---

### Question 18 (Scenario — 5 pts)
A RESTCONF PUT request is sent to configure an interface description:
```
PUT /restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1
Content-Type: application/yang-data+json
{
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet1",
    "description": "WAN Uplink",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": true
  }
}
```
The server returns HTTP 409 Conflict. What is the most likely cause?

- A) The JSON content-type header is incorrect — RESTCONF requires XML. ❌
- B) The interface GigabitEthernet1 does not exist and cannot be created with PUT. ❌
- C) A PUT operation attempts to replace the entire resource — the conflict arises because a required field (such as IP address) already exists with a conflicting value, or the resource is locked by another active NETCONF session. ✅
- D) The router does not support RESTCONF on GigabitEthernet1 — only loopback interfaces are supported. ❌

**Answer:** C — HTTP 409 Conflict in RESTCONF indicates the request could not be completed because it would conflict with the current state of the resource. Common causes include: a NETCONF candidate datastore lock held by another session that prevents modifications, or a resource conflict where the PUT operation's data would violate a uniqueness constraint or create an inconsistency. To diagnose: check for active NETCONF sessions with `show netconf sessions` and verify no candidate lock is held. If a lock is held, wait for it to release or administratively clear it.

**Distractor Analysis:**
- A: `application/yang-data+json` is the correct RESTCONF JSON media type (RFC 8040).
- B: A missing resource would return 404 Not Found; a non-creatable resource situation depends on implementation but is typically 403 or 405.
- D: RESTCONF applies to the device's YANG model universally, not per-interface-type.

---

### Question 19 (Short Answer — 5 pts)
Explain the difference between **NETCONF** and **RESTCONF** as network management protocols. Which would you choose for building a real-time streaming telemetry application versus a one-time configuration change workflow, and why? (3–4 sentences)

**Model Answer:** **NETCONF** (RFC 6241) is an XML-based protocol running over SSH that uses RPC operations (`<get>`, `<edit-config>`, `<commit>`) and supports the `<candidate>` datastore for transactional configuration workflows — it is designed for reliable, stateful configuration management and is preferred when atomic commit/rollback is required. **RESTCONF** (RFC 8040) is a RESTful HTTP-based protocol using JSON or XML over HTTPS that maps YANG models to standard HTTP methods (GET, PUT, POST, DELETE); it is simpler to implement and integrate with web-based tooling and CI/CD pipelines but does not support the `<candidate>` datastore or atomic multi-resource transactions. For a **real-time streaming telemetry** application, neither NETCONF nor RESTCONF is ideal — **gNMI/gRPC with model-driven telemetry** (MDT) is the correct choice as it supports subscription-based streaming of operational data at sub-second intervals with far less overhead than polling. For a **one-time configuration change workflow** integrated into a Python script or web application, RESTCONF's simpler HTTP interface makes it the more practical choice compared to NETCONF's XML-over-SSH complexity.

---

### Question 20 (Short Answer — 5 pts)
A campus network has 500 IP phones and 500 PCs, each connected to the same switch port using a Cisco IP phone (phone connected to switch, PC connected to phone's built-in PC port). Describe the QoS trust model that should be applied at the access layer, including which device's markings are trusted, which are not, and why this distinction is critical for voice quality. (3–4 sentences)

**Model Answer:** The correct access-layer QoS trust model trusts the **IP phone's** DSCP markings but **does not trust** the PC's markings — on Cisco switches, this is implemented with `mls qos trust cos` on the access port combined with a `mls qos trust device cisco-phone` condition that activates trust only when CDP detects a Cisco IP phone on the port. The IP phone marks its own VoIP RTP traffic as DSCP EF (46) and is a trusted endpoint because it is a controlled corporate device with no user interface for changing QoS markings. The PC is untrusted because any user or application can set arbitrary DSCP values — a user running BitTorrent could mark all traffic as DSCP EF to gain voice-class priority, causing actual VoIP calls to experience jitter and packet loss. This trust boundary design ensures that EF treatment in the network is reserved exclusively for genuine real-time voice traffic, maintaining the sub-150ms one-way delay and sub-1% packet loss requirements that voice quality depends on.
