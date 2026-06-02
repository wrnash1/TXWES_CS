# Discussion Forum: Module 09 - Relational Databases with PostgreSQL

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects relational database design to real application scenarios, security decisions, and AWS architecture choices. Choose one scenario and write an initial post addressing all three sub-questions.

---

## Scenario A: Schema Design for a Course Registration System

A university is building a course registration system. The initial database design has a single table:

```sql
CREATE TABLE registrations (
  id          SERIAL PRIMARY KEY,
  student_name VARCHAR(255),
  student_email VARCHAR(255),
  course_name  VARCHAR(255),
  instructor   VARCHAR(255),
  semester     VARCHAR(50),
  grade        CHAR(2)
);
```

A database architect reviews this design and raises concerns about normalization, data integrity, and query performance.

Address all three of the following in your post:

1. Identify two specific problems with this flat table design. For each problem, describe the real consequence — for example, what happens when an instructor's name changes, or when the same student registers for ten courses.
2. Propose a normalized schema using at least three tables. For each table, specify the table name, primary key, at least two non-key columns, and any foreign key relationships.
3. The normalized schema will be hosted on Amazon RDS for PostgreSQL. A developer asks why they cannot simply store the entire registration record as a JSON blob in a single DynamoDB table instead — the data access pattern is always "look up registrations by student ID." Evaluate this proposal: is DynamoDB appropriate here, or should the team stay with RDS? Identify the specific data requirement that makes one option clearly better than the other.

Your initial post should be 175 to 225 words.

---

## Scenario B: SQL Injection in a Student Search Feature

A university student portal includes a search feature. The Express route handler is:

```javascript
app.get('/api/students/search', async (req, res) => {
  const { name } = req.query;
  const { rows } = await pool.query(
    `SELECT id, name, email, gpa FROM students WHERE name ILIKE '%${name}%'`
  );
  res.json(rows);
});
```

A security auditor flags this as a critical SQL injection vulnerability.

Address all three of the following in your post:

1. Demonstrate the SQL injection attack. Show the exact query string a malicious user would enter for `name` that would cause the database to return all rows from the students table regardless of name. Explain what happens to the SQL statement when this input is processed.
2. Rewrite the route handler using a parameterized query with `ILIKE`. Show the corrected `pool.query()` call — the search behavior (case-insensitive partial match) must be preserved.
3. Beyond parameterized queries, describe two additional database or application-layer defenses that a production university portal should implement to limit the damage from a successful SQL injection attack. Consider database user privileges and AWS RDS security configuration in your answer.

Your initial post should be 175 to 225 words.

---

## Scenario C: Transaction Design for a Seat Reservation System

A university is building an online course registration system where students compete to enroll in popular courses. Each course has a `max_enrollment` limit. Two students can submit enrollment requests simultaneously and both may succeed even when only one seat remains — a race condition.

The current implementation:

```javascript
// Non-atomic check-then-insert
const course = await pool.query('SELECT enrolled, max_enrollment FROM courses WHERE id = $1', [courseId]);
if (course.rows[0].enrolled < course.rows[0].max_enrollment) {
  await pool.query('INSERT INTO enrollments (student_id, course_id) VALUES ($1, $2)', [studentId, courseId]);
  await pool.query('UPDATE courses SET enrolled = enrolled + 1 WHERE id = $1', [courseId]);
}
```

Address all three of the following in your post:

1. Explain precisely how the race condition occurs. Trace the execution sequence for two simultaneous requests — show at which point both read the same `enrolled` value and what the final database state is when both proceed.
2. Rewrite the enrollment logic using a PostgreSQL transaction with `BEGIN`/`COMMIT`/`ROLLBACK`. Explain which SQL operation prevents the race condition — consider using `SELECT ... FOR UPDATE` to lock the course row.
3. This registration system will run as an AWS Lambda function behind API Gateway. Lambda can scale to hundreds of concurrent instances. Explain one additional AWS architectural concern that the transaction approach does not fully solve at Lambda scale, and describe the AWS service or configuration that addresses it.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add AWS-specific context or a SQL/PostgreSQL principle that strengthens the answer, or
- Present an alternative approach with trade-off analysis

---

## Due Dates

- Initial post: Wednesday by 11:59 PM
- Peer responses (at least two): Sunday by 11:59 PM

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses all three sub-questions with technical accuracy | 3 |
| Initial post meets the 175 to 225 word count requirement | 1 |
| Initial post uses correct SQL, PostgreSQL, and/or AWS terminology | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

The decision between SQL and NoSQL — between RDS and DynamoDB — is one of the most commonly tested topics on the DVA-C02 exam and one of the most important architectural decisions in real system design. The rule is not "use SQL for everything" or "use NoSQL for everything." The rule is: use SQL when you need relationships between entities, ad-hoc queries, and strong consistency. Use DynamoDB when you have a single, predictable access pattern, need single-digit millisecond latency at massive scale, and can model your data around that one pattern. Every scenario in this discussion is designed to help you practice making that decision with real tradeoffs — not just memorizing a rule.
