# Video Script 2.2: IPv4 Subnetting Basics
**Course:** CIS 3321 - Network Administration (CompTIA Network+)
**Module:** 2 (Network Implementations)
**Estimated Duration:** 7 minutes

---

## Script & Visual Directives

**[00:00 - 01:30] Introduction to IPv4**
**Visual:** Instructor on camera.
**Audio:** "Welcome back. We've conquered Layer 2 and MAC addresses. Now, we move up to Layer 3: The Network layer. This is the domain of Routers and IP Addresses. A MAC address is like your physical fingerprint, but an IP address is like your home mailing address—it tells the network where you currently are in the world."

**[01:30 - 03:00] Anatomy of an IPv4 Address**
**Visual:** The IP address `192.168.1.50` is shown on screen, broken down into four blocks of numbers. Below it, the binary equivalent is displayed.
**[Alt-text: The IPv4 address '192.168.1.50' displayed in large text. Below it is the binary representation: 11000000 . 10101000 . 00000001 . 00110010. Text indicates it is a 32-bit address made of four 8-bit octets.]**
**Audio:** "An IPv4 address is 32 bits long. To make it readable for humans, we write it as four decimal numbers separated by dots, known as dotted-decimal notation. Each number is an 'octet' because it represents 8 binary bits. Because 8 bits can hold 256 unique combinations, each number in an IP address can only range from 0 to 255."

**[03:00 - 05:00] The Subnet Mask**
**Visual:** The IP address `192.168.1.50` is shown with a subnet mask of `255.255.255.0` below it. The first three octets of the IP are highlighted red (Network), the last is highlighted green (Host).
**[Alt-text: IP address 192.168.1.50 with subnet mask 255.255.255.0. The '192.168.1' portion is boxed in red and labeled 'Network ID'. The '.50' portion is boxed in green and labeled 'Host ID'.]**
**Audio:** "Every IP address has two parts: the Network ID (your street) and the Host ID (your specific house). But how does a computer know which part is which? That's the job of the Subnet Mask. In a `255.255.255.0` mask, the 255s act like a highlighter, telling the computer, 'The first three numbers are the Network ID.' The 0 tells the computer, 'The last number is the Host ID.' This is often written in CIDR notation as a `/24`, meaning the first 24 bits belong to the network."

**[05:00 - 07:00] Why We Subnet**
**Visual:** A giant block of 254 IP addresses is sliced into smaller blocks.
**[Alt-text: A large rectangle labeled 'Subnet 192.168.1.0/24 (254 Hosts)' is sliced into four smaller rectangles labeled '/26 (62 Hosts each)'.]**
**Audio:** "Subnetting is simply the act of taking a large network and slicing it into smaller, more efficient networks. If you have 10 computers in the HR department and 10 in IT, you don't want them sharing a massive network of 254 addresses where broadcast traffic causes congestion. You slice the network in half, assign one subnet to HR, one to IT, and use a router to connect them. We will practice the binary math for this in your reading guide."
