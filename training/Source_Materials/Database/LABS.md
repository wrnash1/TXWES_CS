# Database administration Labs (SQL & PostgreSQL focus)

## Lab 1: SQL Fundamentals (DDL & DML)
**Objective**: Create tables and manipulate data.

1.  **Connect**: If PostgreSQL is installed, connect via `psql`. Otherwise, use `sqlite3 lab.db`.
2.  **Create Table**: Create a table `Students` with columns: `StudentID` (Primary Key), `FirstName`, `LastName`, and `GPA`.
3.  **Insert Data**: Insert 5 sample student records.
4.  **Update**: Increase the GPA of all students by 0.1.

## Lab 2: Querying and Filtering
**Objective**: Advanced SELECT statements and Joins.

1.  **Select**: Retrieve all students with a GPA higher than 3.5.
2.  **Sorting**: List students alphabetically by Last Name.
3.  **Aggregation**: Find the average GPA of all students in the table.
4.  **Joins (Conceptual)**: If you had a `Courses` table, describe what type of JOIN you would use to list every student and the classes they are enrolled in.

## Lab 3: Database Security and Backup
**Objective**: Practical administration tasks.

1.  **Users**: Create a 'read-only' user for your database.
2.  **Grant**: Grant SELECT permissions only to that user.
3.  **Backup**: Use `pg_dump` (or `sqlite3` .dump) to export your database to a file named `backup.sql`.
4.  **Restore**: Practice "dropping" your table and restoring it from the `backup.sql` file.

---
**Submission**: Run `../txwes-submit.sh` after completing each lab.
