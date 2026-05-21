# Reading Guide: Module 02 - TCP/IP Model and Network Protocols
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 02 – TCP/IP Model and Network Protocols**! This module bridges the OSI model from Module 01 to the practical TCP/IP protocol suite that powers every modern network. The TCP/IP model is what actually runs on the internet, and CompTIA Network+ N10-009 expects you to map protocols to their correct layers, know their port numbers, and understand how they establish connections. Pay special attention to the differences between TCP and UDP, and the specific port numbers for every major protocol listed here.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **TCP/IP Model**: A four-layer practical networking model that describes how data is transmitted over the internet. Its layers are Application (maps to OSI L5-L7), Transport (maps to OSI L4), Internet (maps to OSI L3), and Network Access/Link (maps to OSI L1-L2).
*   **TCP (Transmission Control Protocol)**: A connection-oriented, reliable Layer 4 protocol that guarantees delivery through acknowledgments (ACKs), sequencing, and retransmission. Establishes connections with a three-way handshake: SYN → SYN-ACK → ACK. Used where data integrity matters (HTTP, FTP, email).
*   **UDP (User Datagram Protocol)**: A connectionless, unreliable Layer 4 protocol with no handshake, no acknowledgments, and no guaranteed delivery. Used where speed matters more than reliability (VoIP, DNS queries, video streaming, DHCP).
*   **HTTP (HyperText Transfer Protocol)**: The application-layer protocol for web browsing. Operates on **port 80**. Transmits data in cleartext — exam tip: always prefer HTTPS in security scenarios.
*   **HTTPS (HTTP Secure)**: HTTP encrypted with TLS/SSL. Operates on **port 443**. The modern standard for all web traffic. Uses asymmetric encryption for key exchange, then symmetric encryption for data transfer.
*   **FTP (File Transfer Protocol)**: A protocol for transferring files between hosts. Uses **port 21** for control/commands and **port 20** for active-mode data transfer. Transmits credentials in cleartext — replaced by SFTP or FTPS in secure environments.
*   **SSH (Secure Shell)**: An encrypted protocol for remote terminal access and secure file transfer (SFTP). Operates on **port 22**. Replaces Telnet (port 23) which sends all data including passwords in cleartext.
*   **SMTP (Simple Mail Transfer Protocol)**: Used for sending and relaying email between mail servers. Operates on **port 25** (server-to-server) and port 587 (client submission with authentication).
*   **POP3 (Post Office Protocol v3)**: Downloads email from a server to a client and typically deletes it from the server. Operates on **port 110** (unencrypted) or port 995 (POP3S over TLS).
*   **IMAP (Internet Message Access Protocol)**: Accesses email on the server without downloading/deleting it, allowing multi-device access. Operates on **port 143** (unencrypted) or port 993 (IMAPS over TLS).
*   **DNS (Domain Name System)**: Resolves human-readable hostnames (www.example.com) to IP addresses. Operates on **port 53**, using UDP for queries and TCP for zone transfers. Record types: A (IPv4), AAAA (IPv6), MX (mail), CNAME (alias), PTR (reverse lookup), NS (name server).
*   **DHCP (Dynamic Host Configuration Protocol)**: Automatically assigns IP address, subnet mask, default gateway, and DNS server to clients. Uses **port 67** (server) and **port 68** (client). Uses UDP. Process: DORA — Discover, Offer, Request, Acknowledge.
*   **SNMP (Simple Network Management Protocol)**: Used for monitoring and managing network devices. Operates on **port 161** (queries) and **port 162** (traps/alerts). SNMPv3 adds authentication and encryption; earlier versions (v1, v2c) use insecure community strings.
*   **RDP (Remote Desktop Protocol)**: Microsoft's protocol for graphical remote desktop access. Operates on **port 3389**.
*   **NTP (Network Time Protocol)**: Synchronizes clocks across network devices. Operates on **port 123** using UDP. Critical for authentication protocols like Kerberos and for log correlation.
*   **ICMP (Internet Control Message Protocol)**: A Layer 3 protocol used for error reporting and diagnostic functions (ping uses ICMP Echo Request/Reply; traceroute uses ICMP TTL-exceeded messages). ICMP has no port number — it operates directly over IP.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** Protocols and the TCP/IP model fall under **Domain 1.0 – Networking Concepts (23%)**. Port numbers are among the most directly tested facts on the entire exam — memorize every port in the glossary above.
*   **TCP vs. UDP decision rule**: If the exam scenario mentions "reliability," "guaranteed delivery," "connection-oriented," or "acknowledgments" — the answer involves TCP. If it mentions "speed," "real-time," "low overhead," or "streaming" — the answer involves UDP. DNS uses both (UDP for lookups, TCP for zone transfers).
*   **DHCP DORA sequence trick**: The exam tests the order: **Discover** (client broadcasts looking for a server), **Offer** (server offers an IP), **Request** (client requests that IP), **Acknowledge** (server confirms the lease). All four messages are broadcasts except the ACK, which can be unicast.
*   **Common exam trap — SMTP vs. POP3 vs. IMAP**: SMTP is for *sending* email; POP3 and IMAP are for *receiving*. The exam will describe a scenario and ask which protocol applies.
*   **Memorize the "secure" port alternatives**: Standard HTTP (80) → HTTPS (443); FTP (21) → SFTP (22) or FTPS (990); LDAP (389) → LDAPS (636); POP3 (110) → POP3S (995); IMAP (143) → IMAPS (993).
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers all protocols and their ports in the Network+ section. His port-number videos are essential study material.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters covering **Application Layer Protocols and TCP/IP** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the TCP/UDP comparison, the three-way handshake, and the DHCP exchange.
*   **Required Video:** Watch Professor Messer's videos on **Network Protocols** and **TCP/UDP** from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/). These free videos provide worked examples that directly reflect exam question scenarios.

---

### Lab & Command Integration
In this week's hands-on lab, you will use Wireshark to capture a DHCP exchange and a DNS query, labeling each packet with its protocol name, port number, and transport protocol (TCP or UDP). You will also use `nslookup` to perform manual DNS queries and `netstat -an` to observe active TCP connections and their states.

---

### 3. Study Checklist
*   [ ] Memorize all port numbers in the glossary, including the secure (TLS) alternatives.
*   [ ] Be able to identify whether each protocol uses TCP, UDP, or both, and explain why.
*   [ ] Recite the DHCP DORA sequence from memory.
*   [ ] Read the **Application Layer Protocols** section in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's protocol videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
