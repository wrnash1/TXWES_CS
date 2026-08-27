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

---

### Question 11

Which step in the CompTIA seven-step troubleshooting methodology involves examining log files, running diagnostic commands, and gathering user reports to understand the nature of the problem?

- A) Establish a theory of probable cause
- B) Identify the problem
- C) Implement the solution
- D) Verify full system functionality

**Correct Answer:** B

**Distractor Analysis:**
- *Why A is incorrect:* Establishing a theory comes after identifying the problem — it is the hypothesis step, not the information-gathering step.
- *Why B is correct:* Step 1 (Identify the problem) includes gathering information, questioning users, reviewing logs, and defining the scope of the issue before proposing any cause.
- *Why C is incorrect:* Implementing the solution is Step 5 — it comes after testing the theory and planning a fix.
- *Why D is incorrect:* Verifying full system functionality is Step 6 — the post-fix confirmation step.

---

### Question 12

A technician suspects that a cable fault exists somewhere between a patch panel and a workstation. Which tool would locate the fault by measuring the distance from the tester to the break?

- A) Cable certifier
- B) Optical power meter
- C) Time Domain Reflectometer (TDR)
- D) Tone generator

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* A cable certifier measures electrical performance parameters (attenuation, NEXT) and certifies compliance — it can include TDR functionality but the TDR is the specific fault-location mechanism.
- *Why B is incorrect:* An optical power meter measures signal strength on fiber optic cables — it does not test copper cables or locate faults by distance.
- *Why C is correct:* A TDR sends a signal pulse down the cable and measures the time for the reflected signal to return, calculating distance to any impedance discontinuity (break, short, bad connector).
- *Why D is incorrect:* A tone generator injects an audible signal for cable tracing — it does not locate faults or measure distance.

---

### Question 13

A workstation is assigned the IP address 169.254.83.45. What is the most likely cause?

- A) The workstation is configured with a static IP address outside the subnet range
- B) The DHCP server responded with an incorrect default gateway
- C) The workstation failed to receive a response from a DHCP server and assigned itself an APIPA address
- D) The workstation has a duplicate IP address conflict with another device

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* A static IP misconfiguration would produce a different address — not one in the 169.254.0.0/16 range, which is exclusively the APIPA range.
- *Why B is incorrect:* If the DHCP server responded, the client would receive a valid lease including the default gateway — the 169.254 address indicates no DHCP response was received.
- *Why C is correct:* Per RFC 3927, when a Windows or macOS host cannot reach a DHCP server after the retry period, it automatically configures itself with a 169.254.x.x address from the APIPA range.
- *Why D is incorrect:* A duplicate IP conflict produces an IP conflict notification but the host keeps the original IP — it does not automatically revert to 169.254.x.x.

---

### Question 14

Using the CompTIA troubleshooting methodology, after implementing a fix for a network issue, what is the NEXT step?

- A) Identify the problem
- B) Establish a theory of probable cause
- C) Document findings, actions, and outcomes
- D) Verify full system functionality and, if applicable, implement preventive measures

**Correct Answer:** D

**Distractor Analysis:**
- *Why A is incorrect:* Identifying the problem is Step 1 — it occurs at the beginning, not after applying a fix.
- *Why B is incorrect:* Establishing a theory of probable cause is Step 2 — it occurs before any fix is applied.
- *Why C is incorrect:* Documentation is Step 7 — the final step. Verification comes before documentation.
- *Why D is correct:* Step 6 is to verify full system functionality and implement preventive measures. After confirming the fix works, the technician documents in Step 7.

---

### Question 15

A technician runs `show interfaces GigabitEthernet0/1` and sees: "Half-duplex, 100Mb/s, input errors 58734, late collisions 12441." What is the most likely cause of these statistics?

- A) The fiber cable connecting to this interface is bent beyond its minimum bend radius
- B) A duplex mismatch — one side is configured for full-duplex while the other negotiated half-duplex
- C) The switch port has exceeded its MAC address table capacity
- D) The interface is experiencing STP topology change events

**Correct Answer:** B

**Distractor Analysis:**
- *Why A is incorrect:* Fiber bend radius issues cause signal loss (CRC errors at low traffic) — they do not produce late collisions, which are a Layer 1 phenomenon specific to half-duplex Ethernet timing.
- *Why B is correct:* Late collisions occur when a collision is detected after the first 64 bytes of a frame are transmitted — this is a diagnostic signature of duplex mismatch. One side transmitting full-duplex does not listen for collisions; the half-duplex side detects collisions outside the normal window.
- *Why C is incorrect:* MAC table overflow causes the switch to flood unknown unicast — it does not produce late collisions or input errors on the interface.
- *Why D is incorrect:* STP topology changes affect the MAC address table aging timer — they do not cause late collisions on a physical interface.

---

### Question 16

Which troubleshooting approach starts at the Physical layer (Layer 1) and works upward through the OSI model?

- A) Top-down
- B) Divide and conquer
- C) Bottom-up
- D) Follow the path

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* Top-down starts at the Application layer (Layer 7) and works downward — checking application function, then transport, then network, then physical.
- *Why B is incorrect:* Divide and conquer starts somewhere in the middle of the OSI model (often Layer 3) and moves up or down based on findings — not from the bottom.
- *Why C is correct:* The bottom-up approach begins at Layer 1 (check cables, connectors, link lights) and progresses upward through each OSI layer until the fault is found.
- *Why D is incorrect:* Follow the path traces the traffic route from source to destination — it is a separate methodology not defined by OSI layer starting point.

---

### Question 17

A user reports they can access websites by IP address but not by domain name. Which command should the technician use FIRST to diagnose this problem?

- A) `ping 127.0.0.1`
- B) `tracert 8.8.8.8`
- C) `nslookup google.com`
- D) `ipconfig /release`

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* Pinging the loopback (127.0.0.1) tests the local TCP/IP stack — since the user can already reach sites by IP, the stack is functional.
- *Why B is incorrect:* Traceroute to an IP address tests routing path — it does not test DNS name resolution, which is the reported symptom.
- *Why C is correct:* `nslookup google.com` directly tests DNS name resolution by querying the configured DNS server. If it fails or returns an error, DNS is the confirmed fault. This is the most targeted diagnostic command for the reported symptom.
- *Why D is incorrect:* Releasing the IP address would disrupt connectivity — it should not be the first step, and it does not test DNS.

---

### Question 18

Which cable testing tool is specifically designed to trace the physical path of an unmarked cable through walls and conduit without cutting into the wall?

- A) OTDR
- B) TDR
- C) Cable certifier
- D) Tone generator and inductive probe

**Correct Answer:** D

**Distractor Analysis:**
- *Why A is incorrect:* An OTDR (Optical TDR) tests fiber optic cables — it measures attenuation and locates faults on fiber, not copper cable paths in walls.
- *Why B is incorrect:* A TDR locates electrical faults on copper cable by measuring signal reflection distance — it does not trace cable paths through physical spaces.
- *Why C is incorrect:* A cable certifier measures electrical performance and certifies compliance with TIA standards — it tests cable quality, not physical routing.
- *Why D is correct:* A tone generator injects a signal onto the cable at one end; the inductive probe is swept along walls, conduit, and patch panels to detect the tone through insulation without cutting or connecting — standard cable tracing technique.

---

### Question 19

According to the CompTIA troubleshooting methodology, when a technician determines that the most likely cause of a problem is a software configuration error, what should they do BEFORE making any changes?

- A) Escalate to a higher-tier technician immediately
- B) Verify full system functionality to confirm the issue
- C) Establish a plan of action and back up any affected configurations
- D) Document findings and close the trouble ticket

**Correct Answer:** C

**Distractor Analysis:**
- *Why A is incorrect:* Escalation is appropriate when the fix is outside the technician's skill level or authorization — if the technician can address the configuration error, escalation is premature.
- *Why B is incorrect:* Verifying full system functionality is Step 6 — it occurs after the fix is applied, not before making changes.
- *Why C is correct:* Step 4 is to establish a plan of action and identify potential effects. Before implementing changes, a good technician backs up the current configuration so the change can be reversed if it causes new problems.
- *Why D is incorrect:* Documentation is Step 7 — the final step after the problem is resolved, not before making changes.

---

### Question 20

A technician is troubleshooting a fiber optic link using an OTDR. The OTDR trace shows a sharp spike followed by a loss event at 120 meters. What does this most likely indicate?

- A) The fiber cable exceeds the maximum supported length for the SFP transceiver
- B) A physical break, splice fault, or connector problem at 120 meters from the OTDR
- C) Chromatic dispersion affecting signal quality across the full fiber run
- D) The fiber optic cable is using the wrong wavelength for the installed SFP

**Correct Answer:** B

**Distractor Analysis:**
- *Why A is incorrect:* Exceeding maximum supported length causes gradual signal attenuation across the full run — it would not produce a localized spike at a specific distance.
- *Why B is correct:* An OTDR sends light pulses and measures reflections. A spike (back-reflection) followed by a loss event at a specific distance indicates a physical discontinuity at that point — a break, a damaged splice, or a bad connector at 120 meters.
- *Why C is incorrect:* Chromatic dispersion is a signal quality issue that affects pulse spreading over long runs — it does not appear as a localized spike event on an OTDR trace.
- *Why D is incorrect:* Wavelength mismatch between cable and SFP affects the entire link uniformly — it would cause high loss across the whole trace, not a localized fault event at a specific distance.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
