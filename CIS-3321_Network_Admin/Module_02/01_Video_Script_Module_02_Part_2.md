# Video Script: Module 02 – TCP/IP Model and Network Protocols
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 2 of 2 | Estimated Duration: 10–12 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: "Module 02 Part 2 — Application Layer Protocols, Port Numbers, and DHCP"]

---

### Section 1: Part 2 Introduction

[00:00 – 00:45]

[SHOW SLIDE: Professor Nash on camera]

Welcome back to Module 02. In Part 1, we covered the TCP/IP model, IP headers, TCP reliability, UDP speed, and ICMP diagnostics. Now in Part 2, we get into the protocols that you interact with every single day — web, email, DNS, DHCP — and the port numbers you absolutely must memorize for the Network+ exam. Let's go.

---

### Section 2: Application Layer Protocols and Port Numbers

[00:45 – 04:30]

[SHOW SLIDE: Port number reference table — left column protocol name, right column port number and transport protocol]

Port numbers identify specific services on a host. When a packet arrives at your computer, the operating system uses the destination port number to determine which application or service should receive the data. There are 65,535 possible port numbers. The ones from 0 to 1,023 are called well-known ports and are assigned to specific services by IANA.

Let's walk through the ones the exam will test you on.

HTTP — Hypertext Transfer Protocol — port 80, TCP. This is standard unencrypted web traffic. If you see port 80 on the exam, think unencrypted web.

HTTPS — HTTP Secure — port 443, TCP. This is HTTP encrypted with TLS. All modern websites use HTTPS. Port 443 plus TLS equals encrypted web.

FTP — File Transfer Protocol — uses two ports. Port 21 is the control channel (commands). Port 20 is the data channel in active mode. FTP transmits credentials in cleartext, making it insecure by default. SFTP (port 22) or FTPS are the secure alternatives.

SSH — Secure Shell — port 22, TCP. SSH provides encrypted terminal access to remote systems. It replaces Telnet, which uses port 23 and sends everything including passwords in cleartext. The exam will always favor SSH over Telnet in a security-conscious scenario.

SMTP — Simple Mail Transfer Protocol — port 25, TCP. SMTP is used for sending and relaying email between mail servers. Port 587 is used for client submission (authenticated SMTP).

POP3 — Post Office Protocol version 3 — port 110, TCP. POP3 downloads email from a server to a client and typically deletes it from the server. The secure version, POP3S, uses port 995.

IMAP — Internet Message Access Protocol — port 143, TCP. IMAP lets clients access and manage email stored on the server without permanently downloading it. This enables multi-device access to the same mailbox. Secure IMAP uses port 993.

DNS — Domain Name System — port 53. DNS uses UDP for regular queries and TCP for zone transfers. This is the one protocol that uses both, and the exam tests this distinction.

DHCP — Dynamic Host Configuration Protocol — ports 67 and 68, UDP. Port 67 is the server port; port 68 is the client port. All DHCP messages use UDP because they involve broadcasts before the client has an IP address.

SNMP — Simple Network Management Protocol — port 161 for queries, port 162 for traps. SNMPv3 adds authentication and encryption; v1 and v2c use insecure community strings.

RDP — Remote Desktop Protocol — port 3389, TCP. Microsoft's protocol for graphical remote desktop access.

NTP — Network Time Protocol — port 123, UDP. Synchronizes clocks across network devices. Critical for authentication protocols like Kerberos and for accurate log timestamps.

> **Network+ Exam Tip:** Port numbers are among the most directly and frequently tested facts on the entire exam. Make yourself a flashcard set for every port in this list and review them daily until test day. A significant portion of the exam's "which protocol is this" questions can be answered in under five seconds if you have these memorized.

---

### Section 3: DHCP — Automatic IP Configuration

[04:30 – 07:00]

[SHOW DIAGRAM: DHCP DORA sequence diagram. Four steps shown as arrows between a client PC on the left and a DHCP server on the right. Step 1: DISCOVER (broadcast from client to all). Step 2: OFFER (server to client — offers IP lease). Step 3: REQUEST (client broadcasts — formally requests the offered IP). Step 4: ACKNOWLEDGE (server confirms lease).]

[Alt-text: A sequence diagram showing the DHCP DORA process. On the left is an icon of a client workstation labeled Client. On the right is a server icon labeled DHCP Server. Four horizontal arrows are shown. Arrow 1 points from client to server and is labeled DISCOVER (broadcast). Arrow 2 points from server to client and is labeled OFFER (IP address lease offer). Arrow 3 points from client to server and is labeled REQUEST (client requests the offered IP). Arrow 4 points from server to client and is labeled ACKNOWLEDGE (server confirms the lease).]

DHCP (Dynamic Host Configuration Protocol) automatically assigns IP configuration to clients when they connect to a network. Without DHCP, a network administrator would have to manually configure every single device's IP address, subnet mask, default gateway, and DNS server. On a large network, that is thousands of manual configurations. DHCP automates all of it.

The DHCP process uses the acronym DORA.

Discover — The client broadcasts a DHCPDISCOVER message to the network (destination IP 255.255.255.255) because it does not yet have an IP address and does not know where the DHCP server is.

Offer — The DHCP server receives the broadcast and responds with a DHCPOFFER, proposing an available IP address, subnet mask, default gateway, DNS server, and lease duration.

Request — The client officially requests the offered address by broadcasting a DHCPREQUEST. This broadcast also notifies any other DHCP servers on the network that the client has selected one offer.

Acknowledge — The DHCP server sends a DHCPACK confirming the lease. The client now has a valid IP configuration.

An important detail: DHCP leases are temporary. When the lease reaches 50% of its duration, the client attempts to renew with the same server. If renewal fails, the client tries again at 87.5%. If the DHCP server is unreachable when both renewal attempts fail, the client's lease expires and it returns to the DISCOVER stage.

---

### Section 4: DNS — Name Resolution

[07:00 – 09:30]

[SHOW DIAGRAM: DNS resolution sequence. A laptop (Client) on the left sends a DNS query for "www.example.com" to a DNS Resolver. The Resolver queries a Root Name Server, then a TLD (.com) Name Server, then the Authoritative Name Server for example.com. The authoritative server returns the IP address 93.184.216.34. The resolver returns this to the client.]

[Alt-text: A DNS resolution flowchart. On the far left is a laptop labeled Client sending a query for www.example.com to a Recursive Resolver. The resolver sends a query to a Root Name Server (labeled "Who handles .com?"). The root server refers to a TLD Name Server. The resolver queries the TLD server (labeled "Who handles example.com?"). The TLD server refers to the Authoritative Name Server for example.com. The resolver queries the authoritative server and receives the IP address. The resolver returns the IP address to the client.]

DNS is the phone book of the internet. When you type a web address into your browser, your computer does not actually know the IP address — it knows the hostname. DNS translates that hostname into an IP address that the network can route to.

DNS uses a hierarchical structure. At the top are the Root Name Servers (13 clusters globally). Below that are Top-Level Domain servers (.com, .org, .edu, .gov). Below that are authoritative name servers for individual domains.

A DNS resolver on your network (often provided by your ISP or a public resolver like 8.8.8.8) handles the recursive lookup process — it queries the hierarchy on your behalf and returns the final answer.

DNS record types you must know for the exam:

A record — maps a hostname to an IPv4 address.

AAAA record — maps a hostname to an IPv6 address.

MX record — identifies the mail server for a domain.

CNAME record — creates an alias that points to another hostname.

PTR record — reverse lookup; maps an IP address back to a hostname.

NS record — identifies the authoritative name servers for a domain.

SOA record — contains administrative information about a DNS zone.

---

### Section 5: Lab Preview and Key Takeaways

[09:30 – 11:30]

[SHOW SLIDE: Lab preview — netstat and nslookup command examples]

In this week's lab, you will use command-line tools to observe TCP/IP protocols in action.

The nslookup command lets you manually query DNS servers. You will run it to look up A records, MX records, and see which DNS server your system is using.

The netstat command shows active TCP connections on your machine. netstat -an shows all connections and listening ports with numerical addresses. You will be able to see which ports are open and what state TCP connections are in.

Before heading to the lab, here are the critical module takeaways.

The TCP/IP model has four layers: Network Access, Internet, Transport, and Application.

TCP is connection-oriented, reliable, and uses a three-way handshake. UDP is connectionless and fast.

ICMP provides network diagnostics — ping uses Echo Request and Echo Reply; traceroute uses Time Exceeded.

DHCP uses the DORA process (Discover, Offer, Request, Acknowledge) over UDP ports 67 and 68.

DNS uses port 53, UDP for queries, TCP for zone transfers.

Know every port number in the reading guide table before you take the quiz.

> **Network+ Exam Tip:** The exam frequently describes a protocol scenario and asks you to identify the protocol, port number, and whether it uses TCP or UDP. Practice reading a scenario like "a client is retrieving email and keeping a copy on the server for access from multiple devices" — that is IMAP on port 143. Build the mental reflex to map scenarios to protocols instantly.

---

### Section 6: Module 02 Closing

[SHOW SLIDE: Module 02 key takeaways list]

That wraps up Module 02. Review the reading guide port number table until those ports are automatic. Complete the lab using nslookup and netstat, take the quiz, and post your discussion by Wednesday.

In Module 03, we go deeper into IPv4 addressing, subnetting, and CIDR notation — the most math-intensive topic in the course. Come prepared.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 2*
