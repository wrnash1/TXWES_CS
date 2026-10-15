# Video Script: Module 03 - IPv6 Addressing and Configuration

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Jeremy's IT Lab &bull; Cisco CCNA 200-301 Complete Course &bull; Module 03</strong>
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
**Estimated Duration:** 23 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Section 1: Why IPv6 Exists and What You Need to Know
Welcome to Module 03. I am Professor Nash. Today we cover IPv6 — the addressing system that will eventually replace IPv4 across the entire internet and enterprise network world.

IPv4 uses 32-bit addresses, which gives us approximately 4.3 billion addresses. That number sounds large, but the internet ran out of unallocated IPv4 blocks in 2011. IPv6 uses 128-bit addresses, providing 340 undecillion unique addresses — enough for every device on earth for the foreseeable future.

The CCNA 200-301 exam tests IPv6 across both the Network Fundamentals and IP Connectivity domains. You will see questions on IPv6 address types, SLAAC configuration, EUI-64 conversion, and Cisco IOS CLI commands. This module gives you everything you need.

Topics covered today:

- IPv6 address format, notation, and abbreviation rules
- IPv6 address types: link-local, global unicast, unique local, multicast
- SLAAC and EUI-64 interface identifier generation
- Cisco IOS IPv6 configuration commands
- IPv6 static routing
- Verification and troubleshooting commands

---

## Section 2: IPv6 Address Format and Abbreviation
An IPv6 address is 128 bits written as eight groups of four hexadecimal digits, separated by colons.

Full form: `2001:0DB8:0000:0001:0000:0000:0000:0001`

Two abbreviation rules make IPv6 addresses shorter and more readable.

Rule 1 - Leading zero compression: You can drop leading zeros within any group.

`2001:0DB8:0000:0001` becomes `2001:DB8:0:1`

Rule 2 - Double-colon compression: One continuous sequence of consecutive all-zero groups can be replaced with `::`. This can only be used once in an address.

`2001:DB8:0:0:0:0:0:1` becomes `2001:DB8::1`

CCNA Exam Tip: The exam presents compressed IPv6 addresses and asks you to expand them, or vice versa. To expand a double-colon, count the existing groups, then insert enough all-zero groups to reach a total of 8 groups. If `2001:DB8::1` has 3 groups written out (2001, DB8, and 1), insert 5 groups of zeros between the two colons.

---

## Section 3: IPv6 Address Types

### Link-Local Addresses (FE80::/10)

Every IPv6-enabled interface automatically generates a link-local address, even without any manual configuration. Link-local addresses always begin with FE80 (in practice, usually FE80:: with a 64-bit interface identifier appended).

Link-local addresses are used for:

- Communication between neighbors on the same segment
- Router Advertisement and Neighbor Discovery messages
- As the next-hop for IPv6 static routes pointing to a directly connected interface

Link-local addresses are never forwarded by a router. They are segment-scoped only.

### Global Unicast Addresses (2000::/3)

Global unicast addresses are publicly routable. They are equivalent to public IPv4 addresses. The IANA allocates global unicast blocks to regional registries, which allocate to ISPs, which assign to customers.

For lab and documentation purposes, the address block 2001:DB8::/32 is reserved and must never be routed on the public internet.

### Unique Local Addresses (FC00::/7)

Unique local addresses are the IPv6 equivalent of RFC 1918 private IPv4 addresses. They are routable within an organization but not on the public internet. The range FC00::/7 encompasses both FC00::/8 and FD00::/8, with FD00::/8 being the commonly used prefix.

### Multicast Addresses (FF00::/8)

IPv6 replaces broadcast with multicast. Key multicast addresses to know:

- FF02::1 — All IPv6 nodes on the local link
- FF02::2 — All IPv6 routers on the local link
- FF02::5 — All OSPFv3 routers
- FF02::6 — OSPFv3 designated routers

CCNA Exam Tip: Memorize the three most testable address types: link-local starts with FE80, global unicast starts with 2000-3FFF (the 2000::/3 range), and unique local starts with FC or FD. The exam will give you an address and ask its type.

---

## Section 4: SLAAC and EUI-64
### SLAAC - Stateless Address Autoconfiguration

SLAAC allows an IPv6 host to configure its own global unicast address without a DHCPv6 server. The process:

1. The host generates a link-local address and sends a Router Solicitation (RS) to FF02::2
2. A router replies with a Router Advertisement (RA) containing the /64 network prefix
3. The host combines the advertised /64 prefix with a 64-bit interface identifier to form its full 128-bit address
4. The host runs Duplicate Address Detection (DAD) to confirm the address is unique on the segment

### EUI-64 Interface Identifier Generation

When a router uses EUI-64 to generate an interface identifier, the process has three steps:

Step 1: Take the 48-bit MAC address: `00:1A:2B:3C:4D:5E`

Step 2: Split the MAC in half and insert FFFE in the middle:

`001A:2B` + `FFFE` + `3C:4D:5E` = `001A:2BFF:FE3C:4D5E`

Step 3: Invert bit 7 (the Universal/Local bit) of the first byte:

First byte `00` in binary is `00000000`. Bit 7 (counting from left, 0-indexed) is the second bit. Inverting it: `00000000` becomes `00000010` = `02`.

Final EUI-64 interface ID: `021A:2BFF:FE3C:4D5E`

Full address with prefix 2001:DB8::/64: `2001:DB8::021A:2BFF:FE3C:4D5E`

CCNA Exam Tip: The exam may give you a MAC address and ask for the EUI-64 interface identifier. Practice the three steps: split, insert FFFE, invert bit 7. The most common mistake is forgetting to invert bit 7.

---

## Section 5: Cisco IOS IPv6 Configuration and Lab Preview
To enable IPv6 routing on a Cisco router, you must enter one global command first:

```ios
Router(config)# ipv6 unicast-routing
```

Without this command, the router will not forward IPv6 packets between interfaces, even if addresses are configured.

Configure a static IPv6 address on an interface:

```ios
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ipv6 address 2001:DB8:ACAD:1::1/64
Router(config-if)# no shutdown
```

Configure using EUI-64 (router generates the interface ID from MAC):

```ios
Router(config-if)# ipv6 address 2001:DB8:ACAD:1::/64 eui-64
```

Configure an IPv6 static route:

```ios
Router(config)# ipv6 route 2001:DB8:ACAD:2::/64 2001:DB8:ACAD:3::2
```

For a default route:

```ios
Router(config)# ipv6 route ::/0 GigabitEthernet0/0 FE80::2
```

Note: When the next-hop is a link-local address, you must specify the exit interface.

Verify IPv6 configuration:

```ios
Router# show ipv6 interface brief
Router# show ipv6 route
Router# show ipv6 neighbors
```

CCNA Exam Tip: Know these three IPv6 show commands cold. The exam uses all three in simulation questions. `show ipv6 neighbors` is the IPv6 equivalent of `show ip arp` — it displays the neighbor cache built by the Neighbor Discovery Protocol.

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

Complete the reading guide and practice the EUI-64 conversion by hand before the lab. I will see you in Module 04 for Switching Concepts and VLANs.

---

## End Card

Module 03 Complete
Next: Module 04 - Switching Concepts and VLANs
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
