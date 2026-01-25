# Windows Server Concepts (Administrative Lab)

**Note**: These labs focus on the *concepts* of Windows Server administration using PowerShell and cross-platform management tools available on Linux.

## Lab 1: PowerShell Core Fundamentals
**Objective**: Familiarize with the PowerShell syntax (cmdlets).

1.  **Installation**: If not installed, PowerShell can be run on Fedora via `pwsh`.
2.  **Cmdlets**: Use `Get-Command` to search for cmdlets related to "Service".
3.  **Process Management**: Use `Get-Process | Sort-Object CPU -Descending | Select-Object -First 10`.
4.  **Aliases**: What is the PowerShell equivalent of the Linux `ls` command?

## Lab 2: Identity & Access Management (AD Concepts)
**Objective**: Understand Users, Groups, and Organizational Units (OUs).

1.  **Conceptual**: Explain the difference between a Local User and a Domain User in an Active Directory environment.
2.  **Groups**: In PowerShell, research the command `New-LocalGroup`. How is this different from the Linux `groupadd` command?
3.  **Permission Inheritance**: Explain how "Inheritance" works when applying permissions to a folder inside an OU.

## Lab 3: Remote Administration and Services
**Objective**: Managing servers remotely.

1.  **WinRM/SSH**: Explain why a modern Windows Administrator might choose SSH over WinRM for remote management.
2.  **Service Control**: Practice starting and stopping a background service (like `crond` or `sshd`) using the PowerShell `Start-Service` and `Stop-Service` cmdlets.
3.  **IIS vs. Apache**: Compare the roles of Internet Information Services (IIS) on Windows with the Apache or Nginx web servers on Linux.

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.
