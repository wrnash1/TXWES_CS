### 1. Video Script 4.1: IAM Roles for Database Administrators
**Estimated Duration:** 6 minutes
**Visual:** Instructor on camera.
**Audio:** "Welcome to Module 4. We've built our databases, made them highly available, and migrated our data. Now, we must secure them. In Google Cloud, access is controlled exclusively through Identity and Access Management, or IAM."
**Visual:** A diagram showing a User, mapped to a Role (Cloud SQL Admin), applied to a Resource (Project).
**[Alt-text: A block diagram showing 'Principal (User)' pointing to 'Role (Cloud SQL Admin)', which points to 'Resource (Project-A)'. Text emphasizes: 'Who can do What on Which Resource'.]**
**Audio:** "IAM answers three questions: Who can do What on Which Resource. You never assign individual permissions directly to a user. Instead, you assign them a Role. A primitive role like 'Owner' or 'Editor' gives broad access to the entire project—never use these for databases. Instead, use predefined roles. The `Cloud SQL Admin` role allows a user to create and delete databases. The `Cloud SQL Client` role only allows them to connect and run queries. The Principle of Least Privilege dictates you only give them the Client role."

---
