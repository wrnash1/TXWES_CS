# Lab Activity: Module 11 - IoT Gateway Security
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

## Objective
Configure and verify systems matching the operational parameters of **IoT Gateway Security**.

---

## Prerequisites
*   Ensure you have access to a terminal or a runtime environment matching the course requirements (e.g., Linux, macOS, Windows, or a cloud/web terminal).
*   Ensure you have administrative privileges if required to install packages or configure system services.

---

## Step-by-Step Instructions
1. **Configure firewall routing rules on a mock gateway interface**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
2. **Isolate IoT devices in separate VLAN subnet**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.
3. **Audit network logs**
   * *Instruction:* Execute this step inside your terminal environment. Verify the command completes without errors.

---

## Troubleshooting Guide
*   *Error:* `Permission Denied`
    * *Fix:* Remember to run administrative command sequences using `sudo` or execute with administrative privileges (e.g., Run as Administrator on Windows).
*   *Error:* `Command Not Found`
    * *Fix:* Verify your environmental path settings, or double-check if the utility package is installed.

---

## Deliverables
1. Document your completed steps with screenshots or terminal output logs showing successful execution.
2. Submit your completion report to your Canvas LMS assignment portal for grading.

---

## Part 9 — Challenge Exercise

### Challenge 1: iptables-Based IoT Zone Firewall on a Linux Gateway

Simulate a production IoT gateway firewall policy using `iptables` (or `nftables`) on a Linux machine or VM. The goal is to enforce unidirectional traffic flow: IoT devices may send telemetry outbound to the cloud broker, but no inbound connections from the internet may reach the IoT subnet.

1. Create two virtual network namespaces to simulate an IoT subnet (`iot-ns`) and a WAN interface (`wan-ns`), connected by a virtual ethernet (`veth`) pair:

```bash
# Create namespaces and veth pair
sudo ip netns add iot-ns
sudo ip netns add wan-ns
sudo ip link add veth-iot type veth peer name veth-wan
sudo ip link set veth-iot netns iot-ns
sudo ip link set veth-wan netns wan-ns

# Assign addresses
sudo ip netns exec iot-ns ip addr add 10.10.1.2/24 dev veth-iot
sudo ip netns exec iot-ns ip link set veth-iot up
sudo ip netns exec wan-ns ip addr add 192.168.100.1/24 dev veth-wan
sudo ip netns exec wan-ns ip link set veth-wan up
```

1. Enable IP forwarding on the host and apply the following `iptables` rules in the `FORWARD` chain to allow only ESTABLISHED/RELATED return traffic into the IoT namespace:

```bash
sudo sysctl -w net.ipv4.ip_forward=1

# Allow outbound IoT telemetry (port 8883 MQTT over TLS) to cloud broker
sudo iptables -A FORWARD -s 10.10.1.0/24 -p tcp --dport 8883 -j ACCEPT
sudo iptables -A FORWARD -s 10.10.1.0/24 -p tcp --dport 443  -j ACCEPT

# Allow return traffic for established sessions only
sudo iptables -A FORWARD -d 10.10.1.0/24 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Drop all other inbound traffic to IoT subnet
sudo iptables -A FORWARD -d 10.10.1.0/24 -j DROP
```

1. Verify the rules with `sudo iptables -L FORWARD -nv --line-numbers`. From the `wan-ns` namespace, attempt a new inbound connection to port 22 of the IoT address and confirm it is dropped: `sudo ip netns exec wan-ns nc -zv 10.10.1.2 22`. From the `iot-ns` namespace, confirm outbound TCP to port 8883 reaches its target (use `nc -zv <broker-ip> 8883`). Document the accepted vs. dropped packet counts from the rule listing.

1. Write a brief policy justification (3–4 sentences) explaining why restricting inbound connections to ESTABLISHED/RELATED state prevents lateral movement from a compromised internet host into the IoT zone, and identify which OWASP IoT Top 10 category this control addresses.

---

### Challenge 2: VLAN Tagging Simulation and Network Log Anomaly Analysis

Simulate VLAN segmentation using Linux bridge utilities and analyze synthetic network logs to identify anomalous cross-VLAN traffic.

1. Install `bridge-utils` and `vlan` kernel module, then create a software bridge with two tagged ports representing VLAN 10 (IoT devices) and VLAN 20 (corporate LAN):

```bash
sudo apt-get install -y bridge-utils vlan
sudo modprobe 8021q

# Create bridge
sudo ip link add name br0 type bridge
sudo ip link set br0 up

# Create VLAN-tagged sub-interfaces on a loopback for simulation
sudo ip link add link lo name lo.10 type vlan id 10
sudo ip link add link lo name lo.20 type vlan id 20
sudo ip link set lo.10 up
sudo ip link set lo.20 up
sudo ip addr add 10.10.10.1/24 dev lo.10
sudo ip addr add 10.20.20.1/24 dev lo.20

# Attach to bridge
sudo ip link set lo.10 master br0
sudo ip link set lo.20 master br0
```

1. Generate a synthetic network log file (`/tmp/gateway_log.txt`) with 50 lines mixing normal IoT telemetry (source 10.10.10.x → destination 203.0.113.5:8883) and 5 anomalous entries where a device on the IoT VLAN (10.10.10.x) attempts to reach the corporate VLAN (10.20.20.x). Use this Python script to generate the log:

```python
import random, datetime

lines = []
ts_base = datetime.datetime(2024, 6, 1, 8, 0, 0)
for i in range(50):
    ts = ts_base + datetime.timedelta(seconds=i * 12)
    src = f"10.10.10.{random.randint(2, 5)}"
    if i in [7, 18, 29, 37, 44]:   # anomalous cross-VLAN attempts
        dst = f"10.20.20.{random.randint(10, 20)}"
        port = random.choice([445, 3389, 22])
        action = "BLOCKED"
    else:
        dst = "203.0.113.5"
        port = 8883
        action = "ALLOWED"
    lines.append(f"{ts.isoformat()} SRC={src} DST={dst} DPORT={port} ACTION={action}")

with open("/tmp/gateway_log.txt", "w") as f:
    f.write("\n".join(lines))
print("Log generated:", len(lines), "entries")
```

1. Write a second Python script that reads `/tmp/gateway_log.txt`, identifies all lines where `DST` falls within the `10.20.20.0/24` range, prints each anomalous line with its line number, and outputs a summary: total entries, allowed entries, blocked entries, and cross-VLAN violation count. Confirm your script detects exactly 5 anomalous entries.

---

### Reflection Questions

1. In Challenge 1, the `iptables` policy allows ESTABLISHED/RELATED return traffic but drops new inbound connections. Describe a scenario where an attacker who has already compromised an IoT device on the 10.10.10.0/24 subnet could abuse the ESTABLISHED state rule to exfiltrate data or establish a reverse shell — and explain what additional control (beyond stateful packet filtering) would detect or prevent this.

2. The VLAN segmentation in Challenge 2 relies on the gateway enforcing VLAN membership rules in software. Identify two failure modes where a device on VLAN 10 could still reach VLAN 20 despite the configuration (for example: misconfigured trunk port, VLAN hopping via double-tagging). For each failure mode, describe the specific misconfiguration that enables it and the mitigation.
