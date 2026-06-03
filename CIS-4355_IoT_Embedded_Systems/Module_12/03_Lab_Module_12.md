# Lab Activity: Module 12 — IoT Security

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Time:** 90–120 minutes

---

## Objective

In this lab you will implement the core security controls covered in Module 12: TLS-secured MQTT communications, certificate-based device authentication using mutual TLS, and a firmware signing workflow using OpenSSL. By the end of this lab you will have hands-on experience with the cryptographic operations that underpin production IoT deployments.

---

## Prerequisites

- Ubuntu 20.04 or later, macOS 12 or later, or WSL2 on Windows 11
- OpenSSL 1.1.1 or later (`openssl version` to check)
- Mosquitto MQTT broker (`sudo apt install mosquitto mosquitto-clients` on Ubuntu)
- Python 3.9 or later with the `paho-mqtt` library (`pip install paho-mqtt`)
- Basic familiarity with terminal commands

---

## Part 1 — Generate a Certificate Authority and Device Certificate

### Step 1.1 — Create a working directory

```bash
mkdir -p ~/iot-security-lab/certs && cd ~/iot-security-lab
```

### Step 1.2 — Generate the CA private key and self-signed certificate

```bash
# Generate a 256-bit ECDSA private key for the CA
openssl ecparam -name prime256v1 -genkey -noout \
  -out certs/ca.key

# Create the CA self-signed certificate (valid 3650 days = 10 years)
openssl req -new -x509 -days 3650 \
  -key certs/ca.key \
  -out certs/ca.crt \
  -subj "/C=US/ST=Texas/O=TXWES IoT Lab/CN=IoT Lab Root CA"
```

Verify the certificate was created:

```bash
openssl x509 -in certs/ca.crt -noout -text | grep -E "Subject:|Issuer:|Not"
```

Expected output shows Subject and Issuer are identical (self-signed) and the validity period spans 10 years.

### Step 1.3 — Generate the broker server certificate

```bash
# Generate server private key
openssl ecparam -name prime256v1 -genkey -noout \
  -out certs/server.key

# Generate a Certificate Signing Request (CSR)
openssl req -new \
  -key certs/server.key \
  -out certs/server.csr \
  -subj "/C=US/ST=Texas/O=TXWES IoT Lab/CN=localhost"

# Sign the server CSR with the CA key
openssl x509 -req -days 365 \
  -in certs/server.csr \
  -CA certs/ca.crt \
  -CAkey certs/ca.key \
  -CAcreateserial \
  -out certs/server.crt
```

### Step 1.4 — Generate a device client certificate

```bash
# Generate device private key
openssl ecparam -name prime256v1 -genkey -noout \
  -out certs/device-001.key

# Generate device CSR — the CN contains the device ID
openssl req -new \
  -key certs/device-001.key \
  -out certs/device-001.csr \
  -subj "/C=US/ST=Texas/O=TXWES IoT Lab/CN=device-001"

# Sign the device CSR with the CA key
openssl x509 -req -days 365 \
  -in certs/device-001.csr \
  -CA certs/ca.crt \
  -CAkey certs/ca.key \
  -CAcreateserial \
  -out certs/device-001.crt
```

Verify all three certificates (CA, server, device) are present:

```bash
ls -la certs/
```

---

## Part 2 — Configure Mosquitto with TLS and mTLS

### Step 2.1 — Create the Mosquitto configuration file

```bash
cat > ~/iot-security-lab/mosquitto-tls.conf << 'EOF'
# Standard listener on port 1883 (plaintext) — we will test rejecting this
listener 1883

# TLS listener on port 8883
listener 8883
certfile /home/USER/iot-security-lab/certs/server.crt
keyfile  /home/USER/iot-security-lab/certs/server.key
cafile   /home/USER/iot-security-lab/certs/ca.crt

# Require client certificates (mutual TLS)
require_certificate true
use_identity_as_username true

allow_anonymous false
EOF
```

Replace `USER` with your actual username, or use `$HOME`:

```bash
sed -i "s|/home/USER|$HOME|g" ~/iot-security-lab/mosquitto-tls.conf
```

### Step 2.2 — Start the Mosquitto broker

```bash
mosquitto -c ~/iot-security-lab/mosquitto-tls.conf -v &
```

The `-v` flag enables verbose logging. You should see output similar to:

```text
1717200000: mosquitto version 2.0.x starting
1717200000: Opening ipv4 listen socket on port 1883
1717200000: Opening ipv4 listen socket on port 8883
```

---

## Part 3 — Test TLS-Secured MQTT Connections

### Step 3.1 — Subscribe using the device certificate (should succeed)

Open a second terminal:

```bash
mosquitto_sub \
  --host localhost \
  --port 8883 \
  --cafile ~/iot-security-lab/certs/ca.crt \
  --cert ~/iot-security-lab/certs/device-001.crt \
  --key ~/iot-security-lab/certs/device-001.key \
  --topic "sensors/temperature" \
  --tls-version tlsv1.3 \
  --id device-001 \
  -v
```

You should see no errors and the client should be waiting for messages.

### Step 3.2 — Publish a test message using the device certificate

Open a third terminal:

```bash
mosquitto_pub \
  --host localhost \
  --port 8883 \
  --cafile ~/iot-security-lab/certs/ca.crt \
  --cert ~/iot-security-lab/certs/device-001.crt \
  --key ~/iot-security-lab/certs/device-001.key \
  --topic "sensors/temperature" \
  --message '{"device_id":"device-001","temp_c":22.5,"timestamp":1717200000}' \
  --tls-version tlsv1.3 \
  -d
```

The subscriber terminal should display the received JSON message. Record this output for your deliverable.

### Step 3.3 — Attempt a plaintext connection (should be rejected)

```bash
mosquitto_pub \
  --host localhost \
  --port 1883 \
  --topic "sensors/temperature" \
  --message "unauthorized plaintext attempt" \
  -d
```

This command should fail because the plaintext listener does not have `allow_anonymous true`. If you configured the broker without password files for port 1883, the connection will be refused. Record the error message.

### Step 3.4 — Attempt a TLS connection without a client certificate (should be rejected)

```bash
mosquitto_pub \
  --host localhost \
  --port 8883 \
  --cafile ~/iot-security-lab/certs/ca.crt \
  --topic "sensors/temperature" \
  --message "no client cert" \
  -d
```

Because `require_certificate true` is set, this connection should fail with a TLS handshake error. Record the error message.

---

## Part 4 — Firmware Signing Simulation

This section simulates the firmware signing workflow that runs in a real OTA update pipeline.

### Step 4.1 — Create a simulated firmware binary

```bash
mkdir -p ~/iot-security-lab/firmware

# Create a test "firmware" file (simulating a compiled binary)
echo "FIRMWARE_VERSION=2.1.0 BUILD_DATE=2026-06-02 PAYLOAD=$(head -c 512 /dev/urandom | base64)" \
  > ~/iot-security-lab/firmware/firmware_v2.1.0.bin
```

### Step 4.2 — Generate the firmware signing key pair

```bash
# Generate the signing private key (kept on signing server — never on device)
openssl ecparam -name prime256v1 -genkey -noout \
  -out ~/iot-security-lab/firmware/signing.key

# Derive the public key (stored in device flash at manufacturing time)
openssl ec -in ~/iot-security-lab/firmware/signing.key \
  -pubout \
  -out ~/iot-security-lab/firmware/signing.pub
```

### Step 4.3 — Sign the firmware image

```bash
# Compute the SHA-256 hash and sign it with ECDSA
openssl dgst -sha256 -sign ~/iot-security-lab/firmware/signing.key \
  -out ~/iot-security-lab/firmware/firmware_v2.1.0.sig \
  ~/iot-security-lab/firmware/firmware_v2.1.0.bin

echo "Firmware signed. Signature file:"
ls -lh ~/iot-security-lab/firmware/firmware_v2.1.0.sig
```

### Step 4.4 — Verify the firmware signature (bootloader simulation)

```bash
# This is what the device bootloader does on every OTA update
openssl dgst -sha256 -verify ~/iot-security-lab/firmware/signing.pub \
  -signature ~/iot-security-lab/firmware/firmware_v2.1.0.sig \
  ~/iot-security-lab/firmware/firmware_v2.1.0.bin
```

Expected output: `Verified OK`

### Step 4.5 — Tamper test — modify the firmware and re-verify

```bash
# Simulate firmware tampering: append a byte to the binary
echo "TAMPERED" >> ~/iot-security-lab/firmware/firmware_v2.1.0.bin

# Attempt verification — should fail
openssl dgst -sha256 -verify ~/iot-security-lab/firmware/signing.pub \
  -signature ~/iot-security-lab/firmware/firmware_v2.1.0.sig \
  ~/iot-security-lab/firmware/firmware_v2.1.0.bin
```

Expected output: `Verification Failure`

This demonstrates that even a single-byte change to the firmware binary causes signature verification to fail — the bootloader would reject this image and keep running the previous firmware.

---

## Part 5 — Python MQTT Client with TLS (Bonus)

Create a Python script that simulates a device publishing sensor data over mTLS:

```python
# file: ~/iot-security-lab/mqtt_tls_client.py
import paho.mqtt.client as mqtt
import ssl
import json
import time
import os

BASE = os.path.expanduser("~/iot-security-lab")
CERTS = f"{BASE}/certs"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[INFO] Connected to broker with mTLS")
    else:
        print(f"[ERROR] Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"[INFO] Message published (mid={mid})")

client = mqtt.Client(client_id="device-001-python")
client.on_connect = on_connect
client.on_publish = on_publish

# Configure TLS with mutual authentication
client.tls_set(
    ca_certs=f"{CERTS}/ca.crt",
    certfile=f"{CERTS}/device-001.crt",
    keyfile=f"{CERTS}/device-001.key",
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.connect("localhost", 8883, keepalive=60)
client.loop_start()

for i in range(5):
    payload = json.dumps({
        "device_id": "device-001",
        "reading": i,
        "temp_c": 20.0 + i * 0.5,
        "timestamp": int(time.time())
    })
    client.publish("sensors/temperature", payload, qos=1)
    print(f"[INFO] Published: {payload}")
    time.sleep(1)

client.loop_stop()
client.disconnect()
print("[INFO] Disconnected")
```

Run the script while your `mosquitto_sub` subscriber is active:

```bash
python3 ~/iot-security-lab/mqtt_tls_client.py
```

Verify that all five messages appear in the subscriber terminal.

---

## Troubleshooting Guide

- **Error: Connection refused on port 8883** — Verify Mosquitto is running (`ps aux | grep mosquitto`). Check the config file paths resolve correctly.
- **Error: SSL: CERTIFICATE_VERIFY_FAILED** — The CA certificate path in your command may be wrong. Use the absolute path (`$HOME/iot-security-lab/certs/ca.crt`).
- **Error: No client certificate provided** — Ensure you are passing both `--cert` and `--key` flags in the mosquitto_pub/sub command.
- **Error: Verification Failure on original firmware** — Re-sign the firmware; the test file may have been modified. Re-run Step 4.1 through 4.4 with a fresh binary.
- **Python ImportError: No module named paho** — Run `pip3 install paho-mqtt` and ensure you are using the correct Python interpreter.

---

## Deliverables

Submit the following to the Canvas LMS assignment portal:

1. Screenshot or terminal output from Step 3.2 showing the successful TLS-authenticated MQTT publish and receive.
2. Screenshot or terminal output from Steps 3.3 and 3.4 showing the two rejected connection attempts and their error messages.
3. Screenshot or terminal output from Steps 4.4 and 4.5 showing `Verified OK` followed by `Verification Failure`.
4. Written answer (100–150 words): Explain why the firmware signature fails verification after the tamper test in Step 4.5. In your answer, describe the cryptographic relationship between the SHA-256 hash, the ECDSA signature, and the public key.
5. Bonus deliverable (optional, 5 extra-credit points): Screenshot showing all five Python MQTT messages received by the Mosquitto subscriber, with timestamps.

---
