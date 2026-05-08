### 1. Video Script 3.1: Network Segmentation and Demilitarized Zones (DMZs)
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 3. If you build a castle, you don't just put one giant wall around it and leave the inside completely open. You build an outer wall, a moat, an inner wall, and a keep. In network security, this is called architecture and segmentation."
**Visual:** A network diagram. The Internet connects to a Firewall. Behind the firewall is a DMZ containing a Web Server. Behind the DMZ is a second Firewall. Behind that is the Internal Network with a Database Server.
**[Alt-text: A diagram illustrating a Demilitarized Zone. Traffic flows from the Internet, through an external firewall, into a DMZ containing a public web server. A second internal firewall separates the DMZ from the secure internal network containing the database.]**
**Audio:** "We use firewalls and VLANs to segment the network. A Demilitarized Zone, or DMZ, is a subnet exposed to the internet, separated from the highly secure internal network. If you host a public web server, it goes in the DMZ. If a hacker breaches the web server, they are still trapped in the DMZ by an internal firewall, protecting your sensitive database."

---
