# Security Labs (CompTIA Security+ Alignment)

## Lab 1: Reconnaissance and Scanning
**Objective**: Learn how to identify open ports and services on a network.

1.  **Nmap**: Run `nmap -sV localhost`. What services are currently running on your VM?
2.  **OS Identification**: Try to identify the OS of your own machine using `nmap -O localhost` (Note: requires `sudo`).
3.  **Port Vulnerability**: If Port 22 (SSH) is open, what are two ways you could harden it to prevent brute-force attacks?

## Lab 2: Cryptography & Hashing
**Objective**: Understand the difference between encryption and hashing.

1.  **Hashing**: Create a text file `secret.txt`. Generate a SHA256 hash of it: `sha256sum secret.txt > hash.txt`.
2.  **Verification**: Change one character in `secret.txt` and generate the hash again. Did the hash change significantly? (The Avalanche Effect).
3.  **Encryption**: Use `gpg` to encrypt `secret.txt`: `gpg -c secret.txt`. Delete the original and try to decrypt the `.gpg` file.

## Lab 3: Firewall and Network Defense
**Objective**: Configure host-based firewalls to block unauthorized traffic.

1.  **Status**: Check the status of the firewall: `sudo firewall-cmd --state`.
2.  **Blocking**: Use `firewall-cmd` to block all incoming traffic on Port 80.
3.  **Persistence**: How do you make a firewall rule permanent so it survives a reboot?
4.  **Logging**: Where are the firewall logs located on Fedora?

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.
