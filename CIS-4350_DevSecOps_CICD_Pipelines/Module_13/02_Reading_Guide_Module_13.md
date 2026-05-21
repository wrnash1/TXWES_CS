# Reading Guide: Module 13 - Compliance as Code – OPA and Policy Enforcement

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

### Introduction

Welcome to **Module 13 - Compliance as Code – OPA and Policy Enforcement**! This module covers the practice of defining security and compliance policies as code — using tools like Open Policy Agent (OPA) and Rego — and enforcing those policies automatically within CI/CD pipelines and Kubernetes admission control. Rather than relying on periodic audits and manual checklists, Compliance as Code embeds policy checks into every pipeline run and every Kubernetes resource creation event, providing continuous compliance assurance. This approach is a key DevSecOps maturity indicator and is tested directly on the CDP exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The CDP certification exam expects you to recognize and apply these concepts in scenario-based questions:

* **Log aggregates**: Collections of log entries from multiple sources (application logs, infrastructure logs, pipeline audit logs, Kubernetes audit logs) consolidated into a centralized storage and query system. In a compliance context, aggregate logs provide the evidence trail that policies were enforced, scans were run, and access was controlled — critical for audit and regulatory reporting.

* **Application telemetry**: The continuous stream of metrics, traces, and logs emitted by a running application and its supporting infrastructure. In a DevSecOps context, telemetry data feeds security dashboards and anomaly detection systems that identify policy violations, unusual access patterns, and security incidents in real time.

* **ELK stack**: The combination of Elasticsearch (data store and search engine), Logstash (log ingestion and transformation pipeline), and Kibana (visualization and dashboard interface) used for centralized log aggregation and security event analysis. The ELK stack (or its modern successor, the Elastic Stack with Beats) is a common foundation for DevSecOps security monitoring dashboards.

* **Prometheus**: An open-source metrics collection and alerting system widely used in Kubernetes environments. Prometheus scrapes metrics from application and infrastructure exporters, stores them as time-series data, and evaluates alerting rules — triggering notifications when metrics breach defined thresholds (e.g., error rate spikes, unusual authentication failure rates) that may indicate security incidents.

* **System alerts**: Automated notifications generated when monitored metrics or log patterns cross defined thresholds, indicating potential security events, policy violations, or system failures. In a DevSecOps pipeline, alerts from Prometheus, ELK, or SIEM systems feed back into the incident response workflow, closing the feedback loop between production security monitoring and development response.

---

### 2. Certification Exam Tips

* **OPA and Rego**: Open Policy Agent is a general-purpose policy engine; Rego is its declarative policy language. The CDP exam tests OPA's use in two contexts: (1) Kubernetes admission control via OPA Gatekeeper (validates resource manifests before they are stored in etcd), and (2) CI/CD pipeline policy checks (evaluating Terraform plans, IaC configs, or pipeline parameters against Rego policies before deployment).
* **Compliance as Code vs. Compliance by Audit**: Distinguish between periodic manual audits (detective, after-the-fact) and Compliance as Code (preventive, every pipeline run). The CDP exam favors Compliance as Code answers when asking about how to continuously enforce security policies in a DevSecOps context.
* **SIEM Integration**: Know that security event data from CI/CD pipelines, container runtimes, and Kubernetes audit logs feeds into SIEM systems (Splunk, IBM QRadar, Microsoft Sentinel) for correlation and incident detection. Pipeline audit logs are a key data source for proving compliance during regulatory audits.
* **Study Resource**: The [Open Policy Agent documentation](https://www.openpolicyagent.org/docs/latest/) provides the authoritative reference for OPA concepts, Rego policy language, and Kubernetes integration via OPA Gatekeeper — review the "How Does OPA Work" and "Kubernetes" sections for CDP exam scenarios.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading**: Read the [Open Policy Agent documentation introduction](https://www.openpolicyagent.org/docs/latest/) — covers OPA's architecture, how Rego policies are evaluated, how OPA integrates with Kubernetes as an admission controller (OPA Gatekeeper), and how it can enforce policies in CI/CD pipelines. Focus on the Kubernetes admission control use case.
* **Required Video**: Watch the monitoring, logging, and compliance segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg) — covers application telemetry flows, centralized log dashboards, and how pipeline audit logs support compliance reporting.

---

### Lab & Command Integration

In this week's hands-on lab, you will implement monitoring and compliance controls by:

* **Map application telemetry flows**: Diagram the data flow from application metrics (Prometheus scrape targets) through alerting rules to notification channels (PagerDuty, Slack), identifying where security-relevant metrics (authentication failures, error rates) are instrumented.
* **Configure alert parameters on server failure states**: Write a Prometheus alerting rule (in `alerts.yaml`) that fires when the HTTP 5xx error rate exceeds a threshold for more than 5 minutes, representing a potential security incident or service degradation event.
* **Review centralized logs dashboards**: Using a sample Kibana or Grafana dashboard, identify key security event log patterns — failed login attempts, unauthorized API calls, pipeline scan failures — and document how each pattern would trigger an incident response workflow.

---

### 3. Study Checklist

* [ ] Read the glossary terms and understand how log aggregation, telemetry, and alerting together provide continuous compliance evidence.
* [ ] Read the Open Policy Agent documentation at [https://www.openpolicyagent.org/docs/latest/](https://www.openpolicyagent.org/docs/latest/).
* [ ] Watch the monitoring and compliance segment of [CI/CD Pipeline & DevSecOps Course by freeCodeCamp](https://www.youtube.com/watch?v=scEDHsr3APg).
* [ ] Complete the Prometheus alerting rule configuration and log dashboard review in the lab activity.
* [ ] Proceed to the weekly hands-on lab activity.
