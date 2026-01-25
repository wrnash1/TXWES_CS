# CIS-3321: Network Administration Labs (CompTIA Network+ Alignment)

## Lab 1: Networking Fundamentals & IP Addressing
**Objective**: Understand OSI model layers and practice IPv4 subnetting.

1.  **OSI Model**: Identify which layer a Router operates at versus a Switch.
2.  **Subnetting**: You are given the network `192.168.1.0/24`. Subnet this into 4 equal networks. What is the new subnet mask?
3.  **Connectivity**: Use `ping` to test connectivity to the DNS server `8.8.8.8`.
4.  **Routing Table**: Run `ip route show`. Identify your default gateway.

## Lab 2: Network Services & Protocols
**Objective**: Configure and troubleshoot common network protocols.

1.  **DNS**: Use `nslookup` or `dig` to find the IP address of `txwes.edu`.
2.  **HTTP/HTTPS**: Use `curl -I https://www.google.com` to view the HTTP header response.
3.  **SSH**: Verify the SSH daemon is listening on port 22 using `ss -tulpn`.
4.  **DHCP**: Identify the IP address assigned to your VM and explain how a DORA process works conceptually.

## Lab 3: Network Security & Troubleshooting
**Objective**: Use industry-standard tools to diagnose network issues.

1.  **Traceroute**: Run `traceroute 8.8.8.8`. How many hops are between you and the destination?
2.  **Packet Capture**: If `tcpdump` is installed, capture 5 packets on the main interface: `sudo tcpdump -c 5`.
3.  **Port Scanning**: Use `nmap` to perform a basic scan of your own machine.
4.  **Troubleshooting**: A user cannot reach the internet. List the first three steps you would take in the CompTIA troubleshooting methodology.

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.
