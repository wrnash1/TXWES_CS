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

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
