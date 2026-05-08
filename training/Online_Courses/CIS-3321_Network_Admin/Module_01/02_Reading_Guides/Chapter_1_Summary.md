# Reading Guide: Chapter 1 - Networking Fundamentals
**Course:** CIS 3321 - Network Administration
**Certification Alignment:** CompTIA Network+ (N10-008) Domain 1.0

## High-Yield Concepts
As you read Chapter 1 of your text, focus heavily on the following concepts, as they are guaranteed to appear on the Network+ certification exam.

### 1. The OSI Model vs. TCP/IP Model
You must be able to compare and contrast the 7-layer OSI model with the 4-layer TCP/IP model.
*   **OSI Layer 7, 6, 5** = **TCP/IP Application Layer**
*   **OSI Layer 4 (Transport)** = **TCP/IP Transport Layer**
*   **OSI Layer 3 (Network)** = **TCP/IP Internet Layer**
*   **OSI Layer 2, 1** = **TCP/IP Network Access / Link Layer**

### 2. Protocol Data Units (PDUs)
Know what data is called at the different OSI layers:
*   Layer 4 (Transport) = **Segments** (TCP) or **Datagrams** (UDP)
*   Layer 3 (Network) = **Packets** (IP addresses are used here)
*   Layer 2 (Data Link) = **Frames** (MAC addresses are used here)
*   Layer 1 (Physical) = **Bits** (1s and 0s)

### 3. Network Topologies
Understand the advantages and disadvantages of each:
*   **Star:** Most common. Single point of failure is the central switch.
*   **Mesh:** Most redundant and expensive. Every node connects to every other node. Formula for connections: `n(n-1)/2`.
*   **Hybrid:** A combination of two or more topologies.

## Key Terms Glossary
*   **Encapsulation:** The process of adding headers to data as it moves down the OSI model.
*   **Decapsulation:** The process of stripping headers as data moves up the OSI model at the receiving end.
*   **MAC Address:** A physical, hardcoded 48-bit address on a Network Interface Card (NIC).
*   **IP Address:** A logical address assigned to a device on a network.
