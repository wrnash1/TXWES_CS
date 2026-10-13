# Discussion Forum: Module 12 — React State Management & API Integration

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects React state management and API integration patterns to real engineering decisions. Choose one scenario and write an initial post addressing all three sub-questions.

---

## Scenario A: The Fetch Bug

A student's React app fetches a list of products from an Express server. The server is having database issues and returns this response for every request:

```
HTTP/1.1 500 Internal Server Error
Content-Type: application/json

{ "error": "Database connection failed" }
```

The student's component code is:

```jsx
useEffect(() => {
  fetch('/api/products')
    .then(res => res.json())
    .then(data => setProducts(data));
}, []);
```

The browser console shows no error, but the product list is blank. When the student adds `.catch(err => console.error(err))`, there is still no output in the console.

Address all three of the following in your post:

1. Explain precisely why there is no error in the console even though the server returned a 500 status code. Describe what the `fetch` API resolves to when the server responds with 500, and what value `data` holds when `.then(data => setProducts(data))` executes.
2. After calling `setProducts` with the error object, the next render calls `products.map()`. Explain what JavaScript error this produces and why, tracing through the type mismatch.
3. Describe the complete fix — the exact code change to `useEffect` that checks the response status before parsing the body and correctly updates the three state variables (`products`, `loading`, `error`) regardless of whether the request succeeds or fails.

Your initial post should be 175 to 225 words.

---

## Scenario B: Shared State Architecture

A developer builds a shopping cart application with this component structure:

```
App
├── ProductList
│   └── ProductCard (has "Add to Cart" button)
└── CartSidebar
    └── CartItem
```

The developer implements state like this:

```jsx
// In ProductList
const [cart, setCart] = useState([]);

// In CartSidebar
const [cart, setCart] = useState([]);
```

The "Add to Cart" button in `ProductCard` calls `setCart` in `ProductList`. The `CartSidebar` renders a count from its own separate `cart` state. Users report that clicking "Add to Cart" has no effect on the cart sidebar count.

Address all three of the following in your post:

1. Explain why the two `cart` state variables are independent and why updating one has no effect on the other, even though they are named the same thing.
2. Describe the "lift state up" pattern. Identify which component should own the `cart` state, and explain how the state and the update function would be passed to both `ProductList` and `CartSidebar`.
3. A teammate suggests solving this problem with a custom hook called `useCart`. Describe what that custom hook would look like — what it would contain, what it would return, and whether it would actually solve the shared state problem or just move the duplication. Explain your reasoning.

Your initial post should be 175 to 225 words.

---

## Scenario C: AWS Full-Stack Architecture Review

A student's capstone project uses this architecture:

- React frontend, Vite, deployed to AWS S3 with CloudFront
- Express API, deployed to AWS Elastic Beanstalk
- The React app calls the API using this code:

```jsx
const API_URL = 'http://localhost:3000';

useEffect(() => {
  fetch(`${API_URL}/api/products`)
    .then(res => res.json())
    .then(data => setProducts(data));
}, []);
```

The app works locally. After deployment, no data loads in the browser. The browser Network tab shows the request is made to `http://localhost:3000/api/products`.

Address all three of the following in your post:

1. Explain the two bugs in this deployment: why `localhost:3000` fails in production, and why the HTTP-to-HTTPS mismatch causes the request to be blocked in a browser (the term for this browser enforcement).
2. Describe the correct fix using Vite environment variables. Name the specific variable prefix required for Vite to embed the value in the browser bundle, show the correct `.env.production` file, and show the corrected `fetch` call.
3. After fixing the URL, the browser console shows a CORS error. Explain where the fix must be applied (client or server), identify the specific Express middleware required, and show the minimum configuration needed to allow requests from the CloudFront domain `https://d1234abcd.cloudfront.net`.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least one classmate who chose a different scenario. Your peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add a detail or edge case that strengthens the answer, or
- Present an alternative approach with trade-off analysis

---

## Due Dates

- Initial post: Thursday by 11:59 PM
- Peer response (at least one): Sunday by 11:59 PM

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses all three sub-questions with technical accuracy | 3 |
| Initial post meets the 175 to 225 word count requirement | 1 |
| Technical explanation uses correct React and JavaScript terminology | 1 |
| Peer response is substantive (75+ words, engages with specific points) | 2 |
| Peer response adds value beyond agreement (corrects, extends, or offers alternatives) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

For Scenario A, posts that say "you need to catch the error" without explaining why no error is thrown in the first place will receive partial credit. The core concept is that `fetch` resolves on any HTTP response — the 500 status code does not reject the promise. That behavior surprises every developer the first time they encounter it, and understanding it correctly is the difference between writing reliable API code and writing code that silently fails.

For Scenario B, the most common mistake is describing `useCart` as a solution to the shared state problem. A custom hook that contains `useState` creates independent state in each component that calls it — the same duplication problem with a different name. Shared state requires a single owner. The hook pattern solves code reuse; lifting state up solves synchronization.

For Scenario C, posts that describe only the URL fix without addressing CORS will receive partial credit. In a real deployment, both bugs appear together. The strongest posts will explain the causal chain: wrong URL → fix URL → CORS error appears → fix CORS on the server.
