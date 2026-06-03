# Lab Activity: Module 13 — Network Security Fundamentals

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Lab Overview

In this lab you will configure five core Layer 2 and AAA security features on a simulated enterprise switch topology using Cisco Packet Tracer. You will enable AAA with a RADIUS server, configure sticky port security, implement DHCP snooping, enable Dynamic ARP Inspection, and verify 802.1X readiness on an access port.

**Estimated Time:** 75 minutes

**Tool:** Cisco Packet Tracer 8.2 or later

---

## Topology Description

```text
[RADIUS Server]         [Rogue DHCP Server]
  10.0.0.50                10.0.0.99
       |                        |
       |                        |
  Gi0/24 (trusted)        Gi0/1 (untrusted)
       |                        |
  [SW1 - Cisco Catalyst 2960]
       |         |         |
   Gi0/2     Gi0/3     Gi0/4
     |          |          |
  [PC-A]    [PC-B]    [Attacker PC]
 10.0.0.10  10.0.0.11  10.0.0.99
  VLAN 10   VLAN 10   VLAN 10
```

### Device Addressing Table

| Device | Interface | IP Address | VLAN |
|---|---|---|---|
| SW1 | VLAN 10 SVI | 10.0.0.1/24 | 10 |
| RADIUS Server | NIC | 10.0.0.50/24 | 10 |
| Rogue DHCP | NIC | 10.0.0.99/24 | 10 |
| PC-A | NIC | DHCP | 10 |
| PC-B | NIC | DHCP | 10 |
| Attacker PC | NIC | 10.0.0.99/24 | 10 |

---

## Part 1: Initial Switch Setup

### Step 1.1 — Set Hostname and Create VLAN 10

```ios
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW1
SW1(config)# vlan 10
SW1(config-vlan)# name CORP-LAN
SW1(config-vlan)# exit
SW1(config)# interface vlan 10
SW1(config-if)# ip address 10.0.0.1 255.255.255.0
SW1(config-if)# no shutdown
SW1(config-if)# exit
```

### Step 1.2 — Assign Access Ports to VLAN 10

```ios
SW1(config)# interface range gigabitethernet 0/1 - 4
SW1(config-if-range)# switchport mode access
SW1(config-if-range)# switchport access vlan 10
SW1(config-if-range)# exit
SW1(config)# interface gigabitethernet 0/24
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
SW1(config-if)# exit
```

**Verification:**

```ios
SW1# show vlan brief
SW1# show interfaces status
```

---

## Part 2: AAA and RADIUS Configuration

### Step 2.1 — Enable AAA and Configure RADIUS

```ios
SW1(config)# aaa new-model
SW1(config)# radius server CORP-RADIUS
SW1(config-radius-server)# address ipv4 10.0.0.50 auth-port 1812 acct-port 1813
SW1(config-radius-server)# key Lab@RADIUS123
SW1(config-radius-server)# exit
SW1(config)# aaa authentication login default group radius local
SW1(config)# aaa authorization exec default group radius local
SW1(config)# username admin privilege 15 secret Admin@Lab1
```

### Step 2.2 — Configure RADIUS Server (Packet Tracer)

In Packet Tracer, click the RADIUS Server device:

1. Go to Services > AAA
2. Enable the AAA service
3. Add a Network device: IP = 10.0.0.1, Secret = Lab@RADIUS123
4. Add a User: Username = labuser, Password = LabPass1!

**Verification:**

```ios
SW1# show aaa servers
SW1# show running-config | include aaa
```

---

## Part 3: Port Security

### Step 3.1 — Configure Sticky Port Security on Gi0/2 and Gi0/3

```ios
SW1(config)# interface gigabitethernet 0/2
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security maximum 1
SW1(config-if)# switchport port-security mac-address sticky
SW1(config-if)# switchport port-security violation restrict
SW1(config-if)# exit
SW1(config)# interface gigabitethernet 0/3
SW1(config-if)# switchport port-security
SW1(config-if)# switchport port-security maximum 1
SW1(config-if)# switchport port-security mac-address sticky
SW1(config-if)# switchport port-security violation restrict
SW1(config-if)# exit
```

### Step 3.2 — Trigger a Violation

On PC-A, send a ping to 10.0.0.1 to populate the sticky MAC entry. Then disconnect PC-A from Gi0/2 and connect the Attacker PC to Gi0/2. Send a ping from the Attacker PC.

**Expected result:** Pings fail. Violation counter increments. Port stays up (restrict mode).

**Verification:**

```ios
SW1# show port-security interface gigabitethernet 0/2
SW1# show port-security address
```

Record the violation count from the output: ______

---

## Part 4: DHCP Snooping

### Step 4.1 — Enable DHCP Snooping

```ios
SW1(config)# ip dhcp snooping
SW1(config)# ip dhcp snooping vlan 10
SW1(config)# no ip dhcp snooping information option
SW1(config)# interface gigabitethernet 0/24
SW1(config-if)# ip dhcp snooping trust
SW1(config-if)# exit
SW1(config)# interface range gigabitethernet 0/1 - 4
SW1(config-if-range)# ip dhcp snooping limit rate 15
SW1(config-if-range)# exit
```

### Step 4.2 — Test Rogue DHCP Server Blocking

In Packet Tracer, configure the Rogue DHCP Server (connected to Gi0/1) to serve addresses in the 10.0.0.100–200 range. Set PC-A to DHCP. Observe that PC-A does NOT receive an address from the rogue server.

**Verification:**

```ios
SW1# show ip dhcp snooping
SW1# show ip dhcp snooping binding
SW1# show ip dhcp snooping statistics
```

Record the number of forwarded vs. dropped DHCP packets: ______

---

## Part 5: Dynamic ARP Inspection

### Step 5.1 — Enable DAI

```ios
SW1(config)# ip arp inspection vlan 10
SW1(config)# interface gigabitethernet 0/24
SW1(config-if)# ip arp inspection trust
SW1(config-if)# exit
SW1(config)# interface range gigabitethernet 0/1 - 4
SW1(config-if-range)# ip arp inspection limit rate 100
SW1(config-if-range)# exit
```

### Step 5.2 — Add ARP ACL for the Switch SVI

```ios
SW1(config)# arp access-list SWITCH-SVI
SW1(config-arp-acl)# permit ip host 10.0.0.1 mac host 0001.0002.0003
SW1(config-arp-acl)# exit
SW1(config)# ip arp inspection filter SWITCH-SVI vlan 10
```

Replace `0001.0002.0003` with the actual MAC address of the VLAN 10 SVI from `show interfaces vlan 10`.

**Verification:**

```ios
SW1# show ip arp inspection
SW1# show ip arp inspection vlan 10
SW1# show ip arp inspection statistics
```

---

## Part 6: 802.1X Readiness

### Step 6.1 — Configure 802.1X on Gi0/4

```ios
SW1(config)# aaa authentication dot1x default group radius
SW1(config)# aaa authorization network default group radius
SW1(config)# dot1x system-auth-control
SW1(config)# interface gigabitethernet 0/4
SW1(config-if)# authentication port-control auto
SW1(config-if)# dot1x pae authenticator
SW1(config-if)# exit
```

**Verification:**

```ios
SW1# show dot1x all
SW1# show dot1x interface gigabitethernet 0/4 detail
SW1# show authentication sessions
```

Note: Full 802.1X supplicant simulation is limited in Packet Tracer. Verify configuration syntax is accepted and port shows `auto` control mode.

---

## Part 7: Save and Verify

### Step 7.1 — Save Configuration

```ios
SW1# copy running-config startup-config
```

### Step 7.2 — Final Verification Checklist

Run each of the following commands and confirm expected output:

```ios
SW1# show running-config
SW1# show port-security
SW1# show ip dhcp snooping binding
SW1# show ip arp inspection
SW1# show dot1x all
SW1# show aaa servers
```

---

## Lab Rubric

| Task | Points | Criteria |
|---|---|---|
| Part 1: VLAN and port setup | 10 | VLAN 10 created; all ports assigned correctly |
| Part 2: AAA/RADIUS configured | 20 | `aaa new-model` present; RADIUS server defined; method lists correct |
| Part 3: Port security configured | 20 | Sticky enabled on Gi0/2–3; restrict mode; violation triggered and counted |
| Part 4: DHCP snooping active | 20 | Enabled on VLAN 10; Gi0/24 trusted; rogue DHCP blocked |
| Part 5: DAI enabled | 15 | `ip arp inspection vlan 10` present; uplink trusted; ARP ACL applied |
| Part 6: 802.1X configured | 10 | `dot1x system-auth-control` present; port set to auto |
| Part 7: Config saved; verification output | 5 | `copy run start` executed; screenshots or output captured |
| **Total** | **100** | |

---

## Submission Instructions

Export your Packet Tracer file (.pka) and submit via the course LMS. Include a screenshot showing:

1. `show port-security interface gi0/2` output with a non-zero violation count
2. `show ip dhcp snooping binding` showing at least one DHCP entry
3. `show ip arp inspection` showing DAI enabled on VLAN 10
