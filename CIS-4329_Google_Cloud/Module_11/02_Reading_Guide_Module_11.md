# Reading Guide: Module 11 – Cloud Monitoring, Logging, and Alerting
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 11 – Cloud Monitoring, Logging, and Alerting**! Observability is a critical operations discipline for any cloud environment. This module covers Cloud Monitoring for metrics and uptime checks, Cloud Logging for log ingestion and analysis, Cloud Trace and Cloud Profiler for application performance insights, and alerting policies that notify your team when something goes wrong. The ACE exam tests your ability to configure monitoring resources, write log queries, route logs to storage sinks, and set up alerting policies.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Cloud Monitoring**: GCP's managed monitoring service (part of Google Cloud Observability, formerly Stackdriver). It collects metrics from GCP resources, Compute Engine VMs, GKE clusters, and custom application instrumentation. Metrics are stored as time series and can be visualized in dashboards or used to trigger alerting policies.

*   **Alerting Policy**: A Cloud Monitoring resource that evaluates a metric condition over a time window and sends notifications when the condition is met. An alerting policy consists of a condition (e.g., CPU utilization > 90% for 5 minutes), one or more notification channels (email, PagerDuty, Pub/Sub, SMS), and optional documentation.

*   **Cloud Logging**: GCP's managed log aggregation service. All GCP services write logs to Cloud Logging automatically. Logs are organized into log buckets with configurable retention periods. The default `_Default` log bucket retains logs for 30 days; you can extend retention up to 3,650 days.

*   **Log Sink**: A Cloud Logging resource that routes log entries matching a filter to a destination outside Cloud Logging. Supported destinations include Cloud Storage (for long-term archival), BigQuery (for analytics), Pub/Sub (for streaming to third-party SIEM tools), and a second Cloud Logging bucket. Log sinks are the standard way to implement custom log retention policies.

*   **Log-Based Metric**: A Cloud Monitoring metric derived from log entries. You define a filter that matches specific log entries (e.g., all ERROR severity entries from a Cloud Run service), and Cloud Monitoring increments a counter each time a matching entry arrives. Use log-based metrics to alert on log patterns that have no native metric equivalent.

*   **Cloud Trace**: A distributed tracing service that collects latency data from GCP applications. Cloud Trace shows you where time is spent across microservice calls, helping identify slow dependencies. It integrates with Cloud Run, App Engine, and GKE automatically, and is instrumentable in custom applications via OpenTelemetry.

---

### 2. Certification Exam Tips

*   **Log sinks for custom retention**: The ACE exam frequently tests log sink configuration. Key pattern: if the question asks how to retain audit logs for 5 years, the answer is to create a log sink that exports matching logs to Cloud Storage with a lifecycle policy. The default Cloud Logging retention (30 days) is too short for compliance requirements.

*   **Uptime checks verify external availability**: Cloud Monitoring uptime checks send probe requests to your service endpoints from multiple GCP regions. If the check fails, it triggers an alerting policy. The exam tests whether you know that uptime checks require an HTTPS or HTTP endpoint — they cannot check internal-only (ClusterIP or private IP) endpoints directly.

*   **Notification channels must be created before the alerting policy**: The ACE exam may test ordering. You create notification channels (email, Pub/Sub, Slack webhook) first, then reference them in the alerting policy. A policy with no notification channel fires but silently — no one is notified.

*   **`gcloud logging` commands for the exam**: Know `gcloud logging read` to query logs from the CLI and `gcloud logging sinks create` to create export sinks. The exam tests both Console-based and CLI-based log management.

*   **Study Resource**: The freeCodeCamp ACE course covers Cloud Monitoring dashboards, alerting policy creation, and log sink configuration with hands-on console walkthroughs: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Operations and Observability chapter using the video index.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review the Cloud Monitoring overview including metrics, alerting policies, notification channels, and uptime checks: [Cloud Monitoring Overview](https://cloud.google.com/monitoring/docs/monitoring_overview). Pay attention to how alerting policies are structured.
*   **Required Reading**: Review Cloud Logging concepts including log buckets, log sinks, and the Logs Explorer query language: [Cloud Logging Overview](https://cloud.google.com/logging/docs/overview). The log sink destination types are directly exam-relevant.
*   **Required Video**: Watch the Operations and Observability segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Cloud Monitoring and Logging chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a Cloud Monitoring alerting policy, configure a log sink to Cloud Storage, and query logs using the Logs Explorer. Key commands to practice:

*   `gcloud logging sinks create my-sink storage.googleapis.com/my-bucket --log-filter='severity>=ERROR'` — creates a log sink exporting ERROR+ logs to Cloud Storage
*   `gcloud logging read 'resource.type="gce_instance" AND severity=ERROR' --limit=50` — queries recent error logs from Compute Engine instances
*   `gcloud monitoring channels create --display-name="Ops Email" --type=email --channel-labels=email_address=ops@example.com` — creates an email notification channel
*   `gcloud alpha monitoring policies create --policy-from-file=alert-policy.json` — creates an alerting policy from a JSON definition file

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Cloud Monitoring Overview](https://cloud.google.com/monitoring/docs/monitoring_overview) documentation page.
- [ ] Read the [Cloud Logging Overview](https://cloud.google.com/logging/docs/overview) documentation page.
- [ ] Watch the Operations and Observability segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create an alerting policy and configure a log sink to Cloud Storage.
- [ ] Proceed to the weekly quiz.
