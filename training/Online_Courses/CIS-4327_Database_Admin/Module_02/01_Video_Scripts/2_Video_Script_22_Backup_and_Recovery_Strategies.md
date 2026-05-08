### 2. Video Script 2.2: Backup and Recovery Strategies
**Estimated Duration:** 5 minutes
**Visual:** Screencast of the Cloud SQL backup console.
**[Alt-text: A screencast of the Google Cloud Console for a Cloud SQL instance. The user navigates to the 'Backups' tab, selects 'Create backup', and then demonstrates enabling 'Point-in-time recovery'.]**
**Audio:** "High Availability protects you from hardware failures. But what if a developer accidentally runs a `DROP TABLE` command? HA will happily replicate that deletion to the standby instance immediately. To protect against human error, we need backups. Cloud SQL offers automated daily backups and on-demand backups. More importantly, it offers Point-in-Time Recovery (PITR). PITR uses Write-Ahead Logs (WAL) to allow you to restore the database to the exact millisecond right before the developer dropped the table."

---
