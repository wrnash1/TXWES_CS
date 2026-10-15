# Video Script: Module 01 – Networking Fundamentals and the OSI Model
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 1 of 2 | Estimated Duration: 12–15 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Professor Messer &bull; CompTIA Network+ (N10-008) Complete Training Course &bull; Module 01</strong>
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

### Section 1: Welcome and Module Overview

Welcome to Module 01 of CIS-3321, Network Administration. I'm Professor Nash, and I want to start by telling you something important: everything you learn in this course — routing, switching, security, wireless — all of it is built on a single conceptual framework called the OSI model. If you invest the time to truly internalize the OSI model this week, every topic that follows will make significantly more sense.

This module has two parts. In Part 1, we cover the theoretical foundation: what the OSI model is, why it exists, what happens at each layer, and how data is transformed as it moves through the stack. In Part 2, we apply those concepts to network topologies and start connecting theory to the tools you will use every day.

Let's begin.

---

### Section 2: Why Do We Need a Network Model?

Before the OSI model existed, networks were proprietary. IBM had its own networking standard. Digital Equipment Corporation had another. A computer from one vendor literally could not communicate with a computer from another vendor without expensive, custom-built translation hardware.

In 1984, the International Organization for Standardization — ISO — published the OSI model to solve this problem. It defined a universal set of rules that any vendor could follow, allowing any two devices, from any manufacturer, running any operating system, to communicate over a network.

The OSI model does not describe actual software. It is a reference model — a conceptual framework. Think of it like building codes for construction. The code does not describe a specific house, but if every builder follows the code, all houses can be safely plumbed, wired, and connected to the city infrastructure.

---

### Section 3: The Seven Layers of the OSI Model
<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 850 490" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 850px; background:#0f172a; border-radius:10px; border:2px solid #1b365d; font-family:-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif;">
  <rect width="100%" height="45" fill="#1b365d"/>
  <text x="425" y="28" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY • CIS-3321 NETWORK ADMINISTRATION</text>
  <text x="425" y="75" fill="#d9a74a" font-size="18" font-weight="bold" text-anchor="middle">OSI 7-Layer Reference Model &amp; Protocol Data Unit (PDU) Encapsulation</text>

  <!-- Left: OSI 7 Layers -->
  <g transform="translate(40, 95)">
    <rect width="400" height="340" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="200" y="24" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">OSI 7-Layer Stack (Top to Bottom)</text>

    <!-- Layer 7 -->
    <rect x="20" y="38" width="360" height="36" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="35" y="60" fill="#c084fc" font-size="11" font-weight="bold">Layer 7: Application</text>
    <text x="365" y="60" fill="#94a3b8" font-size="10" text-anchor="end">HTTP, DNS, DHCP, SSH (Data)</text>

    <!-- Layer 6 -->
    <rect x="20" y="79" width="360" height="36" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="35" y="101" fill="#c084fc" font-size="11" font-weight="bold">Layer 6: Presentation</text>
    <text x="365" y="101" fill="#94a3b8" font-size="10" text-anchor="end">TLS/SSL, JPEG, ASCII, Encryption</text>

    <!-- Layer 5 -->
    <rect x="20" y="120" width="360" height="36" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="35" y="142" fill="#c084fc" font-size="11" font-weight="bold">Layer 5: Session</text>
    <text x="365" y="142" fill="#94a3b8" font-size="10" text-anchor="end">RPC, NetBIOS, Sockets (Dialog)</text>

    <!-- Layer 4 -->
    <rect x="20" y="161" width="360" height="36" fill="#0f172a" stroke="#3b82f6" rx="3"/>
    <text x="35" y="183" fill="#60a5fa" font-size="11" font-weight="bold">Layer 4: Transport</text>
    <text x="365" y="183" fill="#93c5fd" font-size="10" text-anchor="end">TCP / UDP Ports (Segment)</text>

    <!-- Layer 3 -->
    <rect x="20" y="202" width="360" height="36" fill="#0f172a" stroke="#ef4444" rx="3"/>
    <text x="35" y="224" fill="#f87171" font-size="11" font-weight="bold">Layer 3: Network</text>
    <text x="365" y="224" fill="#fca5a5" font-size="10" text-anchor="end">IP Addressing, Routers (Packet)</text>

    <!-- Layer 2 -->
    <rect x="20" y="243" width="360" height="36" fill="#0f172a" stroke="#10b981" rx="3"/>
    <text x="35" y="265" fill="#34d399" font-size="11" font-weight="bold">Layer 2: Data Link</text>
    <text x="365" y="265" fill="#86efac" font-size="10" text-anchor="end">MAC Addr, Switches (Frame)</text>

    <!-- Layer 1 -->
    <rect x="20" y="284" width="360" height="36" fill="#0f172a" stroke="#d9a74a" rx="3"/>
    <text x="35" y="306" fill="#fde047" font-size="11" font-weight="bold">Layer 1: Physical</text>
    <text x="365" y="306" fill="#fef08a" font-size="10" text-anchor="end">Cables, Radio, Bits (1s &amp; 0s)</text>
  </g>

  <!-- Right: Encapsulation Flow -->
  <g transform="translate(460, 95)">
    <rect width="350" height="340" fill="#1e293b" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="175" y="24" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Data Encapsulation Flow (Downward)</text>

    <!-- Payload -->
    <rect x="25" y="45" width="300" height="35" fill="#0f172a" stroke="#a855f7" rx="3"/>
    <text x="175" y="67" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">Application Data Payload</text>

    <!-- Transport Segment -->
    <rect x="25" y="100" width="300" height="40" fill="#0f172a" stroke="#3b82f6" rx="3"/>
    <rect x="30" y="105" width="90" height="30" fill="#1e3a8a" rx="2"/>
    <text x="75" y="124" fill="#93c5fd" font-size="10" font-weight="bold" text-anchor="middle">TCP/UDP Hdr</text>
    <text x="215" y="124" fill="#c084fc" font-size="10" text-anchor="middle">Data Segment</text>

    <!-- Network Packet -->
    <rect x="25" y="160" width="300" height="40" fill="#0f172a" stroke="#ef4444" rx="3"/>
    <rect x="30" y="165" width="65" height="30" fill="#7f1d1d" rx="2"/>
    <text x="62" y="184" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">IP Header</text>
    <rect x="100" y="165" width="70" height="30" fill="#1e3a8a" rx="2"/>
    <text x="135" y="184" fill="#93c5fd" font-size="9" text-anchor="middle">TCP Hdr</text>
    <text x="240" y="184" fill="#c084fc" font-size="10" text-anchor="middle">IP Packet</text>

    <!-- Data Link Frame -->
    <rect x="25" y="220" width="300" height="40" fill="#0f172a" stroke="#10b981" rx="3"/>
    <rect x="30" y="225" width="60" height="30" fill="#064e3b" rx="2"/>
    <text x="60" y="244" fill="#86efac" font-size="9" font-weight="bold" text-anchor="middle">Frame Hdr</text>
    <rect x="95" y="225" width="55" height="30" fill="#7f1d1d" rx="2"/>
    <text x="122" y="244" fill="#fca5a5" font-size="8" text-anchor="middle">IP Hdr</text>
    <rect x="155" y="225" width="55" height="30" fill="#1e3a8a" rx="2"/>
    <text x="182" y="244" fill="#93c5fd" font-size="8" text-anchor="middle">TCP Hdr</text>
    <rect x="265" y="225" width="55" height="30" fill="#064e3b" rx="2"/>
    <text x="292" y="244" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">FCS Trail</text>

    <!-- Physical Bits -->
    <rect x="25" y="280" width="300" height="35" fill="#0f172a" stroke="#d9a74a" rx="3"/>
    <text x="175" y="302" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">01101001 01101110 01110100 (Physical Bits on Wire)</text>
  </g>

  <!-- Footer Banner -->
  <rect x="40" y="445" width="770" height="32" fill="#1e293b" stroke="#334155" rx="6"/>
  <text x="425" y="466" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">⚡ Mnemonic: All People Seem To Need Data Processing | PDUs: Don't Some People Fear Birthdays (Data, Segment, Packet, Frame, Bit)</text>
</svg>
</div>

[Alt-text: A vertical diagram showing seven stacked rectangles representing the OSI model layers. From bottom to top: Layer 1 Physical (red), Layer 2 Data Link (orange), Layer 3 Network (yellow), Layer 4 Transport (green), Layer 5 Session (teal), Layer 6 Presentation (blue), Layer 7 Application (purple). Each rectangle is labeled with the layer number and name.]

There are seven layers. Let me give you a clear description of each one, working from the bottom up — from the physical world of cables and radio waves up to the software world of your web browser.

**Layer 1 — Physical.** This is the actual transmission medium. Copper wire. Fiber optic cable. Radio frequency signals for Wi-Fi. Layer 1 is where electrical signals, light pulses, or radio waves carry raw binary data — ones and zeros — from one device to another. Devices at this layer include hubs, repeaters, and modems. The Protocol Data Unit at Layer 1 is simply called a bit.

**Layer 2 — Data Link.** This layer organizes raw bits into meaningful frames and handles delivery within a single network segment. It introduces the concept of the MAC address — a 48-bit hardware identifier burned into every Network Interface Card. When a switch looks at incoming traffic and decides which port to forward it to, it is making a Layer 2 decision based on MAC addresses. The PDU at Layer 2 is the frame.

**Layer 3 — Network.** This is where IP addresses live. Layer 3 is responsible for logical addressing and routing — moving packets from one network to another. Routers operate at Layer 3. When your laptop sends data to a web server on the other side of the world, the packet passes through dozens of routers, each making a Layer 3 forwarding decision. The PDU at Layer 3 is the packet.

**Layer 4 — Transport.** This layer provides end-to-end communication between hosts. The two primary protocols here are TCP and UDP. TCP is connection-oriented and reliable — it uses a three-way handshake, sequence numbers, and acknowledgements to guarantee delivery. UDP is connectionless and fast — there are no guarantees, but the lower overhead makes it ideal for real-time applications like video streaming and VoIP. The PDU at Layer 4 is called a segment for TCP or a datagram for UDP.

**Layer 5 — Session.** The session layer establishes, manages, and terminates communication sessions between two hosts. Think of a session as a conversation — Layer 5 opens the conversation, keeps track of it, and closes it cleanly when finished. Protocols like NetBIOS and RPC (Remote Procedure Call) operate here.

**Layer 6 — Presentation.** This layer handles data formatting, translation, encryption, and compression. If your browser connects to a bank website over HTTPS, the TLS encryption and decryption happening on your machine occurs at the Presentation layer. Character encoding standards like ASCII and Unicode also belong here.

**Layer 7 — Application.** This is the layer closest to the user — not the application software itself, but the protocols that applications use to communicate. HTTP, HTTPS, SMTP, FTP, DNS, and DHCP are all Layer 7 protocols. When you open a web browser and type a URL, the application layer handles the HTTP request.

---

### Section 4: Mnemonics for the OSI Model

For the CompTIA Network+ exam, you must be able to name the layers from memory — both top-to-bottom and bottom-to-top.

Bottom to top: "Please Do Not Throw Sausage Pizza Away
Physical, Data Link, Network, Transport, Session, Presentation, Application.

Top to bottom: "All People Seem To Need Data Processing
Application, Presentation, Session, Transport, Network, Data Link, Physical.

Pick one and commit it to memory this week. You will use it throughout the entire course.

> **Network+ Exam Tip:** The exam will describe a scenario and ask you which OSI layer is involved. For example: "A device is dropping frames due to a MAC address conflict." That is Layer 2. "A router is unable to forward packets due to a full routing table." That is Layer 3. Practice mapping scenarios to layers.

---

### Section 5: Protocol Data Units and Encapsulation

[Alt-text: A diagram showing the encapsulation process through the OSI layers. Starting at Layer 7 as a plain data block, each lower layer adds a protocol header. Layer 4 adds a transport header creating a Segment. Layer 3 adds an IP header creating a Packet. Layer 2 adds a frame header and trailer creating a Frame. Layer 1 outputs the Frame as a bitstream.]

This brings us to one of the most important concepts in networking: encapsulation and decapsulation.

When you send data across a network, it does not simply travel as-is. As the data moves down the OSI stack on the sending device, each layer adds its own header — and sometimes a trailer — wrapping the data like a series of envelopes. This process is called encapsulation.

Here is how it works step by step. Your email application creates data at Layer 7. At Layer 4, TCP adds a header containing source and destination port numbers, sequence numbers, and flags — this creates a segment. At Layer 3, IP adds a header containing source and destination IP addresses — this creates a packet. At Layer 2, Ethernet adds a frame header containing source and destination MAC addresses, and a Frame Check Sequence trailer for error detection — this creates a frame. At Layer 1, the frame is transmitted as a stream of bits.

When the data arrives at the destination, the process reverses. The receiving device strips each header as the data moves up the stack — this is called decapsulation. The NIC strips the frame header, the OS strips the IP header, the TCP stack strips the transport header, and the application receives the original data.

This is why the OSI model is so powerful. Each layer trusts that the layers below it are handling their job. The IP layer does not need to know anything about Ethernet frames. The TCP layer does not need to know anything about IP routing. Each layer has a clean, well-defined responsibility.

---

### Section 6: Part 1 Summary

Let's recap Part 1. You now understand why the OSI model was created and what happens at each of the seven layers. You know the PDU name at each layer — bit, frame, packet, segment, data. You understand encapsulation (adding headers going down) and decapsulation (removing headers going up).

In Part 2, we will look at how these layers map to real-world network topologies, introduce the TCP/IP model comparison, and preview the lab exercise where you will observe encapsulation directly in Packet Tracer.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 1*
