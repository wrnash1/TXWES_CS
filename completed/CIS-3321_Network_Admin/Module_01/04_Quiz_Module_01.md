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

### Question 11

Which of the following protocols operates at OSI Layer 5 and is responsible for establishing and managing communication sessions between applications on separate hosts?

- A) TCP
- B) NetBIOS
- C) IP
- D) Ethernet

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* TCP operates at Layer 4 (Transport) and provides reliable delivery — it does not manage session-layer dialog control.
- *Why B is correct:* NetBIOS is a Session layer protocol that establishes, manages, and terminates communication sessions between networked applications.
- *Why C is incorrect:* IP is a Layer 3 (Network) protocol responsible for logical addressing and packet routing.
- *Why D is incorrect:* Ethernet is a Layer 1/2 (Physical/Data Link) standard for framing and physical transmission.

---

### Question 12

An administrator needs to identify the manufacturer of a network device based solely on its MAC address. Which portion of the MAC address contains the manufacturer identifier?

- A) The last 24 bits (last three octets)
- B) The first 24 bits (first three octets), known as the OUI
- C) Bits 25–48 (middle two octets)
- D) The entire 48-bit address must be looked up in an ARP table

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* The last 24 bits are the device-specific portion assigned by the manufacturer, not the manufacturer identifier.
- *Why B is correct:* The Organizationally Unique Identifier (OUI) occupies the first 24 bits (first three octets) of a MAC address and is assigned by IEEE to uniquely identify each manufacturer.
- *Why C is incorrect:* There is no defined "middle" manufacturer field in a MAC address — the split is precisely at the 24-bit boundary.
- *Why D is incorrect:* An ARP table maps IP addresses to MAC addresses on a local network; it is not used to identify manufacturers.

---

### Question 13

Which OSI layer is responsible for data encryption and decryption, ensuring that data is presented in a format the application layer can use?

- A) Layer 4 – Transport
- B) Layer 5 – Session
- C) Layer 6 – Presentation
- D) Layer 7 – Application

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Layer 4 handles segmentation, port addressing, and reliable delivery — not format translation or encryption at the presentation level.
- *Why B is incorrect:* Layer 5 manages session establishment and termination between communicating applications, not data format conversion.
- *Why C is correct:* The Presentation layer handles data formatting, encoding (ASCII, Unicode), compression, and encryption/decryption (TLS operates here conceptually).
- *Why D is incorrect:* Layer 7 provides the application-facing interface (HTTP, SMTP, etc.) but relies on Layer 6 for data format translation.

---

### Question 14

A network administrator configures a device that operates only at Layer 1. The device receives an electrical signal on one port and repeats it out all other ports without any filtering or addressing decisions. Which device is described?

- A) Switch
- B) Router
- C) Hub
- D) Bridge

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A switch operates at Layer 2 — it reads MAC addresses and forwards frames to specific ports rather than flooding all ports with raw signals.
- *Why B is incorrect:* A router operates at Layer 3 — it reads IP addresses and makes routing decisions between networks.
- *Why C is correct:* A hub is a Layer 1 device that simply regenerates and broadcasts electrical signals to all ports without any intelligence or addressing awareness.
- *Why D is incorrect:* A bridge operates at Layer 2 and uses MAC address learning to filter traffic between network segments.

---

### Question 15

During the four-way TCP connection termination, which flag does the initiating side send first to signal it has no more data to send?

- A) RST
- B) ACK
- C) SYN
- D) FIN

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* RST (Reset) terminates a TCP connection abruptly due to an error or unexpected condition — it is not the normal graceful termination initiator.
- *Why B is incorrect:* ACK acknowledges receipt of data or control messages; it is sent in response to FIN but is not the initiating flag.
- *Why C is incorrect:* SYN is used during connection establishment (three-way handshake), not connection termination.
- *Why D is correct:* FIN (Finish) is the flag sent by the initiating side during the four-way termination sequence to indicate it has finished sending data and wishes to close its half of the connection.

---

### Question 16

Which of the following best describes the difference between a physical topology and a logical topology?

- A) Physical topology describes the IP addressing scheme; logical topology describes the cable layout.
- B) Physical topology describes how devices are physically connected; logical topology describes how data actually flows through the network.
- C) Physical and logical topologies are always identical in modern networks.
- D) Logical topology refers to the number of devices in a network; physical topology refers to their geographic location.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* IP addressing is a Layer 3 concern, not a topology definition. Physical topology specifically describes cable and device placement, not addressing.
- *Why B is correct:* Physical topology is the actual physical layout of cables and devices. Logical topology is the path data takes, which may differ (e.g., a network that is physically a star but logically a ring using token passing).
- *Why C is incorrect:* Physical and logical topologies can differ. Token Ring networks used a physical star but a logical ring topology.
- *Why D is incorrect:* Neither definition relates to device count or geographic location.

---

### Question 17

A network engineer is asked to calculate the number of dedicated connections required for a full-mesh topology connecting 6 routers. How many connections are needed?

- A) 6
- B) 12
- C) 15
- D) 30

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* 6 connections would only form a partial ring or star — not a full mesh where every node connects to every other node.
- *Why B is incorrect:* 12 connections would cover only some pairings. The correct formula is n(n-1)/2.
- *Why C is correct:* Using the full-mesh formula n(n-1)/2: 6(6-1)/2 = 6(5)/2 = 15 connections. Each router needs a dedicated link to every other router.
- *Why D is incorrect:* 30 = 6 × 5, which counts each link twice (once from each end). Dividing by 2 gives 15.

---

### Question 18

Which of the following correctly describes what happens during decapsulation at the receiving host?

- A) Each layer adds its own header before passing data up to the next layer.
- B) The Physical layer reconstructs the original application data directly without any intermediate processing.
- C) Each layer strips its corresponding header and passes the remaining data up to the next higher layer.
- D) Only the Transport layer processes headers; all other layers pass data through unchanged.

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* Adding headers describes encapsulation (outbound), not decapsulation (inbound).
- *Why B is incorrect:* The Physical layer only handles raw bit transmission. Higher layers must each process their respective headers before the data reaches the application.
- *Why C is correct:* Decapsulation is the reverse of encapsulation. Each layer at the receiver reads and removes its corresponding header, then passes the payload up to the next layer, until the original application data is restored.
- *Why D is incorrect:* Every layer participates in decapsulation — not just Layer 4. Layer 2 strips the Ethernet frame header, Layer 3 strips the IP header, Layer 4 strips the TCP/UDP header, and so on.

---

### Question 19

An ICMP ping is sent from Host A to Host B. At the moment the packet is handed from the Network layer to the Data Link layer for transmission, what is the PDU called?

- A) Segment
- B) Datagram
- C) Frame
- D) Packet

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A segment is the Layer 4 PDU for TCP — it exists before the IP header is added at Layer 3.
- *Why B is incorrect:* A datagram is the Layer 4 PDU for UDP. Once the IP header is added at Layer 3, it becomes a packet.
- *Why C is correct:* When the Network layer (Layer 3) packet is passed down to the Data Link layer (Layer 2), the Data Link layer encapsulates it in an Ethernet frame. The PDU at Layer 2 is called a frame.
- *Why D is incorrect:* A packet is the Layer 3 PDU — it exists while being processed at the Network layer, before the Data Link layer encapsulates it into a frame.

---

### Question 20

A workstation has an IP address of 192.168.10.50 and a subnet mask of 255.255.255.0. It attempts to communicate with a host at 192.168.20.75. Which device must be involved to route this traffic?

- A) A Layer 2 switch
- B) A hub
- C) A router or Layer 3 switch
- D) A network bridge

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* A Layer 2 switch forwards frames within the same network segment using MAC addresses. It cannot route between different IP subnets.
- *Why B is incorrect:* A hub is a Layer 1 device that repeats signals; it has no IP or MAC address awareness and cannot perform routing.
- *Why C is correct:* The two hosts are on different subnets (192.168.10.0/24 vs. 192.168.20.0/24). A router or Layer 3 switch is required to route packets between logically separate networks.
- *Why D is incorrect:* A bridge operates at Layer 2 to segment collision domains; it cannot route between different IP subnets.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
