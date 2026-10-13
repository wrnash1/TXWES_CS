# Video Script: Module 11 - Network Hardware & Connectors

**Course:** CIS-2320 Hardware Fundamentals
**Certification Alignment:** CompTIA A+ Core 1 (220-1101) — Domain 2.1: Compare and contrast Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) ports, protocols, and their purposes; Domain 2.2: Compare and contrast common networking hardware
**Estimated Duration:** 20-24 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

**Components to have on camera or in slides:**

- Physical samples: Cat5e, Cat6, and Cat6a patch cables (labeled)
- Physical samples: RJ-45 plug and RJ-11 plug side by side
- Physical samples or images: ST, SC, and LC fiber connectors
- T568A and T568B wiring diagrams (color-coded slide)
- Cable tester device

**Key exam traps to call out verbally:**

- Cat6 is NOT good enough for 10 Gbps at 80 or 100 meters — only at 55 meters max
- RJ-11 physically fits in an RJ-45 port but does not work for data
- T568A on one end, T568B on the other = crossover cable (PC to PC, not PC to switch)
- LC is the modern fiber connector; ST is legacy; SC is still in use in older data centers
- Single-mode fiber for long runs; multimode for shorter runs inside a building

---

## [00:00 - 02:30] Section 1 — Introduction and Certification Alignment

**[SHOW COMPONENT: Title slide — "Module 11: Network Hardware and Connectors"]**

Good morning, good afternoon, wherever you are — welcome to Module 11 of CIS-2320 Hardware Fundamentals. I am Professor Nash, and today we are going deep on one of the most hands-on, visually testable topics in the entire CompTIA A+ Core 1 exam: network hardware and connectors.

I want you to understand from the start that this is not abstract theory. Every cable you will ever run in a wiring closet, every patch panel port you punch down, every fiber connector you clean before seating — all of it traces back to the concepts we cover today. The exam will show you a scenario and ask you to choose the right cable for the job, or identify what went wrong when a cable test fails. These are skills that transfer directly to day one on the job.

**[PAUSE — transition to slide: "What We Cover Today"]**

Here is our agenda for this session. We have five main sections. First, copper cable categories — Cat5e, Cat6, and Cat6a — and what makes each one the right or wrong choice for a given installation. Second, the RJ-45 and RJ-11 connector types and why confusing them causes real installation problems. Third, fiber optic connector types — ST, SC, and LC — and when you use each one. Fourth, the T568A and T568B wiring standards, including straight-through versus crossover cables. And fifth, we will tie it all together with lab prep and a look at what cable testing tells you.

By the end of this video you will be able to select the correct cable category for any speed and distance scenario the exam throws at you, and you will be able to wire an RJ-45 plug from memory.

---

## [02:30 - 08:00] Section 2 — Copper Cable Categories

**[SHOW COMPONENT: Three cables labeled Cat5e, Cat6, Cat6a side by side]**

Let us start with copper twisted-pair cables. These are the cables that run through the walls and ceilings of every office building, school, and data center in the country. They all look similar from the outside — a gray or blue outer jacket, an RJ-45 connector on each end — but they are very different in what they can do.

**[PAUSE — transition to slide: "Ethernet Cable Category Comparison Table"]**

The three categories you must know cold for the A+ exam are Cat5e, Cat6, and Cat6a.

Cat5e — Category 5 Enhanced — was the standard for many years and still exists in buildings installed in the early 2000s. It supports 1 Gbps at up to 100 meters. That is still useful for most office workstations today. The conductor gauge is 24 AWG, and the pairs are twisted at varying rates to reduce crosstalk between pairs.

**[SHOW COMPONENT: Close-up of Cat5e stripped cable showing four twisted pairs]**

Cat6 — Category 6 — is the modern standard for new installations. It supports 1 Gbps at 100 meters, same as Cat5e, but it also supports 10 Gbps at distances up to 55 meters. It achieves this through tighter pair twisting, thicker conductors, and often an internal plastic spline that separates the four pairs and reduces alien crosstalk. Here is the exam trap to write down right now: Cat6 supports 10 Gbps ONLY up to 55 meters. At 56 meters or longer, Cat6 drops back to 1 Gbps. If the exam gives you a scenario with a 75-meter run that needs to handle 10 Gbps, Cat6 is the wrong answer even though it looks correct.

**[PAUSE — call out in bold on slide: "Cat6 = 10 Gbps ONLY up to 55 meters"]**

Cat6a — Category 6 Augmented — solves that problem. Cat6a supports 10 Gbps at the full 100-meter standard horizontal run. It does this with even thicker insulation, tighter specifications, and often foil shielding around each pair or around the entire cable bundle. Cat6a is physically larger and heavier than Cat6 or Cat5e, which matters when you are trying to pull cables through conduit or bend them around corners in a ceiling plenum. But if you need 10 Gbps at 100 meters, Cat6a is the only copper category that delivers it.

**[SHOW COMPONENT: Cat6a cross-section showing internal spline and shielding]**

Here is a memory trick: think of it this way — Cat6 gets you halfway to the goal for 10 Gbps. Cat6a gets you all the way. The "a" stands for "augmented," which means more capable in every measurable way.

All three categories use the same RJ-45 connector. The difference is entirely in the cable itself. A Cat6a cable plugs into the same RJ-45 jack as a Cat5e cable. This is important for upgrades — you can often re-terminate existing runs with better cable without replacing the wall jacks.

**[PAUSE — transition to speed/distance summary table on slide]**

---

## [08:00 - 13:00] Section 3 — RJ-45 vs RJ-11 and Connector Identification

**[SHOW COMPONENT: RJ-45 plug and RJ-11 plug held side by side on camera]**

Now let us talk about the connectors that go on the ends of these cables. The two you must know are RJ-45 and RJ-11.

RJ-45 is the standard connector for Ethernet. It is an 8-position, 8-contact connector — you will see it written as 8P8C. That means eight positions for conductors and all eight are used. If you look at an RJ-45 plug from the front with the tab pointing down, you see eight gold pins in a row. The connector is approximately 11.7 mm wide. Every network interface card, switch port, and patch panel port you work with uses RJ-45.

RJ-11 is the telephone connector. It is a 6-position, 2-contact connector — 6P2C — meaning it has six positions but typically only uses two of them for a standard telephone line. It is narrower than RJ-45 — about 9.6 mm wide — and physically smaller. You find RJ-11 on telephone handset cords, analog phone lines, and older DSL connections.

**[SHOW COMPONENT: Attempt to insert RJ-11 into RJ-45 port on screen — slide illustration]**

Here is the real-world trap that causes trouble in the field: an RJ-11 plug will physically fit inside an RJ-45 socket. It slides in. It even clicks slightly. But it does not make proper electrical contact across all eight pins, and no data connection is established. In offices where telephone jacks and data jacks are installed side by side — and sometimes use identical wall plate styles — a user can inadvertently plug their Ethernet cable into a phone jack or their phone cable into a data port. The symptom is no network connection. The fix is simply plugging into the correct jack. The exam may describe this scenario and ask what is wrong.

**[PAUSE — exam tip on slide: "RJ-11 in an RJ-45 port = no data connection"]**

A quick visual identification tip: look at the connector end-on. Eight pins means RJ-45 for data. Six or fewer pins means RJ-11 for telephone. When in doubt, count the pins.

---

## [13:00 - 17:30] Section 4 — Fiber Optic Connector Types and T568A vs T568B

**[SHOW COMPONENT: ST, SC, and LC fiber connectors on camera or comparison slide]**

Fiber optic cables carry data as pulses of light rather than electrical current, which means they are immune to electromagnetic interference and can cover much longer distances than copper. There are three connector types you need to know for the A+ exam: ST, SC, and LC.

ST — Straight Tip — is the oldest of the three. It uses a bayonet-style twist-and-lock coupling mechanism, similar to a BNC coaxial connector. ST connectors have a round body with a protruding ceramic ferrule tip. You still encounter them in older enterprise campus wiring closets, particularly in buildings wired in the 1990s and early 2000s. They are being phased out but you will see them on the exam.

**[SHOW COMPONENT: SC connector detail — square body, push-pull mechanism]**

SC — Subscriber Connector, or sometimes called "square connector" for easy memory — has a rectangular, square-bodied housing and uses a push-pull latching mechanism. SC connectors click in and pull straight out. They are common in data center patch panels and in older fiber-to-the-premises ISP installations. SC connectors come in simplex (one fiber) and duplex (two fibers bonded together in a side-by-side housing).

**[SHOW COMPONENT: LC connector detail — small form factor, latch mechanism]**

LC — Lucent Connector, or "little connector" as technicians often call it — is the dominant fiber connector in modern enterprise environments and data centers. It uses a push-pull latch identical in concept to SC but at roughly half the physical size. That smaller footprint is critical in high-density patch panels where you need to fit 48 or 96 fiber ports in a 1U rack space. LC connectors are also common on small form-factor pluggable transceivers — the SFP modules that plug into switches and routers. If you are working in a modern data center today, most of the fiber you handle will use LC connectors.

**[PAUSE — connector comparison table on slide: ST/SC/LC with coupling type, size, and typical use]**

Now let us cover T568A and T568B — the two wiring standards for RJ-45 termination.

**[SHOW COMPONENT: T568A and T568B color-coded wiring diagram side by side]**

Both standards specify which color wire goes into which of the eight RJ-45 pin positions. They are defined by the TIA/EIA-568 standard. The difference between them is a single pair swap: in T568B, the orange pair occupies pins 1 and 2, and the green pair occupies pins 3 and 6. In T568A, those two pairs are reversed — green is on pins 1 and 2, orange is on pins 3 and 6. Every other pair is in the same position in both standards.

T568B is the more common standard in North America for commercial and enterprise installations. Most pre-made patch cables you purchase off the shelf are wired T568B to T568B, which is called a straight-through cable. A straight-through cable connects a PC to a switch port because the transmit pins on one device align with the receive pins on the other device.

A crossover cable uses T568A on one end and T568B on the other end. This swaps the transmit and receive pairs so that two devices of the same type — PC to PC, or switch to switch — can communicate directly. Modern switches with auto-MDI/MDIX capability detect the cable type automatically and adjust internally, so crossover cables are less necessary today. But the exam absolutely tests this: PC to switch equals straight-through T568B to T568B. PC to PC directly equals crossover, meaning T568A on one end and T568B on the other.

**[PAUSE — exam tip on slide: "Crossover = T568A one end, T568B other end"]**

---

## [17:30 - 21:30] Section 5 — Cable Testing and Lab Preparation

**[SHOW COMPONENT: Cable tester device on camera]**

A cable tester is the basic tool that verifies a finished Ethernet cable. You plug one end of the cable into the main unit and the other end into a remote unit. The tester sends a signal through each of the eight conductors in sequence and displays whether each pin has continuity, shows a short, is open, or is crossed with another pin.

When you crimp an RJ-45 connector in the field, the most common failure modes are: a conductor that was not pushed fully to the front of the plug before crimping — the metal IDC pin did not pierce the wire insulation — and a mis-sequenced conductor where you placed the wrong color wire in the wrong position. A cable tester catches both problems. If pin 3 fails continuity, you look at the green wire in the T568B wiring order and re-crimp that end.

**[PAUSE — slide: "Common Cable Test Failures and Causes"]**

For this week's lab, you will be examining cable samples, filling in wiring diagrams, and performing a simulated cable test exercise. You do not need a physical crimper or tester — the lab provides diagrams and a structured observation exercise that mirrors what you would do with physical hardware. Read through the lab document fully before starting. The cable identification and T568A/B diagram sections are the most important for the quiz.

**[SHOW COMPONENT: Lab worksheet preview slide]**

---

## [21:30 - End] End Card

Thank you for watching Module 11. Here is what I need you to do before our next class session:

First, review the Reading Guide for Module 11. It has a comprehensive glossary, cable specification tables, and eight exam trap items that will help you on the quiz.

Second, complete Lab 11. Work through all three parts — cable identification, wiring diagram, and the cable tester simulation. Submit your completed deliverables to Canvas.

Third, take Quiz 11. It covers everything from this video.

Finally, post to the Module 11 Discussion Board by Wednesday at 11:59 PM and respond to two classmates by Sunday.

**[PAUSE — slide: "Module 11 Resources"]**

---

## Additional Resources

- Professor Messer's CompTIA A+ Core 1 Study Notes — Network Cabling section: professormesser.com
- CompTIA A+ Exam Objectives (220-1101) — Domain 2.1 and 2.2: comptia.org
- TIA/EIA-568 Standard Overview — available through your institution's library database
