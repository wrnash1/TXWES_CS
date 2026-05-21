# Quiz: Module 01 - Networking Fundamentals and the OSI Model
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
Which layer of the OSI model is responsible for routing packets across multiple logical networks using IP addressing?
A) Layer 2 (Data Link Layer)
B) Layer 3 (Network Layer)
C) Layer 4 (Transport Layer)
D) Layer 7 (Application Layer)
*   **Correct Answer:** B) Layer 3 (Network Layer)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Layer 2 handles MAC addressing and framing for delivery on the same physical link segment, not routing across multiple logical networks.
    *   *Why C is incorrect:* Layer 4 manages end-to-end transport protocols (TCP/UDP) and port numbers, not routing decisions between networks.
    *   *Why D is incorrect:* Layer 7 handles application-specific protocols (HTTP, SMTP, DNS), not network routing.

---

**Question 2**
A network administrator is documenting the OSI model for a training session. Which of the following correctly identifies the Protocol Data Unit (PDU) and the primary device associated with Layer 2 of the OSI model?
A) PDU: Packet; Device: Router
B) PDU: Segment; Device: Firewall
C) PDU: Frame; Device: Switch
D) PDU: Bit; Device: Hub
*   **Correct Answer:** C) PDU: Frame; Device: Switch
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Packets are the PDU of Layer 3 (Network), and routers are Layer 3 devices.
    *   *Why B is incorrect:* Segments are the PDU of Layer 4 (Transport); firewalls can operate at multiple layers but are not the primary Layer 2 device.
    *   *Why D is incorrect:* Bits are the PDU of Layer 1 (Physical), and hubs are Layer 1 devices.

---

**Question 3**
A network engineer needs to map and trace the exact path of router hops that packets travel to reach a target destination. Which of the following commands is the most appropriate?
A) traceroute
B) ping
C) netstat -ano
D) nslookup
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    *   *Why B is incorrect:* The `ping` command uses ICMP Echo Requests to test basic reachability and measure round-trip latency, but does not reveal intermediate hop information.
    *   *Why C is incorrect:* The `netstat -ano` command displays active local connections, listening ports, and process IDs — it does not trace routes to remote hosts.
    *   *Why D is incorrect:* The `nslookup` command queries DNS servers to resolve hostnames; it has no routing trace capability.

---

**Question 4**
A user reports they cannot browse the internet but can ping 8.8.8.8 by IP address successfully. Which of the following is the most likely cause?
A) The default gateway is misconfigured.
B) The network cable is unplugged.
C) DNS resolution is failing because the configured DNS server is unreachable.
D) The user's subnet mask does not match the rest of the network.
*   **Correct Answer:** C) DNS resolution is failing because the configured DNS server is unreachable.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* If the default gateway were misconfigured, the user could not ping an external IP address (8.8.8.8) at all; pinging by IP succeeds, eliminating this cause.
    *   *Why B is incorrect:* An unplugged cable would prevent all connectivity, including the successful ping by IP address.
    *   *Why D is incorrect:* A subnet mask mismatch would prevent reaching any external hosts; again, the successful IP ping rules this out.

---

**Question 5**
When securing a network against attackers connecting rogue devices directly to internal switch ports, which of the following security controls is the most appropriate first line of defense?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Enable 802.1X Network Access Control (NAC) to require authentication before any device is granted network access.
D) Deploy an Intrusion Prevention System (IPS) to detect and block malicious traffic signatures inline.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    *   *Why A is correct:* Port Security is a Layer 2 switch feature that limits which MAC addresses may connect to a specific physical port, directly preventing unauthorized physical device attachment.
    *   *Why B is incorrect:* Replacing Telnet with SSH encrypts management sessions but does not prevent an unauthorized device from physically connecting to an open switch port.
    *   *Why C is incorrect:* 802.1X NAC is a strong control but is an enterprise-level authentication solution; Port Security is the direct, immediate answer for preventing rogue physical connections on a per-port basis.
    *   *Why D is incorrect:* An IPS inspects traffic flowing through the network but does not prevent an unauthorized device from obtaining a link-layer connection on an open switch port.
