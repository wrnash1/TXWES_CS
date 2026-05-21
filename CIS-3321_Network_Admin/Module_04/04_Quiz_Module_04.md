# Quiz: Module 04 - Security
## Course: CIS-3321_Network_Admin (3321_Network_Admin - CompTIA Network+ (N10-008))

---

**Question 1**
Which of the following security controls operates primarily at Layer 7 (Application) of the OSI model to inspect the payload of network traffic for malicious signatures and actively drop the traffic if an attack is detected?
A) Stateless Firewall
B) Intrusion Detection System (IDS)
C) Intrusion Prevention System (IPS)
D) Layer 3 Switch
*   **Correct Answer:** C) Intrusion Prevention System (IPS)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A stateless firewall operates at Layers 3/4, looking only at IP addresses and ports, not the Layer 7 payload.
    *   *Why B is incorrect:* An IDS detects and alerts on attacks but does *not* actively drop the traffic. An IPS is required to actively block it.
    *   *Why D is incorrect:* A Layer 3 switch performs routing based on IP addresses, not deep packet inspection for malware.

---

---

**Question 2**
A company implements a new policy requiring employees to swipe their smart card and then scan their fingerprint to enter the secure server room. Which authentication factors are being utilized?
A) Something you have and Something you know
B) Something you have and Something you are
C) Something you know and Something you are
D) Something you do and Something you have
*   **Correct Answer:** B) Something you have and Something you are
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A smart card is "something you have", but a fingerprint is not "something you know" (like a PIN or password).
    *   *Why C is incorrect:* A fingerprint is "something you are", but a smart card is not "something you know".
    *   *Why D is incorrect:* "Something you do" refers to behavioral biometrics (like typing cadence or signature dynamics), not scanning a static physical fingerprint.

---

---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
B) traceroute
D) netstat -ano
C) ping
A) nslookup
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.


---

**Question 4**
While working on **Security** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **Security**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

