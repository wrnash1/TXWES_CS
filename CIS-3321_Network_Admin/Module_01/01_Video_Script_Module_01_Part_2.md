# Video Script: Module 01 – Networking Fundamentals and the OSI Model
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 2 of 2 | Estimated Duration: 10–12 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: "Module 01 Part 2 — Network Topologies, TCP/IP Model Comparison, and Lab Preview"]

---

### Section 1: Part 2 Introduction

[00:00 – 00:45]

[SHOW SLIDE: Professor Nash on camera]

Welcome back to Module 01. In Part 1, we broke down all seven OSI layers, learned the PDU names, and walked through the encapsulation process. Now in Part 2, we connect those concepts to real-world network design with topologies, compare the OSI model to the TCP/IP model you will encounter in practice, look at exam strategy, and preview your lab.

---

### Section 2: Physical Network Topologies

[00:45 – 04:00]

[SHOW DIAGRAM: Three labeled network diagrams side by side. Left: Bus topology — a single horizontal cable with five workstations tapping into it via T-connectors. Center: Ring topology — eight workstations arranged in a circle, each connected to the next. Right: Star topology — a central switch in the middle with six workstations connected by individual cables radiating outward.]

[Alt-text: Three network topology diagrams. Left diagram shows a Bus topology: a horizontal line represents a coaxial cable, with five computers connected to it at intervals using T-connectors. A terminator is shown at each end. Center diagram shows a Ring topology: eight computers are arranged in a circle, with cables connecting each computer to its two neighbors. Right diagram shows a Star topology: a central switch is in the middle, and six computers connect to it with individual cables extending outward like spokes on a wheel.]

A network topology describes how devices are arranged and connected. There are three classic physical topologies you must know for the Network+ exam.

The Bus topology uses a single shared backbone cable. All devices tap into this cable. The main advantage is simplicity and low cost. The critical disadvantage is that a break anywhere in the cable takes down the entire network. This was common in early coaxial Ethernet networks in the 1980s. You will not find it in modern networks, but it appears on the exam.

The Ring topology connects each device to exactly two neighbors, forming a closed loop. Data travels around the ring in one direction. Legacy Token Ring networks used this topology. The failure problem here is similar to bus — a single break can disrupt the ring unless the implementation uses a dual counter-rotating ring for redundancy, as seen in FDDI (Fiber Distributed Data Interface).

The Star topology is the dominant topology in modern LANs. Every device connects to a central switch with its own dedicated cable. The critical advantage is fault isolation — if one device's cable fails, only that device loses connectivity. The rest of the network is unaffected. The single point of failure in a star topology is the central switch itself, which is why enterprise networks deploy redundant switches.

> **Network+ Exam Tip:** The exam frequently presents a scenario describing a network where one device failure brings down all communication, and asks you to identify the topology. That is the Bus topology. If one cable failure takes down only one device, that is the Star topology.

---

### Section 3: Logical Topologies vs. Physical Topologies

[04:00 – 06:30]

[SHOW DIAGRAM: A Star topology diagram (central switch with four workstations). A red dashed arrow traces a path: Workstation A sends to the Switch, Switch forwards to Workstation B, Workstation B responds back through the Switch to Workstation A. A label reads "Physical Topology: Star" and "Logical Topology: Depends on traffic flow."]

[Alt-text: A Star topology diagram showing a central switch connected to four workstations labeled A, B, C, and D. A red dashed arrow shows data flowing from Workstation A to the central switch, then from the switch to Workstation B. A second arrow shows the response path from B back through the switch to A. Text labels indicate the physical layout is a Star, while the logical flow is point-to-point through the switch.]

Here is a concept that trips up many students on the Network+ exam: physical topology is not the same as logical topology.

Physical topology describes how cables are physically run and how devices are physically connected. You can see it if you walk through the server room and trace the wires.

Logical topology describes how data actually flows through the network, regardless of the physical cabling. A classic example: Token Ring networks were physically wired as a star — all cables ran to a central device called an MAU (Multistation Access Unit). But logically, data traveled in a ring pattern, passed from one device to the next in sequence around a logical circle.

Today, most networks are physically a star and logically a bus — data broadcast to a segment, with devices filtering out frames not addressed to them. VLANs can create logical separation within a physically connected network. This distinction — physical vs. logical — is a consistent exam theme.

---

### Section 4: The TCP/IP Model vs. the OSI Model

[06:30 – 09:00]

[SHOW DIAGRAM: Two side-by-side models. Left: OSI Model (7 layers, labeled 1–7 bottom to top). Right: TCP/IP Model (4 layers). Lines connect the OSI layers to their corresponding TCP/IP layers: OSI Layers 5, 6, 7 map to TCP/IP Application layer. OSI Layer 4 maps to TCP/IP Transport layer. OSI Layer 3 maps to TCP/IP Internet layer. OSI Layers 1, 2 map to TCP/IP Network Access layer.]

[Alt-text: Two vertical diagrams shown side by side. On the left is the OSI model with seven layers numbered bottom to top from Physical to Application. On the right is the TCP/IP model with four layers bottom to top: Network Access, Internet, Transport, and Application. Horizontal lines connect the two models, showing that OSI Layers 1 and 2 map to TCP/IP Network Access, OSI Layer 3 maps to TCP/IP Internet, OSI Layer 4 maps to TCP/IP Transport, and OSI Layers 5 through 7 collectively map to TCP/IP Application.]

Now let's compare the OSI model to the TCP/IP model, because this comparison appears on the Network+ exam and it is important to understand the difference.

The OSI model has seven layers and is a theoretical reference model used for teaching, troubleshooting, and describing how network components interact. It is not a protocol suite — no software implements all seven OSI layers directly.

The TCP/IP model — also called the Internet model or DoD model — has four layers and reflects how the internet actually works today. The four layers are: Network Access (covers OSI Layers 1 and 2), Internet (covers OSI Layer 3), Transport (covers OSI Layer 4), and Application (covers OSI Layers 5, 6, and 7).

When you are troubleshooting in the real world, you typically think in TCP/IP terms: is it a physical problem? A routing problem? A transport problem? When you are studying for a certification or explaining how a security device operates, you use OSI layer numbers.

> **Network+ Exam Tip:** The exam tests both models. You may see a question that says "Which TCP/IP model layer corresponds to the OSI Session and Presentation layers?" The answer is the Application layer of the TCP/IP model. Practice the mapping.

---

### Section 5: Applying the OSI Model to Troubleshooting

[09:00 – 10:30]

[SHOW SLIDE: A seven-step troubleshooting flowchart labeled "OSI Troubleshooting — Bottom Up". Each step corresponds to an OSI layer question: Layer 1: Is the cable connected? Layer 2: Is the switch port active and showing a MAC address? Layer 3: Is there a valid IP address and can we reach the gateway? Layer 4: Is the TCP connection completing the three-way handshake? Layers 5–7: Is the application responding correctly?]

One of the most valuable uses of the OSI model is systematic troubleshooting. Network engineers commonly troubleshoot "bottom-up" — they start at Layer 1 and work their way up until they find the problem.

If a user says "I can't reach the internet," the bottom-up approach goes like this. Layer 1 — is the network cable plugged in? Is the link light on? Layer 2 — does the NIC have a valid MAC address? Is the switch port up? Layer 3 — does the host have a valid IP address and default gateway? Can we ping the gateway? Layer 4 — is the TCP handshake completing? Are ports being blocked? Layer 7 — is the web server responding to HTTP requests? Is DNS resolving the hostname?

This systematic approach prevents technicians from jumping straight to advanced solutions when the problem might simply be an unplugged cable.

---

### Section 6: Lab Preview and Exam Tips

[10:30 – 12:00]

[SHOW SLIDE: Lab preview screenshot showing Cisco Packet Tracer with two PCs connected to a switch]

In this week's lab, you will use Cisco Packet Tracer to build a simple star topology, assign IP addresses, and test connectivity using the ping command. You will also use Packet Tracer's simulation mode to watch frames move through the network layer by layer — you can literally watch the encapsulation and decapsulation process happen in real time.

Before you head to the lab, review these key exam points.

The OSI model has seven layers. Know them by name and number, both directions.

Know the PDU at each layer: bit at Layer 1, frame at Layer 2, packet at Layer 3, segment or datagram at Layer 4.

Know the devices at each layer: hubs and repeaters at Layer 1, switches and bridges at Layer 2, routers at Layer 3.

Know that TCP is connection-oriented and UDP is connectionless.

Know the three-way handshake: SYN, SYN-ACK, ACK.

The TCP/IP model has four layers. Know how they map to the OSI model.

> **Network+ Exam Tip:** The CompTIA N10-008 exam is scenario-based. You will rarely be asked to simply list the layers. Instead, you will be given a trouble scenario and asked to identify the layer or protocol involved. Practice reading scenarios and mapping them to OSI layers before test day.

---

### Section 7: Module 01 Closing

[SHOW SLIDE: Module 01 key takeaways bullet list]

That wraps up Module 01. Here are your key takeaways:

- The OSI model has seven layers, each with a distinct function, PDU name, and associated devices.
- Encapsulation adds headers going down the stack; decapsulation removes them going up.
- Physical topology describes cable layout; logical topology describes data flow.
- The TCP/IP model has four layers that map to the seven OSI layers.
- Bottom-up troubleshooting starts at Layer 1 and works upward systematically.

Complete the reading guide, take the quiz, do the lab in Packet Tracer, and post your discussion by Wednesday. I'll see you in Module 02.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 2*
