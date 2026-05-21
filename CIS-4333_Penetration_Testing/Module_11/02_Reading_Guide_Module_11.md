# Reading Guide: Module 11 - Social Engineering and Phishing Simulation
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 11 - Social Engineering and Phishing Simulation**! Social engineering attacks target the human element of security rather than technical vulnerabilities — they manipulate people into taking actions or revealing information that grants an attacker access. Phishing campaigns remain the most common initial access vector in real-world breaches, making social engineering simulation an essential component of a comprehensive penetration test. This module maps to the **Attacks and Exploits** domain of PT0-002 (**30% of exam weight**) and covers the social engineering techniques and tools the exam tests directly.

A phishing simulation that succeeds in credential harvesting or malware delivery provides compelling evidence to a client about the risk of human-layer vulnerabilities — often more impactful than technical findings alone.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Spear Phishing**: A targeted phishing attack directed at a specific individual or organization, using personalized information gathered during reconnaissance (name, role, colleagues, recent events) to craft a convincing pretext. Unlike mass phishing, spear phishing is tailored to the target — dramatically increasing success rates. It is the most common social engineering technique tested on PT0-002 and the most common initial access vector in real-world targeted attacks.

*   **Pretexting**: The creation of a fabricated scenario (pretext) used to manipulate a target into performing an action or divulging information. Examples include impersonating IT support to obtain credentials, posing as a vendor to gain physical access, or pretending to be a new employee who needs help resetting an account. Pretexting differs from phishing in that it typically involves direct interaction (phone, in-person) rather than email or a malicious link.

*   **Vishing (Voice Phishing)**: A social engineering attack conducted over the phone in which the attacker impersonates a trusted party — IT help desk, bank, IRS, vendor — to manipulate the target into revealing sensitive information or taking an action (e.g., transferring funds, resetting a password, disabling 2FA). Vishing relies on urgency, authority, and fear as psychological manipulation triggers. PT0-002 tests awareness of vishing as a distinct social engineering vector.

*   **Credential Harvesting**: The process of capturing usernames and passwords through deceptive means — typically a phishing page that mimics a legitimate login portal. Tools like the Social Engineering Toolkit (SET) automate credential harvesting by cloning legitimate websites and serving them from an attacker-controlled server. Harvested credentials are then used for initial access, lateral movement, or account takeover.

*   **Social Engineering Toolkit (SET)**: An open-source Python-based penetration testing framework specifically designed for social engineering attacks. SET automates spear phishing email campaigns, credential harvesting via website cloning, SMS phishing (smishing), and payload delivery through malicious documents. It is the industry-standard tool for social engineering simulation engagements and is explicitly referenced in PT0-002 exam content.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Attacks and Exploits is **30% of PT0-002**. Social engineering questions appear as scenario questions — know the attack type names, how they differ, and which psychological principles they exploit.
*   **Social Engineering Principles (PT0-002 Vocabulary):** The exam tests six psychological influence principles used in social engineering: **Authority** (impersonating figures of power), **Urgency** (time pressure to bypass critical thinking), **Social Proof** (everyone is doing it), **Scarcity** (limited availability), **Intimidation** (threatening consequences), and **Familiarity/Liking** (building rapport before asking for something).
*   **Phishing vs. Spear Phishing vs. Whaling:** Phishing is mass/untargeted. Spear phishing is targeted at a specific individual using personalized details. Whaling is spear phishing specifically targeting C-suite executives (CEO, CFO). PT0-002 may present a scenario and ask which term applies.
*   **Smishing vs. Vishing vs. Phishing:** These are the three delivery channel variants — email (phishing), SMS/text (smishing), and voice/phone (vishing). Know which medium each uses.
*   **Exam Trap — Authorization Required for Social Engineering:** PT0-002 tests that phishing simulations and social engineering are only performed when explicitly included in the scope and Rules of Engagement. Impersonating an employee or sending phishing emails without written authorization violates the RoE and potentially the law.
*   **SET Workflow:** The Social Engineering Toolkit menu hierarchy: `1) Social-Engineering Attacks` → `2) Website Attack Vectors` → `3) Credential Harvester Attack Method` → `2) Site Cloner`. Know the general flow for PT0-002 scenario questions about credential harvesting tool usage.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "Phishing" and "Social Engineering" rooms provide browser-based guided practice with phishing simulation concepts, SET usage, and credential harvesting techniques against realistic lab targets without requiring a local setup.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Social Engineering section for content covering phishing, pretexting, vishing, and SET mapped to PT0-002 domain 3 objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the Phishing and Social Engineering rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe is a browser-based cybersecurity training platform — labs run entirely in the browser with no local VM installation required. The phishing rooms cover email header analysis, credential harvesting simulation, and the psychological principles behind effective social engineering attacks.
*   **Required Video:** Watch the Social Engineering segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This is a free, full-length PT0-002 prep course on YouTube. Use chapter markers to navigate to the social engineering content covering phishing, pretexting, vishing, and the Social Engineering Toolkit.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Launch the Social Engineering Toolkit: `sudo setoolkit`**: You will open SET and navigate its menu to explore the social engineering attack categories available — building familiarity with the tool's structure before executing a specific attack vector.
*   **Clone a credential harvesting page**: Using SET's Website Attack Vector → Credential Harvester → Site Cloner option, you will clone a login page and set up a local listener. You will document how a phishing link to this page would capture credentials entered by a victim, and what those credentials would enable an attacker to access.
*   **Craft a targeted spear phishing pretext**: Using OSINT gathered in earlier modules (LinkedIn, WHOIS, theHarvester results), you will draft a realistic spear phishing email pretext for a hypothetical target — identifying the psychological principles used (authority, urgency, familiarity) and explaining why the pretext would be effective against the specific target persona.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the Phishing and Social Engineering rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Social Engineering section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
