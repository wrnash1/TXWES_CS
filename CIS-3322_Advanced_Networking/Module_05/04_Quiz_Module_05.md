# Quiz: Module 05 - Spanning Tree Protocol (STP & RSTP)
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which criteria is analyzed FIRST during the Root Bridge election process in Spanning Tree?
*   A) System MAC Address
*   B) Port Priority
*   C) Bridge Priority Value
*   D) Link Speed
*   **Correct Answer:** C) STP elects the bridge with the lowest Bridge ID (BID), which begins with the Bridge Priority.
*   **Distractor Analysis:**
    *   *Why correct:* STP elects the bridge with the lowest Bridge ID (BID), which begins with the Bridge Priority.
    *   MAC address is used as a tie-breaker if priorities are equal.

---

**Question 2**
In Spanning Tree Protocol, which port role describes a port that is **not** the root port or designated port, and is placed in a blocking state to prevent Layer 2 loops?
*   A) Alternate Port — a port that provides the best alternative path to the root bridge and transitions to forwarding if the root port fails (RSTP term).
*   B) Blocked Port — a non-root, non-designated port that discards frames and does not participate in active forwarding to prevent switching loops.
*   C) Backup Port — a redundant port on the same switch that provides a second connection to the same shared segment as an existing designated port (RSTP term).
*   D) Disabled Port — a port that has been administratively shut down using the `shutdown` command and does not participate in STP at all.
*   **Correct Answer:** B) Blocked Port — a non-root, non-designated port that discards frames and does not participate in active forwarding to prevent switching loops.
*   **Distractor Analysis:**
    * *Why B is correct:* In IEEE 802.1D STP, non-root non-designated ports enter the Blocking state to break loops. The port role is called "Blocked" in 802.1D and "Alternate/Backup" in RSTP (802.1w).
    * *Why A is incorrect:* The Alternate Port is the RSTP-specific term — in 802.1D this role is simply a blocked port.
    * *Why C is incorrect:* The Backup Port is also an RSTP-specific term for a redundant connection to the same segment, distinct from the Alternate port.
    * *Why D is incorrect:* A Disabled port is administratively down via `shutdown`, which removes it from STP participation entirely — it is not the same as a Blocked port.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
B) traceroute
A) nslookup
C) netstat -ano
D) ping
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Spanning Tree Protocol (STP & RSTP)** in a production environment, you encounter a system alert indicating a **Subnet Mask Mismatch** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
A) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why B is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why A is correct:* Because A host is configured with an incorrect subnet mask, preventing it from identifying local vs. remote addresses. The appropriate fix is to Correct the subnet mask configuration on the interface to match the network segment parameters.
    * *Why D is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.


---

**Question 5**
When configuring **Spanning Tree Protocol**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
D) Enable BPDU Guard on all PortFast-enabled access ports to err-disable the port if a BPDU is received.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Enable Root Guard on uplink ports facing the distribution layer to prevent a rogue switch from claiming the root bridge role.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Port Security directly prevents unauthorized devices from communicating by restricting which MAC addresses are permitted on a port — the most direct control against rogue physical connections.
    * *Why D is incorrect:* BPDU Guard protects against a rogue switch being connected (which sends BPDUs) but does not prevent a regular laptop or access point from connecting to the port.
    * *Why B is incorrect:* SSH/HTTPS secures management traffic but does not prevent unauthorized device connections to switch ports.
    * *Why C is incorrect:* Root Guard prevents topology manipulation by a rogue switch claiming root bridge status — it does not block unauthorized end devices from connecting.
