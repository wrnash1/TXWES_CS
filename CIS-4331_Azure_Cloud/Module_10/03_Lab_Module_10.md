# Lab Activity: Module 10 — Azure Databases

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 100 | AZ-900 Alignment: Describe Azure database and analytics services

---

## Lab Overview

In this lab you will create an Azure SQL Database using the Azure Portal and Azure CLI, configure firewall rules, connect using the built-in Query Editor, create a sample database schema, insert data, and run queries. You will also create an Azure Cosmos DB account and explore its core concepts. This hands-on experience demonstrates the PaaS database model and the difference between relational and NoSQL services.

**Estimated Time:** 60–75 minutes

**Prerequisites:**

- Active Azure account (free trial or student subscription)
- Azure Cloud Shell access
- Completion of Lab Modules 07–09

---

## Learning Objectives

By completing this lab you will be able to:

- Create an Azure SQL logical server and database using the Portal and CLI
- Configure SQL firewall rules to allow Azure services and client access
- Use the Azure Portal Query Editor to create tables and run SQL queries
- Create an Azure Cosmos DB account with Core SQL API
- Insert and query documents in Cosmos DB using Data Explorer
- Explain the difference between relational and NoSQL database interaction patterns

---

## Part 1: Create the Resource Group (3 minutes)

```bash
az group create \
  --name lab10-rg \
  --location eastus
```

---

## Part 2: Create an Azure SQL Database (20 minutes)

**Step 2.1 — Create the SQL Logical Server**

Replace `[initials]` with your initials. The server name must be globally unique.

```bash
az sql server create \
  --name lab10sqlserver[initials] \
  --resource-group lab10-rg \
  --location eastus \
  --admin-user sqladmin \
  --admin-password "TxWes@2024!"
```

Note: Save the server name and password — you will use them to connect.

**Step 2.2 — Create the Database**

```bash
az sql db create \
  --resource-group lab10-rg \
  --server lab10sqlserver[initials] \
  --name lab10db \
  --service-objective S0
```

S0 is a Standard tier SKU appropriate for lab use. It provides 10 DTUs and 250 GB max storage.

**Step 2.3 — Configure Firewall Rules**

Allow Azure services (needed for Portal Query Editor):

```bash
az sql server firewall-rule create \
  --resource-group lab10-rg \
  --server lab10sqlserver[initials] \
  --name AllowAzureServices \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0
```

Get your current public IP and allow it:

```bash
# Get your current public IP
MY_IP=$(curl -s https://api.ipify.org)
echo "Your IP: $MY_IP"

az sql server firewall-rule create \
  --resource-group lab10-rg \
  --server lab10sqlserver[initials] \
  --name AllowMyIP \
  --start-ip-address $MY_IP \
  --end-ip-address $MY_IP
```

**Step 2.4 — Verify Database Creation**

```bash
az sql db show \
  --resource-group lab10-rg \
  --server lab10sqlserver[initials] \
  --name lab10db \
  --query "{name:name, status:status, sku:currentServiceObjectiveName, maxSizeGB:maxSizeBytes}" \
  --output table
```

[SHOW AZURE PORTAL] Navigate to Azure SQL Databases > lab10db > Overview. Point out the server name, subscription, resource group, and the "Query editor (preview)" menu item.

---

## Part 3: Create a Schema and Insert Data Using Query Editor (15 minutes)

**Step 3.1 — Open the Query Editor**

1. In the Azure Portal, navigate to your SQL database (lab10db)
2. In the left menu, click **Query editor (preview)**
3. Log in with:
   - Authentication type: SQL server authentication
   - Login: `sqladmin`
   - Password: `TxWes@2024!`
4. Click **OK**

**Step 3.2 — Create a Table**

In the Query Editor, paste and run the following SQL:

```sql
CREATE TABLE Students (
    StudentId INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    Major NVARCHAR(50),
    EnrollmentYear INT,
    GPA DECIMAL(3,2)
);
```

Click **Run**. The Messages panel should show "Command(s) completed successfully."

**Step 3.3 — Insert Sample Records**

```sql
INSERT INTO Students (FirstName, LastName, Email, Major, EnrollmentYear, GPA)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@txwes.edu', 'Computer Science', 2022, 3.85),
    ('Bob', 'Martinez', 'bob.martinez@txwes.edu', 'Information Systems', 2021, 3.42),
    ('Carol', 'Smith', 'carol.smith@txwes.edu', 'Computer Science', 2023, 3.91),
    ('David', 'Lee', 'david.lee@txwes.edu', 'Cybersecurity', 2022, 3.67),
    ('Emma', 'Wilson', 'emma.wilson@txwes.edu', 'Information Systems', 2020, 3.78);
```

Click **Run**. Verify 5 rows affected.

**Step 3.4 — Query the Data**

Run each of the following queries individually and take a screenshot of the results:

```sql
-- Query 1: Select all students
SELECT * FROM Students ORDER BY LastName;
```

```sql
-- Query 2: Filter by major
SELECT FirstName, LastName, GPA
FROM Students
WHERE Major = 'Computer Science'
ORDER BY GPA DESC;
```

```sql
-- Query 3: Calculate average GPA by major
SELECT Major, COUNT(*) AS StudentCount, AVG(GPA) AS AvgGPA
FROM Students
GROUP BY Major
ORDER BY AvgGPA DESC;
```

**Step 3.5 — Update and Verify**

```sql
-- Update a student's GPA
UPDATE Students
SET GPA = 3.95
WHERE Email = 'carol.smith@txwes.edu';

-- Verify the update
SELECT FirstName, LastName, GPA FROM Students WHERE LastName = 'Smith';
```

[SHOW AZURE PORTAL] Show the Query Editor with results from one of the SELECT queries. Point out the Results tab and the Messages tab.

---

## Part 4: Create an Azure Cosmos DB Account (15 minutes)

**Step 4.1 — Create the Cosmos DB Account**

Replace `[initials]` with your initials:

```bash
az cosmosdb create \
  --name lab10cosmos[initials] \
  --resource-group lab10-rg \
  --default-consistency-level Session \
  --locations regionName=eastus failoverPriority=0 isZoneRedundant=false
```

This deployment takes 3–5 minutes.

**Step 4.2 — Create a Database and Container**

```bash
# Create a database
az cosmosdb sql database create \
  --account-name lab10cosmos[initials] \
  --resource-group lab10-rg \
  --name UniversityDB

# Create a container with /studentId as partition key
az cosmosdb sql container create \
  --account-name lab10cosmos[initials] \
  --resource-group lab10-rg \
  --database-name UniversityDB \
  --name Courses \
  --partition-key-path "/department" \
  --throughput 400
```

**Step 4.3 — Insert Documents Using Data Explorer**

1. In the Azure Portal, navigate to your Cosmos DB account (lab10cosmos[initials])
2. Under **Data Explorer**, expand **UniversityDB** > **Courses**
3. Click **New Item**
4. Replace the default JSON with:

```json
{
    "id": "CS101",
    "department": "Computer Science",
    "courseName": "Introduction to Programming",
    "credits": 3,
    "instructor": "Professor Nash",
    "enrolledStudents": 28,
    "tags": ["python", "beginner", "fall-2024"]
}
```

5. Click **Save**
6. Click **New Item** again and add a second document:

```json
{
    "id": "IS220",
    "department": "Information Systems",
    "courseName": "Azure Cloud Computing",
    "credits": 3,
    "instructor": "Professor Nash",
    "enrolledStudents": 22,
    "tags": ["azure", "cloud", "az-900", "fall-2024"],
    "labRequired": true
}
```

Note that the second document has a `labRequired` field that the first document does not. This demonstrates the flexible schema of NoSQL document databases.

**Step 4.4 — Query Documents Using Data Explorer**

In Data Explorer, click **New SQL Query** and run:

```sql
SELECT * FROM c WHERE c.department = "Computer Science"
```

Then run:

```sql
SELECT c.id, c.courseName, c.enrolledStudents
FROM c
ORDER BY c.enrolledStudents DESC
```

[SHOW AZURE PORTAL] Show the Data Explorer with documents visible in the results pane. Point out the two documents having different sets of fields (labRequired is only on one document).

---

## Part 5: Reflection Questions (5 minutes)

Answer in your submission document (2–3 sentences each):

**Question 1:** When you created the Students table in Azure SQL Database, you defined the schema (columns and data types) before inserting any data. When you added Cosmos DB documents, one document had a `labRequired` field and the other did not. What does this difference illustrate about the fundamental distinction between relational and NoSQL databases?

**Question 2:** You configured a SQL Server firewall rule allowing 0.0.0.0 to 0.0.0.0. This is described as "Allow Azure Services." What does this rule actually do, and what security consideration should you be aware of when using this rule in a production environment?

**Question 3:** The Cosmos DB container was created with `/department` as the partition key. Why is the choice of partition key important in Cosmos DB? What would be a poor partition key choice for the Courses container, and why?

---

## Part 6: Cleanup Resources (5 minutes)

```bash
az group delete \
  --name lab10-rg \
  --yes \
  --no-wait
```

---

## Deliverables

Submit the following to Canvas:

1. **Screenshot 1** — CLI output showing successful SQL Database creation (az sql db show output)
2. **Screenshot 2** — Azure Portal Query Editor showing the SELECT * FROM Students query results
3. **Screenshot 3** — Azure Portal Query Editor showing the GROUP BY Major query results
4. **Screenshot 4** — Azure Portal Cosmos DB Data Explorer showing both documents in the Courses container (with the different field sets visible)
5. **Screenshot 5** — Azure Portal Cosmos DB Data Explorer showing query results
6. **Reflection Document** — Answers to the three reflection questions

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Screenshot 1: SQL Database created with S0 SKU | 10 |
| Screenshot 2: SELECT * query showing all 5 students | 20 |
| Screenshot 3: GROUP BY query showing major averages | 15 |
| Screenshot 4: Cosmos DB with two documents (different schemas visible) | 20 |
| Screenshot 5: Cosmos DB SQL query results | 10 |
| Reflection Q1: Relational vs. NoSQL schema explanation | 8 |
| Reflection Q2: Firewall rule 0.0.0.0 explanation | 8 |
| Reflection Q3: Partition key importance | 9 |
| **Total** | **100** |

---

## Troubleshooting Tips

**Query Editor login fails:** Verify the firewall rule AllowAzureServices was created (0.0.0.0 to 0.0.0.0). Also verify the admin username is `sqladmin` (not your Azure account email).

**SQL syntax error:** Ensure you are running one query block at a time. Highlight only the query you want to run and click Run, rather than running the entire script with multiple queries.

**Cosmos DB account creation timeout:** The Cosmos DB creation command takes 3–5 minutes. If the CLI command seems to hang, wait — it is running. You can check status in the Azure Portal under Cosmos DB Accounts.

**Data Explorer shows empty container:** After creating documents, collapse and re-expand the container node in the Data Explorer tree to refresh it.

---

*Lab 10 — Module 10: Azure Databases | CIS-4331 | Texas Wesleyan University*
