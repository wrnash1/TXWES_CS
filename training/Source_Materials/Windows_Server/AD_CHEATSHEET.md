# Windows Server Concepts - Active Directory (AD) Cheat Sheet

## Key Terms
- **Domain**: A logical group of network objects (users, computers, groups) that share the same AD database.
- **Domain Controller (DC)**: The server that responds to security authentication requests.
- **Forest**: A collection of one or more AD trees.
- **Organizational Unit (OU)**: A container within a domain used to organize objects and apply Group Policies (GPOs).
- **Group Policy Object (GPO)**: A collection of settings that define what a system looks like and how it behaves for a defined group of users.

## PowerShell Cmdlets for AD (Conceptual)
- `Get-ADUser`: Get one or more AD users.
- `New-ADUser`: Create a new AD user.
- `Set-ADAccountPassword`: Set the password for an AD account.
- `Get-ADGroup`: Get one or more AD groups.
