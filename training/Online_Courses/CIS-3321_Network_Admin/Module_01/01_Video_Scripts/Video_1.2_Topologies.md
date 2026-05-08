# Video Script 1.2: Physical vs. Logical Topologies
**Course:** CIS 3321 - Network Administration (CompTIA Network+)
**Module:** 1 (Networking Fundamentals)
**Estimated Duration:** 5 minutes

---

## Script & Visual Directives

**[00:00 - 01:00] Introduction**
**Visual:** Instructor on camera.
**Audio:** "Welcome back. Now that we understand the OSI model layers, let's look at how we physically and logically arrange our devices to communicate. In networking, we call this a topology."

**[01:00 - 03:00] Physical Topologies**
**Visual:** A split-screen graphic showing three diagrams: a Bus, a Ring, and a Star topology.
**[Alt-text: Three network diagrams. Left: A Bus topology showing a single central cable with computers branching off it. Middle: A Ring topology showing computers connected in a closed circle. Right: A Star topology showing a central switch with computers radiating outward like points on a star.]**
**Audio:** "A physical topology is how the cables are actually plugged in. Historically, we used Bus or Ring topologies. If the main cable or ring broke, the whole network went down. Today, we almost exclusively use the Star topology. In a Star, all devices plug into a central switch. If one cable breaks, only that single device goes offline, making it highly resilient."

**[03:00 - 04:30] Logical Topologies**
**Visual:** The Star topology graphic remains, but a red dashed line appears, tracing data flowing sequentially from one computer to the next through the central switch, simulating a ring.
**[Alt-text: The Star topology diagram with a central switch. A red dashed line traces a path from computer A, through the switch, to computer B, then to computer C, illustrating logical data flow independent of the physical cables.]**
**Audio:** "Here is a critical concept for the CompTIA exam: Physical topology is the wiring, but Logical topology is how the data actually flows. You can have a network that is physically wired as a Star, but logically acts like a Ring. The data passes through the switch in a circular logical path, even though the cables are in a star shape."

**[04:30 - 05:00] Conclusion**
**Visual:** Instructor on camera with bullet points: "Physical = Cables, Logical = Data Flow".
**Audio:** "Always distinguish between the physical cables and the logical data flow. In your upcoming lab, you'll simulate building your own Star topology. See you in the lab!"
