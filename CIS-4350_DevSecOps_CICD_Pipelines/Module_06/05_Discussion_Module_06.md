# Discussion Forum: Module 06 - SAST: Static Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Overview

This discussion applies Module 06 concepts — SAST mechanics, tool selection, finding analysis, false positive management, and pipeline integration — to realistic engineering scenarios. Read all three scenarios and respond to the one assigned to your group or the one of your choice. Initial post due Wednesday at 11:59 PM; peer responses due Sunday at 11:59 PM.

---

## Scenario A: The Alert Fatigue Crisis

A DevSecOps engineer integrates Semgrep with the `p/owasp-top-ten` rule pack into a mature Python/Django application's CI/CD pipeline in breaking mode (exit-code 1) on day one. The initial scan produces 1,243 findings across 847 files. Every pull request now fails immediately, development has effectively stopped, and the development team is furious. The security team insists all findings must be fixed before any new code merges. The development team argues the scanner is "useless noise" and wants it removed.

In 175-225 words, address the following: Identify the specific process error that created this situation and explain what the correct rollout strategy should have been. Propose a remediation plan that satisfies both teams' concerns — how do you restore development velocity without abandoning security scanning? Describe the specific pipeline configuration change that implements your plan. Finally, explain how you would prioritize which of the 1,243 findings to remediate first, and why that prioritization criterion is the correct one for a DevSecOps team.

---

## Scenario B: The False Positive Decision

A financial services company's SAST pipeline flags the following finding as a Critical SQL injection on every pipeline run:

```text
Rule: python.django.security.injection.sql.sql-injection
Line 47: raw_query = User.objects.raw(f"SELECT * FROM auth_user WHERE department = '{dept}'")
Severity: ERROR
```

A developer reviews line 47 and discovers that `dept` is not user-controlled — it is hardcoded from a `settings.py` configuration file that cannot be modified by end users. The developer wants to suppress the finding. The security lead argues that suppressing any Critical finding sets a bad precedent.

In 175-225 words, address the following: Evaluate both positions — is this a legitimate false positive, and is suppression appropriate? Describe the technical standard a confirmed false positive must meet before suppression is justified. Write the exact suppression comment syntax needed in Python/Semgrep. Explain what documentation must accompany the suppression. Propose a process the team should establish to prevent unauthorized suppression of genuine vulnerabilities masked as false positives.

---

## Scenario C: The SAST Tool Selection Dilemma

A healthcare startup is building a Java Spring Boot application that processes patient health records. They need to choose a SAST tool. Option 1: Semgrep Community (free, pattern-matching, fast). Option 2: SonarQube Community (free, quality gates, deeper analysis). Option 3: Checkmarx (commercial, deep taint analysis, expensive). The CTO wants to use Semgrep because it is free and fast. The lead developer argues that for HIPAA-regulated healthcare data, they need Checkmarx's deep taint analysis because Java Spring Boot has complex injection patterns that pattern-matching tools miss.

In 175-225 words, address the following: Evaluate both arguments on their technical merits — what does Semgrep miss in a complex Java Spring Boot application that Checkmarx would catch, and why does this matter for HIPAA compliance? Explain the role of a quality gate (SonarQube feature) and why it is relevant to a regulated healthcare environment. Provide a recommendation that balances security thoroughness with the startup's resource constraints, and justify your recommendation using DevSecOps principles.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

Due Wednesday at 11:59 PM. Your post must be 175-225 words, address all elements of your chosen scenario, and use precise SAST and DevSecOps terminology.

- 5-6 pts: Thoroughly addresses all scenario elements with technical accuracy, clear explanations, and appropriate terminology. Meets the word count.
- 3-4 pts: Addresses most elements but lacks technical depth in one or more areas.
- 0-2 pts: Incomplete, missing, or does not substantively address the scenario.

### Peer Responses (4 Points)

Due Sunday at 11:59 PM. Respond to at least two classmates who chose different scenarios.

- 4 pts: Two substantive responses (at least 50 words each) that add technical depth, propose an alternative approach, or cite a specific concept from the reading guide or lab.
- 2 pts: Only one substantive response, or both are superficial.
- 0 pts: No peer responses submitted.

---

## Professor Nash Note

The SAST finding analysis skill you practiced in the lab maps directly to this discussion. When discussing Scenario B, you must take a specific technical position on whether the finding qualifies as a false positive. Saying "it depends" without criteria is not an acceptable answer on the exam or in practice. A false positive must meet a specific standard: the flagged code pattern cannot, under any foreseeable execution path, reach the sink with attacker-controlled data. Apply that standard explicitly in your response.
