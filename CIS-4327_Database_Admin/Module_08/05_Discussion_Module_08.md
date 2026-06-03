# Discussion Forum: Module 08 — Database Backup and Recovery

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Discussion Prompt

Backup and recovery is the area of database administration where decisions made months before a crisis determine whether the organization survives it. In this discussion, you will analyze a real-world failure scenario and design a backup strategy from scratch.

Respond to **both parts** below.

---

## Part A — Failure Scenario Analysis

A healthcare company runs a Cloud SQL for MySQL 8.0 instance storing patient appointment records. On a Tuesday morning, a developer accidentally runs the following command on the production database:

```sql
DELETE FROM appointments WHERE appointment_date < '2024-01-01';
```

This was intended for a staging environment. The command deletes 847,000 historical appointment records. The mistake is discovered 3 hours later. The database has the following configuration at the time of the incident:

- Automated backups: enabled, daily at 2:00 AM
- Binary log: disabled
- Backup retention: 7 days
- Last backup taken: Tuesday at 2:00 AM (9 hours before the deletion)

Address all four points:

1. **What is recoverable?** Given the existing configuration, what is the most recent state the team can restore to? Will any data be lost? How much?

2. **What configuration change would have prevented data loss?** Specifically, which flag was missing and how would it have enabled a different recovery option?

3. **Recovery procedure:** Walk through the step-by-step gcloud command sequence to recover the deleted records. Include the specific `gcloud sql instances restore-backup` flags needed.

4. **Post-incident architecture:** Recommend two configuration changes to the Cloud SQL instance that would reduce the risk of this class of incident in the future. Consider both backup configuration and any other Cloud SQL features that could help.

---

## Part B — Backup Strategy Design

Design a complete backup strategy for the following system:

A Cloud SQL for PostgreSQL instance runs a financial ledger for a mid-sized credit union. The relevant constraints are:

- Regulatory requirement: transaction records must be recoverable for 7 years
- Business RPO: 15 minutes maximum data loss
- Business RTO: 1 hour maximum downtime
- Database size: 250 GB, growing at 5 GB per month
- Transaction volume: approximately 10,000 write transactions per hour during business hours

Your design must specify:

1. Backup type(s) and frequency
2. Retention configuration (automated backups + transaction logs)
3. Where backups are stored (Cloud SQL only, or additional Cloud Storage archiving)
4. How the 7-year retention requirement is met (Cloud SQL managed backup alone is not sufficient — explain why and what additional step is needed)
5. How often you would test recovery, and what the test procedure looks like

---

## Response Requirements

- Initial post: 400–500 words covering both parts.
- Reply to at least two classmates: 100–150 words each.
- For replies, either identify a gap in your classmate's recovery procedure or propose a more efficient approach to meeting the 7-year retention requirement.

---

## Grading Criteria

| Criterion | Points |
|---|---|
| Part A — all four points addressed with specific commands and flags | 40 |
| Part B — complete strategy addressing all five design points | 40 |
| Two substantive peer replies | 15 |
| Professional writing, accurate terminology | 5 |
| **Total** | **100** |

---

## Instructor Notes

Part A is designed to surface a critical misunderstanding: students often assume they can use Cloud SQL PITR to recover from the deletion, but PITR requires binary logging to be enabled — which it is not in this scenario. The correct answer is that the team can only restore to Tuesday at 2:00 AM, losing all transactions from 2:00 AM to the moment of deletion (approximately 9 hours plus whatever was deleted).

For Part B, the key insight is that Cloud SQL automated backups have a maximum retention of 365 days — far short of the 7-year requirement. Meeting the 7-year requirement requires exporting backups to Cloud Storage with a retention policy or lifecycle rule set to 7 years (2,555 days). Strong posts will mention Cloud Storage Retention Policies to prevent premature deletion of archived exports.
