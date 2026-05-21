# Quiz 1: Networking Fundamentals (Domain 1.0)
**Course:** CIS 3321 - Network Administration
**Format:** Question Bank with Distractor Analysis

---

**Question 1**
At which layer of the OSI model does a router operate to determine the best path for data to reach its destination?
A) Layer 2 (Data Link)
B) Layer 3 (Network)
C) Layer 4 (Transport)
D) Layer 7 (Application)

*   **Correct Answer:** B) Layer 3 (Network)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Layer 2 (Data Link) relies on MAC addresses for local delivery, typically handled by switches, not routers.
    *   *Why C is incorrect:* Layer 4 (Transport) handles the reliable or unreliable delivery of segments (TCP/UDP), not path routing based on IP addresses.
    *   *Why D is incorrect:* Layer 7 (Application) is where the software interacts with the network, not where hardware routing decisions are made.

**Question 2**
A network technician is designing a highly redundant network for a datacenter. Which topology requires every node to have a physical connection to every other node?
A) Star
B) Bus
C) Mesh
D) Ring

*   **Correct Answer:** C) Mesh
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A Star topology connects all nodes to a central device (switch), not directly to each other.
    *   *Why B is incorrect:* A Bus topology connects all nodes to a single, shared central backbone cable.
    *   *Why D is incorrect:* A Ring topology connects each node to exactly two other nodes, forming a circle, rather than connecting to every single node.

**Question 3**
Which Protocol Data Unit (PDU) is associated with Layer 4 of the OSI model when using the Transmission Control Protocol (TCP)?
A) Packet
B) Frame
C) Bit
D) Segment

*   **Correct Answer:** D) Segment
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Packets are the PDU for Layer 3 (Network layer).
    *   *Why B is incorrect:* Frames are the PDU for Layer 2 (Data Link layer).
    *   *Why C is incorrect:* Bits are the PDU for Layer 1 (Physical layer).

**Question 4**
In the TCP/IP model, which layer maps directly to the Session, Presentation, and Application layers of the OSI model?
A) Internet Layer
B) Transport Layer
C) Application Layer
D) Network Access Layer

*   **Correct Answer:** C) Application Layer
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The Internet Layer maps to the OSI Network layer (Layer 3).
    *   *Why B is incorrect:* The Transport Layer maps directly to the OSI Transport layer (Layer 4).
    *   *Why D is incorrect:* The Network Access (or Link) Layer maps to the OSI Data Link and Physical layers (Layers 1 and 2).
