# Quiz: Module 09 - Relational Databases with PostgreSQL

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Question 1

Which SQL constraint uniquely identifies each record in a database table?

- A) FOREIGN KEY
- B) UNIQUE INDEX
- C) PRIMARY KEY
- D) DEFAULT

**Correct Answer:** C

**Explanation:** The `PRIMARY KEY` constraint designates a column (or columns) whose values must be unique and non-null for every row, serving as the definitive record identifier and the target for foreign key references from other tables.

**Distractor Analysis:**

- Why A is incorrect: `FOREIGN KEY` creates a reference from one table to the primary key of another — it does not uniquely identify rows in the table where it is defined.
- Why B is incorrect: A `UNIQUE INDEX` enforces uniqueness but allows null values and does not carry the semantic role of a primary key.
- Why C is correct: `PRIMARY KEY` combines `UNIQUE` and `NOT NULL` and semantically designates the record identifier.
- Why D is incorrect: `DEFAULT` provides a fallback column value — it has no uniqueness constraint.

---

## Question 2

Which of the following is the most accurate definition of JOIN queries in SQL?

- A) SQL `INSERT` statements that add new rows from one table into another, merging their data.
- B) SQL clauses that combine rows from two or more tables based on a matching column value — such as `INNER JOIN` (both tables match), `LEFT JOIN` (all left rows plus matching right), and `FULL OUTER JOIN` (all rows from both tables).
- C) SQL `ALTER TABLE` commands that restructure an existing table by merging two schemas.
- D) Stored procedures that automatically run whenever a table event occurs, combining data from related tables into a log.

**Correct Answer:** B

**Explanation:** SQL JOIN operations combine rows from multiple tables based on a shared column value. The join type determines which rows from each table are included in the result set.

**Distractor Analysis:**

- Why A is incorrect: `INSERT INTO ... SELECT` copies data between tables but is not a JOIN — JOINs combine data for reading.
- Why B is correct: This accurately describes SQL JOIN operations and the three most common types.
- Why C is incorrect: `ALTER TABLE` modifies schema structure — it does not combine data from multiple tables.
- Why D is incorrect: This describes database triggers — event-driven procedures distinct from JOIN queries.

---

## Question 3

A developer writes this SQL query but no rows are returned, even though matching data exists in both tables. What is the most likely problem?

```sql
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON o.user_id = users.id;
```

- A) `INNER JOIN` does not work with table aliases — the developer must use `FULL OUTER JOIN`.
- B) The `ON` clause references `users.id` using the table name instead of the alias `u.id` — this mixed reference causes the join condition to fail.
- C) The `SELECT` clause must list all columns from both tables — selecting only two columns returns no rows.
- D) SQL aliases cannot be used in the same query as their full table names.

**Correct Answer:** B

**Explanation:** Once an alias (`u`) is defined for a table, that alias must be used consistently in the query. Mixing `users.id` and `u.name` in the same query may cause an ambiguity or reference error in some databases, and in PostgreSQL specifically, once an alias is defined, referencing the original table name in the `ON` clause may fail because the table is only known by its alias.

**Distractor Analysis:**

- Why A is incorrect: `INNER JOIN` works correctly with aliases — this is standard SQL syntax.
- Why B is correct: Alias consistency is required — the `ON` clause must use `u.id`, not `users.id`.
- Why C is incorrect: Selecting specific columns is valid SQL — `SELECT *` is not required.
- Why D is incorrect: SQL does permit mixing aliases and full names in the same query, though consistency is recommended.

---

## Question 4

A web application builds a SQL query by concatenating user input: `` `SELECT * FROM users WHERE email = '${userInput}'` ``. A user enters `' OR '1'='1`. What vulnerability does this expose and how is it fixed?

- A) Cross-Site Scripting (XSS) — fix by encoding HTML special characters with `encodeURIComponent()`.
- B) SQL injection — fix by using parameterized queries that pass user input as a separate parameter rather than concatenating it into the SQL string.
- C) CSRF — fix by adding a `SameSite=Strict` cookie attribute.
- D) Denial-of-service — fix by rate-limiting the endpoint with Express middleware.

**Correct Answer:** B

**Explanation:** The input `' OR '1'='1` breaks out of the string literal and injects a condition that returns all rows. This is a SQL injection attack. Parameterized queries treat all user input as data, never as executable SQL, completely preventing the injection.

**Distractor Analysis:**

- Why A is incorrect: XSS injects malicious scripts into HTML output — this is a SQL injection attack targeting the database.
- Why B is correct: Parameterized queries are the standard SQL injection prevention mechanism.
- Why C is incorrect: CSRF tricks authenticated users into making unintended requests — unrelated to SQL injection.
- Why D is incorrect: This is not a denial-of-service pattern — rate limiting does not prevent SQL injection.

---

## Question 5

On AWS, which service provides a managed relational database compatible with PostgreSQL that eliminates patching, backup, and server management?

- A) Amazon DynamoDB
- B) Amazon ElastiCache
- C) Amazon RDS for PostgreSQL
- D) AWS Glue

**Correct Answer:** C

**Explanation:** Amazon RDS for PostgreSQL is a fully managed relational database service that handles automated backups, software patching, Multi-AZ replication, and storage scaling — allowing developers to focus on application logic.

**Distractor Analysis:**

- Why A is incorrect: Amazon DynamoDB is a NoSQL key-value and document database — it does not support SQL.
- Why B is incorrect: Amazon ElastiCache provides managed Redis and Memcached in-memory caching — not a relational database.
- Why C is correct: RDS for PostgreSQL offers the full PostgreSQL feature set in a managed environment.
- Why D is incorrect: AWS Glue is a serverless ETL service for data pipelines — not a relational database host.

---

## Question 6

A developer uses `pool.query()` to run a PostgreSQL INSERT statement but needs the newly created row — including the database-assigned `id` and `created_at` — without making a second SELECT query. Which SQL clause accomplishes this?

- A) `SELECT LAST_INSERT_ID()` after the INSERT
- B) `RETURNING *` appended to the INSERT statement
- C) `OUTPUT INSERTED.*` in the INSERT statement
- D) `pool.query()` automatically returns the inserted row in `result.insertId`

**Correct Answer:** B

**Explanation:** PostgreSQL's `RETURNING` clause appended to an INSERT (or UPDATE or DELETE) statement causes the affected rows to be returned in the result set. `RETURNING *` returns all columns of the inserted row, including `id` and `created_at`. This is a PostgreSQL-specific extension to standard SQL.

**Distractor Analysis:**

- Why A is incorrect: `LAST_INSERT_ID()` is MySQL syntax — it does not exist in PostgreSQL.
- Why B is correct: `RETURNING *` is the PostgreSQL mechanism for returning the affected row after an INSERT.
- Why C is incorrect: `OUTPUT INSERTED.*` is Microsoft SQL Server (T-SQL) syntax — not PostgreSQL.
- Why D is incorrect: `pool.query()` does not automatically return inserted rows — `result.insertId` is not a property on PostgreSQL query results.

---

## Question 7

A Node.js route handler performs a database DELETE operation and checks `result.rowCount === 0` before sending a `404` response. What does a `rowCount` of `0` indicate?

- A) The DELETE statement contained a syntax error and no SQL was executed.
- B) No rows matched the WHERE clause — the record to be deleted did not exist in the database.
- C) The database returned an empty result set because DELETE statements never return rows.
- D) The connection pool was exhausted — the query ran but returned no data.

**Correct Answer:** B

**Explanation:** `rowCount` in the node-postgres result object indicates how many rows were affected by the statement. For a DELETE with `WHERE id = $1`, a `rowCount` of `0` means no row with that ID was found — the resource does not exist. This is the correct way to detect a "not found" condition for DELETE operations.

**Distractor Analysis:**

- Why A is incorrect: A SQL syntax error throws an exception caught by `try/catch` — it does not produce a `rowCount` of `0`.
- Why B is correct: `rowCount === 0` after DELETE means the WHERE condition matched no rows.
- Why C is incorrect: While DELETE does not return row data, `rowCount` still reflects the number of rows deleted.
- Why D is incorrect: Connection pool exhaustion throws an exception — it does not produce a `rowCount` of `0`.

---

## Question 8

A developer needs to perform two UPDATE statements that must both succeed or both fail together. If the second UPDATE throws an error, the first must be undone. Which node-postgres pattern implements this requirement?

- A) Call `pool.query()` twice in sequence — if the second fails, node-postgres automatically reverses the first.
- B) Use `pool.connect()` to get a client, wrap both queries in `BEGIN`/`COMMIT`, and call `ROLLBACK` in the `catch` block if an error occurs, then `client.release()` in `finally`.
- C) Wrap both `pool.query()` calls in a JavaScript `try/catch` — the `catch` block's presence automatically issues a database ROLLBACK.
- D) Set `pool.transaction = true` before the first query to enable automatic transaction mode.

**Correct Answer:** B

**Explanation:** Database transactions require a dedicated client connection (not the pool's automatic connection management). The pattern is: `pool.connect()` → `BEGIN` → operations → `COMMIT` on success or `ROLLBACK` in catch → `client.release()` in finally. This guarantees atomicity: both operations succeed or neither does.

**Distractor Analysis:**

- Why A is incorrect: `pool.query()` executes each query in its own auto-committed transaction — it does not roll back previous queries on subsequent failures.
- Why B is correct: This is the standard node-postgres transaction pattern.
- Why C is incorrect: JavaScript `try/catch` handles runtime exceptions in Node.js — it does not issue SQL `ROLLBACK` commands.
- Why D is incorrect: `pool.transaction` is not a valid node-postgres property.

---

## Question 9

An Express route handler runs a SELECT query but is written without `async/await`:

```javascript
router.get('/:id', (req, res, next) => {
  const { rows } = pool.query('SELECT * FROM books WHERE id = $1', [req.params.id]);
  if (rows.length === 0) return res.status(404).json({ error: 'Not found' });
  res.status(200).json(rows[0]);
});
```

What is the result when this route is called?

- A) The route works correctly — `pool.query()` is synchronous in node-postgres.
- B) `pool.query()` returns a Promise. Without `await`, `rows` is `undefined`. Accessing `rows.length` throws a `TypeError` that crashes the handler.
- C) The route returns an empty array for every request because the query result is not awaited.
- D) Express detects the missing `await` and automatically wraps the query in a Promise.

**Correct Answer:** B

**Explanation:** `pool.query()` is asynchronous and returns a Promise. Without `await`, the destructuring `const { rows } = pool.query(...)` attempts to destructure a Promise object, which has no `rows` property. `rows` is `undefined`. Calling `rows.length` throws `TypeError: Cannot read properties of undefined`. The handler must be declared `async` and use `await pool.query(...)`.

**Distractor Analysis:**

- Why A is incorrect: node-postgres is entirely asynchronous — all query methods return Promises.
- Why B is correct: Missing `await` on an async database call is one of the most common Node.js bugs.
- Why C is incorrect: Without `await`, the query result is a Promise object — not an empty array.
- Why D is incorrect: Express does not modify or wrap route handler code.

---

## Question 10

AWS RDS Proxy is placed between Lambda functions and an RDS PostgreSQL database. What specific problem does RDS Proxy solve?

- A) RDS Proxy encrypts database credentials so they are never passed in plaintext to Lambda.
- B) Lambda functions create a new database connection on every cold start. At high concurrency, this exhausts the RDS connection limit. RDS Proxy maintains a persistent connection pool, reusing connections across Lambda invocations.
- C) RDS Proxy converts SQL queries to DynamoDB API calls, allowing Lambda to use either database with the same query syntax.
- D) RDS Proxy provides automatic query caching — repeated SELECT queries return cached results without hitting the database.

**Correct Answer:** B

**Explanation:** RDS has a maximum connection limit (typically 100–500 depending on instance size). Lambda functions are horizontally scaled — at high concurrency, each instance opens its own connection to RDS. Without RDS Proxy, this rapidly exhausts the connection limit. RDS Proxy sits between Lambda and RDS, maintaining a warm pool of connections and multiplexing Lambda requests through it.

**Distractor Analysis:**

- Why A is incorrect: Credential security is handled by AWS Secrets Manager and IAM — not RDS Proxy's primary function.
- Why B is correct: Connection pool exhaustion at scale is the specific problem RDS Proxy solves.
- Why C is incorrect: RDS Proxy works exclusively with RDS — it does not translate between SQL and DynamoDB.
- Why D is incorrect: RDS Proxy does not cache query results — it manages connection pooling only.
