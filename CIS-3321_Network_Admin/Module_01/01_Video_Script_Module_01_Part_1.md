# Video Script: Module 01 – Networking Fundamentals and the OSI Model
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 1 of 2 | Estimated Duration: 12–15 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CIS-3321 Network Administration | Module 01: Networking Fundamentals and the OSI Model | Texas Wesleyan University"]

---

### Section 1: Welcome and Module Overview

[00:00 – 01:30]

[SHOW SLIDE: Professor Nash on camera with module title card]

Welcome to Module 01 of CIS-3321, Network Administration. I'm Professor Nash, and I want to start by telling you something important: everything you learn in this course — routing, switching, security, wireless — all of it is built on a single conceptual framework called the OSI model. If you invest the time to truly internalize the OSI model this week, every topic that follows will make significantly more sense.

This module has two parts. In Part 1, we cover the theoretical foundation: what the OSI model is, why it exists, what happens at each layer, and how data is transformed as it moves through the stack. In Part 2, we apply those concepts to network topologies and start connecting theory to the tools you will use every day.

Let's begin.

---

### Section 2: Why Do We Need a Network Model?

[01:30 – 03:30]

[SHOW SLIDE: Split screen — left side shows two computers from different manufacturers (a Dell PC and an Apple Mac) with a question mark between them; right side shows the same two computers connected with a green checkmark]

Before the OSI model existed, networks were proprietary. IBM had its own networking standard. Digital Equipment Corporation had another. A computer from one vendor literally could not communicate with a computer from another vendor without expensive, custom-built translation hardware.

In 1984, the International Organization for Standardization — ISO — published the OSI model to solve this problem. It defined a universal set of rules that any vendor could follow, allowing any two devices, from any manufacturer, running any operating system, to communicate over a network.

The OSI model does not describe actual software. It is a reference model — a conceptual framework. Think of it like building codes for construction. The code does not describe a specific house, but if every builder follows the code, all houses can be safely plumbed, wired, and connected to the city infrastructure.

---

### Section 3: The Seven Layers of the OSI Model

[03:30 – 07:00]

[SHOW DIAGRAM: Vertical stack of seven labeled rectangles, numbered bottom to top: Layer 1 Physical, Layer 2 Data Link, Layer 3 Network, Layer 4 Transport, Layer 5 Session, Layer 6 Presentation, Layer 7 Application. Each layer has a color band — warm colors for Layers 1–4, cool colors for Layers 5–7.]

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

[07:00 – 08:30]

[SHOW SLIDE: Two mnemonic phrases with each word aligned to a layer]

For the CompTIA Network+ exam, you must be able to name the layers from memory — both top-to-bottom and bottom-to-top.

Bottom to top: "Please Do Not Throw Sausage Pizza Away"
Physical, Data Link, Network, Transport, Session, Presentation, Application.

Top to bottom: "All People Seem To Need Data Processing"
Application, Presentation, Session, Transport, Network, Data Link, Physical.

Pick one and commit it to memory this week. You will use it throughout the entire course.

> **Network+ Exam Tip:** The exam will describe a scenario and ask you which OSI layer is involved. For example: "A device is dropping frames due to a MAC address conflict." That is Layer 2. "A router is unable to forward packets due to a full routing table." That is Layer 3. Practice mapping scenarios to layers.

---

### Section 5: Protocol Data Units and Encapsulation

[08:30 – 11:30]

[SHOW DIAGRAM: A vertical stack showing data transformation at each layer. At the top, a block labeled "Data" at Layer 7. As the stack descends, each layer adds a header. At Layer 4, a "TCP/UDP Header" wraps the data, forming a Segment. At Layer 3, an "IP Header" wraps the segment, forming a Packet. At Layer 2, a "Frame Header" and "FCS Trailer" wrap the packet, forming a Frame. At Layer 1, the frame becomes a stream of Bits.]

[Alt-text: A diagram showing the encapsulation process through the OSI layers. Starting at Layer 7 as a plain data block, each lower layer adds a protocol header. Layer 4 adds a transport header creating a Segment. Layer 3 adds an IP header creating a Packet. Layer 2 adds a frame header and trailer creating a Frame. Layer 1 outputs the Frame as a bitstream.]

This brings us to one of the most important concepts in networking: encapsulation and decapsulation.

When you send data across a network, it does not simply travel as-is. As the data moves down the OSI stack on the sending device, each layer adds its own header — and sometimes a trailer — wrapping the data like a series of envelopes. This process is called encapsulation.

Here is how it works step by step. Your email application creates data at Layer 7. At Layer 4, TCP adds a header containing source and destination port numbers, sequence numbers, and flags — this creates a segment. At Layer 3, IP adds a header containing source and destination IP addresses — this creates a packet. At Layer 2, Ethernet adds a frame header containing source and destination MAC addresses, and a Frame Check Sequence trailer for error detection — this creates a frame. At Layer 1, the frame is transmitted as a stream of bits.

When the data arrives at the destination, the process reverses. The receiving device strips each header as the data moves up the stack — this is called decapsulation. The NIC strips the frame header, the OS strips the IP header, the TCP stack strips the transport header, and the application receives the original data.

This is why the OSI model is so powerful. Each layer trusts that the layers below it are handling their job. The IP layer does not need to know anything about Ethernet frames. The TCP layer does not need to know anything about IP routing. Each layer has a clean, well-defined responsibility.

---

### Section 6: Part 1 Summary

[11:30 – 13:00]

[SHOW SLIDE: Summary table with three columns — Layer Name, PDU Name, Key Devices/Protocols]

Let's recap Part 1. You now understand why the OSI model was created and what happens at each of the seven layers. You know the PDU name at each layer — bit, frame, packet, segment, data. You understand encapsulation (adding headers going down) and decapsulation (removing headers going up).

In Part 2, we will look at how these layers map to real-world network topologies, introduce the TCP/IP model comparison, and preview the lab exercise where you will observe encapsulation directly in Packet Tracer.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 1*
