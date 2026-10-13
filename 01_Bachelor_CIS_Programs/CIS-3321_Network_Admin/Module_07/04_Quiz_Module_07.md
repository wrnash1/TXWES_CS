# Quiz: Module 07 — Network Monitoring and Troubleshooting Tools

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

Instructions: Select the best answer for each question. Each question is worth 10 points (100 points total).

---

### Question 1

A network administrator runs `ping 10.10.10.1` from a workstation and receives "Request timed out" for all four packets. She then runs `ping 127.0.0.1` successfully. Which of the following conclusions is best supported by these two results?

A) The workstation's NIC is defective because ping to the gateway failed, and all network functionality is lost.

B) The workstation's TCP/IP stack is functional, but there is a Layer 3 reachability problem between the workstation and 10.10.10.1 — the gateway may be down, the IP address may be misconfigured, or ICMP may be blocked by a firewall.

C) The ping failure proves that 10.10.10.1 does not exist on the network and the router should be replaced.

D) The workstation must have the wrong subnet mask because successful loopback ping is only possible with a /32 subnet mask.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: A successful ping to 127.0.0.1 (the loopback address) confirms that the TCP/IP stack is installed and functioning. The NIC driver and OS networking stack are operational.
  - Why B is correct: Loopback success proves the local TCP/IP stack works. A timed-out ping to the gateway indicates the problem is external — possible causes include gateway being down, wrong default gateway configured, or ICMP blocked by an ACL or firewall. Further diagnosis is needed.
  - Why C is incorrect: A timed-out ping does not prove the host does not exist — ICMP may simply be blocked. The correct next step is investigation, not hardware replacement.
  - Why D is incorrect: The loopback address 127.0.0.1 is always reachable regardless of subnet mask configuration; its reachability has no relationship to the subnet mask of the physical interface.

---

### Question 2

While running `tracert 8.8.8.8` on a Windows workstation, the administrator notices that hop 5 shows three asterisks (***) and "Request timed out," but hops 6 through 9 show normal RTT values, and the final destination at hop 9 responds successfully. What is the correct interpretation?

A) The path is broken at hop 5 and the successful responses from hops 6–9 are cached results from a previous successful path.

B) Hop 5 is a router that does not respond to ICMP Time Exceeded messages due to rate limiting or firewall policy, but it is actively forwarding packets — the path to the destination is intact.

C) The three asterisks indicate that hop 5 is a firewall that has blocked all traffic; the administrator should open a help desk ticket to have the firewall rule removed.

D) The TTL was exhausted at hop 5, so all subsequent hops are unreachable and the displayed RTTs for hops 6–9 are fabricated by tracert.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: Traceroute does not cache results. Each probe is a live packet sent in real time. The responses from hops 6–9 are live responses from those routers.
  - Why B is correct: Many ISP backbone routers de-prioritize or block ICMP responses to traceroute probes to reduce control-plane load — they simply do not reply to probes. The router is still forwarding data packets normally. The fact that the destination answers proves the path is functional.
  - Why C is incorrect: Traceroute asterisks do not indicate a firewall is blocking all traffic. A firewall blocking all traffic would also block the destination from responding — which it did not, since hop 9 responded.
  - Why D is incorrect: TTL incrementing is the mechanism traceroute uses — it starts at TTL=1, then 2, then 3, and so on. TTL is not exhausted permanently at hop 5; each subsequent probe is sent with a higher TTL value to reach the next hop.

---

### Question 3

A help desk ticket reports that users in the office can access internal servers by IP address but cannot reach any website by name (for example, typing google.com in a browser fails, but typing 142.250.80.78 directly works). Which tool should the administrator run first, and what does the symptom indicate?

A) Run Wireshark and capture all traffic on the LAN; the symptom indicates a Layer 2 switching loop that is causing intermittent packet loss.

B) Run `nslookup google.com`; the symptom indicates a DNS resolution failure — name-to-IP translation is not functioning, but Layer 3 IP connectivity is intact.

C) Run `netstat -r`; the symptom indicates the default route is missing from the routing table, which is preventing access to external names.

D) Run `tracert google.com`; the symptom indicates the WAN link to the ISP is saturated and DNS packets are being dropped due to congestion.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: A Layer 2 switching loop would cause broadcast storms and widespread connectivity failures — users would not be able to reach servers by IP address either. The symptom is specific to name resolution, not general connectivity.
  - Why B is correct: The ability to reach hosts by IP address but not by hostname is the classic signature of DNS failure. Running nslookup will confirm whether DNS queries are succeeding or failing, and which DNS server is being queried.
  - Why C is incorrect: If the default route were missing, users could not reach external IP addresses either — but the scenario states that typing a raw IP address (142.250.80.78) works. The routing table is functional.
  - Why D is incorrect: If congestion were dropping DNS packets selectively, some DNS queries would succeed intermittently. The scenario describes a complete failure of all name resolution. Tracert to a hostname also depends on DNS to resolve the name — it would fail for the same reason.

---

### Question 4

An administrator runs `netstat -an` on a Windows server and sees the following entry:

`TCP    0.0.0.0:3389    0.0.0.0:0    LISTENING`

What does this entry indicate, and what is the security implication?

A) The server has an established RDP connection to a remote client on port 3389 and data is actively being transferred.

B) TCP port 3389 (Remote Desktop Protocol) is open and accepting connections from any IP address on all interfaces; if RDP is not intentionally enabled, this may be a security risk.

C) The server is attempting to connect to a remote service on port 3389 but the connection has not yet been established.

D) Port 3389 is blocked by the Windows Firewall and the LISTENING state indicates the block is active.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: The LISTENING state means the port is waiting for incoming connections — no connection has been established yet. An active data transfer would show ESTABLISHED with a specific foreign IP address and port.
  - Why B is correct: 0.0.0.0:3389 in LISTENING state means the Remote Desktop service is running and bound to all interfaces, accepting connections from any source. If RDP was not intentionally configured, this represents an attack surface — RDP is a frequent target for brute-force and exploitation attempts.
  - Why C is incorrect: An outbound connection attempt would appear with the local port as a high ephemeral number and the remote address set to the server being connected to, not 0.0.0.0:0. LISTENING always indicates a server-side waiting state, not a client-side connection attempt.
  - Why D is incorrect: Windows Firewall blocking a port does not appear in netstat output. Netstat shows the TCP stack's view of connections, which is independent of firewall rules. A blocked port might still show LISTENING in netstat even if the firewall is dropping inbound packets at the network layer.

---

### Question 5

A network engineer wants to implement automated, continuous monitoring of CPU utilization, interface bandwidth, and memory usage across 200 network devices. She needs version-specific security: all monitoring traffic must be authenticated and encrypted because the management network traverses a shared infrastructure segment. Which solution satisfies all requirements?

A) Deploy SNMPv2c with the default community strings `public` and `private` — these strings serve as encrypted authentication tokens in v2c.

B) Deploy SNMPv3 with authPriv security level, which provides HMAC-SHA authentication and AES encryption for all management traffic.

C) Use syslog on UDP 514 to collect performance metrics from each device; syslog provides both authentication and encryption for metric data.

D) Configure NetFlow on each device to export CPU and memory utilization records to a central collector.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: SNMPv2c community strings are transmitted in plain text — they are not encrypted authentication tokens. The default strings `public` and `private` are well-known and represent a critical vulnerability if left unchanged. SNMPv2c provides no encryption.
  - Why B is correct: SNMPv3 with authPriv (authentication + privacy) provides HMAC-MD5 or HMAC-SHA for authentication and DES or AES for encryption. This is the only SNMP version that satisfies both the authentication and encryption requirements.
  - Why C is incorrect: Syslog collects log messages, not performance metrics such as CPU utilization or interface bandwidth. Standard syslog on UDP 514 also provides no authentication or encryption.
  - Why D is incorrect: NetFlow captures network traffic flow metadata (IP addresses, ports, byte counts) — it does not capture device CPU utilization, memory usage, or interface bandwidth utilization as polled metrics. NetFlow also provides no encryption for the management traffic itself.

---

### Question 6

A security analyst is reviewing traffic on a core router and needs to identify which specific hosts and applications are consuming the most WAN bandwidth over the past 24 hours, including source/destination IP pairs, port numbers, and byte counts per flow. Which monitoring technology provides this information?

A) SNMP polling — queries interface input/output octet counters every 5 minutes to track total bandwidth utilization per interface.

B) NetFlow — exports flow-level records for every unique source IP, destination IP, source port, destination port, and protocol combination observed on the interface.

C) Syslog — generates a log entry for every packet that crosses the router interface and includes byte counts in each entry.

D) Wireshark running continuously on the router — captures full packet contents for all 24 hours and stores them for later analysis.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: SNMP polling reports aggregate interface counters — total bytes in and total bytes out for the entire interface. It does not break down traffic by source/destination IP pair or application port. It cannot identify which hosts or applications are responsible for the bandwidth.
  - Why B is correct: NetFlow captures the 5-tuple (source IP, destination IP, source port, destination port, protocol) for every flow, along with byte count, packet count, and timestamps. A NetFlow analyzer can produce exactly the top-talker report described — by host pair and by application port.
  - Why C is incorrect: Syslog does not generate per-packet log entries on a router by default — that would be prohibitively resource-intensive. Standard syslog captures system events such as routing changes and interface state transitions, not per-packet bandwidth data.
  - Why D is incorrect: Running Wireshark continuously on a high-throughput router interface for 24 hours would generate terabytes of capture data and consume excessive CPU and storage. Wireshark is not deployed as a continuous production monitoring tool; it is used for targeted, time-limited packet-level investigation.

---

### Question 7

A network administrator receives a syslog message from a core router with severity level 2. A second message arrives from the same router with severity level 6. Which statement correctly characterizes these messages?

A) Severity 6 is more critical than severity 2 because higher numbers indicate greater urgency in the syslog severity scale.

B) Severity 2 is Critical and requires immediate attention; severity 6 is Informational and represents a routine operational message.

C) Both severity 2 and severity 6 represent Warning-level messages; the difference is only the specific subsystem reporting them.

D) Severity 2 messages are sent to the syslog server on TCP port 514; severity 6 messages are sent on UDP port 514 based on their urgency level.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: The syslog severity scale is inverted — lower numbers are more severe. Level 0 is Emergency (most severe) and level 7 is Debug (least severe). Severity 6 is Informational, which is far less urgent than severity 2.
  - Why B is correct: Syslog level 2 is Critical (a critical condition requiring urgent attention). Syslog level 6 is Informational (a normal operational message such as a configuration change confirmation). The administrator should investigate the severity 2 message immediately.
  - Why C is incorrect: Warning is specifically level 4 in the syslog severity scale. Neither level 2 nor level 6 corresponds to Warning.
  - Why D is incorrect: Syslog does not use different ports based on message severity. Standard syslog uses UDP 514 regardless of severity level. Encrypted syslog over TLS uses TCP 6514. The severity level does not determine the transport port.

---

### Question 8

During a Wireshark capture of traffic between a client at 192.168.1.20 and a web server at 203.0.113.50, an administrator observes three packets in sequence: first a packet with SYN flag only, then a packet with both SYN and ACK flags, then a packet with ACK flag only. The administrator then applies the display filter `tcp.flags.syn == 1 && tcp.flags.ack == 0`. Which packet(s) will this filter display?

A) All three packets in the handshake, because SYN is set in the first two packets and ACK is set in the last two.

B) Only the first packet (SYN only), because it is the only packet where SYN=1 and ACK=0 simultaneously.

C) Only the second packet (SYN-ACK), because it has both SYN and ACK set, which satisfies both conditions in the AND filter.

D) None of the packets, because the filter requires SYN=1 AND ACK=0 simultaneously, which is not a valid TCP flag combination.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: The filter requires SYN=1 AND ACK=0 simultaneously. The second packet has SYN=1 but also ACK=1 — the ACK=0 condition fails for that packet, so it is excluded.
  - Why B is correct: Only the first packet (pure SYN) has SYN=1 and ACK=0 at the same time. This is the TCP connection initiation packet sent by the client. The second packet has SYN=1 but ACK=1, and the third has ACK=1 but SYN=0 — both fail the filter.
  - Why C is incorrect: The SYN-ACK packet has ACK=1, which fails the `tcp.flags.ack == 0` condition of the filter. It would not be displayed.
  - Why D is incorrect: SYN=1 with ACK=0 is a perfectly valid and common TCP flag combination — it is the standard initial SYN packet used to open every TCP connection. The filter is valid and will match the first packet.

---

### Question 9

A network administrator is tasked with establishing a network baseline for a new corporate campus. She plans to collect SNMP interface utilization data, NetFlow records, and syslog messages. A colleague suggests collecting data for just 48 hours since the network is new and traffic patterns are simple. What is the standard recommended minimum collection period for a meaningful baseline, and why?

A) 48 hours is sufficient because modern networks have consistent traffic patterns that stabilize within two days of initial deployment.

B) One full business week (5 days) is required to capture peak business hours; weekend data is unnecessary for an office environment.

C) At least two full business weeks, to capture both daily traffic cycles (peak vs. off-hours) and weekly cycles (business days vs. weekends and any recurring weekly patterns).

D) Six months of data is required before any baseline is considered valid, because seasonal traffic variations must be captured.

- Correct Answer: C
- Distractor Analysis:
  - Why A is incorrect: 48 hours captures at most two daily cycles and is insufficient to identify weekly patterns such as Monday morning login storms, Friday afternoon backup jobs, or weekend maintenance windows. A 48-hour baseline would miss most recurring traffic patterns.
  - Why B is correct that a week is better than 48 hours, but C is more complete: One week captures daily cycles but misses the second week's data needed to confirm repeatability. The standard is two weeks, not one.
  - Why C is correct: Two full business weeks is the standard minimum baseline period. It captures daily cycles (morning peak, lunch dip, evening decline, overnight low) and weekly cycles (Monday heavier than Friday, weekend maintenance traffic). Two weeks also allows confirmation that patterns are repeatable, not anomalous.
  - Why D is incorrect: While longer periods provide richer data, six months is not a practical requirement for establishing a working baseline. The standard for CompTIA Network+ purposes is a minimum of two weeks. Annual re-baselining accounts for seasonal and growth changes.

---

### Question 10

A junior administrator is troubleshooting a report that users on VLAN 20 cannot reach the internet. He starts by running `ping 8.8.8.8` from a VLAN 20 workstation — it fails. He then runs `ping 10.20.0.1` (the VLAN 20 default gateway) — it succeeds. He then runs `ping 172.16.1.1` (the WAN router's LAN interface) — it fails. Which troubleshooting approach is this administrator using, and what has he determined so far?

A) He is using the top-down approach. He has determined that the application layer is functioning correctly and the problem is at the transport layer.

B) He is using the divide-and-conquer approach. He has determined that Layer 3 connectivity exists within VLAN 20 (workstation can reach its gateway) but fails beyond the gateway — the problem is between the distribution/core layer and the WAN router or on the WAN link itself.

C) He is using the bottom-up approach. He has determined that the physical cable is functioning because ping succeeded to the gateway, and the problem must be a duplex mismatch.

D) He is using the top-down approach. He has determined that DNS is the root cause because ping uses DNS to resolve 8.8.8.8 before sending ICMP packets.

- Correct Answer: B
- Distractor Analysis:
  - Why A is incorrect: The administrator is using ping (Layer 3 test), not application-layer diagnostics. Top-down would start with the application itself — trying to open a browser, testing HTTP, then working down.
  - Why B is correct: The administrator started at Layer 3 with ping and incrementally extended the test scope — first to the local gateway (success), then to the next upstream device (failure). This is divide-and-conquer: each test cuts the problem space. The conclusion is correct: Layer 3 works within VLAN 20 but fails between the access/distribution layer and the WAN router.
  - Why C is incorrect: Bottom-up troubleshooting starts at Layer 1 — checking cable, link lights, and interface status — before running any ping commands. The administrator did not examine physical layer indicators first.
  - Why D is incorrect: Ping to an IP address (8.8.8.8) does not use DNS — the IP address is used directly. DNS resolution only occurs when pinging a hostname. The description of top-down is also incorrect as explained in option A.

---

### Question 11

A network administrator uses the `netstat -an` command on a Windows server and observes a connection with the state "TIME_WAIT." What does this TCP connection state indicate?

- A) The connection has been fully established and data is actively being transferred.
- B) The server is listening for incoming connections on the specified port.
- C) The local side has sent a FIN to close the connection and is waiting for the remote side's TIME_WAIT period to expire.
- D) The connection is half-closed — the local application has sent a FIN and is waiting for all packets to expire from the network before the port is reused.

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* An actively transferring connection is in the ESTABLISHED state, not TIME_WAIT.
- *Why B is incorrect:* A port waiting for incoming connections is in the LISTEN state, not TIME_WAIT.
- *Why C is incorrect:* TIME_WAIT is not simply waiting for the remote side — it is the local side's waiting period after sending the final ACK, designed to ensure all delayed packets from the session expire from the network before the port is reused.
- *Why D is correct:* TIME_WAIT is the final TCP state. After sending the last ACK in the four-way FIN exchange, the closing side enters TIME_WAIT (typically 2 × MSL = 2 minutes). This ensures that any lingering packets from the closed connection are discarded and do not corrupt a new connection using the same port.

---

### Question 12

An administrator suspects high CPU utilization on a router is causing packet loss. Which SNMP concept should be configured to automatically alert the NMS when the CPU threshold exceeds 80%?

- A) SNMP GET request
- B) SNMP TRAP
- C) SNMP SET command
- D) SNMP Walk

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* An SNMP GET request is a poll sent FROM the NMS TO the device, requesting the current value of a specific OID. It does not automatically alert when thresholds are exceeded.
- *Why B is correct:* An SNMP TRAP is an unsolicited message sent FROM the device TO the NMS when a defined threshold or event occurs. Configuring a CPU threshold trap on the router causes it to proactively notify the NMS without waiting for a poll.
- *Why C is incorrect:* An SNMP SET command is sent from the NMS to modify a configuration value on the device. It is used for remote management, not alerting.
- *Why D is incorrect:* An SNMP Walk retrieves all OID values under a branch of the MIB tree through sequential GET-NEXT requests. It is used for inventory or discovery — not threshold alerting.

---

### Question 13

A network engineer uses Wireshark and applies the display filter `tcp.port == 443 and ip.src == 10.0.0.50`. What traffic will this filter display?

- A) All TCP traffic from any host using any port communicating with 10.0.0.50
- B) All HTTPS traffic from the host 10.0.0.50 as the source
- C) All TCP traffic where either the source or destination is 10.0.0.50, on port 443
- D) Only outbound HTTPS traffic initiated by host 10.0.0.50, not responses to it

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The filter specifies `tcp.port == 443`, which limits results to port 443 traffic only — not all TCP traffic.
- *Why B is correct:* `tcp.port == 443` matches any TCP packet where source OR destination port is 443. Combined with `ip.src == 10.0.0.50`, the filter shows only TCP port 443 packets where 10.0.0.50 is the source IP — which is outbound HTTPS traffic from that host.
- *Why C is incorrect:* The filter specifies `ip.src`, which means source IP must be 10.0.0.50. It does not also match traffic where 10.0.0.50 is the destination. For bidirectional filtering, `ip.addr` would be needed.
- *Why D is incorrect:* TCP port matching in Wireshark (`tcp.port`) matches both source and destination port 443. This includes both SYN packets (client to server on port 443) and all response traffic flowing back through the same TCP stream where 10.0.0.50 is the source.

---

### Question 14

Which network monitoring protocol version introduced authentication and encryption using MD5/SHA, addressing a critical security weakness present in earlier versions?

- A) SNMPv1
- B) SNMPv2c
- C) SNMPv3
- D) Syslog over TLS

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* SNMPv1 uses community strings (cleartext passwords) for authentication — no encryption. It is considered insecure.
- *Why B is incorrect:* SNMPv2c retained the same community string authentication as SNMPv1 (still cleartext). It improved performance and added bulk retrieval (GetBulk) but did not add encryption or strong authentication.
- *Why C is correct:* SNMPv3 introduced user-based security with authentication (HMAC-MD5 or HMAC-SHA) and optional encryption (DES or AES). This addresses the community string cleartext weakness of v1 and v2c and is the recommended version for production networks.
- *Why D is incorrect:* Syslog over TLS (RFC 5425) is a separate protocol for secure log forwarding — it is not an SNMP version and is not related to SNMP authentication.

---

### Question 15

A network engineer runs `traceroute 8.8.8.8` and sees that hop 5 shows three asterisks (***). Hop 6 shows normal RTT values. What does the asterisk at hop 5 most likely indicate?

- A) Hop 5 is offline and all packets after it are being rerouted.
- B) Hop 5 is a router configured to not respond to ICMP TTL-exceeded messages, but it is still forwarding packets.
- C) The traceroute has reached the final destination, which uses asterisks to confirm successful arrival.
- D) Hop 5 is experiencing 100% packet loss and the rest of the traceroute results are unreliable.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* If hop 5 were offline and packets were being rerouted, subsequent hops (like hop 6) might show unusual paths or the route might fail entirely. The fact that hop 6 shows normal results indicates hop 5 is still forwarding packets.
- *Why B is correct:* Asterisks in traceroute indicate that the router at that hop is not generating ICMP Time Exceeded responses (often due to ACLs or rate limiting on ICMP). The router is still forwarding packets (as evidenced by responses at hop 6) — it is simply silent about its own address.
- *Why C is incorrect:* Traceroute reaches its destination when it receives an ICMP Port Unreachable (UDP-based traceroute) or ICMP Echo Reply (ICMP-based traceroute) from the final host. Asterisks appear in the middle of a route, not at the destination.
- *Why D is incorrect:* If hop 5 were truly unreachable (100% packet loss at that node), all subsequent hops would also fail because packets could not pass through. Since hop 6 responds normally, hop 5 is forwarding packets.

---

### Question 16

What is the primary purpose of a network baseline, and how often should it be updated according to best practice?

- A) A baseline records MAC address table contents to recover from switch failures. It should be updated daily.
- B) A baseline documents normal network performance metrics (bandwidth, latency, CPU utilization) used to identify deviations. It should be updated at least annually or after significant infrastructure changes.
- C) A baseline encrypts configuration backups for compliance auditing. It should be updated after every configuration change.
- D) A baseline defines which IP addresses are statically assigned versus DHCP. It should be updated whenever IP addresses change.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* MAC address tables are dynamic, switch-maintained data structures — not a baseline document. They rebuild automatically and do not need manual backup.
- *Why B is correct:* A performance baseline captures normal metric values (typical bandwidth utilization, average latency, packet error rates, CPU/memory utilization under normal load). When current measurements deviate significantly from the baseline, it indicates a problem. Baselines should be re-captured annually and after major infrastructure changes (new devices, link upgrades, significant growth).
- *Why C is incorrect:* Configuration backups are separate from performance baselines. Encrypting configuration files is a security practice, not a baselining activity.
- *Why D is incorrect:* IP address documentation (IPAM) is a separate administrative function. While important, it is distinct from performance baselining.

---

### Question 17

Which tool would a network administrator use to capture and analyze raw network packets traversing an interface for the purpose of protocol-level troubleshooting?

- A) SNMP NMS (Network Management System)
- B) Syslog server
- C) Protocol analyzer (packet sniffer)
- D) NetFlow collector

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* An SNMP NMS collects and displays performance statistics from managed devices via SNMP polling. It shows metrics but does not capture raw packet payloads for protocol analysis.
- *Why B is incorrect:* A syslog server collects event and error messages from network devices. Syslog messages are text-based logs — they do not contain raw packet captures.
- *Why C is correct:* A protocol analyzer (packet sniffer), such as Wireshark or tcpdump, captures raw packets at the wire level and decodes them frame-by-frame. This enables protocol-level troubleshooting — examining headers, flags, payloads, and the exact sequence of exchanges between devices.
- *Why D is incorrect:* A NetFlow collector receives summarized traffic flow records (source/destination IP, protocol, byte counts, duration) exported by routers and switches. NetFlow provides traffic volume analysis but not raw packet captures — you cannot see individual frame headers or protocol exchanges with NetFlow data alone.

---

### Question 18

An administrator uses the `nslookup` tool and sets the server to a known-good public DNS server (8.8.8.8). He queries a company's internal hostname and receives a "Server failed" or "NXDOMAIN" response. The same query against the company's internal DNS server succeeds. What does this indicate?

- A) The internal hostname exists only in the company's private DNS zone and is not published to public DNS.
- B) The company's DNS server is misconfigured and returning incorrect responses.
- C) The public DNS server 8.8.8.8 is unreachable.
- D) Split DNS is disabled and all DNS queries must go through the company's proxy.

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Internal hostnames (such as `intranet.company.local` or internal server names) are typically hosted in a private DNS zone that is only accessible via the organization's internal DNS servers. Public DNS servers like 8.8.8.8 do not have records for internal names by design. This is expected and correct behavior — it is often called a split-horizon or split-DNS configuration.
- *Why B is incorrect:* The internal DNS server is returning a successful response, which indicates it is functioning correctly. The "failure" is from the public server not knowing about an internal name — this is normal, not a misconfiguration.
- *Why C is incorrect:* If 8.8.8.8 were unreachable, the nslookup query would time out entirely rather than returning NXDOMAIN or "Server failed" with a specific response.
- *Why D is incorrect:* A DNS proxy configuration is unrelated to why a public DNS server lacks records for private internal hostnames.

---

### Question 19

What does the SNMP OID (Object Identifier) represent in the context of network monitoring?

- A) The IP address of the SNMP-managed device
- B) A unique numerical identifier for a specific manageable data point in the Management Information Base (MIB)
- C) The SNMP community string used for authentication
- D) The version number of the SNMP protocol being used

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The managed device's IP address is used to identify the device in SNMP communications — it is not an OID. OIDs identify specific data values within a device.
- *Why B is correct:* An OID is a hierarchical numerical address (e.g., 1.3.6.1.2.1.1.1.0) that uniquely identifies a specific manageable variable in the MIB tree. For example, one OID identifies CPU utilization, another identifies interface input errors. SNMP GET requests specify which OID to retrieve.
- *Why C is incorrect:* The community string is a cleartext password used in SNMPv1/v2c for authentication. It is a separate field from the OID.
- *Why D is incorrect:* The SNMP version is indicated in the protocol header (version 1, 2c, or 3). It is not encoded in an OID.

---

### Question 20

A network administrator needs to capture traffic at a specific switch port without interrupting the live network. The switch is a managed Cisco Catalyst. Which switch feature should be configured to copy traffic from the production port to a monitoring port where a packet analyzer is connected?

- A) Port Security
- B) SPAN (Switched Port Analyzer)
- C) VLAN access control list (VACL)
- D) EtherChannel

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Port Security restricts which MAC addresses can connect to a switch port. It does not copy traffic for monitoring purposes.
- *Why B is correct:* SPAN (Switched Port Analyzer), also called port mirroring, is a Cisco switch feature that copies all traffic from one or more source ports (or VLANs) to a designated destination port where a packet analyzer is connected. The original traffic flows unaffected.
- *Why C is incorrect:* A VACL (VLAN Access Control List) filters traffic within a VLAN based on policy. While VACLs can be used with a capture ACL to redirect matching traffic, SPAN is the standard tool for non-intrusive traffic capture.
- *Why D is incorrect:* EtherChannel bundles multiple physical links into one logical link for increased bandwidth and redundancy. It is unrelated to traffic capture or monitoring.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
