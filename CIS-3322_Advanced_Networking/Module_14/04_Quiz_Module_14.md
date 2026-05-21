# Quiz: Module 14 - Network Automation & REST APIs
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
In a Software-Defined Networking architecture, which API is used to communicate between the controller and the application layer?
*   A) Southbound API
*   B) Northbound API
*   C) Eastbound API
*   D) OpenFlow
*   **Correct Answer:** B) Northbound APIs connect the controller to applications and orchestration tools. Southbound APIs connect to network devices.
*   **Distractor Analysis:**
    *   *Why correct:* Northbound APIs connect the controller to applications and orchestration tools. Southbound APIs connect to network devices.
    *   OpenFlow is a southbound protocol.

---

**Question 2**
Which of the following most accurately describes **JSON and XML data formats** in the context of network automation?
*   A) Two data serialization formats used to structure the payloads exchanged between REST API clients and network controllers, with JSON using key-value pairs in curly braces and XML using opening and closing tags.
*   B) Two network management protocols used by SNMP agents and managers to exchange device health metrics, interface counters, and configuration change notifications across IP networks.
*   C) Two encryption standards used to protect REST API payloads in transit, with JSON providing symmetric encryption and XML providing asymmetric public-key encryption of API responses.
*   D) Two types of configuration templates used by Ansible playbooks to define device configurations — JSON templates for Cisco IOS devices and XML templates for Juniper JunOS devices.
*   **Correct Answer:** A) Two data serialization formats used to structure the payloads exchanged between REST API clients and network controllers, with JSON using key-value pairs in curly braces and XML using opening and closing tags.
*   **Distractor Analysis:**
    * *Why A is correct:* JSON and XML are data interchange formats. REST APIs use them to structure request and response bodies. JSON is lighter-weight and preferred in modern APIs; XML is more verbose but still widely used (e.g., NETCONF uses XML).
    * *Why B is incorrect:* This describes SNMP and its MIB-based communication — JSON and XML are not SNMP components.
    * *Why C is incorrect:* JSON and XML are data formats, not encryption standards. HTTPS (TLS) provides transport encryption for REST APIs, regardless of whether JSON or XML is used.
    * *Why D is incorrect:* Ansible can use both JSON and YAML (not XML) for playbooks, and the choice is not vendor-specific — this option is fabricated.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
D) netstat -ano
A) nslookup
B) ping
C) traceroute
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Network Automation & REST APIs** in a production environment, you encounter a system alert indicating a **Subnet Mask Mismatch** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Correct Answer:** A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why B is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why C is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why A is correct:* Because A host is configured with an incorrect subnet mask, preventing it from identifying local vs. remote addresses. The appropriate fix is to Correct the subnet mask configuration on the interface to match the network segment parameters.


---

**Question 5**
When deploying **Network Automation & REST APIs**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Implement network access control (NAC) using 802.1X to require device certificate or credential validation before any device is granted access to a switch port.
D) Use Ansible to automate the deployment of consistent ACL policies across all switches, ensuring no switch is left with permissive rules that allow unauthorized devices.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Port Security directly restricts which devices can connect to a switch port by MAC address, providing immediate physical access control.
    * *Why B is incorrect:* SSH/HTTPS secures management sessions but does not prevent unauthorized devices from physically connecting to switch ports.
    * *Why C is incorrect:* 802.1X NAC is a stronger enterprise control, but Port Security is the direct CCNA-level answer for MAC-based switch port restriction.
    * *Why D is incorrect:* Automating ACL deployment with Ansible improves consistency but ACLs filter traffic at Layer 3 after a device is already connected — they do not prevent the physical port connection.
