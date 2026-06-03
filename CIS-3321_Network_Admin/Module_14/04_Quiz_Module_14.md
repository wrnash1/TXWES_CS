# Quiz: Module 14 — Network Troubleshooting Methodology

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. This quiz covers Module 14 video lectures and reading guide material.

---

## Questions

### Question 1

A network technician is following the CompTIA troubleshooting methodology. After gathering information and talking to the user, the technician immediately changes several settings on the router to see if any of them fix the problem. Which step of the methodology did the technician skip?

- A) Step 1 — Identify the Problem
- B) Step 2 — Establish a Theory of Probable Cause
- C) Step 6 — Verify Full System Functionality
- D) Step 7 — Document Findings

Correct Answer: B

Explanation: The technician jumped from gathering information (Step 1) directly to making changes (essentially Step 5) without forming a theory of probable cause (Step 2) or testing that theory (Step 3). This is "shotgun troubleshooting" and is the most common deviation from the methodology.

---

### Question 2

A user receives the IP address 169.254.82.44 on their Windows workstation. What is the most likely cause?

- A) The user manually configured a static IP in the 169.254.0.0/16 range
- B) The DHCP server assigned this address as part of the voice VLAN
- C) DHCP discovery failed and Windows assigned an APIPA address
- D) DNS resolution failed and the workstation cannot resolve the DHCP server name

Correct Answer: C

Explanation: The 169.254.0.0/16 range is APIPA (Automatic Private IP Addressing). Windows assigns an APIPA address when DHCP discovery fails — the client broadcasts for a DHCP server, receives no response, and self-assigns within this range. DNS is not involved in DHCP address assignment.

---

### Question 3

A technician uses a cable certifier on a Cat6 horizontal run and the test reports a NEXT failure. What type of cable problem does NEXT measure?

- A) Signal attenuation over distance
- B) Near End Crosstalk — interference between adjacent wire pairs measured at the same end
- C) Far End Crosstalk — interference measured at the opposite end from the signal source
- D) Open circuit — a wire with no continuity

Correct Answer: B

Explanation: NEXT (Near End Crosstalk) measures electromagnetic interference between wire pairs at the same end as the signal source. It is caused by poor cable quality, incorrect termination (untwisting pairs too far), or split pairs. A basic cable tester cannot detect NEXT — a cable certifier is required.

---

### Question 4

A user can ping a server by its IP address (192.168.5.50) but cannot connect to it by hostname (fileserver.corp.local). Which troubleshooting step should be performed next?

- A) Replace the network cable
- B) Check the default gateway configuration
- C) Run nslookup fileserver.corp.local to test DNS resolution
- D) Reboot the server

Correct Answer: C

Explanation: The ability to ping by IP confirms Layers 1–3 are functional. The inability to connect by name points to Layer 7 (DNS) as the problem layer. nslookup tests DNS resolution directly — it will reveal whether the name resolves and which DNS server is responding.

---

### Question 5

A switch port shows the following statistics: Speed 100Mb/s, Duplex Half, Input errors 78,000, Late collisions 12,000. What is the most likely cause?

- A) The cable connecting the device is broken
- B) A duplex mismatch — one end is set to full-duplex, the other to half-duplex
- C) The SFP transceiver has failed
- D) STP has placed the port in a blocking state

Correct Answer: B

Explanation: Late collisions are a classic indicator of a duplex mismatch. When one side operates full-duplex and the other half-duplex, the full-duplex side transmits freely while the half-duplex side detects collisions after the normal collision window. The high input error count also supports this diagnosis.

---

### Question 6

Which tool should be used to trace a specific cable through a conduit and patch panel when the cable is not labeled?

- A) Cable certifier
- B) Optical power meter
- C) Tone generator and inductive probe
- D) Time Domain Reflectometer (TDR)

Correct Answer: C

Explanation: A tone generator injects an audible signal onto the cable at one end. An inductive probe detects the tone through the cable's insulation without requiring physical access to the conductor — allowing the technician to trace the cable through conduit, walls, and across patch panels.

---

### Question 7

A technician follows the bottom-up OSI troubleshooting approach. They confirm the physical link is active, the VLAN is correctly configured, and the IP address is correct. The next step in the bottom-up approach is to verify which layer?

- A) Layer 1 — Physical (again)
- B) Layer 3 — Network routing and gateway
- C) Layer 7 — Application service availability
- D) Layer 4 — Transport layer (firewall, port availability)

Correct Answer: D

Explanation: In the bottom-up approach, after confirming Layer 3 (correct IP, subnet, and gateway), the next layer to verify is Layer 4 — Transport. Check whether a firewall is blocking the required port or whether the application service is listening on the expected port.

---

### Question 8

After resolving a complex network outage, a technician skips Step 7 (Documentation) because the fix was straightforward. Three months later, an identical issue occurs and takes the same 4 hours to resolve. What could documentation have prevented?

- A) Nothing — the problem was hardware failure and would recur regardless
- B) Faster resolution using the knowledge base record from the first incident
- C) The initial outage from occurring
- D) The need for escalation during the second incident

Correct Answer: B

Explanation: A knowledge base record from the first incident would allow the next technician (or the same technician) to immediately identify the cause and apply the known solution — reducing MTTR from 4 hours to minutes. Documentation converts individual experience into organizational knowledge.

---

### Question 9

A technician runs tracert from a workstation to a remote server and observes that the first three hops respond normally, but hop 4 shows *** (three asterisks) and hop 5 responds normally. What does this most likely indicate?

- A) The network path is broken at hop 4
- B) Hop 4 is a router configured to not respond to traceroute probes (ICMP filtered)
- C) Hop 4 is the destination server and the trace is complete
- D) The workstation has a routing loop between hops 3 and 4

Correct Answer: B

Explanation: Three asterisks at a single hop followed by successful replies at subsequent hops is characteristic of a router configured to filter ICMP time-exceeded messages — it does not respond to traceroute probes but still forwards packets. This is not a network break. A true break would show *** at every hop from that point onward.

---

### Question 10

A technician is troubleshooting a fiber optic link that shows no signal. They have checked that the fiber cables are connected at both ends. Which action should be performed FIRST?

- A) Replace the SFP transceivers on both switches
- B) Inspect and clean the fiber connectors using a fiber inspection microscope and cleaning tool
- C) Replace the fiber cable with a new one
- D) Check whether the switches have the correct firmware version

Correct Answer: B

Explanation: The most common cause of fiber link failure is dirty connectors. Microscopic contamination on an SC, LC, or ST connector can attenuate the signal to zero. Inspection and cleaning is fast, free, and should always be performed before replacing hardware. Replacing cables or SFPs before cleaning is expensive and frequently unnecessary.
