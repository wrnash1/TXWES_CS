# Quiz: Module 11 - NAT and PAT Configurations
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which NAT terminology describes the public IP address of an inside host as seen by external devices on the internet?
*   A) Inside Local
*   B) Inside Global
*   C) Outside Local
*   D) Outside Global
*   **Correct Answer:** B) Inside Global is the public address mapped to the internal host's Inside Local private address.
*   **Distractor Analysis:**
    *   *Why correct:* Inside Global is the public address mapped to the internal host's Inside Local private address.
    *   Inside Local is the private IP. Outside Global is the target public IP.

---

**Question 2**
Which of the following most accurately describes **inside local and inside global** address definitions in Cisco NAT?
*   A) Inside Local is the private IP address assigned to an internal host as seen from within the organization's network; Inside Global is the public IP address that same host appears to use when viewed from outside the network.
*   B) Inside Local is the IP address of the NAT router's WAN interface, which represents the organization to the internet; Inside Global is the private IP address pool from which hosts are dynamically assigned.
*   C) Inside Local refers to the IP address of the DNS server inside the organization; Inside Global refers to the publicly registered DNS server address used by external clients to reach internal resources.
*   D) Inside Local is the first usable host address in the inside subnet; Inside Global is the network address (first address) of the public IP block allocated by the ISP to the organization.
*   **Correct Answer:** A) Inside Local is the private IP address assigned to an internal host as seen from within the organization's network; Inside Global is the public IP address that same host appears to use when viewed from outside the network.
*   **Distractor Analysis:**
    * *Why A is correct:* This is the exact Cisco definition. Inside Local = 10.x/172.16.x/192.168.x private IP. Inside Global = the translated public IP the host appears as on the internet.
    * *Why B is incorrect:* The WAN interface IP is used as the Inside Global address in PAT configurations, but this option confuses the roles — it reverses the local/global relationship.
    * *Why C is incorrect:* DNS server addresses are irrelevant to NAT address terminology. This option is a distractor introducing unrelated concepts.
    * *Why D is incorrect:* NAT terminology is not about "first usable" or "network addresses" — it specifically refers to how a host's IP appears from different vantage points.


---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
B) netstat -ano
D) ping
A) traceroute
C) nslookup
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **NAT and PAT Configurations** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.


---

**Question 5**
When configuring **NAT and PAT**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
C) Configure a NAT pool with a limited number of public IP addresses to restrict the number of devices that can simultaneously access the internet.
D) Apply an inbound ACL on the NAT inside interface to block traffic from any source IP not in the authorized internal subnet range.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Port Security prevents unauthorized devices from connecting at the switch port level, stopping rogue devices before they can obtain a NAT translation.
    * *Why C is incorrect:* Limiting NAT pool size slows down unauthorized access but does not prevent a rogue device from physically connecting and using an available translation slot.
    * *Why D is incorrect:* An ACL on the NAT inside interface filters traffic after the device is already connected to the switch — it does not prevent the physical connection itself.
    * *Why B is incorrect:* SSH/HTTPS secures management sessions but does not prevent unauthorized devices from physically connecting to internal switch ports.
