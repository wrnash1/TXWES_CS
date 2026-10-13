# Discussion Forum: Module 16 — Capstone Reflection

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

## Overview

This is the final discussion forum for CIS-3326. The prompts below ask you to
reflect on the full arc of the course — what you have learned, how the
technologies connect to each other, and where your skills will take you next.
Technical depth is still expected, but this discussion also values genuine
professional reflection.

---

## Prompt 1 — Technology Integration: Building the Stack

Windows Server administration is not a collection of isolated skills. The
technologies from this course form layers that depend on each other. A domain
controller running AD DS depends on DNS. Group Policy requires AD. Remote
Desktop Services requires WinRM for management. Hyper-V hosts benefit from
Storage Spaces for virtual disk storage. DSC can enforce all of the above.

For your initial post, address all three points below.

- Choose any two technologies from different modules in this course — for
  example, Hyper-V (Module 12) and Storage Replica (Module 13), or JEA
  (Module 14) and DSC (Module 15) — and explain how they work together in a
  real-world deployment scenario. Describe a specific configuration where one
  technology would be incomplete or unreliable without the other.
- During the course, which single topic was the most difficult for you to
  understand at first, and what helped you eventually grasp it? Be specific —
  reference a concept, a lab step, or a command.
- Looking at your career goals, identify one role in IT infrastructure or
  cloud operations that this course has prepared you for. Name the role,
  explain which modules are most directly applicable, and identify one
  certification beyond this course that would strengthen your candidacy for
  that role.

Post length: 175 to 250 words.

---

## Prompt 2 — Security in Depth: Layered Defense

Module 14 introduced security technologies individually. This prompt asks you
to combine them into a coherent defense strategy.

For your initial post, address all three points below.

- A university IT department manages 400 servers across academic and
  administrative divisions. Privileged access is currently handled through
  shared local administrator accounts with the same password on all servers.
  Design a layered privileged access strategy using at least three technologies
  from Module 14 (LAPS, JEA, Credential Guard, WFAS, audit logging). For each
  technology, state what threat it mitigates and how it interacts with the
  others.
- Consider an attacker who has obtained domain user credentials through
  phishing. Trace the path of an attempted lateral movement attack across the
  environment you designed and identify at least two points where your controls
  would detect or stop the attacker.
- What is one limitation of your proposed design — a threat or scenario it
  does not fully address — and what additional control or monitoring capability
  would you add to close that gap?

Post length: 200 to 250 words.

---

## Prompt 3 — Automation and Compliance: The Future of Administration

PowerShell and DSC represent a shift in how Windows Server infrastructure is
managed — from manual configuration to declared, enforced, and auditable state.
This prompt asks you to reason about where that shift is heading.

For your initial post, address all three points below.

- An organization currently uses manual procedures documented in runbooks to
  configure new servers. A junior administrator follows the runbook steps,
  but configuration drift accumulates over months as patches, incidents, and
  emergency changes modify servers without updating the runbook. Describe how
  replacing the runbook-based process with DSC configurations under
  `ApplyAndAutoCorrect` mode would change the compliance posture of the
  environment. What does the organization gain, and what new operational
  discipline does it require?
- DSC is a Push-mode or Pull-mode technology. For an organization with 800
  servers across five data centers, make the case for Pull mode over Push mode.
  What infrastructure is required, and what operational benefit justifies the
  added complexity?
- Automation introduces its own risks: a misconfigured DSC resource that
  disables a critical service can propagate across thousands of nodes before
  anyone notices. What testing and deployment strategy (for example, Test
  nodes, Canary deployments, Audit mode) would you use to validate DSC
  configurations before applying them to production?

Post length: 200 to 250 words.

---

## Peer Response Requirements

Read at least two classmates' posts and reply to each. Each reply must be at
least 60 words and must add substantive technical content or professional
insight — do not simply agree or echo what they wrote.

Suggested approaches for peer replies:

- Challenge the technology pairing in Prompt 1 by suggesting a different
  integration point they did not consider.
- Strengthen the security design in Prompt 2 by identifying a detection gap
  and suggesting a specific event ID or log source that would catch the
  attack they described.
- Offer an alternative DSC deployment strategy in Prompt 3 — for example,
  if they proposed a Pull Server, compare it to Azure Automation DSC as an
  alternative.

---

## Grading Rubric — 20 Points Total

Initial post — 12 points:

- 10 to 12 points: All three sub-points fully addressed with correct technical
  terminology, specific technology names, and clear reasoning grounded in
  course content. Meets word count.
- 7 to 9 points: Most sub-points addressed but one is thin or missing specific
  technical content.
- 4 to 6 points: Two or more sub-points are vague, technically incorrect, or
  do not engage with course material.
- 0 to 3 points: Post is incomplete, missing, or demonstrates little
  understanding of the topics.

Peer responses — 8 points:

- 7 to 8 points: Two or more substantive replies that add new technical
  content, identify gaps, or extend the technical discussion meaningfully.
- 4 to 6 points: Two replies submitted but one is superficial or fewer than
  60 words.
- 2 to 3 points: Only one peer reply submitted.
- 0 to 1 point: No peer replies, or replies are non-substantive.

---

## Due Dates

- Initial post: Wednesday at 11:59 PM
- Peer responses: Sunday at 11:59 PM

---

## Closing Note

This is the last assignment of CIS-3326. The technologies you have studied —
Active Directory, Group Policy, Hyper-V, Storage Spaces, security enforcement,
and PowerShell automation — are the foundation of Windows Server administration
in production environments. The certification exam ahead tests whether you can
apply these concepts in realistic scenarios.

Best of luck on your exam and in your career.
