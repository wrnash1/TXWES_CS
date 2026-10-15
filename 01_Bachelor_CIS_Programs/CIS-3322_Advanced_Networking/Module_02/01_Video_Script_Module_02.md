# Video Script: Module 02 - Subnetting and VLSM Configurations

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course &bull; Module 02</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ" title="Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 1: Network Fundamentals - 20%)
**Estimated Duration:** 24 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Section 1: Introduction and Why Subnetting Matters
Welcome to Module 02. I am Professor Nash, and today we tackle one of the most important skills on the entire CCNA exam: subnetting and Variable Length Subnet Masking, or VLSM.

The CCNA 200-301 exam includes multiple subnetting questions, and many of them require you to calculate subnet addresses, usable host ranges, and broadcast addresses under time pressure. Students who master the binary math early in this course consistently outperform those who skip it.

In this module we will cover:

- Binary and CIDR notation refresher
- Classical subnetting: borrowing host bits to create subnets
- VLSM: using different subnet sizes within the same address space
- Efficient address allocation strategy
- Cisco IOS verification commands for IP addressing

By the end of this module you will be able to divide a given address block into subnets of varying sizes, determine the network address, broadcast address, and usable host range for each subnet, and explain why VLSM is more address-efficient than fixed-length subnetting.

---

## Section 2: Binary, CIDR, and the Subnet Mask
Before we calculate subnets, you need to be comfortable reading and writing subnet masks in three forms: dotted decimal, prefix notation, and binary.

A subnet mask is a 32-bit value. Every bit set to 1 represents a network bit. Every bit set to 0 represents a host bit. The boundary between 1s and 0s defines where the network portion ends and the host portion begins.

```text
/24 = 255.255.255.0   = 11111111.11111111.11111111.00000000
/25 = 255.255.255.128 = 11111111.11111111.11111111.10000000
/26 = 255.255.255.192 = 11111111.11111111.11111111.11000000
/27 = 255.255.255.224 = 11111111.11111111.11111111.11100000
/28 = 255.255.255.240 = 11111111.11111111.11111111.11110000
/29 = 255.255.255.248 = 11111111.11111111.11111111.11111000
/30 = 255.255.255.252 = 11111111.11111111.11111111.11111100
```

The key formulas are:

- Number of subnets = 2 raised to the number of borrowed bits
- Total addresses per subnet = 2 raised to the number of remaining host bits
- Usable hosts = total addresses minus 2

CCNA Exam Tip: Memorize the usable host counts for /24 through /30. The exam provides no calculator. If you can recall that /28 gives 14 usable hosts without calculating, you save two to three minutes per question.

---

## Section 3: Classical Subnetting Worked Example
Let us work through a complete subnetting example. You are assigned 192.168.1.0/24 and need to create four equal subnets.

You need 4 subnets, so you borrow 2 bits (2^2 = 4). Starting from /24, borrowing 2 bits gives /26.

```text
Subnet 1: 192.168.1.0/26
  Network:    192.168.1.0
  First host: 192.168.1.1
  Last host:  192.168.1.62
  Broadcast:  192.168.1.63

Subnet 2: 192.168.1.64/26
  Network:    192.168.1.64
  First host: 192.168.1.65
  Last host:  192.168.1.126
  Broadcast:  192.168.1.127

Subnet 3: 192.168.1.128/26
  Network:    192.168.1.128
  First host: 192.168.1.129
  Last host:  192.168.1.190
  Broadcast:  192.168.1.191

Subnet 4: 192.168.1.192/26
  Network:    192.168.1.192
  First host: 192.168.1.193
  Last host:  192.168.1.254
  Broadcast:  192.168.1.255
```

Each subnet starts exactly 64 addresses after the previous one. The block size is 2^6 = 64. This is your increment.

CCNA Exam Tip: Calculate the block size first, then add that block size to each network address to find the next subnet. You do not need binary addition for every subnet — just add the increment.

---

## Section 4: VLSM - Variable Length Subnet Masking
VLSM allows different subnet sizes within the same address space. This is critical for efficient allocation because not every segment needs the same number of hosts.

Scenario: You are given 192.168.5.0/24 and must support four networks:

- Network A: 50 hosts required
- Network B: 25 hosts required
- Network C: 10 hosts required
- Network D: point-to-point WAN link (2 hosts required)

Allocate largest first, then carve smaller subnets from remaining space:

```text
Network A - 50 hosts needed: use /26 (62 usable hosts)
  Network:    192.168.5.0/26
  First host: 192.168.5.1
  Last host:  192.168.5.62
  Broadcast:  192.168.5.63

Network B - 25 hosts needed: use /27 (30 usable hosts)
  Network:    192.168.5.64/27
  First host: 192.168.5.65
  Last host:  192.168.5.94
  Broadcast:  192.168.5.95

Network C - 10 hosts needed: use /28 (14 usable hosts)
  Network:    192.168.5.96/28
  First host: 192.168.5.97
  Last host:  192.168.5.110
  Broadcast:  192.168.5.111

Network D - WAN link, 2 hosts needed: use /30
  Network:    192.168.5.112/30
  First host: 192.168.5.113
  Last host:  192.168.5.114
  Broadcast:  192.168.5.115
```

The addresses 192.168.5.116 through 192.168.5.255 remain available for future subnets.

CCNA Exam Tip: Always start VLSM allocation with the subnet requiring the most hosts. If you start with a small subnet, you may fragment the address space and waste large blocks.

---

## Section 5: Cisco IOS Configuration and Lab Preview
After calculating your subnets, configure IP addresses on router interfaces:

```ios
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip address 192.168.5.1 255.255.255.192
Router(config-if)# no shutdown
Router(config-if)# end
```

Verify with:

```ios
Router# show ip interface brief
Router# show interfaces GigabitEthernet0/0
Router# show ip route
```

If an interface shows "administratively down," you forgot the `no shutdown` command.

CCNA Exam Tip: On the exam, if a question asks whether a given IP address is a valid host address, check the host portion. All zeros equals the network address; all ones equals the broadcast address. Neither can be assigned to a host.

For additional study resources, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

Complete the reading guide and work through all VLSM practice problems before the lab. I will see you in Module 03 for IPv6 addressing.

---

## End Card

Module 02 Complete
Next: Module 03 - IPv6 Addressing and Configuration
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
