# Quiz: Module 16 — CySA+ CS0-003 Exam Preparation and Capstone

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Instructions

This quiz covers all four CySA+ CS0-003 exam domains with cross-domain integration questions. Select the best answer for each question. Distractor analysis is provided to reinforce understanding across the full course.

---

## Question 1

A security analyst is reviewing a SIEM dashboard and sees three correlated alerts: (1) a successful logon from a user account outside business hours, (2) the same account accessing a file server share containing finance records, and (3) 47 GB of outbound data transferred to an external cloud storage service. Which MITRE ATT&CK tactic sequence does this evidence most strongly suggest?

- A) Initial Access → Persistence → Impact
- B) Initial Access → Credential Access → Lateral Movement
- C) Initial Access → Collection → Exfiltration
- D) Execution → Discovery → Defense Evasion

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Impact techniques destroy, encrypt, or disrupt data. Transferring data to an attacker-controlled external location is Exfiltration, not Impact. Persistence would require the attacker to create mechanisms to maintain access, which is not indicated. Why B is incorrect: Credential Access involves stealing or forging credentials. The scenario uses valid credentials for access — there is no evidence of credential theft activity. Lateral Movement involves moving to other internal systems; the data went externally. Why C is correct: The three events map directly to three ATT&CK tactics in sequence. The unusual after-hours logon with valid credentials represents Initial Access via a valid account (T1078). Accessing finance file shares represents Collection — gathering data of interest (T1039). The 47 GB outbound transfer to external cloud storage represents Exfiltration — transferring data outside the organization (T1567). Why D is incorrect: Execution, Discovery, and Defense Evasion do not describe the pattern of external access, data access, and data transfer described in the scenario.

---

## Question 2

An organization completes a CySA+ exam study session and wants to identify which ATT&CK techniques they currently have zero detection coverage for. Which tool is most appropriate for visualizing this gap?

- A) Shodan — to identify internet-facing assets with no security monitoring
- B) MITRE ATT&CK Navigator — to map current detection coverage against the ATT&CK matrix and visually identify uncovered techniques
- C) Nessus — to scan for unpatched vulnerabilities associated with known ATT&CK techniques
- D) Wireshark — to capture network traffic and identify techniques actively being used against the organization

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Shodan identifies internet-exposed assets and open services, not ATT&CK detection coverage gaps. Why B is correct: The ATT&CK Navigator is specifically designed to visualize technique coverage. Teams color-code techniques: green (detectable by automated rules), yellow (hunting coverage), red or blank (no coverage). This visualization directly answers the question of which techniques have zero coverage. Why C is incorrect: Nessus identifies software vulnerabilities. While some vulnerabilities enable ATT&CK techniques, Nessus does not map detection capability against the ATT&CK matrix. Why D is incorrect: Wireshark captures and analyzes network traffic. It cannot visualize detection rule coverage gaps; it only shows what traffic is currently present.

---

## Question 3

A CISO asks the security team to demonstrate the return on investment of the threat hunting program. The team completed 30 hunts last year. Four hunts resulted in confirmed incident escalations that would have been missed by automated detection. The average cost of a data breach at the organization's scale is estimated at $3.2 million. The annual cost of the hunting program (analyst time and tooling) is $180,000. Which statement most accurately represents the program's ROI?

- A) The program cannot demonstrate ROI because threat hunting has no measurable output
- B) If even one of the four confirmed incidents would have resulted in a reportable breach, the cost avoidance likely exceeds the program cost by a factor of 17 or more
- C) ROI should be calculated only on the number of hunts completed, not on incident escalations
- D) The program is not cost-effective because 26 of 30 hunts found nothing

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Threat hunting has measurable outputs — confirmed incidents detected, detection rules created, dwell time reduced, and cost avoidance. The statement is false. Why B is correct: $3.2M average breach cost divided by $180,000 program cost = 17.8x. If even one of the four escalated incidents would have become a full breach without hunting detection, the cost avoidance alone exceeds program cost by nearly 18 times. This is the standard ROI argument for proactive security programs. Why C is incorrect: Hunt volume (30 hunts) is an activity metric, not an outcome metric. Outcome metrics — incidents detected, rules created, dwell time reduced — are what demonstrate ROI. Why D is incorrect: 26 negative-result hunts are not failures. They demonstrate coverage (26 techniques/time periods were actively checked and confirmed clear), establish baselines, and generate new detection rules. The ROI argument treats each hunt as having value regardless of whether active threats were found.

---

## Question 4

An analyst is preparing for the CySA+ CS0-003 exam and is reviewing the four exam domains. Which domain carries the highest percentage weight and therefore warrants the most study time?

- A) Domain 2: Vulnerability Management at 30%
- B) Domain 3: Incident Response and Digital Forensics at 20%
- C) Domain 1: Security Operations at 33%
- D) Domain 4: Reporting and Communication at 17%

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Domain 2 (Vulnerability Management) carries 30% — the second highest weight. It is important but not the largest domain. Why B is incorrect: Domain 3 (Incident Response and Digital Forensics) carries 20%, the third highest weight. Why C is correct: Domain 1 (Security Operations) carries 33% — the largest single domain on the CS0-003 exam. It covers SIEM operations, threat intelligence, log analysis, tool identification, threat hunting, and automation. Analysts who master Domain 1 have the greatest advantage on the exam. Why D is incorrect: Domain 4 (Reporting and Communication) carries 17% — the smallest domain by weight. It is not optional, but it warrants proportionally less study time than Domains 1 and 2.

---

## Question 5

An analyst studying for the CySA+ exam encounters a practice question asking: "What is the FIRST step an analyst should take upon receiving a SIEM alert for potential ransomware?" Four answer options are provided: (A) Isolate the affected host, (B) Triage the alert to confirm it is a true positive, (C) Notify the legal team, (D) Begin eradication. Using CySA+ exam strategy, which answer is correct and why?

- A) A — Isolate immediately to stop spread before it gets worse
- B) B — Triage first to confirm the alert before taking any action
- C) C — Legal notification is required before any technical action
- D) D — Begin eradication immediately to remove the threat

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Isolation before triage is a common exam trap. Isolating a host before confirming the alert is a true positive wastes resources, disrupts business operations, and in some cases destroys forensic evidence — all for what may be a false positive. The NIST 800-61 framework places triage within the Detection and Analysis phase, which precedes Containment. Why B is correct: Triage is always the first step upon receiving any alert. You must confirm the alert is a true positive before taking disruptive action. Only after triage confirms ransomware activity does isolation become appropriate. This follows the NIST 800-61 phase sequence precisely. Why C is incorrect: Legal notification occurs when an incident is confirmed and the scope is understood — not as the first step upon receiving an alert. Notifying legal before confirming the incident is premature. Why D is incorrect: Eradication occurs after containment, which occurs after confirmed triage. Eradication as the first step would be wildly out of NIST phase sequence.

---

## Question 6

Which combination of metrics best demonstrates that a vulnerability management program is both thorough in its identification and effective in its remediation?

- A) Total vulnerabilities discovered per quarter and total scan hours logged
- B) Percentage of assets scanned with credentialed scans and percentage of Critical/High vulnerabilities remediated within SLA
- C) Number of vulnerability scanners deployed and number of IT tickets submitted for patching
- D) The CVSS score distribution of open vulnerabilities and the number of exception requests submitted

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Total discoveries and scan hours are activity metrics. They measure effort, not effectiveness. A program that finds many vulnerabilities but remediates none is not effective, yet both metrics could look strong. Why B is correct: Credentialed scan coverage measures the thoroughness of identification — are we actually seeing inside systems? Percentage of Critical/High vulnerabilities remediated within SLA measures remediation effectiveness — are we fixing the most important things on time? Together these two metrics answer the two core questions of any vulnerability management program. Why C is incorrect: Scanner count and ticket volume are activity metrics. More scanners and more tickets do not prove findings are being remediated or that scans cover the right assets. Why D is incorrect: CVSS score distribution shows the current risk profile but not how it is changing over time. Exception counts show how often policy is bypassed but not program health overall.

---

## Question 7

A CySA+ exam question presents this scenario: "An analyst captures a Wireshark trace during a suspected data exfiltration event. The trace shows a series of HTTPS POST requests from an internal server to an external IP, each carrying approximately 500 KB of data, occurring every 11 minutes for 6 hours." The question asks: "Which threat behavior does this traffic pattern MOST likely represent?" Which answer is correct?

- A) Port scanning — the server is probing the external IP for open services
- B) Brute force authentication — the server is attempting login attempts against the external host
- C) Automated data exfiltration — the consistent interval and payload size suggest programmatic, scheduled data transfer to attacker-controlled infrastructure
- D) Normal backup traffic — HTTPS POST to external IP is a standard backup protocol

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Port scanning generates connection attempts to many different ports or hosts in rapid succession, not repeated large POST requests to a single destination at regular intervals. Why B is incorrect: Brute force authentication produces many small authentication attempts, typically at sub-second intervals. The pattern described — 500 KB payloads every 11 minutes — does not match authentication attempt patterns. Why C is correct: Three characteristics together confirm this is automated exfiltration: (1) regular interval (every 11 minutes, not random user-driven timing), (2) consistent payload size (programmatically chunked data), and (3) outbound POST to a single external IP (data is being sent, not retrieved). This pattern matches automated staged exfiltration over C2 infrastructure. Why D is incorrect: Legitimate backup solutions use authenticated, organizational-approved endpoints — not arbitrary external IPs. They also typically use backup-specific protocols, not plain HTTPS POST to unknown infrastructure. An analyst should never assume external HTTPS POST traffic is a backup without verification.

---

## Question 8

Which of the following correctly distinguishes between a vulnerability assessment and a penetration test?

- A) A vulnerability assessment is performed by external consultants; a penetration test is performed by internal staff only
- B) A vulnerability assessment identifies and reports weaknesses without exploiting them; a penetration test actively exploits vulnerabilities to demonstrate real-world impact and requires written authorization (rules of engagement)
- C) A vulnerability assessment uses only automated tools; a penetration test uses only manual techniques
- D) A vulnerability assessment tests all systems; a penetration test is limited to web applications only

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Both assessments can be performed by external or internal teams. The source of the assessors does not define the activity type. Why B is correct: This is the definitive distinction. A vulnerability assessment discovers and documents weaknesses using scanning tools and analysis, but does not exploit them. A penetration test goes further by actively attempting to exploit vulnerabilities to prove that exploitation is possible and to understand the realistic impact. Penetration tests require formal written authorization (rules of engagement) because they can disrupt systems or cause unintended harm. Why C is incorrect: Vulnerability assessments often include manual analysis, and penetration tests heavily rely on automated tools alongside manual techniques. The tool type does not define the activity. Why D is incorrect: Both vulnerability assessments and penetration tests can cover any scope — network infrastructure, applications, cloud environments, physical security, or social engineering. Scope is defined by the rules of engagement, not by activity type.

---

## Question 9

An analyst completes the CySA+ exam and passes. Which statement most accurately describes what CySA+ certification represents in the security industry?

- A) CySA+ certifies that the holder is qualified to lead an incident response team as CISO
- B) CySA+ is an entry-level certification equivalent to CompTIA A+, demonstrating basic computer literacy
- C) CySA+ is an intermediate-level certification validating the skills of a working security analyst including threat detection, vulnerability management, incident response, and reporting
- D) CySA+ is a vendor-specific certification valid only for Cisco security products

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: CySA+ is not a leadership or executive certification. It validates analyst-level skills. Leadership and strategic roles typically require experience and certifications like CISM or CISSP. Why B is incorrect: CySA+ is intermediate-level and specifically requires security operations knowledge. It is not equivalent to A+ (entry-level hardware/software support). CompTIA positions CySA+ as requiring Security+ or equivalent experience as a prerequisite. Why C is correct: CompTIA positions CySA+ as an intermediate analyst certification validating skills in security monitoring, threat detection, vulnerability management, incident response, reporting, and communication. It demonstrates that the holder can perform real-world analyst work across the security operations lifecycle. Why D is incorrect: CySA+ is vendor-neutral. It is not specific to Cisco, Microsoft, Palo Alto, or any other vendor. It validates skills applicable across any security toolset or environment.

---

## Question 10

Reflecting on the full CIS-4332 course, a student is asked to identify which single skill area most directly enables all other security analyst disciplines. Which answer is most defensible?

- A) Python scripting, because automation removes human error from all security processes
- B) Log analysis, because every detection, investigation, and forensic activity begins with evidence in log data, and the analyst who cannot read logs cannot perform any downstream function effectively
- C) Threat hunting, because proactive detection is more valuable than reactive detection
- D) Compliance management, because organizations that pass audits have no security gaps

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Python scripting is highly valuable and multiplies analyst productivity, but an analyst who cannot read and interpret log data manually cannot validate automated outputs, investigate novel incidents, or perform forensic analysis. Automation builds on manual skill, not the reverse. Why B is correct: Every security analyst function — SIEM triage, incident investigation, forensic analysis, threat hunting, vulnerability prioritization, and compliance monitoring — relies on reading, interpreting, and acting on log data. An analyst who cannot understand what a log entry means cannot effectively triage alerts, investigate incidents, or hunt for threats. Log analysis is the foundational skill upon which all others are built. Why C is incorrect: Threat hunting is a high-value skill but it presupposes the ability to interpret endpoint telemetry, network logs, and authentication records — all forms of log analysis. You cannot hunt without reading telemetry. Why D is incorrect: Compliance audit passage is a compliance milestone, not a security guarantee. As demonstrated in Module 13, organizations can pass audits while having active attackers in their environment. Compliance does not eliminate security gaps; it verifies control existence, not effectiveness.

---

## Question 11

A CySA+ exam question presents four answer choices, all of which seem plausible. The question asks: "Which action should an analyst take FIRST upon discovering a suspected insider threat collecting sensitive HR data?" Option A says to terminate the employee immediately. Option B says to secretly install keylogger software on the employee's machine. Option C says to consult with legal and HR before taking any action to ensure the investigation is lawful and admissible. Option D says to immediately delete all the employee's access to all systems. Which answer is correct for the exam context?

- A) A — Termination stops the insider threat immediately
- B) B — Real-time monitoring is the most direct detection method
- C) C — Legal and HR consultation ensures the investigation is authorized, lawful, and can support disciplinary or legal action
- D) D — Removing access is always the first containment step

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Terminating the employee before a lawful investigation is complete may violate employment law, tip off co-conspirators, destroy evidence, and expose the organization to wrongful termination liability. Termination is a business action that follows investigation, not precedes it. Why B is incorrect: Installing keylogger software without proper legal authorization may violate federal wiretapping laws (the Electronic Communications Privacy Act), employee privacy rights, and the organization's own acceptable use policies. Unauthorized monitoring is illegal even against suspected malicious insiders. Why C is correct: Insider threat investigations require coordination between security, legal counsel, and HR before any action is taken. This ensures monitoring or evidence collection is authorized, the investigation method is admissible in disciplinary proceedings or legal action, and the organization's response is proportionate and lawful. The CySA+ exam consistently selects "consult legal/HR" as the first step in sensitive investigation scenarios involving employee activity. Why D is incorrect: Removing access immediately alerts the subject, potentially causing them to destroy evidence, contact co-conspirators, or accelerate their activities. Access termination is a containment action taken under proper authorization, not an unilateral immediate first step.

---

## Question 12

An analyst is reviewing a SIEM correlation rule that fires when any user account generates more than five failed logon attempts (Event ID 4625) within five minutes. The rule has a 94% false positive rate over the past month. Which tuning approach best reduces false positives while preserving detection of real brute force attacks?

- A) Increase the threshold to 500 failed logons before the alert fires
- B) Disable the rule entirely and rely on endpoint detection for brute force identification
- C) Add conditions: exclude known service accounts and script accounts by name, require the failed logons to originate from external IP addresses or multiple different source IPs, and require at least one subsequent successful logon within 10 minutes of the failures
- D) Reduce the time window to 30 seconds to make the rule more precise

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Raising the threshold to 500 would miss most real brute force attacks. Effective brute force tools can generate 500 attempts, but most automated attacks are detected at much lower thresholds. Raising the threshold to reduce false positives removes the detection capability entirely. Why B is incorrect: Disabling the rule eliminates coverage for an important attack technique. The goal is tuning, not removal. Why C is correct: The multi-condition approach targets the specific false positive sources. Service accounts and automation scripts legitimately generate repeated authentication failures during misconfiguration periods — excluding known accounts removes this common false positive source. Requiring external or multi-source IPs focuses the rule on actual attack patterns rather than internal misconfiguration. Requiring a subsequent successful logon strongly suggests the failures were deliberate credential attacks rather than accidental lockout. Each condition independently improves precision without removing real attack coverage. Why D is incorrect: Reducing the time window to 30 seconds would catch only the most aggressive automated tools. It would miss slower, more sophisticated brute force attacks that operate at a deliberate pace to avoid lockout thresholds. It also does not address the root cause of the false positives.

---

## Question 13

A CySA+ exam question asks: "Which phase of the NIST 800-61 Incident Response lifecycle is MOST concerned with identifying the scope, impact, and severity of an incident?" Which answer is correct?

- A) Preparation — establishing the IR capability before incidents occur
- B) Detection and Analysis — identifying and validating the incident, determining scope and severity
- C) Containment, Eradication, and Recovery — stopping the spread and removing the threat
- D) Post-Incident Activity — reviewing what happened and improving the process

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: The Preparation phase occurs before any incident. It encompasses building the IR team, establishing tools and processes, and developing playbooks. Preparation is not concerned with identifying the scope of a specific incident because no incident exists yet. Why B is correct: The Detection and Analysis phase is precisely where analysts determine: Is this a real incident? What systems are affected? What is the severity? What attack vector was used? What is the timeline? Scope determination is the core output of this phase. Everything downstream — containment decisions, notification requirements, resource allocation — depends on the scope and severity findings from Detection and Analysis. Why C is incorrect: Containment, Eradication, and Recovery operate on an already-scoped incident. The scope was determined in Detection and Analysis. CEaR focuses on stopping the damage, removing the threat, and restoring operations — not on discovering what the incident is. Why D is incorrect: Post-Incident Activity occurs after the incident is resolved. It reviews what happened, identifies improvement opportunities, and updates the IR capability. It does not scope an active incident.

---

## Question 14

A CySA+ scenario asks: "An analyst investigates a phishing compromise and determines the attacker used the compromised account to access SharePoint, download 2,400 files from a finance folder, and send 15 internal emails impersonating the compromised user. Which NIST 800-61 information impact category best describes this incident?"

- A) None — no data left the organization's environment
- B) Privacy Breach — personally identifiable information may have been accessed
- C) Proprietary Breach — organizational financial data was accessed and may have been exfiltrated
- D) Integrity Loss — the attacker modified or destroyed data

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Data accessed and downloaded from a finance folder by an unauthorized actor represents a data breach even if the exfiltration path cannot be confirmed. The attacker had read access to and downloaded 2,400 financial files — this is not a "no impact" scenario. Why B is incorrect: A Privacy Breach applies when personally identifiable information (PII) such as Social Security numbers, health records, or personal contact information is accessed. Finance folder contents are organizational financial data, not necessarily personal information about individuals. The correct category is Proprietary Breach. Why C is correct: NIST 800-61 defines a Proprietary Breach as an incident where organizational information (trade secrets, financial data, proprietary processes) has been accessed or disclosed without authorization. Finance records accessed by an unauthorized actor — regardless of whether confirmed external exfiltration occurred — represent a Proprietary Breach. Why D is incorrect: Integrity Loss applies when data is modified, deleted, or corrupted. The described scenario involves unauthorized access and potential exfiltration, not modification or destruction.

---

## Question 15

During a CySA+ practice exam, a student encounters this question: "A threat hunter identifies a Cobalt Strike beacon running inside `svchost.exe` on a production server. The beacon has been present for an estimated 8 days. Which is the MOST appropriate immediate action?" The student narrows the choices to: (A) Isolate the server immediately to stop C2 communication, (B) Continue monitoring the beacon silently for 24 more hours to collect more intelligence before acting. Which answer is correct and what exam reasoning applies?

- A) A — Immediate isolation is always the correct response to any confirmed C2 beacon
- B) B — Intelligence collection benefits outweigh the risk of 24 additional hours of attacker access
- C) A — but only after creating a full memory image for forensic analysis first, and escalating to the IR team who makes the isolation decision
- D) B — threat hunters never perform containment actions unilaterally

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect as stated: Immediate isolation without capturing forensic evidence and without involving the IR team is a unilateral action that may destroy valuable evidence and bypass the proper escalation process. The hunting analyst does not own the containment decision. Why B is incorrect: Allowing an active, confirmed C2 beacon to continue operating for 24 more hours exposes the organization to significant additional risk — data exfiltration, lateral movement, additional persistence mechanisms. Intelligence collection value does not justify this risk extension. The correct balance is forensic preservation before, not delayed containment. Why C is correct: This answer correctly identifies the sequence: preserve forensic evidence (memory image captures the injected code, active connections, and volatile artifacts), escalate to the IR team with all findings, and let the IR team make the containment decision. The hunter's role is detect and escalate, not independently decide containment timing. The IR team has organizational authority and context to make the isolation call. Why D is incorrect: While threat hunters generally do not perform containment actions, this is not an absolute rule about 24 additional hours of delay. The correct principle is escalate immediately, not delay for intelligence.

---

## Question 16

A CySA+ question presents a scenario where an analyst discovers that the company's AWS S3 bucket containing customer data is publicly accessible — anyone on the internet can download its contents without authentication. Which CySA+ domain does the analyst's remediation and reporting work most directly fall under, and what is the correct immediate technical action?

- A) Domain 1: Security Operations — continue monitoring with GuardDuty for active exploitation
- B) Domain 2: Vulnerability Management — remediate by enabling S3 Block Public Access on the bucket and reporting the misconfiguration through the vulnerability management program
- C) Domain 3: Digital Forensics — acquire a forensic image of the S3 bucket before making changes
- D) Domain 4: Reporting — brief the board on the misconfiguration before taking any technical action

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Monitoring for active exploitation when you know the bucket is publicly accessible is insufficient. Active exploitation may already be occurring silently — monitoring doesn't reduce the ongoing risk. Why B is correct: A publicly accessible S3 bucket is a cloud misconfiguration — a vulnerability in the configuration of a cloud resource. Remediating misconfigurations falls under Vulnerability Management (Domain 2). The immediate technical action is to enable S3 Block Public Access, which overrides all bucket and object-level public access settings instantly. This is the AWS-recommended immediate remediation for accidental public exposure. The misconfiguration then flows through the vulnerability management tracking process for root cause and recurrence prevention. Why C is incorrect: Digital forensics involves collecting and preserving evidence from compromised systems. Remediating a misconfiguration is an operational action, not a forensic investigation. A forensic approach would delay the remediation and extend the exposure window. Why D is incorrect: Board briefing before technical remediation creates an unnecessary delay while the bucket remains publicly readable. Remediate first, then report through appropriate channels. The "report before acting" trap is a common distractor on CySA+ exam questions — the answer almost always is to take the technical action first, then report.

---

## Question 17

A security analyst calculates their organization's vulnerability program metrics: mean time to remediate (MTTR) for Critical vulnerabilities is 24 days against a 15-day SLA. The analyst wants to identify the root cause of the SLA breach. Which data analysis approach would most effectively identify where in the remediation pipeline the delay occurs?

- A) Scan more frequently — daily scans will find vulnerabilities earlier and improve MTTR
- B) Break down the total remediation time into pipeline stages (discovery-to-ticket creation, ticket-creation-to-assignment, assignment-to-patch-deployment, deployment-to-verification) and measure average time in each stage to identify the bottleneck
- C) Lower the severity threshold — re-classify some Critical vulnerabilities as High to reduce the number of Criticals in the SLA window
- D) Exclude vulnerabilities on legacy systems from MTTR calculations, since they cannot be patched

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Scanning frequency affects how quickly new vulnerabilities are discovered but does not accelerate the remediation pipeline. If the bottleneck is patch deployment, scanning more often has no effect on MTTR for already-discovered vulnerabilities. Why B is correct: A 24-day average MTTR against a 15-day SLA means 9 days of excess time are being consumed somewhere in the pipeline. Without stage-by-stage analysis, the analyst cannot determine whether the delay is in initial ticket creation (operational inefficiency), assignment routing (ticketing process), patch acquisition and testing (change management), deployment (infrastructure constraint), or post-deployment verification (scan scheduling). Breaking the pipeline into measurable stages and measuring each identifies the actual bottleneck, enabling targeted process improvement. Why C is incorrect: Reclassifying Critical vulnerabilities to reduce the SLA metric is metric manipulation, not program improvement. The actual risk does not change; only the measurement changes. This is an audit failure and a governance violation. Why D is incorrect: Excluding legacy systems from MTTR calculations hides a real risk. Legacy systems with unpatched critical vulnerabilities are often the highest-risk assets. If they cannot be patched, they require compensating controls and exception tracking — not exclusion from the program.

---

## Question 18

On the CySA+ exam, a question involves a scenario where a junior analyst has discovered what appears to be active data exfiltration and asks the senior analyst: "Should I block the attacker's IP address at the firewall right now?" Which response reflects the correct CySA+ exam reasoning?

- A) Yes — block the IP immediately to stop the exfiltration
- B) No — blocking the IP is a network team responsibility, not an analyst responsibility
- C) It depends on the IR team's containment decision — first notify the IR team lead with your findings, preserve evidence of the active connection, and execute the block only if the IR team authorizes it as part of the containment strategy
- D) No — IP blocks are ineffective because attackers change their IP addresses immediately

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Unilateral IP blocking without IR team authorization bypasses the incident response process, may alert the attacker to change tactics, may block legitimate traffic if the IP is shared infrastructure, and denies the IR team the opportunity to monitor the connection for additional intelligence. Why B is incorrect: Analysts often do perform firewall rule changes as part of authorized containment actions. Saying it is always outside analyst responsibility is false. The issue is authorization and coordination, not role definition. Why C is correct: This answer correctly identifies the process: document and preserve evidence of the active connection (volatile evidence that may be needed for forensics), escalate immediately to the IR team lead with specific findings, and execute the block only under IR team authorization. The IR team may choose to monitor the connection for additional intelligence, sinkhole the traffic, or implement a coordinated multi-system containment rather than a single IP block. Why D is incorrect: While it is true that sophisticated attackers may rotate infrastructure, IP blocking does disrupt current exfiltration. Effectiveness is not zero. The reason to delay unilateral blocking is IR process coordination, not effectiveness doubt.

---

## Question 19

A CySA+ candidate studies the relationship between the Pyramid of Pain and effective threat intelligence. Which statement correctly applies the Pyramid of Pain concept to detection and response strategy?

- A) Blocking IP addresses is the highest-value defensive action because IP addresses are the most stable attacker attribute
- B) Indicators at the top of the pyramid (TTPs — attacker tools, techniques, and procedures) are the hardest for attackers to change; detections based on TTPs are therefore the most durable and force the highest cost on adversaries
- C) File hash-based detection is superior to all other detection methods because hashes uniquely identify malicious files
- D) The Pyramid of Pain applies only to nation-state threat actors, not to commodity cybercriminal groups

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: The Pyramid of Pain places IP addresses at the bottom (trivial to change). IP blocking is the lowest-value defensive action because an attacker can change their IP address in minutes with minimal effort. Why B is correct: David Bianco's Pyramid of Pain places TTPs at the apex. TTPs represent how an attacker operates — their preferred techniques, tooling choices, and procedural habits. These are the hardest attributes for attackers to change because changing TTPs requires retraining, re-tooling, and adapting operational patterns — a significant investment. Detection rules that identify attacker behaviors (e.g., "Excel spawning PowerShell with encoded arguments") remain effective even as the attacker changes their IP addresses, domains, and file hashes. This is precisely why TTP-based hunting and TTP-based detection rules are valued over IOC-based approaches. Why C is incorrect: File hashes are near the bottom of the Pyramid of Pain — trivially easy to change by modifying a single byte of the malicious file (polymorphic malware). Hash-based detection is the least durable method. Why D is incorrect: The Pyramid of Pain applies to all adversary categories. The concept of response cost vs. detection durability is universal across nation-state, cybercriminal, and hacktivist actors.

---

## Question 20

After completing all 16 modules of CIS-4332, a student is asked to describe the relationship between the five core analyst disciplines covered in the course. Which statement best describes how these disciplines form an integrated security operations capability?

- A) The five disciplines are independent — proficiency in one provides no advantage in the others
- B) Threat intelligence feeds vulnerability management, which drives hardening; log analysis detects attacker activity that both intelligence and forensics refine; incident response coordinates containment while automation multiplies analyst capacity across all functions — together they form a continuous improvement cycle
- C) Incident response is the most important discipline and the others are support functions with minimal direct value
- D) Automation will eventually replace all five disciplines, making analyst skill development unnecessary

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: The disciplines are deeply interdependent. A threat hunt finding generates detection rules for the SIEM (log analysis). An incident investigation produces IOCs that feed threat intelligence. Vulnerability management findings identify the attack surface that threat hunters should prioritize. The disciplines reinforce each other in a continuous cycle. Why B is correct: This answer describes the actual integration. Threat intelligence (knowledge of adversary TTPs) directs both vulnerability management (patch what attackers exploit) and threat hunting (hunt for what attackers do). Log analysis is the data layer that feeds both SIEM detection and forensic investigation. Incident response is the process that coordinates the response function and feeds lessons learned back to all other disciplines. Automation (SOAR, scripting) increases the throughput and speed of each function without replacing the analyst. Together they form a security operations lifecycle, not a collection of independent activities. Why C is incorrect: Incident response without effective detection (log analysis, threat intelligence) would respond to incidents it never discovers. Without vulnerability management, incidents caused by known patched vulnerabilities recur. Each discipline is essential. Why D is incorrect: Automation requires humans to design, configure, validate, and improve it. Automation bias — over-trusting automated outputs — is a documented failure mode in security operations. Analyst skill is required to build, maintain, and critically evaluate automated systems.
