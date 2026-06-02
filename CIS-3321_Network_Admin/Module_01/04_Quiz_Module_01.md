# Quiz: Module 01 – Networking Fundamentals and the OSI Model
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

**Instructions:** Select the best answer for each question. Each question is worth 10 points (100 points total).

---

**Question 1**

Which layer of the OSI model is responsible for routing packets across multiple logical networks using IP addressing?

A) Layer 2 (Data Link Layer)

B) Layer 3 (Network Layer)

C) Layer 4 (Transport Layer)

D) Layer 7 (Application Layer)

- **Correct Answer:** B) Layer 3 (Network Layer)
- **Distractor Analysis:**
  - *Why A is incorrect:* Layer 2 handles MAC addressing and framing for delivery on the same physical link segment, not routing across multiple logical networks.
  - *Why C is incorrect:* Layer 4 manages end-to-end transport protocols (TCP/UDP) and port numbers, not routing decisions between networks.
  - *Why D is incorrect:* Layer 7 handles application-specific protocols (HTTP, SMTP, DNS), not network routing.

---

**Question 2**

A network administrator is documenting the OSI model for a training session. Which of the following correctly identifies the Protocol Data Unit (PDU) and the primary device associated with Layer 2 of the OSI model?

A) PDU: Packet; Device: Router

B) PDU: Segment; Device: Firewall

C) PDU: Frame; Device: Switch

D) PDU: Bit; Device: Hub

- **Correct Answer:** C) PDU: Frame; Device: Switch
- **Distractor Analysis:**
  - *Why A is incorrect:* Packets are the PDU of Layer 3 (Network), and routers are Layer 3 devices.
  - *Why B is incorrect:* Segments are the PDU of Layer 4 (Transport); firewalls can operate at multiple layers but are not the primary Layer 2 device.
  - *Why D is incorrect:* Bits are the PDU of Layer 1 (Physical), and hubs are Layer 1 devices.

---

**Question 3**

A network engineer needs to map and trace the exact path of router hops that packets travel to reach a target destination. Which of the following commands is the most appropriate?

A) traceroute

B) ping

C) netstat -ano

D) nslookup

- **Correct Answer:** A) traceroute
- **Distractor Analysis:**
  - *Why B is incorrect:* The ping command uses ICMP Echo Requests to test basic reachability and measure round-trip latency, but does not reveal intermediate hop information.
  - *Why C is incorrect:* The netstat -ano command displays active local connections, listening ports, and process IDs — it does not trace routes to remote hosts.
  - *Why D is incorrect:* The nslookup command queries DNS servers to resolve hostnames; it has no routing trace capability.

---

**Question 4**

A user reports they cannot browse the internet but can ping 8.8.8.8 by IP address successfully. Which of the following is the most likely cause?

A) The default gateway is misconfigured.

B) The network cable is unplugged.

C) DNS resolution is failing because the configured DNS server is unreachable.

D) The user's subnet mask does not match the rest of the network.

- **Correct Answer:** C) DNS resolution is failing because the configured DNS server is unreachable.
- **Distractor Analysis:**
  - *Why A is incorrect:* If the default gateway were misconfigured, the user could not ping an external IP address (8.8.8.8) at all; pinging by IP succeeds, eliminating this cause.
  - *Why B is incorrect:* An unplugged cable would prevent all connectivity, including the successful ping by IP address.
  - *Why D is incorrect:* A subnet mask mismatch would prevent reaching any external hosts; again, the successful IP ping rules this out.

---

**Question 5**

When securing a network against attackers connecting rogue devices directly to internal switch ports, which of the following security controls is the most appropriate first line of defense?

A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.

B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.

C) Enable 802.1X Network Access Control (NAC) to require authentication before any device is granted network access.

D) Deploy an Intrusion Prevention System (IPS) to detect and block malicious traffic signatures inline.

- **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
- **Distractor Analysis:**
  - *Why A is correct:* Port Security is a Layer 2 switch feature that limits which MAC addresses may connect to a specific physical port, directly preventing unauthorized physical device attachment.
  - *Why B is incorrect:* Replacing Telnet with SSH encrypts management sessions but does not prevent an unauthorized device from physically connecting to an open switch port.
  - *Why C is incorrect:* 802.1X NAC is a strong control but is an enterprise-level authentication solution; Port Security is the direct, immediate answer for preventing rogue physical connections on a per-port basis.
  - *Why D is incorrect:* An IPS inspects traffic flowing through the network but does not prevent an unauthorized device from obtaining a link-layer connection on an open switch port.

---

**Question 6**

A technician is reviewing a network diagram and observes that all devices connect to a single central switch via dedicated cables. If the central switch loses power, all communication on the network stops. Which topology does this describe?

A) Bus topology

B) Mesh topology

C) Ring topology

D) Star topology

- **Correct Answer:** D) Star topology
- **Distractor Analysis:**
  - *Why A is incorrect:* A bus topology uses a single shared backbone cable, not a central switch with dedicated connections. Failure of the bus cable — not a central device — brings down communication.
  - *Why B is incorrect:* A mesh topology connects every device to every other device; there is no single central device whose failure would disable all communication.
  - *Why C is incorrect:* A ring topology connects each device to two neighbors in a circle; there is no central aggregating switch.
  - *Why D is correct:* The description matches a star topology exactly — dedicated cables from all devices to a central switch, and the central switch is the single point of failure.

---

**Question 7**

During troubleshooting, a technician applies the bottom-up OSI model approach. A workstation cannot communicate on the network. The technician observes that the NIC link light is not lit. At which OSI layer should the technician focus first?

A) Layer 3 – Network

B) Layer 2 – Data Link

C) Layer 1 – Physical

D) Layer 4 – Transport

- **Correct Answer:** C) Layer 1 – Physical
- **Distractor Analysis:**
  - *Why A is incorrect:* Layer 3 troubleshooting involves IP addressing and routing — the technician cannot reach Layer 3 diagnosis when there is no physical link.
  - *Why B is incorrect:* Layer 2 involves MAC addressing and frame switching. The absence of a link light indicates the physical layer has not been established, which must be resolved before Layer 2 can function.
  - *Why C is correct:* A missing link light indicates the physical connection (Layer 1) has failed. The technician should check the cable, the port, and the NIC before advancing to higher layers.
  - *Why D is incorrect:* Layer 4 (TCP/UDP) troubleshooting requires functional Layers 1 through 3 to be in place first.

---

**Question 8**

Which of the following best describes the process of encapsulation in the OSI model?

A) Stripping protocol headers from data as it moves up the OSI stack at the receiving device.

B) Adding protocol headers at each layer as data moves down the OSI stack toward the physical medium.

C) Compressing data at Layer 6 to reduce the size of packets for more efficient transmission.

D) Translating a hostname into an IP address before a packet is transmitted.

- **Correct Answer:** B) Adding protocol headers at each layer as data moves down the OSI stack toward the physical medium.
- **Distractor Analysis:**
  - *Why A is incorrect:* Stripping headers as data moves up the receiving stack is called decapsulation, not encapsulation.
  - *Why B is correct:* Encapsulation is the process of wrapping data with headers (and sometimes trailers) at each layer as it descends the OSI stack — Transport adds a TCP/UDP header, Network adds an IP header, Data Link adds an Ethernet frame header.
  - *Why C is incorrect:* Data compression at Layer 6 (Presentation) is a separate function and does not describe the full encapsulation process.
  - *Why D is incorrect:* Hostname-to-IP translation is performed by DNS (Layer 7/Application layer), not the encapsulation process.

---

**Question 9**

A host running Windows cannot establish a TCP connection to a web server. A packet capture shows the host sending a SYN packet but never receiving a SYN-ACK. Which phase of the TCP connection process has failed?

A) The three-way handshake is complete; the failure is in data transfer.

B) The server has not acknowledged the initial connection request, so the handshake was never completed.

C) The client sent an ACK before the SYN, violating TCP sequence rules.

D) The connection failed because UDP was used instead of TCP for this web session.

- **Correct Answer:** B) The server has not acknowledged the initial connection request, so the handshake was never completed.
- **Distractor Analysis:**
  - *Why A is incorrect:* The three-way handshake requires SYN → SYN-ACK → ACK in sequence. If only a SYN was sent and no SYN-ACK was received, the handshake is not complete.
  - *Why B is correct:* The absence of a SYN-ACK means the server either did not receive the SYN, is unreachable, or is actively refusing the connection (firewall, closed port). The handshake cannot complete without the SYN-ACK.
  - *Why C is incorrect:* The scenario does not describe an ACK being sent before a SYN. The SYN was sent correctly; the issue is that no SYN-ACK was returned.
  - *Why D is incorrect:* HTTP and HTTPS use TCP by definition. UDP is not used for web browsing under the standard protocol stack.

---

**Question 10**

An administrator needs to identify which OSI layer a specific network problem affects. A switch is receiving frames but forwarding them to the wrong ports, flooding traffic everywhere. Which layer is experiencing this problem?

A) Layer 1 – Physical

B) Layer 2 – Data Link

C) Layer 3 – Network

D) Layer 4 – Transport

- **Correct Answer:** B) Layer 2 – Data Link
- **Distractor Analysis:**
  - *Why A is incorrect:* Layer 1 problems involve physical signal transmission failures (broken cable, bad connector, no link light), not incorrect frame forwarding decisions.
  - *Why B is correct:* Frame forwarding is a Layer 2 function performed by switches. Flooding frames to all ports occurs when a switch cannot find the destination MAC address in its MAC address table — a Layer 2 forwarding issue.
  - *Why C is incorrect:* Layer 3 handles IP routing between networks. Frame flooding within a segment is a Layer 2 switching behavior, not a routing problem.
  - *Why D is incorrect:* Layer 4 manages end-to-end transport (TCP/UDP); it has no involvement in how frames are forwarded within a local segment by a switch.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
