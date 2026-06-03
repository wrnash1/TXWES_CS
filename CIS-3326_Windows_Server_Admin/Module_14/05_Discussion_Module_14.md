# Discussion Forum: Module 14 — Windows Server Security

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Microsoft Windows Server Administration

---

## Discussion Prompt

Security is ultimately about making attacker success expensive and unlikely. In this discussion, you apply the module's security technologies to real-world attack scenarios and defend architectural decisions with technical evidence.

---

## Primary Post (Due by Thursday)

Respond to **one** of the following prompts in 200–300 words. Clearly state which prompt you are answering at the top of your post.

---

### Prompt A — Lateral Movement Defense

A penetration tester has been granted access to a single low-privilege workstation in your organization's network. Their goal is to reach the SQL Server cluster. Your organization has Windows Defender, WFAS, Credential Guard, and LAPS deployed.

Address the following in your post:

- Walk through at least three specific steps the tester would attempt and explain which security control blocks each step.
- At which point in the attack chain does Credential Guard specifically intervene, and what does it prevent the tester from doing?
- At which point does LAPS specifically intervene, and what does it prevent?
- Is there any step in this attack chain that none of the deployed controls address? If so, what additional control would you recommend?

---

### Prompt B — JEA Design for a Helpdesk Team

Your organization wants to give a 12-person helpdesk team the ability to restart specific Windows services and view event logs on production servers, without giving them full administrative access. You have been asked to design a JEA solution.

Address the following in your post:

- What commands would you include in the Role Capability File for this helpdesk role?
- Would you use a virtual account or a Group Managed Service Account (gMSA) for this endpoint? Justify your choice.
- How does the `NoLanguage` mode in JEA prevent a clever helpdesk operator from escalating privileges by writing a clever PowerShell script?
- What compliance benefit does JEA transcript logging provide for a regulated industry like healthcare or finance?

---

### Prompt C — Defender and ASR in a Regulated Environment

A financial services company is rolling out Windows Defender with Attack Surface Reduction rules to all 800 Windows servers. The security team wants to enable ASR rules immediately in Block mode. The server operations team objects, saying this will break production applications.

Address the following in your post:

- What is Attack Surface Reduction, and how does it differ from traditional signature-based antivirus detection?
- Why is it important to deploy ASR rules in Audit mode first, and what information does Audit mode provide?
- Describe the process for transitioning from Audit mode to Block mode for a specific ASR rule.
- How would you handle the operations team's concern about production application compatibility during the rollout?

---

## Reply Posts (Due by Sunday)

Write substantive replies to **two** classmates. Each reply should be 100–150 words and include at least one of the following:

- Identify a gap or additional attack vector in a classmate's lateral movement analysis
- Propose a JEA role capability enhancement with specific cmdlet examples
- Challenge or extend the ASR deployment approach with a specific scenario
- Connect the security topic to storage (Module 13) or PowerShell automation (Module 15)

---

## Grading Criteria

Grades are based on the following point distribution:

- Primary post addresses all prompt sub-questions: 40 points
- Technical accuracy and correct module terminology: 25 points
- Analytical depth — reasoning through trade-offs, not just listing features: 15 points
- Two substantive reply posts: 20 points
- Total: 100 points

---

## Tips for a Strong Post

For Prompt A, the most insightful posts are those that identify the gap — the step that current controls do NOT address. Think about social engineering, keyloggers, or scenarios where the attacker already has valid credentials.

For Prompt B, specificity wins. Instead of saying "helpdesk can restart services," write: `Restart-Service -Name "W32Time","Spooler"` — demonstrate you know what goes in a Role Capability file.

For Prompt C, look up at least one real-world case where an ASR rule in Block mode caused an unexpected production issue. Real examples make security discussions much more concrete.

---

## Looking Ahead

Module 15 covers PowerShell Automation and Desired State Configuration. Notice that all five security technologies in Module 14 can be deployed and enforced at scale using PowerShell and DSC. As you complete this discussion, think about how you would automate the deployment of JEA endpoints or LAPS configuration across hundreds of servers using DSC resources.
