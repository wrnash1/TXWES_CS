# Lab 06: Designing a RESTful API

**Course:** CIS-3340 Full Stack Web Development
**Module:** 06 - RESTful API Principles
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will design the complete REST API specification for a university course registration system. You will define endpoints, HTTP methods, request and response formats, status codes, and error responses. You will also test an existing mock API using the VS Code Thunder Client extension or Postman to practice making HTTP requests and reading responses.

This is a design lab — you will write documentation, not code. In Module 07 you will implement the API you design here in Express.

---

## Prerequisites

- VS Code with the Thunder Client extension installed (or Postman)
- Understanding of HTTP methods and status codes from the reading guide
- Internet access for API testing against JSONPlaceholder

---

## Part 1: API Design Document

Create a file called `api-design.md` in a folder called `lab06`.

Write a complete REST API specification for the following domain:

**Domain:** University Course Registration System

**Entities:** Students, Courses, Enrollments, Instructors

For each resource, specify the full CRUD endpoint set.

### Template for each endpoint:

```markdown
### [HTTP METHOD] /api/resource

**Description:** What this endpoint does.

**Request:**
- Headers: Content-Type, Authorization (if required)
- Path Parameters: (if any)
- Query Parameters: (if any)
- Body (if applicable):

**Success Response:**
- Status Code:
- Body:

**Error Responses:**
- 400: (condition and body)
- 404: (condition and body)
- (others as appropriate)
```

### Step 1: Design the Students resource

Design all six endpoints for the Students resource:

- List all students
- Get a single student by ID
- Create a new student
- Replace a student (PUT)
- Partially update a student (PATCH)
- Delete a student

For the "Create student" POST endpoint, specify:

- All required fields: `firstName`, `lastName`, `email`, `programId`
- The Location header in the 201 response (format: `/api/students/{newId}`)
- A 409 Conflict response when the email already exists
- A 422 Unprocessable Entity response when `email` format is invalid

### Step 2: Design the Courses resource

Design the following endpoints for Courses:

- `GET /api/courses` — list all courses; support `?department=CS` and `?semester=fall2025` query parameters
- `GET /api/courses/:id` — get one course
- `POST /api/courses` — create a course (fields: `code`, `title`, `credits`, `instructorId`, `maxEnrollment`)
- `PUT /api/courses/:id` — replace a course
- `DELETE /api/courses/:id` — delete a course (409 Conflict if students are enrolled)

### Step 3: Design the Enrollments nested resource

Design the Enrollments as a nested resource under Students:

- `GET /api/students/:studentId/enrollments` — list all enrollments for a student
- `POST /api/students/:studentId/enrollments` — enroll in a course (body: `{ courseId, semester }`)
- `DELETE /api/students/:studentId/enrollments/:enrollmentId` — drop a course

For the POST enrollment endpoint, specify these error cases:

- 404: Student not found
- 404: Course not found
- 409: Student is already enrolled in this course
- 422: Enrollment would exceed course `maxEnrollment`

### Step 4: Design the API versioning and base URL

Write a short section explaining the versioning strategy. Your API should use URL versioning with the prefix `/api/v1/` on all endpoints. Explain what will happen to `/api/v1/` endpoints when `/api/v2/` is released.

### Step 5: Write the error response format

Define a consistent JSON error response format used by all endpoints in this API. The format should include at minimum:

- `error` — a human-readable error description
- `code` — a machine-readable error code (for example: `STUDENT_NOT_FOUND`, `EMAIL_ALREADY_EXISTS`)
- `details` — an optional array of field-level validation errors

Provide one example for a 400 validation error and one example for a 404 not found error.

---

## Part 2: Testing an Existing API with Thunder Client

### Step 6: Install Thunder Client

In VS Code, press Ctrl+Shift+X to open Extensions. Search for "Thunder Client" and install it. Once installed, click the lightning bolt icon in the left sidebar to open it.

Alternatively, download and install Postman from the official Postman website.

### Step 7: Test GET requests

Use Thunder Client or Postman to make the following GET requests to `https://jsonplaceholder.typicode.com`:

| Request | Expected Status | What to Verify |
|---|---|---|
| `GET /users` | 200 | Response is a JSON array with 10 objects |
| `GET /users/1` | 200 | Response is a single user object |
| `GET /users/999` | 404 | Status code is 404 |
| `GET /posts?userId=1` | 200 | All returned posts have `userId: 1` |
| `GET /posts/1/comments` | 200 | Returns array of comments for post 1 |

For each request, screenshot the Thunder Client response panel showing the status code and response body.

### Step 8: Test POST request

Create a new request in Thunder Client:

- Method: POST
- URL: `https://jsonplaceholder.typicode.com/posts`
- Add a header: `Content-Type: application/json`
- Body (JSON):

```json
{
  "title": "CIS-3340 Test Post",
  "body": "Testing REST API design principles in Lab 06.",
  "userId": 1
}
```

Send the request. Verify:

- Status code is `201 Created`
- The response body includes the same `title` and `body` you sent, plus an `id` field assigned by the server
- Screenshot the response

Note: JSONPlaceholder does not actually persist data — it simulates a correct REST response.

### Step 9: Test PUT and DELETE

Make a PUT request:

- Method: PUT
- URL: `https://jsonplaceholder.typicode.com/posts/1`
- Body:

```json
{
  "id": 1,
  "title": "Updated Post Title",
  "body": "The complete post body has been replaced.",
  "userId": 1
}
```

Verify: status 200. Screenshot.

Make a DELETE request:

- Method: DELETE
- URL: `https://jsonplaceholder.typicode.com/posts/1`

Verify: status 200 (JSONPlaceholder returns 200 for DELETE; in a production-quality API this would be 204). Screenshot.

---

## Deliverables

Submit to Canvas:

1. `api-design.md` — your complete REST API design document
2. Screenshots from Thunder Client / Postman for all five GET requests (showing status codes)
3. Screenshot for the POST request (showing 201 status and response body)
4. Screenshot for the PUT request (showing 200 status)
5. Screenshot for the DELETE request (showing 200 status)

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Students resource: all 6 endpoints designed with correct method, status, body | 20 |
| Courses resource: 5 endpoints with query parameters and 409 conflict case | 15 |
| Enrollments nested resource: 3 endpoints with all error cases | 15 |
| Consistent error response format defined with two examples | 10 |
| URL versioning section with migration strategy explanation | 10 |
| Thunder Client GET screenshots — all 5 requests with correct status codes | 15 |
| Thunder Client POST screenshot showing 201 status | 5 |
| Thunder Client PUT and DELETE screenshots | 5 |
| Correct use of REST conventions throughout (no verbs in URLs, correct methods) | 5 |
| **Total** | **100** |
