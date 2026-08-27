# Quiz: Module 02 – TCP/IP Model and Network Protocols
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

**Instructions:** Select the best answer for each question. Each question is worth 10 points (100 points total).

---

**Question 1**

An administrator wants to segment a switch's ports logically into separate broadcast domains. Which technology should they configure?

A) NAT (Network Address Translation)

B) DHCP (Dynamic Host Configuration Protocol)

C) VLAN (Virtual Local Area Network)

D) STP (Spanning Tree Protocol)

- **Correct Answer:** C) VLAN (Virtual Local Area Network)
- **Distractor Analysis:**
  - *Why A is incorrect:* NAT translates between public and private IP addresses at Layer 3; it does not segment local switch broadcast domains.
  - *Why B is incorrect:* DHCP dynamically assigns IP configuration to clients; it does not create broadcast domain boundaries on a switch.
  - *Why D is incorrect:* STP prevents Layer 2 switching loops in redundant topologies; it does not divide a switch into isolated broadcast domains.
  - *Why C is correct:* VLANs logically partition a physical switch into multiple isolated broadcast domains without requiring separate physical hardware.

---

**Question 2**

A network technician is troubleshooting email delivery. Users can receive email but cannot send new messages to external recipients. Which protocol and port combination is most likely involved in the sending failure?

A) IMAP on port 143 — the client cannot retrieve messages from the mail server

B) SMTP on port 25 — the outbound mail server cannot relay messages to external domains

C) POP3 on port 110 — the client is downloading messages and deleting them from the server

D) HTTPS on port 443 — the webmail interface is unreachable due to a TLS certificate error

- **Correct Answer:** B) SMTP on port 25 — the outbound mail server cannot relay messages to external domains
- **Distractor Analysis:**
  - *Why A is incorrect:* IMAP (port 143) is a receive-side protocol for accessing stored email; it plays no role in sending messages to external recipients.
  - *Why C is incorrect:* POP3 (port 110) downloads messages from a server to a client; it is a receive-side protocol and has no role in sending outbound email.
  - *Why D is incorrect:* HTTPS (port 443) would affect the webmail interface login, but the question specifies outbound mail delivery failure, which is an SMTP function.

---

**Question 3**

A network engineer needs to verify basic IP connectivity and measure round-trip latency to a remote server. Which command is most appropriate?

A) ping

B) traceroute

C) netstat -ano

D) nslookup

- **Correct Answer:** A) ping
- **Distractor Analysis:**
  - *Why B is incorrect:* traceroute maps each intermediate router hop along the path; it provides routing path information, not a simple latency/connectivity test.
  - *Why C is incorrect:* netstat -ano displays active local TCP/UDP connections, listening ports, and process IDs on the local machine — it does not test remote connectivity.
  - *Why D is incorrect:* nslookup queries DNS servers to resolve hostnames to IP addresses; it does not measure IP-layer connectivity or latency.

---

**Question 4**

A workstation receives an IP address of 169.254.x.x after booting. The user cannot access any network resources. What is the most likely cause?

A) The DNS server is offline and cannot resolve hostnames.

B) The workstation failed to receive a DHCP lease and self-assigned an APIPA address.

C) The default gateway is configured with an incorrect subnet mask.

D) The network switch port has Port Security enabled and is blocking the device's MAC address.

- **Correct Answer:** B) The workstation failed to receive a DHCP lease and self-assigned an APIPA address.
- **Distractor Analysis:**
  - *Why A is incorrect:* A DNS failure would produce a valid DHCP-assigned IP address; the user could still ping IP addresses directly. An APIPA address (169.254.x.x) specifically indicates the DHCP discovery process failed entirely.
  - *Why C is incorrect:* A gateway subnet mask error would still result in a valid IP address being assigned; it would not produce the 169.254.x.x APIPA range.
  - *Why D is incorrect:* Port Security blocking a MAC address would prevent all frames from passing, resulting in no network link — not an APIPA address assignment.

---

**Question 5**

A security audit finds that administrators are managing network switches using a protocol that transmits all credentials and commands in cleartext over port 23. Which security control should be implemented to remediate this vulnerability?

A) Disable Telnet and configure SSH on port 22 for all switch management sessions.

B) Enable HTTPS on port 443 and disable HTTP on port 80 for the switch web interface.

C) Implement SNMP v3 with authentication and encryption to replace SNMP v1 community strings.

D) Deploy a RADIUS server to centralize authentication for all management access using 802.1X.

- **Correct Answer:** A) Disable Telnet and configure SSH on port 22 for all switch management sessions.
- **Distractor Analysis:**
  - *Why A is correct:* Port 23 is Telnet, which is the cleartext protocol described in the scenario. SSH (port 22) provides encrypted terminal access and is the direct replacement.
  - *Why B is incorrect:* Switching HTTP to HTTPS addresses web interface security, but the scenario specifically identifies port 23 (Telnet) as the problem, not HTTP/HTTPS.
  - *Why C is incorrect:* Upgrading to SNMPv3 addresses insecure SNMP community strings (port 161), not the Telnet management vulnerability on port 23.
  - *Why D is incorrect:* RADIUS/802.1X centralizes authentication but does not by itself replace the unencrypted Telnet protocol with an encrypted one.

---

**Question 6**

A client is sending an email from her corporate mail client to an external address. She reports the email appears to send successfully from her email application but the message never arrives at the recipient. Which two protocols are most likely involved in getting the message from her client to the recipient's mail server?

A) IMAP and POP3

B) HTTP and HTTPS

C) SMTP (port 587 from client) and SMTP (port 25 for server relay)

D) DNS and NTP

- **Correct Answer:** C) SMTP (port 587 from client) and SMTP (port 25 for server relay)
- **Distractor Analysis:**
  - *Why A is incorrect:* IMAP and POP3 are used for retrieving and reading email, not sending it. Neither protocol plays a role in outbound mail delivery.
  - *Why B is incorrect:* HTTP and HTTPS are web protocols; they are not involved in SMTP-based email delivery between mail servers.
  - *Why C is correct:* The client submits the email to the outbound mail server using SMTP on port 587 (authenticated submission). The mail server then relays the message to the recipient's mail server using SMTP on port 25.
  - *Why D is incorrect:* DNS is involved in looking up the MX record to route the email, and NTP is for clock synchronization, but neither directly carries the email message.

---

**Question 7**

A network administrator wants to query the IP address of the mail server responsible for handling incoming email for the domain "university.edu." Which nslookup command accomplishes this?

A) nslookup -type=A university.edu

B) nslookup -type=MX university.edu

C) nslookup -type=PTR university.edu

D) nslookup -type=CNAME university.edu

- **Correct Answer:** B) nslookup -type=MX university.edu
- **Distractor Analysis:**
  - *Why A is incorrect:* An A record maps a hostname to an IPv4 address; it returns the web server or host IP for the domain, not the mail server.
  - *Why B is correct:* An MX (Mail Exchanger) record identifies the mail server(s) responsible for handling email for a domain. This is exactly what is needed to find the incoming mail server.
  - *Why C is incorrect:* A PTR record is a reverse DNS record that maps an IP address back to a hostname; it requires an IP address as input, not a domain name.
  - *Why D is incorrect:* A CNAME record creates an alias from one hostname to another; it does not identify mail server infrastructure.

---

**Question 8**

In the TCP three-way handshake, a client sends a SYN packet to a server. The server receives it and responds. What is the next packet the client sends, and what does it signify?

A) The client sends a FIN packet, signifying it wants to close the connection.

B) The client sends an ACK packet, completing the handshake and signifying that the connection is established.

C) The client sends another SYN packet to confirm its original request.

D) The client sends a RST packet to reset the connection before data transfer.

- **Correct Answer:** B) The client sends an ACK packet, completing the handshake and signifying that the connection is established.
- **Distractor Analysis:**
  - *Why A is incorrect:* FIN is used to initiate TCP connection termination, not establishment. A FIN would only come after data transfer is complete.
  - *Why B is correct:* The three-way handshake sequence is SYN → SYN-ACK → ACK. After the server's SYN-ACK, the client sends the final ACK, completing the handshake and establishing the connection.
  - *Why C is incorrect:* Sending a second SYN is not part of the standard handshake sequence. A duplicate SYN could indicate a connection problem or retransmission, not a normal step.
  - *Why D is incorrect:* RST (Reset) abruptly terminates a connection without graceful close; it is not the normal next step in a successful handshake.

---

**Question 9**

Which of the following correctly describes the purpose of ICMP Type 11 (Time Exceeded) messages in the context of network diagnostics?

A) ICMP Type 11 is generated by a destination host to indicate that a specific service port is closed.

B) ICMP Type 11 is generated by an intermediate router when it drops a packet because the TTL field has reached zero, and it is the mechanism traceroute uses to discover each hop.

C) ICMP Type 11 is generated by the source host to signal that a fragmented packet was reassembled incorrectly.

D) ICMP Type 11 is generated by a firewall to indicate that an access control list has denied the packet.

- **Correct Answer:** B) ICMP Type 11 is generated by an intermediate router when it drops a packet because the TTL field has reached zero, and it is the mechanism traceroute uses to discover each hop.
- **Distractor Analysis:**
  - *Why A is incorrect:* A closed port generates an ICMP Type 3 Destination Unreachable message, not Type 11. Type 11 is specifically about TTL expiration.
  - *Why B is correct:* When a router receives a packet and decrements the TTL to 0, it drops the packet and sends an ICMP Type 11 Time Exceeded message back to the source. Traceroute exploits this by sending packets with TTL values starting at 1 and incrementing, causing each router to respond with Type 11.
  - *Why C is incorrect:* Fragmentation issues are handled by ICMP Type 3 Code 4 (Fragmentation Needed), not Type 11.
  - *Why D is incorrect:* Firewalls that silently drop packets generate no ICMP response. An ACL deny typically produces no ICMP message or a Type 3 in specific configurations.

---

**Question 10**

A company is standardizing its email client configuration. Users need to access their corporate email from both desktop computers and mobile devices. Messages should remain on the server after being read so they are accessible on all devices. Which email protocol best meets this requirement?

A) SMTP on port 25

B) POP3 on port 110

C) IMAP on port 143

D) FTP on port 21

- **Correct Answer:** C) IMAP on port 143
- **Distractor Analysis:**
  - *Why A is incorrect:* SMTP is an outbound email protocol used for sending and relaying messages; it cannot be used to retrieve email from a server.
  - *Why B is incorrect:* POP3 downloads email to a single client and typically deletes it from the server, preventing multi-device access. This does not meet the requirement.
  - *Why C is correct:* IMAP allows clients to access and manage email stored on the server without removing it. Multiple devices can connect to the same mailbox, and all devices stay synchronized with the server state.
  - *Why D is incorrect:* FTP is a file transfer protocol with no role in email retrieval. It is not an email protocol.

---

### Question 11

A technician uses the `nslookup` command and receives a response indicating the DNS server's IP address and the resolved hostname. Which TCP/IP model layer does DNS primarily operate at?

- A) Network Access
- B) Internet
- C) Transport
- D) Application

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* Network Access covers Layers 1–2 (Ethernet, MAC addressing) — DNS is not a framing or physical protocol.
- *Why B is incorrect:* The Internet layer handles IP addressing and routing (Layer 3) — DNS provides name resolution services above the transport layer.
- *Why C is incorrect:* The Transport layer handles TCP/UDP segmentation and port addressing — DNS uses these services but operates above them.
- *Why D is correct:* DNS is an Application layer protocol in the TCP/IP model, corresponding to OSI Layers 5–7. It uses UDP port 53 (and TCP port 53 for zone transfers) to resolve hostnames to IP addresses.

---

### Question 12

Which of the following ICMP message types is sent by a router when it drops a packet because the TTL (Time to Live) field has been decremented to zero?

- A) Type 0 – Echo Reply
- B) Type 3 – Destination Unreachable
- C) Type 8 – Echo Request
- D) Type 11 – Time Exceeded

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* ICMP Type 0 is the Echo Reply — the response to a ping request. It is not related to TTL expiration.
- *Why B is incorrect:* ICMP Type 3 (Destination Unreachable) is sent when a packet cannot reach its destination due to reasons such as a closed port, no route, or fragmentation needed.
- *Why C is incorrect:* ICMP Type 8 is the Echo Request — the outbound ping. It is sent by the source, not by a router dropping a packet.
- *Why D is correct:* ICMP Type 11 (Time Exceeded) is generated when a router decrements the TTL to zero and discards the packet. This is the mechanism `traceroute` exploits to map each hop.

---

### Question 13

A network engineer captures traffic and observes that a client sends a DHCP message to the broadcast address 255.255.255.255 with source IP 0.0.0.0. Which step of the DHCP DORA process does this represent?

- A) DHCP Offer
- B) DHCP Request
- C) DHCP Discover
- D) DHCP Acknowledgement

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* The DHCP Offer is sent from the DHCP server to the client, offering an IP address — the server sends this, not the client with source IP 0.0.0.0.
- *Why B is incorrect:* The DHCP Request is sent by the client after receiving an Offer, formally requesting the offered IP. At this stage the client still uses 0.0.0.0 as source, but the Discover (initial broadcast) precedes this step.
- *Why C is correct:* The DHCP Discover is the very first message — the client has no IP address yet (source: 0.0.0.0) and broadcasts to 255.255.255.255 seeking any available DHCP server.
- *Why D is incorrect:* The DHCP Acknowledgement is the server's final confirmation to the client that the IP address lease has been granted.

---

### Question 14

Which of the following correctly explains why UDP is preferred over TCP for real-time voice (VoIP) traffic?

- A) UDP provides built-in encryption for voice payloads, whereas TCP does not.
- B) UDP eliminates the overhead of connection setup and retransmission, making it faster and more suitable for latency-sensitive applications.
- C) UDP guarantees delivery of voice packets in order, which is essential for call quality.
- D) UDP operates at Layer 3, allowing VoIP packets to bypass router queues.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Neither UDP nor TCP provides built-in encryption. TLS (at the Presentation/Application layer) is used for encryption, regardless of whether TCP or UDP is the transport.
- *Why B is correct:* UDP has no connection handshake, no retransmission, and no sequencing overhead. In VoIP, a small amount of packet loss is tolerable, but delay caused by TCP retransmission would severely degrade call quality.
- *Why C is incorrect:* UDP does not guarantee delivery or ordering — that is TCP's responsibility. VoIP applications handle minor out-of-order delivery at the application layer using jitter buffers.
- *Why D is incorrect:* UDP operates at Layer 4 (Transport), not Layer 3. Transport layer protocol selection does not bypass router queuing.

---

### Question 15

An administrator wants to securely transfer a configuration file between two Linux servers. Which protocol should be used as a replacement for FTP that provides encrypted file transfer?

- A) TFTP (port 69)
- B) HTTP (port 80)
- C) SFTP (port 22)
- D) SMTP (port 25)

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* TFTP (Trivial File Transfer Protocol) uses UDP and provides no authentication or encryption — it is less secure than standard FTP, not more.
- *Why B is incorrect:* HTTP is a web protocol, not a file transfer protocol, and transmits data in cleartext without authentication for file transfers.
- *Why C is correct:* SFTP (SSH File Transfer Protocol) runs over SSH on port 22 and provides encrypted, authenticated file transfer between systems — it is the standard FTP replacement in secure environments.
- *Why D is incorrect:* SMTP is an email sending protocol and has no capability for interactive file transfer between servers.

---

### Question 16

A DNS record query returns the IP address associated with the hostname `www.example.com`. Which DNS record type was queried?

- A) MX record
- B) A record
- C) PTR record
- D) CNAME record

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* An MX (Mail Exchange) record maps a domain to the mail server responsible for receiving email, not to a web server's IP address.
- *Why B is correct:* An A (Address) record maps a hostname to an IPv4 address. Querying `www.example.com` and receiving an IP address is the standard function of a DNS A record lookup.
- *Why C is incorrect:* A PTR (Pointer) record performs reverse DNS lookup — mapping an IP address back to a hostname, which is the opposite of what was described.
- *Why D is incorrect:* A CNAME (Canonical Name) record creates an alias from one hostname to another hostname, not directly to an IP address.

---

### Question 17

Which of the following port numbers is used by HTTPS to provide encrypted web traffic?

- A) 80
- B) 443
- C) 8080
- D) 22

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Port 80 is used by HTTP (unencrypted web traffic). HTTPS encrypts the connection using TLS and uses a different port.
- *Why B is correct:* HTTPS (HTTP Secure) uses TCP port 443. The TLS handshake occurs before any HTTP data is exchanged, encrypting the entire session.
- *Why C is incorrect:* Port 8080 is a common alternate HTTP port used for development servers and proxies — it is not the standard HTTPS port.
- *Why D is incorrect:* Port 22 is used by SSH (Secure Shell) for encrypted terminal access, not web traffic.

---

### Question 18

A network administrator needs to synchronize the clocks of all network devices to a single authoritative time source. Which protocol is used for this purpose?

- A) SNMP
- B) LDAP
- C) NTP
- D) TFTP

**Correct Answer:** C

**Distractor Analysis:**

- *Why A is incorrect:* SNMP (Simple Network Management Protocol) is used for monitoring and managing network devices, not for clock synchronization.
- *Why B is incorrect:* LDAP (Lightweight Directory Access Protocol) is used for directory services and authentication, not time synchronization.
- *Why C is correct:* NTP (Network Time Protocol) on UDP port 123 is the standard protocol for synchronizing clocks across network devices. Accurate timestamps are essential for log correlation, Kerberos authentication, and certificate validation.
- *Why D is incorrect:* TFTP (Trivial File Transfer Protocol) is used for simple, unauthenticated file transfers (e.g., firmware uploads to switches), not for time synchronization.

---

### Question 19

A network administrator configures a server to listen on TCP port 3389. Which service is most likely running on this port?

- A) SSH
- B) HTTP
- C) SNMP
- D) RDP

**Correct Answer:** D

**Distractor Analysis:**

- *Why A is incorrect:* SSH uses TCP port 22 for encrypted remote terminal sessions — not port 3389.
- *Why B is incorrect:* HTTP uses TCP port 80 for unencrypted web traffic — not port 3389.
- *Why C is incorrect:* SNMP uses UDP port 161 for device management queries — not TCP port 3389.
- *Why D is correct:* RDP (Remote Desktop Protocol) uses TCP port 3389 by default. It provides a graphical remote desktop session between Windows clients and servers.

---

### Question 20

Which of the following describes the primary difference between TCP and UDP at the Transport layer?

- A) TCP uses IP addresses; UDP uses MAC addresses.
- B) TCP is connection-oriented and provides reliability through acknowledgements and retransmission; UDP is connectionless with no delivery guarantee.
- C) TCP operates at Layer 3; UDP operates at Layer 4.
- D) UDP supports larger payloads than TCP because it does not use port numbers.

**Correct Answer:** B

**Distractor Analysis:**

- *Why A is incorrect:* Both TCP and UDP use IP addresses (Layer 3). Neither protocol uses MAC addresses — MAC addressing is a Layer 2 (Data Link) function.
- *Why B is correct:* This is the definitive distinction. TCP uses a three-way handshake, sequence numbers, acknowledgements, and retransmission to guarantee ordered, reliable delivery. UDP omits all of these mechanisms in favor of low-overhead, low-latency transmission.
- *Why C is incorrect:* Both TCP and UDP are Layer 4 (Transport) protocols. Neither operates at Layer 3.
- *Why D is incorrect:* UDP does use port numbers — ports are a Layer 4 feature shared by both TCP and UDP. UDP headers include source and destination port fields.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
