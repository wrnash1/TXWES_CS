# Lab Activity – Module 06: IoT Cloud Platforms – AWS IoT Core, Azure IoT Hub, GCP IoT

**Course:** CIS-4355 IoT and Embedded Systems
**Instructor:** Professor Nash
**Points:** 100
**Submission:** Canvas – Module 06 Lab Assignment

---

## Overview

In this lab you will analyze AWS IoT Core policy documents for security violations, trace a Device Shadow synchronization sequence, evaluate Azure Device Twin configurations, and assess a GCP Pub/Sub access control setup. All work is analytical and written — no cloud account is required.

---

## Learning Objectives

By completing this lab you will be able to:

- Read an AWS IoT Core Policy JSON document and identify least-privilege violations.
- Trace an AWS Device Shadow desired/reported/delta sequence for a device reconnecting after offline period.
- Evaluate Azure Device Twin configurations for operational and security issues.
- Assess GCP Pub/Sub IAM access controls for data exposure risks.
- Compare all three platforms' authentication mechanisms and state synchronization models.

---

## Prerequisites

- Completed Module 06 video lecture and reading guide.
- No cloud account required. All analysis uses provided documents and scenarios.

---

## Part 1: AWS IoT Core Policy Analysis (30 points)

### Part 1 Background

AWS IoT Core policies are JSON documents using IAM-style Allow/Deny rules. Each statement specifies:

- Effect: Allow or Deny.
- Action: one or more IoT actions such as iot:Connect, iot:Publish, iot:Subscribe, iot:Receive.
- Resource: the ARN (Amazon Resource Name) of the topic, client, or shadow resource.

A secure policy grants only the minimum actions on the minimum resources required for a specific device.

### Part 1 Policy Documents

The following three policy documents are submitted for security review. Analyze each one.

Policy A (submitted for device sensor-node-42 in region us-east-1 account 123456789012):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iot:*",
      "Resource": "*"
    }
  ]
}
```

Policy B (submitted for temperature sensor fleet):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["iot:Connect"],
      "Resource": "arn:aws:iot:us-east-1:123456789012:client/${iot:ClientId}"
    },
    {
      "Effect": "Allow",
      "Action": ["iot:Publish"],
      "Resource": "arn:aws:iot:us-east-1:123456789012:topic/sensors/${iot:ClientId}/temperature"
    },
    {
      "Effect": "Allow",
      "Action": ["iot:Subscribe", "iot:Receive"],
      "Resource": "arn:aws:iot:us-east-1:123456789012:topicfilter/$aws/things/${iot:ClientId}/shadow/update/delta"
    }
  ]
}
```

Policy C (submitted for actuator controller fleet):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["iot:Connect", "iot:Publish", "iot:Subscribe", "iot:Receive"],
      "Resource": "arn:aws:iot:us-east-1:123456789012:*"
    }
  ]
}
```

### Part 1 Questions

For each policy, answer all three sub-questions:

Question 1A: Is Policy A least-privilege compliant? Identify every specific violation. If a sensor node using Policy A had its certificate stolen, what is the full scope of access the attacker would have? Rewrite Policy A as a least-privilege policy for a sensor node that only publishes temperature readings and subscribes to its own shadow delta.

Question 1B: Evaluate Policy B. Is it correctly scoped? Explain what the `${iot:ClientId}` substitution variable does and why it is critical for this policy to be secure. Would Policy B still be safe if two sensor devices shared the same Client ID?

Question 1C: Is Policy C acceptably scoped? Identify the specific security issue with the resource ARN and explain what it permits. Propose a corrected policy for an actuator device that must subscribe to a command topic and publish a status topic, both scoped to the device's own Client ID.

### Part 1 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1A: Violations identified, attack scope explained, corrected policy written | 12 |
| Question 1B: Policy B evaluated correctly, ClientId variable explained, shared-ID risk addressed | 9 |
| Question 1C: Issue identified, corrected policy provided with correct ARN scoping | 9 |
| Total | 30 |

---

## Part 2: AWS Device Shadow Trace (25 points)

### Part 2 Instructions

Analyze the following Device Shadow scenario and answer all five questions.

A temperature controller device (Thing Name: hvac-unit-07) has been offline for 4 hours. During that time, the facility manager updated the desired setpoint from 72°F to 68°F and enabled a new setting called economy_mode.

The Device Shadow document at the time the device reconnects:

```json
{
  "state": {
    "desired": {
      "setpoint_f": 68,
      "economy_mode": true,
      "fan_speed": "auto"
    },
    "reported": {
      "setpoint_f": 72,
      "fan_speed": "auto",
      "firmware_version": "2.1.4"
    }
  },
  "metadata": {
    "desired": {
      "setpoint_f": {"timestamp": 1717305600},
      "economy_mode": {"timestamp": 1717305600},
      "fan_speed": {"timestamp": 1717290000}
    },
    "reported": {
      "setpoint_f": {"timestamp": 1717291200},
      "fan_speed": {"timestamp": 1717291200},
      "firmware_version": {"timestamp": 1717291200}
    }
  },
  "version": 14,
  "timestamp": 1717305600
}
```

Question 1: What delta document does AWS IoT Core deliver to hvac-unit-07 on reconnect? Write out the complete delta JSON structure.

Question 2: After the device applies the setpoint and economy_mode changes, it publishes an update to the shadow. Write the JSON body of the MQTT PUBLISH message the device sends to the shadow update topic to report the new state.

Question 3: The `fan_speed` property appears in both desired and reported with the same value "auto". Does this property appear in the delta? Explain why or why not.

Question 4: The device does not know about the `economy_mode` setting because its firmware version 2.1.4 predates the feature. What should a well-designed device firmware do when it receives a desired property it does not recognize?

Question 5: The desired shadow update was made at timestamp 1717305600 and the reported setpoint was last updated at 1717291200. What does this difference indicate, and why is tracking these timestamps important for fleet management?

### Part 2 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1: Correct delta document written (setpoint_f and economy_mode only) | 7 |
| Question 2: Correct shadow update PUBLISH body written | 5 |
| Question 3: fan_speed delta exclusion correctly explained | 5 |
| Question 4: Unknown property handling behavior correctly described | 4 |
| Question 5: Timestamp significance accurately explained | 4 |
| Total | 25 |

---

## Part 3: Azure Device Twin Analysis (20 points)

### Part 3 Instructions

Review the following Azure IoT Hub Device Twin document for a smart building occupancy sensor and answer the three questions.

```json
{
  "deviceId": "occupancy-sensor-b3-204",
  "etag": "AAAAAAAAAAE=",
  "status": "enabled",
  "tags": {
    "building": "B",
    "floor": 3,
    "room": 204,
    "sensor_type": "PIR"
  },
  "properties": {
    "desired": {
      "reporting_interval_sec": 30,
      "motion_threshold": 0.85,
      "firmware_target": "3.2.0",
      "$version": 12
    },
    "reported": {
      "reporting_interval_sec": 60,
      "motion_threshold": 0.85,
      "firmware_version": "3.1.2",
      "$version": 9
    }
  }
}
```

Question 1: List all properties that are out of sync between desired and reported. For each property, describe what action the device should take to bring itself into the desired state.

Question 2: The tags section contains building, floor, and room metadata. Explain how a facility manager could use the IoT Hub Registry query language to find all sensors on Floor 3 of Building B that are currently running firmware older than 3.2.0. Describe the query structure (you do not need to know exact Azure SDK syntax — describe it in plain English).

Question 3: The `$version` field is 12 in desired and 9 in reported. Explain what the version number represents and what it indicates when desired version is higher than reported version.

### Part 3 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1: Out-of-sync properties identified and required device actions described | 8 |
| Question 2: Fleet query approach accurately described | 6 |
| Question 3: Version field meaning and implication correctly explained | 6 |
| Total | 20 |

---

## Part 4: GCP Pub/Sub Access Control Review (25 points)

### Part 4 Instructions

A GCP IoT Core deployment routes telemetry from 800 smart grid power meters to a Pub/Sub topic named `projects/util-corp-prod/topics/meter-telemetry`. Answer all four questions in complete sentences.

Question 1: An audit reveals the Pub/Sub topic has the following IAM binding: `allUsers: roles/pubsub.subscriber`. Explain what this binding permits, identify the OWASP IoT Top 10 item it violates, and describe the specific data exposure risk given that the topic receives power consumption readings from 800 residential meters.

Question 2: The correct IAM binding should restrict the `roles/pubsub.subscriber` role to a specific service account used by the analytics pipeline. Describe the corrected binding in plain English and explain why using a dedicated service account (rather than a user account) is a best practice for automated pipelines.

Question 3: GCP IoT Core devices authenticate using JWTs signed with device private keys. The utility provisioned all 800 meters with the same RSA key pair to simplify manufacturing. One meter is physically stolen and the private key is extracted from its firmware. Describe the full scope of what the attacker can now do on the GCP IoT Core platform and why the blast radius extends beyond the stolen meter's data.

Question 4: Propose a three-step remediation plan for the utility that addresses the shared key problem, the compromised key, and the public Pub/Sub binding. Be specific about what action must be taken at each step and in what order.

### Part 4 Grading Rubric

| Criterion | Points |
|---|---|
| Question 1: Binding effect explained, OWASP item correct, data exposure risk specific | 7 |
| Question 2: Corrected binding described, service account rationale explained | 6 |
| Question 3: Attack scope accurately described including cross-device impact | 6 |
| Question 4: Three-step remediation specific, ordered correctly | 6 |
| Total | 25 |

---

## Submission Checklist

- [ ] Part 1: All three policy analysis questions answered with corrected policies.
- [ ] Part 2: All five Device Shadow trace questions answered with JSON documents where required.
- [ ] Part 3: All three Device Twin analysis questions answered.
- [ ] Part 4: All four GCP Pub/Sub review questions answered.

---

## Overall Grading Summary

| Part | Description | Points |
|---|---|---|
| 1 | AWS IoT Core policy analysis | 30 |
| 2 | AWS Device Shadow trace | 25 |
| 3 | Azure Device Twin analysis | 20 |
| 4 | GCP Pub/Sub access control review | 25 |
| Total | | 100 |

---

End of Lab – Module 06
