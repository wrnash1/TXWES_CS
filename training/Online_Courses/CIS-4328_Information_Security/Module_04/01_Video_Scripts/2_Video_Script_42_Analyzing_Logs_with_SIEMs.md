### 2. Video Script 4.2: Analyzing Logs with SIEMs
**Estimated Duration:** 7 minutes
**Visual:** Screencast of a SIEM dashboard (like Splunk or Microsoft Sentinel) showing a spike in failed login attempts.
**[Alt-text: A dark-themed dashboard with various charts. One prominent line graph shows a massive spike in 'Failed Login Attempts' originating from foreign IP addresses. A red alert banner reads 'Potential Brute Force Attack'.]**
**Audio:** "A firewall generates logs. An antivirus generates logs. Windows generates logs. A large enterprise generates millions of log events every hour. No human can read all of that. We use a SIEM—a Security Information and Event Management system. The SIEM ingests all these logs, normalizes them into a common format, and uses correlation rules to spot attacks. If the firewall sees traffic from Russia, and Active Directory sees 500 failed logins for the Admin account, the SIEM connects the dots and fires an alert for a Brute Force attack."

---
