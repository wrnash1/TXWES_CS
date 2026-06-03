# Discussion Forum: Module 12 — Post-Exploitation & Privilege Escalation

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Discussion Prompt

Post-exploitation and privilege escalation represent the phase of an attack where theoretical access becomes demonstrated business impact. A low-privilege foothold on a single web server becomes a critical finding when the tester escalates to root and demonstrates they could have exfiltrated the customer database, pivoted to the domain controller, or dumped every employee's credentials.

Real-world ransomware groups and nation-state actors follow the same post-exploitation methodology covered in this module — not because the techniques are exotic, but because they are reliable and often necessary. The Mimikatz tool has appeared in incident response reports from the NSA, CISA, and major threat intelligence firms because it is the standard tool for Windows credential extraction.

### Initial Post (Due Wednesday at 11:59 PM)

In 200–250 words, address the following:

1. Select one real-world attack campaign or incident (ransomware operation, APT group report, documented breach) where privilege escalation or post-exploitation techniques from this module were used. Examples include: NotPetya (2017), the SolarWinds Orion compromise (2020), the Colonial Pipeline attack (2021), or any named APT report published by Mandiant, CrowdStrike, or Microsoft MSTIC.

2. Identify at least two specific techniques from this module that were used in the attack. Be precise — name the tool or technique (e.g., Mimikatz credential dumping, pass-the-hash lateral movement, unquoted service path escalation) and cite where in the incident report or news coverage this technique is described.

3. Explain how understanding these techniques as a penetration tester would help a defender better detect or prevent the attack. What log sources, security controls, or configurations would have interrupted the attack chain at the privilege escalation stage?

Include at least one citation (news article, CISA advisory, or threat intel report URL).

### Peer Responses (Due Sunday at 11:59 PM)

Write a substantive reply (at least 75 words) to at least two classmates. In each reply, address one of the following:

- Your classmate cited specific tools (e.g., Mimikatz, PsExec, Cobalt Strike). Describe a specific defensive control — a Windows Event ID to monitor, a Group Policy setting, or a security product feature — that would detect or block the tool they described.
- Your classmate described a privilege escalation technique. Add technical detail about the conditions required for that technique to work. What configuration change would make the technique fail?
- Connect the attack campaign your classmate described to a different MITRE ATT&CK technique ID that also applies, explaining why that technique is present in the attack chain.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

- 5–6 pts: Clearly identifies a real attack campaign with specific named techniques from the module. Correctly describes how they apply in the attack context. Provides a meaningful defensive recommendation with specific technical detail. Meets word count. Includes at least one citation.
- 3–4 pts: Identifies an attack and one technique, but the connection is vague or the defensive recommendation is generic (e.g., "keep systems patched"). Missing citation or below word count.
- 0–2 pts: Post is incomplete, does not reference a real attack, or demonstrates minimal engagement with module content.

### Peer Responses (4 Points)

- 4 pts: Responds to two peers with substantive technical additions — specific Event IDs, Group Policy settings, ATT&CK technique IDs, or configuration details.
- 2 pts: Responds to only one peer, or both responses lack technical depth.
- 0 pts: No peer responses submitted by the deadline.

---

## Resources for Finding Real-World Attack Reports

- CISA Known Exploited Vulnerabilities Catalog: cisa.gov/known-exploited-vulnerabilities-catalog
- MITRE ATT&CK: attack.mitre.org (search by technique to find example groups and campaigns)
- Mandiant Threat Intelligence: mandiant.com/resources/blog (free reports on named APT groups)
- Microsoft MSTIC Blog: microsoft.com/en-us/security/blog
- The Hacker News breach coverage: thehackernews.com

---

*End of Module 12 Discussion Forum*
