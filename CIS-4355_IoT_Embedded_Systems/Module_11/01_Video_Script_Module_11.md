# Video Script: Module 11 — IoT Device Management and OTA Updates

**Course:** CIS-4355 IoT and Embedded Systems

**Institution:** Texas Wesleyan University | Professor Nash

**Estimated Duration:** 20–24 minutes

**Certification Alignment:** IoT Fundamentals / Embedded Systems

---

## SEGMENT 1 — Introduction (0:00–1:30)

Welcome back to CIS-4355. I am Professor Nash. Over the past ten modules we have built embedded hardware, written firmware, connected devices to wireless networks, and pushed telemetry to the cloud. Now we face the question that every production IoT deployment eventually confronts: how do you manage thousands of deployed devices over years of operation?

Device management is the operational spine of any serious IoT program. Without it, your devices drift out of patch compliance, fail silently in the field, and eventually become liabilities rather than assets. OWASP ranks poor device management as two of the top ten IoT vulnerabilities — category 8 (Lack of Device Management) and category 4 (Lack of Secure Update Mechanism). Today we address both.

By the end of this module you will understand how devices are provisioned with a unique cryptographic identity at manufacture, how a device registry tracks thousands of devices, how over-the-air update campaigns deliver firmware safely to staged rollout groups, how health monitoring detects failures before users notice them, and how decommissioning securely retires devices at end-of-life.

---

## SEGMENT 2 — Device Provisioning (1:30–6:00)

### The Identity Problem

Every device in a fleet must have a unique, cryptographically verifiable identity. Without it, your cloud platform cannot distinguish device A from device B, cannot revoke a single compromised device, and cannot audit which device generated a particular event. The process that establishes this identity is called provisioning.

Provisioning happens at manufacture or first deployment. The goal is to generate a unique X.509 certificate and private key for each device, enroll the device in the cloud registry, and load the initial configuration. The critical rule: the private key must be generated on the device itself and must never leave it. If you generate keys on a server and push them to devices, a compromise of that server exposes every device's identity at once.

### How Provisioning Works

Here is the provisioning sequence. A device boots for the first time with a temporary claim certificate — a credential used only for the provisioning handshake. The device connects to a provisioning endpoint, presents its claim certificate, and requests final credentials. The provisioning service verifies the claim, generates a unique device certificate, registers the device in the registry, and pushes the final certificate down to the device. The device stores the final certificate in secure storage, discards the claim certificate, and reboots with its permanent identity.

This pattern — zero-touch provisioning — is implemented by AWS IoT Fleet Provisioning and Azure Device Provisioning Service. The word zero-touch means a technician never manually enrolls each device. Devices self-register on first boot using the claim certificate, and the provisioning service handles enrollment automatically. In a fleet of fifty thousand devices, this is the difference between a one-day deployment and a six-month manual project.

### Secure Storage of Credentials

Where do the private key and final certificate live on the device? The answer matters for security. On a microcontroller with a hardware security module — an HSM or secure element chip — credentials live in hardware-encrypted storage that resists physical extraction. On a general-purpose Linux IoT device, credentials are stored in a protected file system path with restricted permissions, ideally with disk encryption. If an attacker physically extracts a device and reads the flash, they should not be able to recover the private key.

---

## SEGMENT 3 — Device Registry (6:00–10:00)

### What a Registry Does

The device registry is the cloud-side database of record for your fleet. Every enrolled device has an entry. That entry tracks: device identity and certificate status, current firmware version, connectivity state (online or offline and since when), configuration parameters, and custom metadata like location or asset tag.

AWS calls the per-device record a device shadow or thing shadow. Azure calls it a device twin. The concept is the same across platforms: a JSON document in the cloud that represents the device's desired and reported state. When you want to change a device's configuration, you update the desired state in the shadow. The device, on next connection, reads the desired state, applies the change, and reports back the actual state. This desired-versus-reported pattern handles the reality that IoT devices are not always connected — you write your instruction to the shadow, and the device picks it up whenever it comes online.

### Fleet Queries

With a registry, you can query your fleet with precision. Give me all devices running firmware version 2.3.1. Give me all devices in building seven that have been offline for more than twelve hours. Give me all devices in the canary group for the pending firmware release. Without a registry, these questions require manual spreadsheets. With a registry, they are API calls.

The registry also enforces authorization. Only devices with a valid, non-revoked certificate can connect to the message broker. If you suspect a device is compromised, you revoke its certificate in the registry. The device can no longer authenticate — even if it still has its certificate locally. Certificate revocation is the primary security response to a compromised device.

---

## SEGMENT 4 — OTA Update Campaigns (10:00–16:00)

### Why OTA Updates Are Non-Negotiable

Every firmware binary ships with vulnerabilities. Some are discovered the day you release; others surface three years later. In a traditional embedded system you would recall the hardware or dispatch a technician with a programmer. In IoT, you push a firmware update over the air. This capability is not a convenience — it is a security requirement.

OWASP IoT category 4 (Lack of Secure Update Mechanism) describes deployments where devices cannot be patched, or where the update channel is not authenticated and encrypted. An attacker who can inject malicious firmware onto thousands of devices owns those devices. The update mechanism must use signed firmware — meaning the device verifies the manufacturer's cryptographic signature before installing — and encrypted transport over TLS.

### The Staged Rollout Pattern

You never push a firmware update to your entire fleet at once. The staged rollout pattern limits the blast radius of a defective firmware release. The stages are:

First, the canary group — one to five percent of devices, randomly selected or specifically designated. These devices receive the update first. You monitor them for twenty-four to seventy-two hours. If error rates spike or devices start rebooting in a loop, you halt the campaign before touching the rest of the fleet.

Second, the pilot group — ten to twenty percent of devices. If the canary group passes, the pilot group receives the update. Another monitoring period follows.

Third, general availability — the remaining fleet. If the pilot group passes, you roll out to everyone.

### Rollout Halts and Rollbacks

Every OTA campaign management system — AWS IoT Jobs, Azure IoT Hub automatic deployments, Mender.io — supports automatic halts. You define a success threshold: if fewer than ninety-five percent of devices in the current stage acknowledge success within forty-eight hours, halt the campaign automatically. When a campaign halts, you investigate, fix the firmware, and restart the staged rollout with a new candidate build.

Rollback means pushing the previous firmware version as a new campaign. There is no magic undo button. The rollback is itself a staged OTA campaign. This is why you always maintain the previous validated firmware version in your artifact store.

### Update Integrity: Signing and Verification

Every firmware binary must be signed by the manufacturer before distribution. The signature is created with the manufacturer's private signing key. The device holds the corresponding public verification key in read-only storage — ideally in a secure element. Before installing any firmware, the bootloader verifies the signature using that public key. If verification fails, the device rejects the binary and continues running the current firmware. This prevents an attacker who intercepts the OTA channel from pushing malicious code to your fleet.

---

## SEGMENT 5 — Device Health Monitoring (16:00–19:30)

### What to Monitor

Health monitoring is continuous observation of device telemetry to detect failures and anomalies. At minimum you monitor: CPU load, memory utilization, battery level or power supply voltage, connectivity uptime, firmware version, and error log rates. On a constrained microcontroller you may only be able to report a heartbeat message once per minute — but even the absence of a heartbeat is meaningful information.

Cloud platforms provide device metrics dashboards out of the box. In AWS IoT, Device Defender monitors device behavior against a trained baseline and fires alerts when a device starts making unexpected DNS lookups or opens ports it has never used before — behavioral signatures of compromise or malfunction.

### Proactive vs. Reactive Maintenance

The value of health monitoring is proactive maintenance. Without it, you learn a device has failed when a customer calls. With it, you learn a device's battery is at twelve percent and dispatch a replacement before it dies. In industrial IoT — a factory floor, a utility grid, a pipeline monitoring system — proactive maintenance is the entire business value proposition.

Anomaly detection goes further. If a device that normally reports twelve telemetry events per hour suddenly reports twelve thousand, that is an anomaly. It might be a firmware bug causing a reporting loop. It might be a compromised device exfiltrating data. Either way, your monitoring platform fires an alert and flags the device for investigation before the problem reaches users or the backend.

---

## SEGMENT 6 — Device Decommissioning (19:30–21:30)

### The Decommissioning Checklist

Decommissioning is the formal process of retiring a device at end-of-life or when it is replaced. It is not optional. An improperly decommissioned device leaves active credentials in the world — credentials an attacker could use to impersonate the device, inject false telemetry into your backend, or gain a foothold into your cloud infrastructure.

The decommissioning checklist has four steps. First: revoke the device's X.509 certificate in the cloud registry. The device can no longer authenticate even if the certificate is still physically present on the hardware. Second: delete the device twin or shadow from the registry to remove the cloud-side state record. Third: perform cryptographic erasure on the device — overwrite the flash sectors containing the private key and certificate with zeros or random data. Simply deleting a file is not enough; the flash sectors must be explicitly overwritten. Fourth: physical disposal — follow your organization's e-waste and data destruction policy.

### Why Revocation Alone Is Not Enough

Revoking the certificate stops the device from connecting to your cloud broker. But if the decommissioned hardware ends up in a salvage bin and someone recovers it, they have a device with embedded credentials. If those credentials were not erased from flash, the recovered device exposes the private key to analysis. Defense in depth means both revoke in the cloud and erase on the device.

---

## SEGMENT 7 — Exam Prep and Summary (21:30–23:00)

Let us close with the high-yield exam points for this module.

Provisioning establishes unique cryptographic identity at manufacture or first boot using a claim certificate that is replaced by a final device certificate. The private key is generated on the device and never exported.

The device registry is the authoritative record of every enrolled device. AWS calls the per-device record a device shadow. Azure calls it a device twin. The desired-versus-reported pattern in the shadow handles disconnected devices gracefully.

OTA update campaigns use staged rollout — canary group, pilot group, then general availability — to limit blast radius. Campaigns halt automatically if success rates fall below the configured threshold. Firmware must be signed by the manufacturer and verified by the bootloader before installation.

Health monitoring detects offline devices, performance degradation, and behavioral anomalies. AWS IoT Device Defender does behavioral baselining. Proactive monitoring enables dispatch before failure rather than after.

Decommissioning requires four steps: revoke the certificate, delete the device twin, cryptographically erase credentials on-device, and physically dispose following e-waste policy.

For your certification exam, know OWASP IoT categories 4 and 8 by name and description, understand zero-touch provisioning with claim certificates, and be able to explain the rationale for staged OTA rollouts. These topics appear in certification scenario questions regularly.

I will see you in Module 12, where we go deep on IoT security architecture — attack surfaces, network segmentation, and secure-by-design principles. See you there.

---

End of Module 11 Video Script

Professor Nash | CIS-4355 IoT and Embedded Systems | Texas Wesleyan University
