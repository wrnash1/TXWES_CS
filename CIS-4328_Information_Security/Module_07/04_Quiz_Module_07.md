# Quiz: Module 07 - Network Security - Firewalls, IDS/IPS, VPNs
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A security architect is designing the network for a new branch office. The requirement states that the security device must not only filter traffic based on IP address and port number, but also identify and block specific applications regardless of what port they use. Which device best meets this requirement?
A) Stateful Firewall
B) Packet-Filtering Firewall
C) Next-Generation Firewall (NGFW)
D) Network-Based IDS
*   **Correct Answer:** C) Next-Generation Firewall (NGFW)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A stateful firewall tracks connection state and filters by IP address, port, and protocol — it cannot identify applications that operate on non-standard ports or tunnel through common ports like 443.
    *   *Why B is incorrect:* A packet-filtering firewall examines individual packets by source/destination IP and port only — it has no application-layer visibility and is the most basic firewall type.
    *   *Why D is incorrect:* A network-based IDS passively monitors traffic and generates alerts but does not block anything — it cannot enforce application control policies.

---

---

**Question 2**
A security operations team receives an alert that the IDS flagged a port scan originating from an internal host at 2:00 AM. After investigation, the team determines the scan was performed by an authorized vulnerability scanner running on schedule. How should this alert be classified?
A) True Positive
B) True Negative
C) False Positive
D) False Negative
*   **Correct Answer:** C) False Positive
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A true positive means the IDS correctly identified a real attack — the scan here was authorized and benign, so flagging it as malicious is incorrect.
    *   *Why B is incorrect:* A true negative means the IDS correctly did not alert on legitimate traffic — the IDS did fire an alert in this scenario, so this classification does not apply.
    *   *Why D is incorrect:* A false negative means the IDS missed a real attack and did not alert — the IDS did generate an alert here, so it is not a false negative.

---

---

**Question 3**
An organization needs to allow remote employees to securely access internal resources over the internet. The solution must encrypt all traffic between the employee's device and the corporate network without requiring a specialized VPN client application. Which VPN type best satisfies this requirement?
A) IPsec tunnel mode site-to-site VPN
B) SSL/TLS VPN (clientless)
C) IPsec transport mode host-to-host VPN
D) L2TP VPN without IPsec encapsulation
*   **Correct Answer:** B) SSL/TLS VPN (clientless)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IPsec tunnel mode site-to-site VPN connects two entire networks (e.g., two office locations) and requires VPN gateway hardware at both ends — it is not designed for individual remote user access.
    *   *Why C is incorrect:* IPsec transport mode encrypts traffic between two specific hosts and requires IPsec software on both endpoints — it is not a remote access VPN solution and does not provide web-based clientless access.
    *   *Why D is incorrect:* L2TP without IPsec provides tunneling with no encryption — traffic is transmitted in plaintext, making it unsuitable for any security-conscious remote access scenario.

---

**Question 4**
A network security engineer is tuning an IPS deployed at the corporate internet edge. After deployment, the operations team reports that legitimate customer HTTPS traffic to the e-commerce site is being intermittently blocked. What should the engineer do to resolve this while maintaining security?
A) Disable the IPS temporarily and replace it with an IDS to eliminate all blocking.
B) Review the triggered signatures, identify those causing false positives, and create tuned exceptions for known-good traffic patterns.
C) Switch the IPS from inline mode to tap mode so it no longer blocks traffic.
D) Increase the IPS sensitivity threshold to maximum to ensure all threats are caught.
*   **Correct Answer:** B) Review the triggered signatures, identify those causing false positives, and create tuned exceptions for known-good traffic patterns.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Replacing an IPS with an IDS removes all active blocking capability — the organization would lose the protection the IPS provides against real attacks, not just the false positives.
    *   *Why C is incorrect:* Switching to tap (passive) mode converts the IPS into a monitoring-only device equivalent to an IDS — this eliminates all prevention capability and is an overreaction to a tuning problem.
    *   *Why D is incorrect:* Increasing sensitivity makes false positives worse, not better — higher sensitivity means more signatures fire on ambiguous traffic, which increases both false positives and legitimate traffic disruption.

---

**Question 5**
A company wants to segment its network so that its industrial control systems (ICS) cannot communicate directly with corporate workstations, even if both are on the internal network. Which network security control achieves this segmentation?
A) Deploy a VPN between the ICS network and the corporate network.
B) Place a firewall between the ICS VLAN and the corporate VLAN with a default-deny policy.
C) Install an IDS sensor on the ICS network to monitor traffic between the segments.
D) Require all users to authenticate with MFA before accessing any internal resource.
*   **Correct Answer:** B) Place a firewall between the ICS VLAN and the corporate VLAN with a default-deny policy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A VPN creates an encrypted tunnel for communication — it facilitates connectivity between networks rather than restricting it. Deploying a VPN between the segments would increase reachability, not segment it.
    *   *Why C is incorrect:* An IDS passively monitors and alerts on traffic — it does not block or prevent communication between the ICS and corporate segments. Detection does not equal prevention.
    *   *Why D is incorrect:* MFA controls who can authenticate to systems but does not create a network-layer barrier between VLANs. An authenticated user could still reach ICS systems if there is no firewall policy enforcing segmentation.
