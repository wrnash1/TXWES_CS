# CIS-3326: Windows Server Administration Labs

## Lab 1: PowerShell Automation for Admins
**Objective**: master the command-line interface for Windows Server management.

1.  **Object Pipeline**: Use PowerShell to list the top 5 processes by memory usage.
2.  **Remote Management**: Explain the requirements for enabling PowerShell Remoting (WinRM).
3.  **Variable Handling**: Write a PowerShell snippet that stores all running services in a variable and then filters for those that are stopped.

## Lab 2: Active Directory (AD) & Group Policy
**Objective**: Understand the infrastructure of a Windows domain.

1.  **User Provisioning**: Write a PowerShell command to create 10 new users with a standard naming convention.
2.  **Group Policy**: Explain the order of GPO application (LSDOU).
3.  **Security Filtering**: How would you apply a GPO to only a specific group of users within an OU?

## Lab 3: Server Roles & Infrastructure
**Objective**: Configure essential network services on Windows Server.

1.  **DHCP/DNS**: Explain the "D" in DORA and how DNS recursion works.
2.  **File Server**: Configure a "Hidden Share" (Admin Share) and explain why it is used.
3.  **IIS**: Install the Web Server (IIS) role using `Install-WindowsFeature` (Conceptual).

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.
