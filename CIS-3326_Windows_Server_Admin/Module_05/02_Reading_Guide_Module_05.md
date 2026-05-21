# Reading Guide: Module 05 - Group Policy Objects (GPOs) - Creation and Management

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 05 – Group Policy Objects (GPOs): Creation and Management**! This week's study material covers how to create, link, filter, and troubleshoot Group Policy — the primary mechanism for centrally managing user and computer settings across a Windows domain. GPO management is a core competency on the AZ-800 exam and one of the most frequently used tools in daily Windows Server administration.

As a student, you will learn the LSDOU processing order, how WMI filters and Security Filtering target GPOs to specific machines, and how to diagnose GPO application failures using `gpresult` and Group Policy Results. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Group Policy Object (GPO)**: A collection of policy settings stored as two components — a Group Policy Container (GPC) in AD DS and a Group Policy Template (GPT) in SYSVOL. GPOs are linked to sites, domains, or OUs and applied to the computers and users in those containers.
* **LSDOU Processing Order**: GPOs are applied in the order Local → Site → Domain → Organizational Unit. When settings conflict, the last policy applied wins — meaning OU-linked GPOs override Domain-linked GPOs unless the "Enforced" flag is set.
* **Enforced vs. Block Inheritance**: Setting a GPO link to "Enforced" prevents lower-level OUs from overriding it. Setting an OU to "Block Inheritance" prevents higher-level GPOs from flowing down to it. An Enforced GPO always wins over Block Inheritance.
* **Security Filtering**: By default, the "Authenticated Users" group is in the Security Filtering list, meaning the GPO applies to all authenticated domain objects. Removing a group or adding a "Deny" access control entry (ACE) prevents specific users or computers from receiving the policy.
* **WMI Filter**: A WMI query attached to a GPO that causes the policy to apply only to machines that return TRUE from the query. Used to target specific OS versions, hardware configurations, or installed software without creating separate OUs.
* **gpupdate /force**: A command run on a client machine to immediately refresh both User Configuration and Computer Configuration policies, rather than waiting for the default 90-minute background refresh interval.

---

### 2. Certification Exam Tips

* **LSDOU order and last-writer-wins**: AZ-800 scenario questions frequently set up conflicting GPO settings at different levels and ask which setting takes effect. Remember: OU wins over Domain wins over Site wins over Local — unless an Enforced GPO is in play.
* **gpresult /r vs. gpresult /h**: `gpresult /r` outputs a quick text summary of applied GPOs for the current user and computer. `gpresult /h report.html` generates a full HTML report with detailed Resultant Set of Policy (RSoP) data. Know when to use each for troubleshooting.
* **Loopback Processing**: When Loopback Processing is enabled in Replace or Merge mode, the Computer Configuration GPOs also apply User Configuration settings based on the machine's OU location, not the user's OU. This is critical for kiosk and shared-computer scenarios.
* **Microsoft Learn Reference**: Review Group Policy architecture and troubleshooting at [Microsoft Learn – Group Policy Overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11)) for detailed coverage of all settings tested on AZ-800.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the Group Policy documentation at [Microsoft Learn: Group Policy Overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11)). Focus on GPO processing order, filtering, and the `gpresult` and `gpupdate` command references.
* **Required Video:** Watch the video lecture on **Group Policy Objects** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will create a GPO using the Group Policy Management Console (GPMC), link it to an OU, configure a Computer Configuration setting, and verify application on a domain-joined machine using `gpresult /r`. You will also experiment with Security Filtering to restrict GPO application to a specific group.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the Group Policy overview at [Microsoft Learn: Group Policy Overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11)).
* [ ] Watch the video lecture on **Group Policy Objects** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
