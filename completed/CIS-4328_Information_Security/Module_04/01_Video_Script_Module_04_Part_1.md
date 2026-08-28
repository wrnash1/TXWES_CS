# Video Script: Module 04 — Threats, Attacks, and Vulnerabilities (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome back to CIS-4328. I'm Professor Nash, and this is Module 04, Part 1.

This module covers the threat landscape — malware categories, phishing variants, social engineering, supply chain attacks, zero-day exploits, and indicators of compromise. Domain 2 of the Security+ exam — "Threats, Vulnerabilities, and Mitigations" — accounts for 22% of your total score. Everything in this module has direct exam weight.

Let's anchor three definitions before we go further. A **threat** is any potential danger to a system or data. A **vulnerability** is a weakness that can be exploited. An **attack** is the act of exploiting that weakness. The exam will test you on the precise relationship between all three, so keep them distinct.

---

### [SECTION 1 — Malware Taxonomy — 2:00]

Malware means "malicious software." Every subcategory has a specific mechanism, propagation method, and primary goal. Those three dimensions are how the exam tests your knowledge.

#### Ransomware

Ransomware encrypts victim files or locks system access, then demands payment — typically cryptocurrency — for the decryption key.

Two delivery stages matter:

- **Initial access** — phishing email, exposed RDP, or a vulnerable public-facing application.

- **Lateral movement and staging** — attackers dwell in the network for days or weeks before triggering encryption. Modern RansomOps models show attackers exfiltrating data first to enable double extortion: pay or we publish your data.

Modern ransomware families like LockBit and BlackCat (ALPHV) operate as **Ransomware-as-a-Service (RaaS)**. Core developers lease the toolkit to affiliates in exchange for a revenue split.

Key exam point: **offline, immutable backups** are the primary recovery control. If backups are also encrypted, there is no recovery path.

#### Spyware and Adware

Spyware covertly monitors user activity — keystrokes, screenshots, browser history, clipboard contents — and exfiltrates data to the attacker.

Adware delivers intrusive ads and often bundles with spyware components. The exam treats them as related but distinct categories.

Commercial spyware like **Pegasus** (NSO Group) represents the extreme: a zero-click mobile exploit that grants complete device access. Behavioral signatures — unexpected outbound data flows — are the primary IoC for spyware detection.

#### Rootkits

A rootkit is designed to **hide its presence** from the operating system and from security tools.

Rootkits operate at multiple privilege levels:

- **User-mode rootkits** — patch running processes or DLLs; easier to detect.

- **Kernel-mode rootkits** — modify the OS kernel; much harder to detect.

- **Bootkits** — infect the Master Boot Record or UEFI firmware; persist across OS reinstalls.

Exam key point: rootkits require **out-of-band scanning** or trusted boot mechanisms (Secure Boot, TPM attestation) to detect reliably. The compromised OS cannot be trusted to report its own state truthfully.

#### Backdoors

A backdoor is an intentional, covert method for bypassing normal authentication.

Attackers install backdoors after initial compromise to **maintain persistence**. Unlike a rootkit that hides, a backdoor's primary goal is re-entry. A common pattern is malware installing a backdoor while a rootkit hides it.

The exam distinguishes backdoors from **Remote Access Trojans (RATs)**. A RAT provides full interactive control. A simple backdoor may only open a command shell or add a new privileged local account.

#### Trojans, Worms, and Viruses

These three appear repeatedly across Security+ scenarios:

- **Virus** — attaches to a legitimate file; requires user action to spread.

- **Worm** — self-propagating across networks; no host file required.

- **Trojan** — disguised as legitimate software; does not self-replicate.

**Exam trap**: If a scenario says "spread through a network without user interaction," the answer is worm, not virus.

---

### [SECTION 2 — Phishing Variants — 7:00]

Phishing is the delivery mechanism behind the majority of successful breaches. Security+ tests multiple variants, and the distinctions between them are precise.

#### Standard Phishing

Mass-sent emails impersonating trusted brands — banks, shipping companies, Microsoft, or the IRS. The goal is credential theft or malware delivery. Volume is the strategy: even a 0.1% click rate across a million emails yields thousands of victims.

#### Spear Phishing

Targeted phishing directed at a **specific individual** using personalized information gathered through OSINT (open-source intelligence). The attacker may reference your manager's name, a project you're working on, or internal tools your company uses. Personalization dramatically increases click-through rates compared to mass phishing.

**Exam trap**: Spear phishing targets individuals or small groups. Regular phishing targets large populations. This distinction is consistently tested.

#### Whaling

Whaling is spear phishing targeting **executives** — CEOs, CFOs, general counsel, board members. The name reflects the size of the target. A successful attack against a CFO can authorize fraudulent wire transfers via **Business Email Compromise (BEC)** for millions of dollars.

#### Vishing

Voice phishing. Attackers call targets impersonating IT support, the IRS, a bank fraud department, or a law enforcement agency. Urgency and authority are the psychological levers.

With AI voice cloning accessible to attackers, voice samples from public earnings calls or interviews can generate convincing synthetic audio. The exam recognizes vishing as a growing and legitimate threat vector.

#### Smishing

SMS-based phishing. Text messages containing malicious links or urgent requests ("Your package delivery failed — verify your address"). Mobile users tend to click more readily, making smishing highly effective against non-technical targets.

#### Pharming

Pharming redirects legitimate website requests to fraudulent sites, either by **DNS cache poisoning** or by modifying the local hosts file on the victim's machine. The user types the correct URL and still lands on a fake site.

**Exam distinction**: Pharming does not require the user to click a malicious link. Phishing requires user interaction with a malicious element. Pharming intercepts users who do everything correctly.

---

### [SECTION 3 — Social Engineering — 10:30]

Social engineering exploits human psychology rather than technical vulnerabilities. The Security+ exam categorizes these precisely.

#### Pretexting

The attacker creates a fabricated scenario — a pretext — to gain trust and extract information or access. Example: "I'm from the IT team; we're migrating your account and need your current password to complete the transfer." The invented context makes the request seem legitimate.

#### Baiting

An attacker leaves a USB drive in a parking lot labeled "Q3 Salary Data" or "Board Meeting Notes." Human curiosity does the rest. When plugged into a workstation, the drive executes malware automatically. Physical media is the bait; the malware is the payload.

#### Quid Pro Quo

Offering something in exchange for information or access. "I'll fix your computer problem if you give me your login credentials." Unlike pretexting, quid pro quo involves an explicit and visible exchange offer.

#### Tailgating and Piggybacking

Physical security attacks that bypass electronic access controls:

- **Tailgating** — following an authorized person through a secured door without their knowledge or consent.

- **Piggybacking** — the authorized person knowingly holds the door for an unauthorized individual.

**Exam distinction**: tailgating is covert; piggybacking involves the authorized person's cooperation (even if socially pressured).

#### Authority and Urgency

Social engineering consistently combines two psychological triggers: **authority** (impersonating someone with power — IT director, CEO, federal agent) and **urgency** (creating time pressure that prevents careful thinking). When you see both in an attack scenario on the exam, that combination is a high-confidence social engineering indicator.

---

### [SECTION 4 — Supply Chain Attacks — 12:30]

A supply chain attack compromises a target indirectly — by attacking a trusted vendor, a software library, or a hardware component that the target depends on.

#### SolarWinds (SUNBURST)

The canonical modern example: attackers compromised SolarWinds' software build pipeline and inserted the SUNBURST backdoor into a legitimate signed update package. When SolarWinds customers installed the routine update, they installed the backdoor. Approximately 18,000 organizations were affected.

**Key lesson**: Code signing did not prevent this attack because the malicious code was signed by SolarWinds' legitimate key. The compromise occurred before signing.

#### Open-Source Dependency Attacks

The **event-stream** npm package incident and the **xz-utils** backdoor (2024) demonstrate patient attackers who contribute to open-source projects, earn maintainer trust over months or years, then inject malicious code in a later update.

**Exam point**: SY0-701 Domain 2 explicitly addresses supply chain risk at **hardware, software, and vendor service** levels. Know all three vectors.

#### Hardware Supply Chain Risk

Malicious chips, firmware implants, or modified components inserted during manufacturing. The exam tests awareness of this vector even when real-world confirmed examples are limited.

---

### [SECTION 5 — Zero-Day Exploits — 14:00]

A zero-day exploit targets a **previously unknown vulnerability** for which no patch exists at the time of attack.

The term "zero-day" refers to the number of days the software vendor has had to address the issue: zero.

Zero-days are high-value commodities. Nation-state actors and sophisticated criminal groups pay millions for reliable zero-days targeting widely deployed platforms. Once a vendor is notified and releases a patch, the vulnerability transitions to a **known vulnerability** — the zero-day designation no longer applies.

Indicators that suggest a zero-day may be in use:

- Exploitation behavior with no corresponding CVE or patch.

- Unexpected process execution chains — a PDF reader spawning a command shell.

- Anomalous outbound connections from trusted, normally non-network-communicating applications.

**Exam nuance**: Zero-days are not unstoppable. Defense-in-depth, behavioral monitoring, and least-privilege access can limit the blast radius even when a zero-day is the initial access vector.

---

### [INDICATORS OF COMPROMISE — 14:45]

An **Indicator of Compromise (IoC)** is a forensic artifact suggesting that a system has been or is being compromised.

IoC categories the exam tests:

- **Network IoCs** — unusual outbound traffic, regular beaconing to unknown IPs, DNS queries for domain-generated algorithm (DGA) domains.

- **Host IoCs** — new scheduled tasks, unexpected services, modified registry run keys, newly created privileged accounts.

- **File IoCs** — known malicious hashes (MD5, SHA-256), executables in temp directories, signed binaries with mismatched metadata.

- **Behavioral IoCs** — process injection, living-off-the-land binary (LOLBin) execution, credential dumping activity (e.g., lsass memory access).

IoCs feed into the **incident response** and **threat detection** workflow — they are the signal that triggers investigation.

---

### [OUTRO — 15:00]

That is Part 1. You now have the foundational threat taxonomy: malware types by mechanism, phishing variants by scope, social engineering by psychological lever, supply chain by attack vector, and zero-days by their defining characteristic.

In Part 2 we shift to defenses, detection tools, and we work through the specific exam traps in this domain. I will show you exactly how Security+ question writers try to blur the lines between these categories.

See you in Part 2.

---

*End of Part 1 — Module 04*
