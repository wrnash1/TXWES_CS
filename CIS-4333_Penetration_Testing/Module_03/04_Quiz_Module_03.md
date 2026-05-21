# Quiz: Module 03 - OSINT and Passive Reconnaissance
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which command-line tool is used for passive DNS gathering, specifically retrieving mail server configurations?
*   A) dig example.com MX
*   B) nmap example.com
*   C) ping example.com
*   D) traceroute example.com
*   **Correct Answer:** A) `dig` queries DNS name servers. Passing `MX` retrieves mail records passively without targeting the server directly.
*   **Distractor Analysis:**
    *   *Why correct:* `dig` queries DNS name servers. Passing `MX` retrieves mail records passively without targeting the server directly.
    *   *Why B is incorrect:* Nmap sends active probe packets to the target host — it is an active reconnaissance tool, not a passive DNS lookup utility.
    *   *Why C is incorrect:* Ping sends ICMP echo requests directly to the target, which constitutes active reconnaissance and may appear in the target's logs.
    *   *Why D is incorrect:* Traceroute maps network hops by sending packets with incrementing TTL values — it is an active technique that touches target infrastructure.

---

**Question 2**
In penetration testing OSINT, which of the following best defines the **`host` command** as used during passive DNS reconnaissance?
*   A) A DNS lookup utility that resolves hostnames to IP addresses and queries specific record types (A, MX, NS, TXT), providing a simpler alternative to `dig` for quick passive name resolution checks.
*   B) A network scanner that sends TCP SYN packets to enumerate open ports on a target system and identify running services.
*   C) A password cracking tool that performs dictionary and brute-force attacks against hashed credentials recovered from a compromised system.
*   D) A wireless packet capture tool that places a network interface into monitor mode to intercept 802.11 frames in the air.
*   **Correct Answer:** A) A DNS lookup utility that resolves hostnames to IP addresses and queries specific record types (A, MX, NS, TXT), providing a simpler alternative to `dig` for quick passive name resolution checks.
*   **Distractor Analysis:**
    *   *Why A is correct:* The `host` command is a standard Unix/Linux DNS resolution utility. Like `dig`, it queries public DNS resolvers and leaves no trace on the target's systems, making it a passive reconnaissance tool tested on PT0-002.
    *   *Why B is incorrect:* This describes Nmap, an active port scanner that sends probe packets to target systems.
    *   *Why C is incorrect:* This describes tools like Hashcat or John the Ripper, which are post-exploitation credential cracking tools — not OSINT utilities.
    *   *Why D is incorrect:* This describes `airmon-ng`, a wireless interface management tool used in wireless penetration testing, not passive DNS reconnaissance.

---

**Question 3**
A tester wants to enumerate subdomains of a target organization without sending any packets to the target's systems. Which passive technique would be most effective?
*   A) Run `nmap -sn target.com` to discover live hosts via ICMP sweep.
*   B) Query certificate transparency logs at crt.sh for SSL/TLS certificates issued to `%.target.com`.
*   C) Use `dirb` to brute-force common subdomain names against the target's web server.
*   D) Perform a DNS zone transfer with `dig axfr @ns1.target.com target.com`.
*   **Correct Answer:** B) Query certificate transparency logs at crt.sh for SSL/TLS certificates issued to `%.target.com`.
*   **Distractor Analysis:**
    *   *Why B is correct:* Certificate transparency logs are a public, passive data source. Every issued SSL/TLS certificate is logged publicly, and tools like crt.sh allow testers to enumerate all subdomains for which certificates have been issued — without touching the target.
    *   *Why A is incorrect:* Nmap sends ICMP and/or TCP packets directly to the target — this is active reconnaissance that appears in the target's firewall and IDS logs.
    *   *Why C is incorrect:* Dirb sends HTTP requests directly to the target web server to brute-force directory/subdomain names — this is active reconnaissance with a high detection footprint.
    *   *Why D is incorrect:* A DNS zone transfer (`dig axfr`) contacts the target's authoritative name server directly. This is semi-active and will appear in the target's DNS server logs.

---

**Question 4**
A penetration tester uses Shodan to search for a client's publicly exposed infrastructure. Which of the following best describes why Shodan is classified as a passive reconnaissance tool?
*   A) Shodan uses stealth scanning techniques that avoid detection by the target's IDS.
*   B) Shodan indexes banner information it collected from its own prior scanning of public IP space — the tester retrieves pre-collected data without sending probes to the target.
*   C) Shodan operates exclusively over encrypted HTTPS connections, making queries undetectable.
*   D) Shodan only scans systems that have explicitly opted in to the service, making it a consensual data source.
*   **Correct Answer:** B) Shodan indexes banner information it collected from its own prior scanning of public IP space — the tester retrieves pre-collected data without sending probes to the target.
*   **Distractor Analysis:**
    *   *Why B is correct:* Shodan's crawler scans the internet on its own schedule and stores the results in a searchable database. When a tester queries Shodan, they are searching that pre-collected database — not probing the target directly. This makes it passive from the target's perspective.
    *   *Why A is incorrect:* Shodan itself does send active probes when building its index, but the tester's use of the search interface is passive. Stealth is not the defining characteristic.
    *   *Why C is incorrect:* The encryption of the query channel (HTTPS) is about protecting the tester's query from interception — it has no bearing on whether the target can detect reconnaissance activity.
    *   *Why D is incorrect:* Shodan scans all public IP addresses without opt-in. It is passive for the tester because they query a database, not because Shodan itself has consent.

---

**Question 5**
When conducting OSINT against a target, a penetration tester runs theHarvester and collects a list of employee email addresses in the format `firstname.lastname@target.com`. Beyond social engineering, how is this data most directly useful to the penetration tester?
*   A) The email addresses can be fed directly into Metasploit as target identifiers for automated exploitation.
*   B) The email addresses reveal the naming convention used for domain accounts, enabling targeted password spray attacks against services like OWA, VPN, or Office 365.
*   C) The email addresses allow the tester to bypass firewall rules by spoofing SMTP traffic from known internal addresses.
*   D) The email addresses can be used to perform SQL injection by inserting them into database query fields on the target's login portal.
*   **Correct Answer:** B) The email addresses reveal the naming convention used for domain accounts, enabling targeted password spray attacks against services like OWA, VPN, or Office 365.
*   **Distractor Analysis:**
    *   *Why B is correct:* Most organizations use email addresses as usernames or derive usernames directly from the email prefix. Knowing the format `firstname.lastname` lets a tester construct a valid username list for password spray attacks against externally exposed authentication services — a direct and high-value intelligence output from theHarvester.
    *   *Why A is incorrect:* Metasploit exploits target specific vulnerabilities in services and applications — it does not use email addresses as target identifiers in any standard module workflow.
    *   *Why C is incorrect:* SMTP spoofing requires access to a mail relay or DNS manipulation — knowing a valid email address alone does not enable firewall bypass.
    *   *Why D is incorrect:* SQL injection exploits vulnerable input fields that pass unsanitized data to a database. An email address harvested externally does not inherently enable SQLi on a login form.
