# CIS-4328: Fundamentals of Information Systems Security (Security+ Alignment)

## Lab 1: Cryptography & PKI
**Objective**: Implement and verify data confidentiality and integrity.

1.  **AES Encryption**: Use `openssl` to encrypt a message using AES-256-CBC.
2.  **Digital Signatures**: Sign a text file using a private key and verify it with a public key.
3.  **Certificates**: Inspect the SSL certificate of `txwes.edu`. Identify the CA and expiration date.

## Lab 2: Threat Detection & Incident Response
**Objective**: Analyze system logs for signs of compromise.

1.  **Log Analysis**: Search `/var/log/auth.log` (or `journalctl`) for failed SSH login attempts.
2.  **Malware Analysis**: Explain the difference between static and dynamic analysis of a suspicious binary.
3.  **SIEM**: Describe how a SIEM (like Splunk or ELK) aggregates security events from multiple sources.

## Lab 3: Hardening & Compliance
**Objective**: Apply security controls to satisfy industry standards.

1.  **UFW/Firewalld**: Configure the firewall to allow only traffic from a specific subnet.
2.  **Hardening Scripts**: Run a basic CIS Benchmark check on your system using an automated tool.
3.  **Social Engineering**: List three common indicators of a phishing email.

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.
