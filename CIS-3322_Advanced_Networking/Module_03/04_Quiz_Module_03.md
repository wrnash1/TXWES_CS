# Quiz: Module 03 - IPv6 Addressing and Configuration
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
What command enables a Cisco router to forward IPv6 traffic?
*   A) ip routing
*   B) ipv6 address autoconfig
*   C) ipv6 unicast-routing
*   D) ipv6 routing enable
*   **Correct Answer:** C) Cisco routers require the global command `ipv6 unicast-routing` to act as an IPv6 router.
*   **Distractor Analysis:**
    *   *Why correct:* Cisco routers require the global command `ipv6 unicast-routing` to act as an IPv6 router.
    *   ip routing is for IPv4. autoconfig sets up client address learning. routing enable is invalid syntax.

---

**Question 2**
Which of the following most accurately describes the **EUI-64** method of generating an IPv6 interface identifier?
*   A) A process that combines the 48-bit MAC address with the hex value FFFE inserted in the middle and the seventh bit inverted to produce a 64-bit interface ID.
*   B) A stateless mechanism in which a host listens for Router Advertisement messages and combines the advertised prefix with a randomly generated 64-bit suffix.
*   C) A 6-byte hardware address assigned to every network interface card at the factory, used by switches to build their MAC address tables for Layer 2 forwarding.
*   D) A Cisco proprietary algorithm that generates a 64-bit host identifier by hashing the device hostname and serial number to ensure uniqueness across the network.
*   **Correct Answer:** A) A process that combines the 48-bit MAC address with the hex value FFFE inserted in the middle and the seventh bit inverted to produce a 64-bit interface ID.
*   **Distractor Analysis:**
    * *Why A is correct:* EUI-64 is the IEEE standard method: split the MAC at 3 bytes, insert FFFE, and flip bit 7 (the universal/local bit) to create a 64-bit interface identifier.
    * *Why B is incorrect:* This describes SLAAC with a random or privacy extension suffix — not the EUI-64 derivation process specifically.
    * *Why C is incorrect:* This describes a MAC address itself, not the EUI-64 conversion algorithm.
    * *Why D is incorrect:* EUI-64 is an IEEE standard, not Cisco proprietary, and it derives the ID from the MAC address, not hostname or serial number.


---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
A) netstat -ano
B) ping
D) traceroute
C) nslookup
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **IPv6 Addressing and Configuration** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.


---

**Question 5**
When configuring **IPv6 Addressing**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Configure IPv6 RA Guard on switch ports to block unauthorized devices from sending Router Advertisement messages.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable IPv6 First-Hop Security (FHS) binding table to track and validate IPv6 source addresses on access ports.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Port Security restricts which MAC addresses can communicate on a switchport, directly preventing unauthorized devices from connecting and obtaining network access.
    * *Why C is incorrect:* RA Guard protects against rogue RA messages (a separate IPv6-specific attack), but does not prevent unauthorized physical device connections to the switch port.
    * *Why B is incorrect:* SSH/HTTPS secures management access but does not prevent a rogue device from connecting to a switch port.
    * *Why D is incorrect:* IPv6 FHS binding table validates source addresses but is a complementary control, not the primary defense against unauthorized port connections.
