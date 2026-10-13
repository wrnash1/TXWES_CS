# Discussion Forum: Module 05 - Asynchronous JavaScript

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects async JavaScript concepts to real production architectures on AWS. Choose one scenario and write an initial post addressing all three sub-questions.

---

## Scenario A: Lambda Timeout Caused by Missing Await

A production application on AWS processes customer orders through an API Gateway endpoint backed by an AWS Lambda function. The function writes the order to DynamoDB and sends a confirmation email via Amazon SES. Users report that orders are being saved to DynamoDB but confirmation emails are never sent. A review of the Lambda code reveals:

```javascript
exports.handler = async (event) => {
  const order = JSON.parse(event.body);
  await dynamodb.put({ TableName: 'Orders', Item: order }).promise();

  ses.sendEmail({
    Source: 'orders@example.com',
    Destination: { ToAddresses: [order.email] },
    Message: { Subject: { Data: 'Order Confirmed' }, Body: { Text: { Data: 'Your order is confirmed.' } } }
  }).promise(); // no await

  return { statusCode: 200, body: JSON.stringify({ message: 'Order saved.' }) };
};
```

Address all three of the following in your post:

1. Explain precisely why the email is never sent, using your knowledge of async/await and how AWS Lambda handles the return value of async handlers. What does Lambda do when an async handler returns?
2. The developer added `.promise()` to the SES call, which converts it to a Promise. Why does adding `.promise()` alone not fix the problem? What is the minimum code change needed?
3. Explain the broader principle: in any `async` function, what is the risk of initiating an async operation without `await`ing the returned Promise before the function returns? Give a real-world example beyond this Lambda scenario.

Your initial post should be 175 to 225 words.

---

## Scenario B: CORS Debugging in a Full-Stack AWS Application

A team has deployed a React front-end to S3 + CloudFront and an Express API to an EC2 instance. The front-end domain is `https://app.example.com` and the API domain is `https://api.example.com`. The developers test in Postman and every API call succeeds. But when the React app makes the same `fetch()` calls, the browser console shows:

```
Access to fetch at 'https://api.example.com/users' from origin 'https://app.example.com'
has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present
on the requested resource.
```

Address all three of the following in your post:

1. Explain why Postman does not encounter CORS errors but the browser does. What is the fundamental difference in how Postman and browsers make HTTP requests that explains this discrepancy?
2. The Express API has the `cors` npm package installed but it is not working. Review the following code and explain what is wrong:

   ```javascript
   const express = require('express');
   const cors    = require('cors');
   const app     = express();

   app.get('/users', (req, res) => {
     app.use(cors({ origin: 'https://app.example.com' }));
     res.json(users);
   });
   ```

3. The team wants to use AWS API Gateway as a proxy in front of the EC2 Express server to gain managed CORS configuration, caching, and rate limiting. Describe one advantage and one limitation of this architectural change from the perspective of the CORS fix specifically.

Your initial post should be 175 to 225 words.

---

## Scenario C: Race Conditions and Promise Ordering in a Search UI

A developer builds a real-time search feature. Every time the user types a character, the app calls an API to retrieve matching results:

```javascript
searchInput.addEventListener('input', async function() {
  const query = this.value;
  const results = await fetchSearchResults(query);
  displayResults(results);
});
```

During testing, the developer types "javascript" quickly. The console shows that API calls fire for "j", "ja", "jav", "java", and "javascript" in sequence. But sometimes the results from "java" arrive after the results from "javascript" — and the page displays Java results when the user typed "javascript."

Address all three of the following in your post:

1. Explain the race condition in this code. Why can API responses arrive out of order, and why does this cause incorrect results to be displayed? Use your understanding of network latency and async Promise resolution to explain the mechanism.
2. Propose a fix using a debounce timer (delay the API call until the user stops typing for 300ms). Show the debounce implementation using `setTimeout` and `clearTimeout`, and explain how it reduces both race condition risk and unnecessary API calls.
3. Even with debouncing, a response to an earlier request can theoretically arrive after a later one. Propose a secondary guard using a request ID or timestamp comparison that prevents stale results from overwriting fresh ones. Show the implementation.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add AWS-specific context, a network behavior detail, or a code improvement, or
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
| Initial post uses correct async JavaScript and/or AWS terminology | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

The race condition in Scenario C is one of the most underestimated bugs in real production applications. I have seen it in enterprise dashboards, e-commerce search boxes, and autocomplete fields at companies that should know better. Debouncing handles 99 percent of cases. Request ID tracking handles the remaining 1 percent. Building both habits now means you will naturally write correct async search code throughout your career.
