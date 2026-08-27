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

---

### Question 11 (5 points)

A component renders a list with `items.map(item => <li>{item.name}</li>)`. React logs a warning about missing keys. Which fix is correct?

- A) `items.map((item, index) => <li key={item.name}>{item.name}</li>)` — always use the name as the key.
- B) `items.map(item => <li key={item.id}>{item.name}</li>)` — use the stable unique ID from the data.
- C) `items.map((item, index) => <li key={index}>{item.name}</li>)` — array index is always the correct key.
- D) Add `suppressKeyWarning={true}` to the parent `<ul>` element.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Names may not be unique and can change, making them unreliable as keys. Stable IDs from the data source are preferred.
  - Why B is correct: A stable, unique `id` from the data source is the ideal key — it survives reordering, filtering, and sorting without causing reconciliation bugs.
  - Why C is incorrect: Array index is problematic when the list can be reordered, filtered, or have items inserted in the middle, as the index no longer corresponds to the same item.
  - Why D is incorrect: `suppressKeyWarning` is not a real React prop — the warning cannot be suppressed this way.

---

### Question 12 (5 points)

Which statement correctly describes the difference between `useEffect` cleanup and no cleanup?

- A) Cleanup functions run before the component mounts, not after it unmounts.
- B) A cleanup function returned from `useEffect` runs when the component unmounts or before the effect re-runs due to a dependency change — preventing resource leaks such as subscriptions or intervals.
- C) Cleanup functions are required for all `useEffect` calls — omitting one causes a runtime error.
- D) Cleanup only applies to effects with non-empty dependency arrays; effects with `[]` never need cleanup.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Cleanup runs on unmount or before the next effect run — not before mount.
  - Why B is correct: Returning a function from `useEffect` registers a cleanup that React calls when the component unmounts or when dependencies change and the effect is about to re-run.
  - Why C is incorrect: Cleanup is optional — many effects (like one-time data fetches) do not need to clean anything up.
  - Why D is incorrect: Even with `[]`, cleanup runs on unmount — for example, clearing a `setInterval` started on mount.

---

### Question 13 (5 points)

A parent component passes `<Child onSave={handleSave} />`. Inside `Child`, how should the callback be invoked when a button is clicked?

- A) `<button onClick={onSave()}>Save</button>` — call the function directly in JSX.
- B) `<button onClick={() => onSave()}>Save</button>` — wrap in an arrow function so it is called on click, not on render.
- C) `<button onClick={props.handleSave}>Save</button>` — use the parent function name directly.
- D) `<button onSave={onSave}>Save</button>` — use the prop name as the event attribute.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `onClick={onSave()}` calls the function immediately during render, not on click. The return value (likely `undefined`) becomes the onClick handler.
  - Why B is correct: `onClick={() => onSave()}` passes a new function that calls `onSave` when the click event fires. Alternatively, `onClick={onSave}` works if no arguments need to be passed.
  - Why C is incorrect: Inside `Child`, the prop is accessed as `onSave` (the prop name), not `handleSave` (the parent's variable name).
  - Why D is incorrect: `onSave` is a custom prop name, not a valid DOM event attribute. The correct event attribute is `onClick`.

---

### Question 14 (5 points)

What is the purpose of `React.Fragment` (or the shorthand `<>...</>`)?

- A) It creates a higher-order component that wraps child components with additional logic.
- B) It groups multiple sibling elements for return from a component without adding an extra DOM node.
- C) It improves rendering performance by memoizing the wrapped elements.
- D) It replaces the need for a `key` prop when rendering lists.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Higher-order components are a separate pattern involving wrapping a component with a function — not related to `Fragment`.
  - Why B is correct: A React component must return a single element. `Fragment` satisfies this requirement without inserting a real `<div>` or other node into the DOM.
  - Why C is incorrect: Memoization is the purpose of `React.memo` and `useMemo` — not `Fragment`.
  - Why D is incorrect: `Fragment` does not eliminate the need for `key` props in lists — when using `Fragment` as the list item wrapper, you must use the long form `<React.Fragment key={id}>`.

---

### Question 15 (5 points)

A developer writes `const [items, setItems] = useState([]); items.push(newItem); setItems(items);`. What is the bug?

- A) `items.push()` is asynchronous and the state update races with the render.
- B) Directly mutating the state array with `push` violates React's immutability requirement. React uses reference equality to detect changes, so modifying the same array object may not trigger a re-render.
- C) `setItems` expects a callback function, not an array value.
- D) `useState` does not support arrays — an object must be used instead.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Array.push` is synchronous. The problem is mutation, not timing.
  - Why B is correct: React compares the previous and next state by reference. Since `push` mutates the existing array and `setItems` receives the same reference, React may skip re-rendering. The correct approach is `setItems([...items, newItem])`.
  - Why C is incorrect: `setItems` accepts either a new state value or a functional updater — both forms are valid.
  - Why D is incorrect: `useState` supports arrays, objects, primitives, and any serializable value.

---

### Question 16 (5 points)

When does `useEffect` run if called with no dependency array — `useEffect(fn)`?

- A) Only once, when the component first mounts.
- B) Never — a dependency array is required for `useEffect` to run.
- C) After every render, including the initial render and every subsequent re-render.
- D) Only when the component unmounts.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Running only once on mount requires an empty dependency array `[]`. Without any array, the effect runs after every render.
  - Why B is incorrect: The dependency array is optional — omitting it is valid and causes the effect to run on every render.
  - Why C is correct: No dependency array = no condition on re-running. The effect executes after every completed render cycle.
  - Why D is incorrect: Running only on unmount requires a cleanup function returned from an effect with `[]` — the effect itself does not run only on unmount.

---

### Question 17 (5 points)

A Vite React project has the environment variable `VITE_API_URL=https://api.example.com` in its `.env` file. How is this variable accessed in a component?

- A) `process.env.API_URL`
- B) `process.env.VITE_API_URL`
- C) `import.meta.env.VITE_API_URL`
- D) `window.env.VITE_API_URL`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `process.env` is a Node.js API. In Vite, environment variables are exposed via `import.meta.env`, not `process.env`. Also, the `VITE_` prefix would be missing.
  - Why B is incorrect: `process.env` is not available in browser-side Vite code unless a polyfill is configured.
  - Why C is correct: Vite exposes variables prefixed with `VITE_` on the `import.meta.env` object at build time.
  - Why D is incorrect: `window.env` is not a standard browser API — it does not exist unless explicitly created.

---

### Question 18 (5 points)

Two sibling components `<Cart />` and `<Header />` both need to display the number of items in the cart. Neither is a parent of the other. What is the correct React pattern?

- A) Pass a `ref` from `Cart` to `Header` so `Header` can read `Cart`'s internal state.
- B) Lift the cart state up to their nearest common ancestor and pass it down as props to both components.
- C) Use `localStorage` to share state between sibling components in real time.
- D) Have `Header` import and directly read `Cart`'s `useState` variable.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `ref` is used to access DOM nodes or keep mutable values — it is not a state-sharing mechanism between sibling components.
  - Why B is correct: "Lifting state up" is the canonical React pattern for sharing state between siblings — move the state to the closest common parent and pass it down as props.
  - Why C is incorrect: `localStorage` is not reactive — `Header` would not automatically re-render when `Cart` writes to `localStorage`.
  - Why D is incorrect: React state is local to the component instance. Another component cannot import or read another component's `useState` variable.

---

### Question 19 (5 points)

A component conditionally renders an admin panel: `{isAdmin && <AdminPanel />}`. When `isAdmin` is `false`, what does React render?

- A) A comment node `<!-- AdminPanel -->` as a placeholder.
- B) An empty `<div>` where the component would have appeared.
- C) Nothing — `false` is not rendered by React.
- D) The string `"false"` in the DOM.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: React does not render comment nodes as placeholders for falsy expressions.
  - Why B is incorrect: No wrapper element is inserted — React renders nothing when the expression is `false`, `null`, or `undefined`.
  - Why C is correct: In JSX, `false`, `null`, `undefined`, and `0` (except when used as a short-circuit with a number) are valid children that render nothing.
  - Why D is incorrect: The string `"false"` would only render if `isAdmin` were the string `"false"` — the boolean `false` renders nothing.

---

### Question 20 (5 points)

What is the correct way to update a specific field in a state object without overwriting the other fields?

```jsx
const [user, setUser] = useState({ name: 'Alice', role: 'student', gpa: 3.8 });
```

- A) `setUser({ gpa: 4.0 })` — React merges partial updates automatically for objects.
- B) `user.gpa = 4.0; setUser(user)` — mutate and re-set the reference.
- C) `setUser({ ...user, gpa: 4.0 })` — spread the existing state and override the changed field.
- D) `setUser(prev => prev.gpa = 4.0)` — use the functional updater to mutate and return the field value.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Unlike `this.setState` in class components, the `useState` setter replaces state entirely — it does not merge partial objects.
  - Why B is incorrect: Mutating the existing object and passing the same reference may not trigger a re-render, and direct mutation violates React's immutability requirement.
  - Why C is correct: Spreading the existing state (`...user`) copies all fields, then the override (`gpa: 4.0`) replaces only the changed field, producing a new object reference.
  - Why D is incorrect: `prev.gpa = 4.0` mutates the existing state object and returns the field value (`4.0`), not an object — this would replace the entire state with the number `4.0`.
