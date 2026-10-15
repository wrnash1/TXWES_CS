# Video Script: Module 02 – TCP/IP Model and Network Protocols
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 2 of 2 | Estimated Duration: 10–12 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course &bull; Module 02</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLG49S3nxzAnmpm1HP80g85VIyFCxs34ee" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLG49S3nxzAnmpm1HP80g85VIyFCxs34ee" title="Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

---

### Pre-Roll Slide

---

### Section 1: Part 2 Introduction

Welcome back to Module 02. In Part 1, we covered the TCP/IP model, IP headers, TCP reliability, UDP speed, and ICMP diagnostics. Now in Part 2, we get into the protocols that you interact with every single day — web, email, DNS, DHCP — and the port numbers you absolutely must memorize for the Network+ exam. Let's go.

---

### Section 2: Application Layer Protocols and Port Numbers

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
<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-3321 NETWORK ADMINISTRATION</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">TCP Reliable Connection Architecture: 3-Way Handshake &amp; 4-Step Teardown</text>

  <!-- Left: 3-Way Handshake -->
  <g transform="translate(40, 95)">
    <rect width="380" height="330" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="190" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">TCP 3-Way Handshake (Establishment)</text>

    <!-- Client & Server Columns -->
    <rect x="30" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="70" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CLIENT</text>
    <rect x="270" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="310" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">SERVER</text>

    <line x1="70" y1="80" x2="70" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="310" y1="80" x2="310" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- Step 1 SYN -->
    <line x1="70" y1="110" x2="305" y2="140" stroke="#38bdf8" stroke-width="2.5"/>
    <polygon points="310,140 298,133 300,145" fill="#38bdf8"/>
    <rect x="120" y="105" width="140" height="24" fill="#0f172a" rx="3"/>
    <text x="190" y="121" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">1. SYN (Seq = x)</text>

    <!-- Step 2 SYN-ACK -->
    <line x1="310" y1="165" x2="75" y2="195" stroke="#10b981" stroke-width="2.5"/>
    <polygon points="70,195 82,188 80,200" fill="#10b981"/>
    <rect x="100" y="160" width="180" height="24" fill="#0f172a" rx="3"/>
    <text x="190" y="176" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">2. SYN-ACK (Seq=y, Ack=x+1)</text>

    <!-- Step 3 ACK -->
    <line x1="70" y1="220" x2="305" y2="250" stroke="#d9a74a" stroke-width="2.5"/>
    <polygon points="310,250 298,243 300,255" fill="#d9a74a"/>
    <rect x="120" y="215" width="140" height="24" fill="#0f172a" rx="3"/>
    <text x="190" y="231" fill="#d9a74a" font-size="10" font-weight="bold" text-anchor="middle">3. ACK (Seq=x+1, Ack=y+1)</text>

    <rect x="30" y="285" width="320" height="25" fill="#059669" rx="3"/>
    <text x="190" y="302" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">STATUS: ESTABLISHED (Bidirectional Stream)</text>
  </g>

  <!-- Right: 4-Step Teardown -->
  <g transform="translate(440, 95)">
    <rect width="370" height="330" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="6"/>
    <text x="185" y="24" fill="#f59e0b" font-size="13" font-weight="bold" text-anchor="middle">TCP 4-Step Connection Termination</text>

    <rect x="30" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="70" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CLIENT</text>
    <rect x="260" y="45" width="80" height="30" fill="#0f172a" stroke="#cbd5e1" rx="4"/><text x="300" y="65" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">SERVER</text>

    <line x1="70" y1="80" x2="70" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="300" y1="80" x2="300" y2="280" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- Step 1 FIN -->
    <line x1="70" y1="105" x2="295" y2="130" stroke="#ef4444" stroke-width="2"/>
    <polygon points="300,130 288,124 290,135" fill="#ef4444"/>
    <text x="185" y="115" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">1. FIN (Client Closes)</text>

    <!-- Step 2 ACK -->
    <line x1="300" y1="145" x2="75" y2="170" stroke="#cbd5e1" stroke-width="2"/>
    <polygon points="70,170 82,164 80,175" fill="#cbd5e1"/>
    <text x="185" y="155" fill="#cbd5e1" font-size="10" text-anchor="middle">2. ACK (Server Confirms)</text>

    <!-- Step 3 FIN -->
    <line x1="300" y1="190" x2="75" y2="215" stroke="#ef4444" stroke-width="2"/>
    <polygon points="70,215 82,209 80,220" fill="#ef4444"/>
    <text x="185" y="200" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">3. FIN (Server Closes)</text>

    <!-- Step 4 ACK -->
    <line x1="70" y1="235" x2="295" y2="260" stroke="#cbd5e1" stroke-width="2"/>
    <polygon points="300,260 288,254 290,265" fill="#cbd5e1"/>
    <text x="185" y="245" fill="#cbd5e1" font-size="10" text-anchor="middle">4. ACK (Client Confirms)</text>

    <rect x="25" y="285" width="320" height="25" fill="#b91c1c" rx="3"/>
    <text x="185" y="302" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">STATUS: CLOSED (TIME_WAIT Expired)</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="435" width="770" height="35" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="457" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Network+ Rule: UDP has NO handshake, no sequence numbers, and no delivery acknowledgments.</text>
</svg>
</div>

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

That wraps up Module 02. Review the reading guide port number table until those ports are automatic. Complete the lab using nslookup and netstat, take the quiz, and post your discussion by Wednesday.

In Module 03, we go deeper into IPv4 addressing, subnetting, and CIDR notation — the most math-intensive topic in the course. Come prepared.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 2*
