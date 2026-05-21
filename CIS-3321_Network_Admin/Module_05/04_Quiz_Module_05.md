# Quiz: Module 05 - Network Infrastructure – Cables, Switches, Routers
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A network technician needs to support 10 Gbps Ethernet over copper at the full 100-meter distance. Which cable standard meets this requirement?
A) Cat5e
B) Cat6
C) Cat6a
D) Cat3
*   **Correct Answer:** C) Cat6a
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cat5e supports a maximum of 1 Gbps at 100 m; it cannot carry 10 Gbps over copper at any useful distance.
    *   *Why B is incorrect:* Cat6 supports 10 Gbps but only up to 55 m due to alien crosstalk; it cannot reliably reach 100 m at 10 Gbps.
    *   *Why D is incorrect:* Cat3 is a legacy voice-grade cable rated for 10 Mbps; it is completely unsuitable for 10 Gbps data transmission.

---

**Question 2**
A switch receives a frame destined for a MAC address that is not in its CAM table. Which action does the switch take?
A) Drops the frame and sends an ICMP Destination Unreachable message to the source.
B) Forwards the frame only to the default gateway port for routing.
C) Floods the frame out all ports except the port it was received on.
D) Sends an ARP request on behalf of the source to discover the destination MAC.
*   **Correct Answer:** C) Floods the frame out all ports except the port it was received on.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Switches do not drop frames for unknown destinations or generate ICMP messages — that is a Layer 3 router function. Unknown-destination frames are flooded, not dropped.
    *   *Why B is incorrect:* A switch forwards based on MAC addresses at Layer 2; it does not route to a default gateway. Routing is performed by Layer 3 devices.
    *   *Why D is incorrect:* ARP is initiated by end hosts to resolve IP-to-MAC mappings; a switch does not send ARP requests on behalf of sources. The switch simply floods the unknown-destination frame.

---

**Question 3**
A wireless access point in a remote location has no nearby power outlet. The network closet is 40 meters away, connected via Cat5e. Which technology eliminates the need for a separate power adapter at the access point?
A) Fiber optic uplink with a media converter
B) Power over Ethernet (PoE) via IEEE 802.3af or 802.3at
C) A crossover cable to connect the AP directly to the router
D) An SFP transceiver module installed in the AP
*   **Correct Answer:** B) Power over Ethernet (PoE) via IEEE 802.3af or 802.3at
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Fiber optic cabling carries data using light and cannot deliver electrical power to a remote device; a media converter would only handle the signal conversion.
    *   *Why C is incorrect:* A crossover cable is a wiring convention for connecting like devices; it carries data only and does not deliver power to remote equipment.
    *   *Why D is incorrect:* An SFP module is a pluggable transceiver that changes the physical media type of a port; it is a data-layer component and has no power-delivery function.

---

**Question 4**
A network segment experiences frequent collisions and slow performance. Investigation reveals all workstations share a single device where every incoming signal is repeated out every port simultaneously. Which device is causing this behavior, and what should replace it?
A) The device is a Layer 2 switch; replace it with a Layer 3 switch for inter-VLAN routing.
B) The device is a hub; replace it with a managed switch to give each device its own collision domain.
C) The device is a router; replace it with a firewall to control inter-network traffic.
D) The device is a wireless access point operating in bridge mode; replace it with one in access point mode.
*   **Correct Answer:** B) The device is a hub; replace it with a managed switch to give each device its own collision domain.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A switch forwards frames based on MAC addresses to individual ports — it does not repeat all signals out all ports. The described behavior is specific to hubs.
    *   *Why C is incorrect:* A router makes Layer 3 forwarding decisions based on IP addresses between different networks; it does not broadcast all signals to all ports on a segment.
    *   *Why D is incorrect:* A wireless AP in bridge mode connects two wired segments wirelessly; it does not cause the Layer 1 signal-flooding behavior described.

---

**Question 5**
A security administrator wants to prevent unauthorized devices from connecting to open switch ports in a corporate office. Which combination of controls provides the most effective defense?
A) Enable IEEE 802.1X port authentication on all access ports and configure Port Security with sticky MAC learning as a backup.
B) Disable unused switch ports in the configuration and place them in an unused VLAN.
C) Deploy network-based IDS sensors on each floor to detect unauthorized connection attempts.
D) Require all users to register their MAC addresses manually with the help desk before connecting.
*   **Correct Answer:** A) Enable IEEE 802.1X port authentication on all access ports and configure Port Security with sticky MAC learning as a backup.
*   **Distractor Analysis:**
    *   *Why A is correct:* 802.1X requires authentication credentials before a port grants network access; Port Security with sticky MAC limits which physical device can use the port — together these form a layered, automated defense.
    *   *Why B is incorrect:* Disabling unused ports and isolating them in an unused VLAN reduces exposure but does not protect active ports, which remain open for any device to connect.
    *   *Why C is incorrect:* An IDS detects and alerts on unauthorized connections after they occur; it does not prevent the initial connection from being established.
    *   *Why D is incorrect:* Manual MAC registration is administratively burdensome, easily bypassed via MAC spoofing, and provides no automated enforcement at the port level.
