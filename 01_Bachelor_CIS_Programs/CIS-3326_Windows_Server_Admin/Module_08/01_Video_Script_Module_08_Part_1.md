# Video Script: Module 08 — Group Policy Objects (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Introduction

Welcome back to CIS-3326 Windows Server Administration.

I am Professor Nash. Module 08 is about Group Policy — the mechanism that lets
a single administrator enforce settings across thousands of computers and users
in a Windows domain.

Every time a Windows computer starts up or a user logs on in a domain
environment, Group Policy runs silently in the background, applying settings that
were configured centrally on a domain controller. Understanding how Group Policy
works, processes, and is inherited is one of the most important skills for any
Windows Server administrator.

Part 1 covers the concepts, architecture, and processing order. Part 2 covers
the hands-on creation, configuration, and troubleshooting using the GUI and
PowerShell.

---

## Section 1: What Is a Group Policy Object?

A **Group Policy Object (GPO)** is a collection of settings stored in Active
Directory and the SYSVOL folder on domain controllers. These settings control the
behavior of users and computers in the domain.

GPOs have two primary sides:

- **Computer Configuration** — settings that apply to the computer regardless
  of who is logged on. These are applied during computer startup.

- **User Configuration** — settings that apply to the logged-on user regardless
  of which computer they use. These are applied at user logon.

A single GPO can contain both Computer and User Configuration settings
simultaneously.

GPO settings fall into three categories:

- **Administrative Templates** — registry-based settings that control the Windows
  interface, applications, and system behavior. Thousands of settings are
  available here.

- **Security Settings** — account policies (password length, lockout), audit
  policies, User Rights Assignments, and security options.

- **Software Installation** — MSI-based software deployment to computers or users
  (though this is largely replaced by tools like Intune in modern environments).

---

## Section 2: Where GPOs Are Stored

Understanding where GPO data is stored is important for both troubleshooting and
exam questions.

A GPO is actually stored in **two** locations:

**Active Directory** — The Group Policy Container (GPC). This is an AD object
that holds metadata: the GPO's unique identifier (a GUID), version numbers, and
settings for WMI filters. This is what you see when you look at a GPO in the
Active Directory database.

**SYSVOL** — The Group Policy Template (GPT). This is a folder on every domain
controller's SYSVOL share that holds the actual policy settings files —
Administrative Template settings, scripts, and security templates.

Both components must be present and in sync for a GPO to function correctly. If
they get out of sync (a common replication issue), Group Policy clients may apply
outdated settings or fail to apply the GPO entirely.

SYSVOL is replicated between domain controllers using **DFS Replication (DFSR)**
in Windows Server 2008 R2 and later environments, replacing the older File
Replication Service (FRS).

---

## Section 3: Linking GPOs to the Directory

Creating a GPO does not automatically apply it. A GPO must be **linked** to a
container before it takes effect.

The containers you can link a GPO to are:

- **Site** — applies to all computers in an Active Directory site, regardless of
  domain. Rarely used because sites span multiple domains.

- **Domain** — applies to all objects in the entire domain. Used for domain-wide
  settings like password policies (though Fine-Grained Password Policies are
  preferred in modern environments).

- **Organizational Unit (OU)** — applies to all user and computer objects within
  the OU and any child OUs (unless blocked). This is the most common and
  flexible linking point.

One GPO can be linked to multiple containers. One container can have multiple
GPOs linked to it. The order in which multiple GPOs are listed in a container
determines their priority — more on that shortly.

---

## Section 4: Policy Processing Order — LSDOU

This is one of the most tested concepts in Group Policy. The order in which
GPOs are processed is remembered with the acronym **LSDOU**:

- **L** — Local Group Policy (the local computer's own policy, applied first)

- **S** — Site (AD site-linked GPOs applied next)

- **D** — Domain (domain-linked GPOs applied next)

- **O** — OU (OU-linked GPOs applied last, with parent OUs before child OUs)

**Why does the order matter?** When the same setting exists in multiple GPOs,
the last writer wins. GPOs processed later in the LSDOU chain override GPOs
processed earlier.

So if the Domain GPO sets the desktop wallpaper to the university logo, and a
child OU GPO sets it to a department-specific image, the OU policy wins because
it is processed last.

Within a single OU with multiple GPOs linked, the GPO with the **lower link
order number** (higher in the list in Group Policy Management Console) has the
highest priority and is processed last, overriding GPOs with higher numbers.

---

## Section 5: Inheritance, Enforcement, and Block Inheritance

By default, GPO settings flow down from parent OUs to child OUs through
**inheritance**. A GPO linked to the domain applies to all OUs below it unless
overridden.

Two mechanisms alter this default behavior:

### Block Inheritance

Applied to an OU, Block Inheritance prevents GPOs from parent containers
(domain or parent OUs) from applying to that OU. This is useful for OUs that
need completely separate policy — for example, a `Kiosks` OU that should not
receive the standard user desktop restrictions.

**Block Inheritance does not block Enforced GPOs** — which brings us to the
second mechanism.

### Enforced (No Override)

Applied to a **GPO link**, Enforced means this GPO's settings will apply
regardless of any Block Inheritance settings below it. An Enforced GPO always
wins.

Use Enforced sparingly — typically only for security-critical or compliance
settings that must apply everywhere without exception.

**Priority summary:** Enforced GPO from the domain > Block Inheritance on an OU
> standard OU GPOs.

---

## Section 6: Resultant Set of Policy (RSoP)

When a computer has many GPOs from different levels — Local, Site, Domain,
multiple OUs — it can become very difficult to reason about what the actual
effective policy will be.

**Resultant Set of Policy (RSoP)** tools let you see the combined effective
policy after all GPOs have been evaluated.

There are two RSoP modes:

**Planning Mode** — simulates what policy a user or computer would receive
without them actually logging on. Useful for testing "what if" scenarios before
deploying a new GPO.

**Logging Mode** — queries the actual applied policy on a computer that has
already processed Group Policy. Shows exactly which settings are in effect and
which GPO was the "winner" for each setting.

The primary tool for RSoP in modern environments is **gpresult**:

```powershell
# View RSoP summary for the current user and computer
gpresult /r

# View RSoP in HTML format — much more readable
gpresult /h C:\GPOReport.html

# View RSoP for a specific user on a remote computer
gpresult /s RemotePC /u CORP\jsmith /r
```

The `gpresult /h` HTML report is the most useful for troubleshooting — it shows
every applied GPO, every winning policy setting, and the source GPO for each.

---

## Section 7: Loopback Processing

Standard Group Policy applies Computer Configuration at startup and User
Configuration at logon. The User Configuration follows the user — it comes from
the GPOs linked to the OU where the user account lives.

**Loopback Processing** changes this behavior for special-purpose computers like
kiosks, terminal servers, or lab workstations where you want the computer's
location to determine the user policy, not the user's location.

There are two loopback modes:

**Merge mode** — The computer's User Configuration settings are added to the
user's normal User Configuration settings. If there is a conflict, the computer's
settings win.

**Replace mode** — The computer's User Configuration settings completely replace
the user's normal User Configuration settings. The user's OU-based User
Configuration is discarded entirely.

**Use case:** You have a `PublicKiosks` OU. You link a GPO to that OU with
loopback processing in Replace mode. Any user who logs on to a kiosk computer
in that OU receives only the kiosk-specific User Configuration settings,
regardless of which OU their user account lives in.

---

## Section 8: Common Security Policies in Group Policy

Let us review the most commonly configured security settings:

**Account Policies** (under Computer Configuration > Windows Settings > Security
Settings > Account Policies):

- **Password Policy** — minimum length, complexity, maximum age, history count.

- **Account Lockout Policy** — threshold (number of failed attempts), lockout
  duration, observation window.

**Security Options** (under Computer Configuration > Windows Settings > Security
Settings > Local Policies > Security Options):

- Interactive logon messages (legal notices shown at logon).

- Disabling the storage of LAN Manager hash values.

- Renaming the local Administrator account.

**User Rights Assignment:**

- Allow logon locally, deny logon through Remote Desktop Services.

- Manage auditing and security logs.

**Administrative Templates — User Configuration:**

- Prevent access to Control Panel and PC Settings.

- Remove Run from the Start menu.

- Disable the command prompt.

- Configure folder redirection for Desktop, Documents, AppData.

---

## Wrap-Up: Part 1 Summary

Let us review what we covered in Part 1:

- A GPO is a collection of settings split into Computer Configuration and
  User Configuration, stored in both Active Directory (GPC) and SYSVOL (GPT).

- GPOs must be linked to a Site, Domain, or OU before they take effect.

- LSDOU is the processing order: Local → Site → Domain → OU. Later-processed
  GPOs win when settings conflict.

- Block Inheritance prevents parent GPOs from applying to an OU. Enforced
  overrides Block Inheritance.

- RSoP tools — especially `gpresult /h` — reveal the effective policy on any
  computer or user.

- Loopback Processing (Merge and Replace modes) controls whether the user's
  OU or the computer's OU determines the User Configuration settings applied.

- Common security policies cover password policies, account lockout, security
  options, user rights, and Administrative Template restrictions.

In Part 2, we will create GPOs in the Group Policy Management Console, link
them to OUs, configure security and user restriction settings, and use
`gpresult` and `Get-GPOReport` to verify results.

See you in Part 2.
