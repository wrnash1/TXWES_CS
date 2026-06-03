# Quiz: Module 09 — React Fundamentals

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

---

## Instructions

Select the single best answer for each question. Questions 7 and 9 include code snippets — read them carefully before answering.

---

### Question 1

Which statement best describes the React virtual DOM?

A. A shadow copy of the real DOM stored in a database for persistence.

B. A lightweight JavaScript object representation of the real DOM used to compute minimal updates.

C. A browser-native feature that caches DOM nodes to speed up re-renders.

D. An alternate rendering engine that completely bypasses the real DOM.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — the virtual DOM lives in memory, not a database, and is not for persistence.
- C is incorrect — the virtual DOM is React's own construct, not a browser-native API.
- D is incorrect — React still applies changes to the real DOM; the virtual DOM is used only to compute what changes are needed.

---

### Question 2

What is the correct way to embed a JavaScript expression inside JSX?

A. `<p>${ username }</p>`

B. `<p>{{ username }}</p>`

C. `<p>{username}</p>`

D. `<p><%= username %></p>`

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — `${}` is template literal syntax, not JSX.
- B is incorrect — double braces are used in some other frameworks (Angular, Vue) but not React JSX.
- D is incorrect — `<%= %>` is EJS template syntax, not JSX.

---

### Question 3

A React functional component named `studentCard` (lowercase s) is defined and imported. When rendered as `<studentCard />`, what happens?

A. It renders correctly because JSX is case-insensitive.

B. React throws a compile-time error because function components must start with uppercase.

C. React treats it as a custom HTML element and renders nothing meaningful.

D. React calls the function but skips the return value.

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — JSX is case-sensitive; lowercase names are treated as native HTML tags.
- B is incorrect — this is not a compile error; Babel/esbuild will process it. The issue is runtime behavior.
- D is incorrect — React does not call user-defined functions whose names are lowercase.

---

### Question 4

Which statement about props is accurate?

A. A child component can modify props to communicate state changes back to the parent.

B. Props flow bidirectionally so parent and child stay automatically synchronized.

C. Props are read-only; a child must use a callback prop to communicate back to the parent.

D. Props and state are interchangeable — both can be mutated directly.

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — props must not be modified by the child; that would violate React's unidirectional data flow.
- B is incorrect — data flows one direction only: parent to child.
- D is incorrect — props are read-only; state can only be changed through its setter function, never by direct mutation.

---

### Question 5

What does `useState` return?

A. A single state value that React updates automatically when data changes.

B. An array containing the current state value and a setter function.

C. A Promise that resolves to the current state when the component mounts.

D. An object with `value` and `update` keys.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `useState` returns a pair, not a single value.
- C is incorrect — `useState` is synchronous; it does not return a Promise.
- D is incorrect — the return is an array destructured by convention as `[value, setValue]`, not an object.

---

### Question 6

You want to fetch data from an API exactly once when a component first mounts. Which `useEffect` call is correct?

A. `useEffect(fetchData);`

B. `useEffect(fetchData, null);`

C. `useEffect(fetchData, []);`

D. `useEffect(fetchData, [fetchData]);`

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — no dependency array means the effect runs after every render.
- B is incorrect — `null` is not a valid dependency array; behavior is undefined and may cause errors.
- D is incorrect — passing `fetchData` as a dependency would cause the effect to re-run on every render if `fetchData` is redefined each render.

---

### Question 7

Consider the following code:

```jsx
const [score, setScore] = useState(0);

function handleClick() {
  setScore(score + 1);
  setScore(score + 1);
  setScore(score + 1);
}
```

After `handleClick` is called once, what is the value of `score`?

A. 3

B. 2

C. 1

D. 0

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — all three `setScore` calls read the same stale `score` value (0) from the closure; they all set score to 1.
- B is incorrect — same reason; batched updates all see the original `score` value.
- D is incorrect — the state does change; after re-render `score` is 1.

**Teaching note:** To increment by 3, use the functional updater form: `setScore(prev => prev + 1)` called three times — each call receives the latest pending value.

---

### Question 8

Which statement about the `key` prop in a mapped list is correct?

A. `key` must be a string — numbers are not accepted.

B. Using the array index as a key is always safe because indices are unique.

C. `key` helps React track which list items changed, were added, or were removed during reconciliation.

D. `key` is optional in mapped lists — React handles reconciliation without it.

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — numbers are valid keys; React stringifies them internally.
- B is incorrect — array index is unsafe when the list can be filtered, sorted, or reordered, because the index no longer corresponds to the same item.
- D is incorrect — omitting `key` causes React to log a warning and can produce incorrect re-rendering behavior.

---

### Question 9

Consider the following `useEffect`:

```jsx
useEffect(() => {
  const id = setInterval(() => setCount(c => c + 1), 1000);
}, []);
```

What is the problem with this code?

A. `setInterval` is not supported inside `useEffect`.

B. The effect is missing a cleanup function, so the interval continues running after the component unmounts, causing a memory leak.

C. The dependency array is incorrect — `setCount` must be listed as a dependency.

D. Using a functional updater inside `setInterval` is not allowed.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `setInterval` works fine inside `useEffect`.
- C is incorrect — `setCount` from `useState` is a stable reference that never changes, so it does not need to be in the dependency array.
- D is incorrect — functional updaters are explicitly recommended inside `setInterval` to avoid stale closures.

---

### Question 10

A React application is deployed as a static build to Amazon S3 with CloudFront as the CDN. The app calls a backend REST API on API Gateway. Where do the AWS credentials used to invoke DynamoDB live?

A. Embedded in the React build's JavaScript bundle as environment variables prefixed with `VITE_`.

B. In an AWS IAM Role attached to the Lambda function that API Gateway invokes — the React app never holds credentials.

C. Stored in the browser's `localStorage` so the React app can sign requests directly.

D. Passed as `Authorization` HTTP headers in every React fetch call to DynamoDB.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `VITE_` environment variables are embedded in the client bundle and are publicly visible; never put AWS credentials there.
- C is incorrect — storing AWS credentials in `localStorage` is a serious security vulnerability; they would be accessible to any JavaScript on the page.
- D is incorrect — the React app should never call DynamoDB directly; all AWS service calls go through the backend Lambda function.
