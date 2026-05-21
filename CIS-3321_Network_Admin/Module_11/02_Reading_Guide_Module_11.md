# Reading Guide: Module 11 - Switching – VLANs, STP, and EtherChannel
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 11 – Switching: VLANs, STP, and EtherChannel**! Advanced switching concepts are heavily tested on the CompTIA Network+ N10-009 exam. You must understand how VLANs segment broadcast domains, how Spanning Tree Protocol prevents Layer 2 loops, and how EtherChannel bundles physical links for increased bandwidth and redundancy. These topics appear in both the Network Implementations and Network Troubleshooting domains.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **VLAN (Virtual LAN)**: A logical network segment created on a switch that isolates broadcast domains regardless of physical port location. Devices in different VLANs cannot communicate at Layer 2 — they require routing (Layer 3) to communicate. VLANs improve security, performance, and network management.
*   **Access Port**: A switch port configured to belong to a single VLAN. Connects end devices (workstations, IP phones, printers). Traffic enters and exits without VLAN tags — the device is unaware it is on a VLAN.
*   **Trunk Port**: A switch port configured to carry traffic for multiple VLANs simultaneously using IEEE 802.1Q tagging. Used for switch-to-switch and switch-to-router links. Each frame is tagged with a 4-byte 802.1Q header containing the VLAN ID (1–4094).
*   **802.1Q (Dot1Q)**: The IEEE standard for VLAN tagging on trunk links. Inserts a 4-byte tag into the Ethernet frame header containing the VLAN ID. The native VLAN is sent untagged across a trunk port.
*   **Native VLAN**: The VLAN whose traffic is sent untagged across an 802.1Q trunk port. Both ends of a trunk must agree on the native VLAN — a mismatch causes a native VLAN mismatch error and potential traffic routing to the wrong VLAN.
*   **Inter-VLAN Routing**: The process of routing traffic between VLANs. Options: (1) Router-on-a-Stick — a router with a single trunk link and sub-interfaces for each VLAN; (2) Layer 3 Switch — performs routing internally using SVIs (Switched Virtual Interfaces) for each VLAN.
*   **SVI (Switched Virtual Interface)**: A virtual Layer 3 interface on a Layer 3 switch representing a VLAN. Assigned an IP address that acts as the default gateway for hosts in that VLAN, enabling inter-VLAN routing without an external router.
*   **STP (Spanning Tree Protocol)**: IEEE 802.1D protocol that prevents Layer 2 switching loops by placing redundant switch ports in a blocking state. STP elects a Root Bridge, then determines the shortest path from each switch to the Root Bridge. Ports not on the best path are blocked.
*   **RSTP (Rapid Spanning Tree Protocol)**: IEEE 802.1w — the modern replacement for STP. Converges in seconds rather than the 30–50 seconds of classic STP. Uses port roles (Root, Designated, Alternate, Backup) and port states (Discarding, Learning, Forwarding).
*   **STP Root Bridge Election**: The switch with the lowest Bridge ID (Bridge Priority + MAC address) becomes the Root Bridge. Default Bridge Priority = 32768. Administrators can manually set a lower priority to control which switch becomes Root.
*   **STP Port States (802.1D)**: Blocking → Listening → Learning → Forwarding → Disabled. Ports in Blocking state do not forward frames but do receive BPDUs. The Listening→Learning→Forwarding transition takes ~30–50 seconds in classic STP.
*   **PortFast**: A Cisco STP feature that immediately transitions an access port to Forwarding state, bypassing Listening and Learning. Used only on ports connected to end devices — never on ports connected to other switches (risk of creating loops). Must be combined with BPDU Guard.
*   **BPDU Guard**: A Cisco STP security feature enabled on PortFast ports. If a BPDU is received on a PortFast port (indicating a switch was connected), the port is immediately err-disabled to prevent loops. Protects against unauthorized switch connections.
*   **EtherChannel (Link Aggregation)**: The bundling of multiple physical Ethernet links between two switches into a single logical link. Provides increased bandwidth (up to 8 links) and redundancy — if one physical link fails, traffic continues on the remaining links. Negotiated using LACP (IEEE 802.3ad) or PAgP (Cisco proprietary).
*   **LACP (Link Aggregation Control Protocol)**: IEEE 802.3ad standard for dynamically negotiating EtherChannel. Uses Active/Passive modes. Active initiates negotiation; Passive waits for the remote end to initiate. Two Passive ports will not form an EtherChannel.
*   **DTP (Dynamic Trunking Protocol)**: A Cisco proprietary protocol that automatically negotiates trunk links between Cisco switches. Security best practice is to disable DTP on all ports not intended to be trunks (`switchport nonegotiate`) to prevent VLAN hopping attacks.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** VLANs and STP fall under **Domain 2.0 – Network Implementations (20%)** and **Domain 5.0 – Network Troubleshooting (23%)**. VLAN configuration problems and STP topology questions are common in both domains.
*   **Access port vs. trunk port — the most-tested VLAN distinction**: Access = one VLAN, untagged, connects to end devices. Trunk = multiple VLANs, 802.1Q tagged, connects switches and routers. The exam gives a scenario and asks which port type to configure.
*   **STP root bridge tie-breaker**: If two switches have the same bridge priority, the switch with the lowest MAC address wins the Root Bridge election. The exam may present this tie-breaker scenario.
*   **PortFast + BPDU Guard always together**: The exam considers PortFast without BPDU Guard an incomplete or insecure configuration. Any scenario enabling PortFast should also mention BPDU Guard to prevent loops from unauthorized switch connections.
*   **LACP Active/Active or Active/Passive forms EtherChannel; Passive/Passive does NOT**: The exam may present an EtherChannel that fails to form and ask why. If both ends are Passive, neither initiates negotiation and the channel never forms.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers VLANs, STP, and link aggregation in the Network Implementations and Troubleshooting sections.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **VLANs, Spanning Tree, and Link Aggregation** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the 802.1Q frame format, STP port state transitions, and EtherChannel negotiation modes.
*   **Required Video:** Watch Professor Messer's **VLANs and Trunking**, **Spanning Tree Protocol**, and **Link Aggregation** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's hands-on lab, you will configure VLANs and trunk ports on Cisco switches in Packet Tracer, verify VLAN assignments with `show vlan brief` and trunk status with `show interfaces trunk`, observe STP port roles with `show spanning-tree`, and configure an EtherChannel using LACP, verifying with `show etherchannel summary`.

---

### 3. Study Checklist
*   [ ] Know access ports vs. trunk ports and the 802.1Q VLAN tagging standard.
*   [ ] Understand inter-VLAN routing — both Router-on-a-Stick and Layer 3 Switch with SVIs.
*   [ ] Know STP Root Bridge election (lowest Bridge Priority + lowest MAC address wins).
*   [ ] Know STP port states and the PortFast/BPDU Guard security combination.
*   [ ] Understand EtherChannel and LACP Active/Passive mode combinations.
*   [ ] Know the native VLAN and the security risk of native VLAN mismatches.
*   [ ] Read the **VLANs and Switching** chapters in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's VLAN and STP videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
