# Quiz: Module 16 - Final Exam Preparation

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A company is deploying a new Windows Server environment. The security team requires that the domain controller OS volumes be encrypted, that only authenticated domain computers can register DNS records, and that remote VPN access must work from networks that block all ports except 443. Which combination of Windows Server features satisfies all three requirements simultaneously?

A) BitLocker TPM-only mode on DCs, DNS secondary zone with no dynamic updates, and PPTP VPN on RRAS.
B) BitLocker TPM + PIN on DCs, AD-integrated DNS zone with Secure-only dynamic updates, and SSTP VPN on RRAS.
C) EFS on the DC OS volume, DNS primary zone with Nonsecure and Secure dynamic updates, and IKEv2 VPN on RRAS.
D) BitLocker with USB Startup Key on DCs, DNS stub zone, and Always On VPN with L2TP/IPsec.

* **Correct Answer:** B) BitLocker TPM + PIN on DCs, AD-integrated DNS zone with Secure-only dynamic updates, and SSTP VPN on RRAS.
* **Distractor Analysis:**
  * *Why A is incorrect:* TPM-only mode encrypts the volume but allows unattended booting without a PIN. PPTP uses port 1723 and GRE protocol 47, both of which are blocked by a firewall that permits only port 443. Only SSTP operates over HTTPS on port 443.
  * *Why C is incorrect:* EFS encrypts individual files per user — it cannot encrypt an OS volume. DNS "Nonsecure and Secure" allows unauthenticated clients to register records, which violates the authenticated-only requirement. IKEv2 uses UDP ports 500 and 4500, which would be blocked.
  * *Why D is incorrect:* A DNS stub zone contains only NS, SOA, and glue records and does not accept dynamic registrations at all — workstations would not be able to register their A records. L2TP/IPsec uses UDP ports 500, 1701, and 4500, which are blocked by the port-443-only firewall.

---

### Question 2

An administrator is troubleshooting Group Policy application on a Windows 11 workstation. A user reports that the desktop background policy configured at the Domain level is not applying, even though the same policy applies correctly on other workstations. The administrator suspects a Security Filtering issue. Which command-line tool produces a detailed report showing which GPOs applied, which were filtered, and why?

A) `gpupdate /force`, which refreshes all GPOs on the workstation and logs the results to the Application event log.
B) `gpresult /h C:\gpreport.html /user username`, which generates an HTML report showing applied and denied GPOs with Security Filtering and WMI Filter details for the specified user.
C) `dcdiag /test:dns`, which tests DNS resolution and AD replication health — the most common cause of GPO application failures.
D) `nltest /dsgetsite`, which identifies the Active Directory site the workstation is assigned to, revealing whether the wrong site GPO is being applied.

* **Correct Answer:** B) `gpresult /h C:\gpreport.html /user username`, which generates an HTML report showing applied and denied GPOs with Security Filtering and WMI Filter details for the specified user.
* **Distractor Analysis:**
  * *Why A is incorrect:* `gpupdate /force` re-applies Group Policy but does not produce a diagnostic report. It would not reveal which GPOs were filtered or why a specific policy failed to apply.
  * *Why C is incorrect:* `dcdiag /test:dns` validates DNS and replication health on domain controllers. While DNS failures can prevent GPO downloads, the scenario indicates other workstations receive the policy correctly, making a DC-wide DNS failure unlikely. The Security Filtering issue is better diagnosed with `gpresult`.
  * *Why D is incorrect:* `nltest /dsgetsite` identifies the AD site for the workstation, which is relevant for troubleshooting site-linked GPO scoping. However, it does not show which GPOs were applied or filtered and does not identify Security Filtering denials.

---

### Question 3

A domain administrator needs to restore 50 user accounts that were accidentally deleted from Active Directory. The AD Recycle Bin is enabled, the accounts were deleted 6 hours ago, and the tombstone lifetime is 180 days. The administrator wants to restore all deleted accounts from the `Users` container in a single operation. Which PowerShell command accomplishes this?

A) `Get-ADObject -Filter {isDeleted -eq $True -and ObjectClass -eq 'user'} -IncludeDeletedObjects | Restore-ADObject`
B) `Get-ADUser -Filter {Enabled -eq $False} | Enable-ADAccount`
C) `ntdsutil "authoritative restore" "restore subtree CN=Users,DC=domain,DC=com" quit quit`
D) `Restore-ADObject -Identity "CN=Users,DC=domain,DC=com" -TargetPath "CN=Users,DC=domain,DC=com"`

* **Correct Answer:** A) `Get-ADObject -Filter {isDeleted -eq $True -and ObjectClass -eq 'user'} -IncludeDeletedObjects | Restore-ADObject`
* **Distractor Analysis:**
  * *Why B is incorrect:* `Get-ADUser -Filter {Enabled -eq $False} | Enable-ADAccount` re-enables disabled accounts — it does not recover deleted objects. Deleted accounts are not returned by `Get-ADUser` without `-IncludeDeletedObjects` and are not simply disabled; they are moved to the Deleted Objects container.
  * *Why C is incorrect:* The `ntdsutil` authoritative restore command is used in Directory Services Restore Mode after a system state backup restore — it is not used for Recycle Bin recovery and would require taking the DC offline. When AD Recycle Bin is enabled, `Restore-ADObject` is the correct mechanism.
  * *Why D is incorrect:* `Restore-ADObject` with `-Identity` pointing to a container DN would attempt to restore the container itself, not enumerate all deleted child objects within it. The correct approach is to use `Get-ADObject` with `-IncludeDeletedObjects` to find all deleted user objects and pipe them to `Restore-ADObject`.

---

### Question 4

An organization uses Pass-Through Authentication (PTA) via Azure AD Connect to synchronize on-premises Active Directory with Azure AD for Microsoft 365 sign-in. After the on-premises AD DS domain controllers go offline for an emergency maintenance window, users report they cannot sign in to Microsoft 365. Which Azure AD Connect configuration change would have allowed users to continue signing in to Microsoft 365 during the on-premises outage?

A) Switch from PTA to Password Hash Synchronization (PHS), which stores a transformed hash of each user's password in Azure AD so authentication can succeed even when on-premises DCs are unreachable.
B) Deploy a second Azure AD Connect server in Active mode, which takes over authentication processing when the primary server goes offline.
C) Enable Azure AD Seamless SSO on the Azure AD Connect server, which stores credentials in the cloud so that sign-in continues without on-premises connectivity.
D) Configure Hybrid Azure AD Join on all workstations, which caches Azure AD tokens locally so users can authenticate to Microsoft 365 during on-premises outages.

* **Correct Answer:** A) Switch from PTA to Password Hash Synchronization (PHS), which stores a transformed hash of each user's password in Azure AD so authentication can succeed even when on-premises DCs are unreachable.
* **Distractor Analysis:**
  * *Why B is incorrect:* Azure AD Connect supports only one Active server at a time; a second server can be deployed in Staging mode as a warm standby for failover, but Staging mode servers do not process PTA authentication. Having a second Azure AD Connect server does not help with on-premises DC outages because PTA still requires a functioning on-premises AD to validate passwords.
  * *Why C is incorrect:* Seamless SSO provides a Kerberos-based single sign-on experience for domain-joined devices on the corporate network — it does not store passwords or authentication credentials in Azure AD and does not enable cloud-only authentication during on-premises outages.
  * *Why D is incorrect:* Hybrid Azure AD Join allows devices to obtain Azure AD tokens, but Microsoft 365 user authentication still depends on the configured sign-in method (PTA in this case). Hybrid Join does not store user password credentials in Azure AD or enable cloud-only sign-in when PTA cannot reach on-premises DCs.

---

### Question 5

An administrator reviewing the AZ-800 exam objectives needs to identify which Windows Server technology best addresses each of the following four scenarios in sequence: (1) providing fault-tolerant DC promotion without shared storage, (2) enabling a single administrative console to manage GPOs across multiple domains, (3) automating the installation of Windows features on 100 servers using a declarative script, and (4) encrypting inter-site AD replication traffic. Which set of technologies correctly maps to all four scenarios?

A) (1) Hyper-V Replica, (2) Active Directory Administrative Center, (3) Windows Server Backup, (4) BitLocker
B) (1) Read-Only Domain Controller (RODC), (2) Group Policy Management Console (GPMC), (3) PowerShell Desired State Configuration (DSC), (4) IPsec via Windows Defender Firewall
C) (1) RODC with Password Replication Policy, (2) Active Directory Sites and Services, (3) PowerShell `Install-WindowsFeature` in a loop, (4) SSTP VPN on RRAS
D) (1) AD DS stretched cluster, (2) GPMC, (3) DSC, (4) SMB Encryption

* **Correct Answer:** B) (1) Read-Only Domain Controller (RODC), (2) Group Policy Management Console (GPMC), (3) PowerShell Desired State Configuration (DSC), (4) IPsec via Windows Defender Firewall
* **Distractor Analysis:**
  * *Why A is incorrect:* Hyper-V Replica replicates VMs between hosts and is not a DC promotion fault-tolerance technology for Active Directory replication. Windows Server Backup creates backups of servers — it does not automate Windows feature installation declaratively. BitLocker encrypts volumes at rest on local machines, not inter-site replication traffic in transit.
  * *Why C is incorrect:* RODC with PRP addresses branch-office security for credential caching but does not inherently provide fault tolerance for DC promotion in the way a writable DC does. `Install-WindowsFeature` in a loop is an imperative script, not a declarative DSC configuration. SSTP VPN is a client VPN protocol on RRAS — it is not used to encrypt AD replication traffic between domain controllers.
  * *Why D is incorrect:* An AD DS stretched cluster requires shared storage and is primarily a high-availability solution for the cluster itself, not a standard DC promotion fault-tolerance pattern. SMB Encryption protects SMB file sharing traffic — it does not encrypt AD replication traffic between domain controllers, which uses LDAP/Kerberos and is secured by IPsec when end-to-end encryption is required.
