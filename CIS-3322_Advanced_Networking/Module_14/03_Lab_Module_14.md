# Lab Activity: Module 14 — Wireless Networking

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Lab Overview

In this lab you will configure a controller-based wireless network in Cisco Packet Tracer. You will set up a Cisco Wireless LAN Controller (WLC), associate two lightweight access points, create two WLANs (corporate and guest) with different security policies, and verify wireless client connectivity and VLAN separation.

**Estimated Time:** 70 minutes

**Tool:** Cisco Packet Tracer 8.2 or later

---

## Topology Description

```text
[WLC]
  |
  | (Management VLAN 1 / 10.0.0.2)
  |
[SW1 - Layer 3 Switch]
  |           |           |
Trunk      Gi0/2       Gi0/3
  |           |           |
[AP-1]     [AP-2]    [Router/DHCP]
                       10.0.0.1/24

Wireless Clients:
  SSID: CORP-WLAN  -> VLAN 10 (10.10.10.0/24)
  SSID: GUEST-WLAN -> VLAN 20 (10.20.20.0/24)
```

### Device Addressing Table

| Device | Interface/VLAN | IP Address | Role |
|---|---|---|---|
| SW1 | VLAN 1 | 10.0.0.10/24 | Distribution switch |
| WLC | Management | 10.0.0.2/24 | Wireless controller |
| WLC | Dynamic (CORP) | 10.10.10.2/24 | VLAN 10 interface |
| WLC | Dynamic (GUEST) | 10.20.20.2/24 | VLAN 20 interface |
| Router | Gi0/0 | 10.0.0.1/24 | Default gateway + DHCP |
| AP-1 | CAPWAP | 10.0.0.11 (DHCP) | Lightweight AP |
| AP-2 | CAPWAP | 10.0.0.12 (DHCP) | Lightweight AP |
| Laptop-1 | Wireless | 10.10.10.x (DHCP) | Corporate WLAN client |
| Laptop-2 | Wireless | 10.20.20.x (DHCP) | Guest WLAN client |

---

## Part 1: Wired Infrastructure Setup

### Step 1.1 — Configure VLANs on SW1

```ios
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW1
SW1(config)# vlan 10
SW1(config-vlan)# name CORP-WLAN
SW1(config-vlan)# exit
SW1(config)# vlan 20
SW1(config-vlan)# name GUEST-WLAN
SW1(config-vlan)# exit
```

### Step 1.2 — Configure Trunk Port to WLC

```ios
SW1(config)# interface gigabitethernet 0/1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 1,10,20
SW1(config-if)# exit
```

### Step 1.3 — Configure SVI Interfaces

```ios
SW1(config)# interface vlan 1
SW1(config-if)# ip address 10.0.0.10 255.255.255.0
SW1(config-if)# no shutdown
SW1(config-if)# exit
SW1(config)# interface vlan 10
SW1(config-if)# ip address 10.10.10.10 255.255.255.0
SW1(config-if)# no shutdown
SW1(config-if)# exit
SW1(config)# interface vlan 20
SW1(config-if)# ip address 10.20.20.10 255.255.255.0
SW1(config-if)# no shutdown
SW1(config-if)# exit
SW1(config)# ip routing
SW1(config)# ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

### Step 1.4 — Configure Access Ports for APs

```ios
SW1(config)# interface gigabitethernet 0/2
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 1
SW1(config-if)# exit
SW1(config)# interface gigabitethernet 0/3
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 1
SW1(config-if)# exit
```

**Verification:**

```ios
SW1# show vlan brief
SW1# show interfaces trunk
```

---

## Part 2: DHCP Server Configuration

### Step 2.1 — Configure DHCP on the Router

```ios
Router(config)# ip dhcp pool MGMT-POOL
Router(dhcp-config)# network 10.0.0.0 255.255.255.0
Router(dhcp-config)# default-router 10.0.0.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# option 43 ascii 10.0.0.2
Router(dhcp-config)# exit
Router(config)# ip dhcp pool CORP-POOL
Router(dhcp-config)# network 10.10.10.0 255.255.255.0
Router(dhcp-config)# default-router 10.10.10.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# exit
Router(config)# ip dhcp pool GUEST-POOL
Router(dhcp-config)# network 10.20.20.0 255.255.255.0
Router(dhcp-config)# default-router 10.20.20.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# exit
Router(config)# ip dhcp excluded-address 10.0.0.1 10.0.0.10
Router(config)# ip dhcp excluded-address 10.10.10.1 10.10.10.10
Router(config)# ip dhcp excluded-address 10.20.20.1 10.20.20.10
```

Note: DHCP Option 43 in ASCII format `10.0.0.2` tells APs the WLC IP address during the discovery process.

---

## Part 3: WLC Initial Setup

### Step 3.1 — WLC Setup Wizard (Packet Tracer GUI)

In Packet Tracer, click the WLC device and navigate to the Config tab. Set the following:

* Management IP: 10.0.0.2
* Subnet Mask: 255.255.255.0
* Default Gateway: 10.0.0.1
* Admin username: admin
* Admin password: Admin@WLC1

### Step 3.2 — Create Dynamic Interfaces

In the WLC GUI go to Controller > Interfaces > New:

Create CORP interface:

* Interface name: corp-vlan
* VLAN ID: 10
* IP address: 10.10.10.2
* Netmask: 255.255.255.0
* Gateway: 10.10.10.10
* DHCP server: 10.0.0.1

Create GUEST interface:

* Interface name: guest-vlan
* VLAN ID: 20
* IP address: 10.20.20.2
* Netmask: 255.255.255.0
* Gateway: 10.20.20.10
* DHCP server: 10.0.0.1

---

## Part 4: WLAN Configuration

### Step 4.1 — Create the Corporate WLAN

In the WLC GUI go to WLANs > Create New:

* WLAN ID: 1
* Profile name: CORP-WLAN
* SSID: CORP-WLAN
* Status: Enabled

Under the Security tab:

* Layer 2 Security: WPA2
* Authentication Key Management: PSK
* PSK format: ASCII
* PSK: CorpWiFi@2024

Under the Advanced tab:

* Interface: corp-vlan

### Step 4.2 — Create the Guest WLAN

In the WLC GUI go to WLANs > Create New:

* WLAN ID: 2
* Profile name: GUEST-WLAN
* SSID: GUEST-WLAN
* Status: Enabled

Under the Security tab:

* Layer 2 Security: WPA2
* Authentication Key Management: PSK
* PSK format: ASCII
* PSK: Guest@2024

Under the Advanced tab:

* Interface: guest-vlan

---

## Part 5: AP Association Verification

### Step 5.1 — Verify AP Join

Power on AP-1 and AP-2. In Packet Tracer, the APs should automatically receive IP addresses via DHCP on VLAN 1 and use Option 43 to discover the WLC.

Verify in the WLC GUI under Monitor > Access Points. Both APs should appear in the list with:

* Status: Registered
* Mode: Local
* IP Address: 10.0.0.11 and 10.0.0.12

### Step 5.2 — Verify WLC CLI

Access the WLC CLI through the terminal:

```ios
(WLC)> show ap summary
(WLC)> show wlan summary
(WLC)> show interface summary
```

Record: How many APs appear as Registered? ______

---

## Part 6: Wireless Client Connectivity Test

### Step 6.1 — Connect Laptop-1 to CORP-WLAN

In Packet Tracer, click Laptop-1. Go to the Wireless PC card configuration:

* SSID: CORP-WLAN
* Security: WPA2-PSK
* PSK: CorpWiFi@2024

Set IP configuration to DHCP. Verify Laptop-1 receives an IP in the 10.10.10.0/24 range.

### Step 6.2 — Connect Laptop-2 to GUEST-WLAN

Click Laptop-2. Configure:

* SSID: GUEST-WLAN
* Security: WPA2-PSK
* PSK: Guest@2024

Set IP configuration to DHCP. Verify Laptop-2 receives an IP in the 10.20.20.0/24 range.

### Step 6.3 — Verify VLAN Isolation

From Laptop-1, attempt to ping Laptop-2's IP address. The ping should fail, confirming VLAN isolation between the corporate and guest WLANs.

From Laptop-1, ping 10.0.0.1 (default gateway). This should succeed.

Record results: Laptop-1 to Laptop-2 ping: ______ | Laptop-1 to gateway ping: ______

---

## Part 7: Save and Final Verification

### Step 7.1 — Verify Wired Infrastructure

```ios
SW1# show vlan brief
SW1# show interfaces trunk
SW1# show ip interface brief
```

### Step 7.2 — Final WLC Verification

In the WLC GUI, navigate to:

* Monitor > Summary — confirm AP count, client count, and WLAN status
* Monitor > Clients — verify both laptops are associated with correct WLANs and VLANs

---

## Lab Rubric

| Task | Points | Criteria |
|---|---|---|
| Part 1: VLANs and trunking correct | 15 | VLANs 10 and 20 created; trunk to WLC configured |
| Part 2: DHCP configured with Option 43 | 15 | Three pools created; Option 43 points to WLC |
| Part 3: WLC interfaces created | 20 | Management, corp-vlan, guest-vlan interfaces correct |
| Part 4: Both WLANs created | 20 | Correct SSIDs, WPA2-PSK, and VLAN mapping |
| Part 5: Both APs registered | 15 | APs appear as Registered in WLC Monitor |
| Part 6: Clients connect and VLAN isolated | 10 | Correct IP ranges; cross-VLAN ping fails |
| Part 7: Verification output captured | 5 | Screenshots of WLC monitor and SW1 trunk output |
| **Total** | **100** | |

---

## Submission Instructions

Submit your Packet Tracer .pka file through the course LMS. Include screenshots showing:

1. WLC Monitor > Access Points with both APs showing Registered status
2. WLC Monitor > Clients showing both laptops with correct VLAN assignments
3. Ping output from Laptop-1 demonstrating VLAN isolation
