# Quiz: Module 02 - Social Engineering and Phishing
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
An attacker sends a highly customized email specifically to the Chief Financial Officer (CFO) of a company, referencing a recent board meeting and asking them to click a link to review an urgent invoice. What type of social engineering attack is this?
A) Vishing
B) Whaling
C) Smishing
D) Pharming
*   **Correct Answer:** B) Whaling
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Vishing (Voice Phishing) relies on telephone calls, not email. The attacker speaks directly with the victim to extract information or credentials verbally.
    *   *Why C is incorrect:* Smishing (SMS Phishing) is delivered via text message, not email. It typically contains a shortened URL to a credential-harvesting site.
    *   *Why D is incorrect:* Pharming poisons DNS records to redirect users from legitimate URLs to malicious sites — it does not involve sending targeted emails. Whaling is spear phishing aimed specifically at high-value executives.

---

---

**Question 2**
A security analyst needs to collect forensic evidence from a compromised workstation. According to the standard order of volatility, which of the following data sources should the analyst collect FIRST?
A) The local hard drive (HDD/SSD)
B) The routing tables and ARP cache
C) System Memory (RAM)
D) Archival backup tapes
*   **Correct Answer:** C) System Memory (RAM)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Hard drives store non-volatile data that survives a reboot — they have a lower volatility than RAM and should be collected after volatile sources are captured.
    *   *Why B is incorrect:* Routing tables and ARP cache are volatile but considered slightly less critical to capture before full RAM, which contains running processes, encryption keys, and active network connections.
    *   *Why D is incorrect:* Archival backup tapes are the least volatile storage medium; the data is static and can be retrieved at any time during the investigation.

---

---

**Question 3**
An employee receives a phone call from someone claiming to be from the company's IT helpdesk. The caller says there is a security incident and asks the employee to provide their password immediately to prevent account lockout. Which social engineering technique is the attacker primarily using?
A) Smishing
B) Pharming
C) Vishing combined with pretexting
D) Spear phishing
*   **Correct Answer:** C) Vishing combined with pretexting
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Smishing is delivered via SMS text message, not a phone call. This scenario involves a live voice interaction.
    *   *Why B is incorrect:* Pharming is a technical DNS-manipulation attack that silently redirects browser traffic — it does not involve a phone call or a fabricated scenario.
    *   *Why D is incorrect:* Spear phishing is a targeted email attack. This attack uses a telephone call (vishing) combined with a fabricated helpdesk scenario (pretexting) to manufacture urgency and authority.

---

**Question 4**
A user reports that after clicking a link in an email, they were taken to what appeared to be their bank's login page. They entered their credentials but noticed the URL in the browser bar was slightly different from normal. Which type of attack does this describe?
A) Vishing
B) Smishing
C) Pharming
D) Phishing / Credential harvesting
*   **Correct Answer:** D) Phishing / Credential harvesting
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Vishing is a voice-based attack over the telephone — no email link or website is involved.
    *   *Why B is incorrect:* Smishing delivers the malicious link via SMS text message, not email. The delivery channel here is email.
    *   *Why C is incorrect:* Pharming redirects a user who typed a legitimate URL to a fake site by poisoning DNS — the user does not click a link in an email. Here the user clicked a link, making this a classic phishing credential-harvesting attack.

---

**Question 5**
When designing employee security awareness training to reduce social engineering risk, which of the following mitigations is MOST effective against phishing attacks?
A) Deploy a perimeter firewall with deep packet inspection to block all external email.
B) Train employees to verify sender identity through a separate trusted channel before acting on urgent requests.
C) Enforce full disk encryption on all endpoints to protect stored credentials.
D) Require employees to change their passwords every 30 days regardless of compromise indicators.
*   **Correct Answer:** B) Train employees to verify sender identity through a separate trusted channel before acting on urgent requests.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Blocking all external email is operationally infeasible for any business — organizations depend on external communication. Technical filters reduce phishing volume but cannot catch all attacks, especially targeted spear phishing.
    *   *Why C is incorrect:* Full disk encryption protects data confidentiality at rest if a device is lost or stolen — it does not prevent an employee from voluntarily entering credentials into a phishing site.
    *   *Why D is incorrect:* Frequent mandatory password resets have limited effectiveness against phishing. If an employee just entered credentials on a phishing site, the attacker already has the current password. Out-of-band verification breaks the social engineering chain before credentials are disclosed.
