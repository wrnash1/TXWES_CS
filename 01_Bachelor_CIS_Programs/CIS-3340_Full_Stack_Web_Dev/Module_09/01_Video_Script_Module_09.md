# Video Script: Module 09 — React Fundamentals

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with React project open, browser with React DevTools
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for browser output; [PAUSE] for slide transitions
- Have Vite project scaffolded before recording
- Chrome with React DevTools extension installed

---

## Section 1: Introduction — Why React? (0:00 – 1:30)

Welcome back to CIS-3340 Full Stack Web Development. I'm Professor Nash, and today we begin Module 09 — React Fundamentals.

You've already built static HTML pages, styled them with CSS, and added interactivity with vanilla JavaScript. That foundation matters. But as applications grow — more features, more data, more users interacting simultaneously — vanilla JavaScript becomes painful to maintain. You end up with hundreds of `document.getElementById` calls, complex event listener trees, and no clear way to reuse UI patterns.

React was created at Facebook and open-sourced in 2013 to solve exactly that problem. It gives you a component model for building UIs, a virtual DOM for efficient updates, and a unidirectional data flow that makes your application predictable.

By the end of this module you will write JSX, build functional components, pass data with props, manage local state with `useState`, handle side effects with `useEffect`, compose components into working interfaces, and debug with React DevTools.

[PAUSE — slide: Module 09 Learning Objectives]

---

## Section 2: The Virtual DOM and How React Works (1:30 – 3:30)

React introduces the virtual DOM — a lightweight JavaScript object representation of the real DOM that lives in memory. When your data changes, React builds a new virtual DOM tree, compares it with the previous one in a process called reconciliation, and applies only the minimal set of real DOM changes needed. This is dramatically faster than re-rendering entire pages.

[PAUSE — slide: Virtual DOM reconciliation diagram]

React is also declarative. You describe what the UI should look like given the current data. React handles how to update the DOM to match. Compare this to imperative DOM manipulation where you tell the browser every step to take.

[SHOW CODE]

```js
// Imperative — vanilla JS
const el = document.getElementById('count');
el.textContent = newCount;

// Declarative — React
// You describe the UI; React updates the DOM automatically
return <p>Count: {count}</p>;
```

The declarative model becomes enormously valuable as applications scale.

[PAUSE — slide: Declarative vs Imperative comparison]

---

## Section 3: Setting Up a React Project with Vite (3:30 – 5:30)

We use Vite to scaffold React projects because it is fast, modern, and uses native ES modules in development. Create React App is older and slower — Vite is the industry standard today.

[SHOW CODE]

```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

Vite scaffolds a project with `src/`, `public/`, `index.html`, and `vite.config.js`. Open `src/main.jsx`.

[SHOW CODE]

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

`ReactDOM.createRoot` finds the `<div id="root">` in `index.html` and hands control to React. `App` is your root component. `React.StrictMode` runs extra checks during development — it does not affect production builds.

[PAUSE — slide: Vite project structure diagram]

---

## Section 4: JSX — JavaScript XML (5:30 – 8:30)

JSX is a syntax extension for JavaScript that lets you write HTML-like markup inside JS files. Browsers do not understand JSX. Vite's build step — using esbuild — transpiles JSX to plain JavaScript function calls before it reaches the browser.

[SHOW CODE]

```jsx
// JSX syntax
const element = <h1 className="title">Hello, World!</h1>;

// What esbuild compiles it to
const element = React.createElement('h1', { className: 'title' }, 'Hello, World!');
```

You never need to write `React.createElement` directly. JSX is the developer-friendly shorthand.

Three JSX rules to memorize.

Rule one: return a single root element. Wrap siblings in a Fragment if needed.

[SHOW CODE]

```jsx
// Valid — single root
return <div><h1>Title</h1><p>Body</p></div>;

// Also valid — Fragment syntax adds no extra DOM node
return (
  <>
    <h1>Title</h1>
    <p>Body</p>
  </>
);
```

Rule two: close all tags. Self-closing elements need a slash.

[SHOW CODE]

```jsx
<img src="/logo.png" alt="TxWes logo" />
<input type="text" />
<br />
```

Rule three: use `className` instead of `class`, and `htmlFor` instead of `for`. JSX is JavaScript, and both `class` and `for` are reserved keywords.

Use curly braces `{}` to embed any JavaScript expression.

[SHOW CODE]

```jsx
const name = 'Texas Wesleyan';
const isLoggedIn = true;
const score = 94.7;

return (
  <>
    <h1>Welcome to {name}</h1>
    <p>{isLoggedIn ? 'Logged in' : 'Please sign in'}</p>
    <p>Score: {score.toFixed(1)}%</p>
  </>
);
```

[PAUSE — slide: JSX Rules cheatsheet]

---

## Section 5: Functional Components (8:30 – 11:00)

A React component is a JavaScript function that returns JSX. Component names must start with a capital letter — that is how React distinguishes your components from native HTML tags like `div` and `h1`.

[SHOW CODE]

```jsx
// src/components/Greeting.jsx
function Greeting() {
  return (
    <div className="greeting">
      <h2>Good morning!</h2>
      <p>Ready to learn React?</p>
    </div>
  );
}

export default Greeting;
```

Arrow function syntax is identical in behavior.

[SHOW CODE]

```jsx
const Greeting = () => (
  <div className="greeting">
    <h2>Good morning!</h2>
    <p>Ready to learn React?</p>
  </div>
);

export default Greeting;
```

To use this component in another file, import and render it like an HTML tag.

[SHOW CODE]

```jsx
import Greeting from './components/Greeting';

function App() {
  return (
    <main>
      <Greeting />
      <Greeting />
    </main>
  );
}
```

Rendering `<Greeting />` twice gives you two identical sections. That is the power of reusability.

[PAUSE — slide: Component hierarchy tree]

---

## Section 6: Props — Passing Data to Components (11:00 – 13:30)

Props — short for properties — are how parent components pass data to children. Think of props as function arguments for your component. Data flows one direction: parent down to child. This is unidirectional data flow, a core React design principle.

[SHOW CODE]

```jsx
// Child — destructures props in the parameter list
function StudentCard({ name, gpa, major }) {
  return (
    <div className="card">
      <h3>{name}</h3>
      <p>Major: {major}</p>
      <p>GPA: {gpa.toFixed(2)}</p>
    </div>
  );
}

// Parent — passes props as JSX attributes
function App() {
  return (
    <div>
      <StudentCard name="Alice Johnson" gpa={3.8} major="Computer Science" />
      <StudentCard name="Bob Martinez" gpa={3.5} major="Information Systems" />
    </div>
  );
}
```

`gpa={3.8}` uses curly braces because it is a number, not a string. All non-string types need curly braces.

Props are read-only. If a child needs to communicate back to the parent, pass a callback function as a prop.

[SHOW CODE]

```jsx
function DeleteButton({ onDelete, label }) {
  return <button onClick={onDelete}>{label}</button>;
}

function App() {
  const handleDelete = () => alert('Item deleted!');
  return <DeleteButton onDelete={handleDelete} label="Remove" />;
}
```

[PAUSE — slide: Props flow diagram — parent to child]

---

## Section 7: State with useState (13:30 – 16:30)

Props give components data from outside. State is data that lives inside a component and can change over time. When state changes, React re-renders the component automatically.

`useState` is a React Hook — a function that lets functional components use React features.

[SHOW CODE]

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

`useState(0)` returns a pair: the current value and a setter. Never mutate state directly.

[SHOW CODE]

```jsx
// WRONG — React does not detect this
count = count + 1;

// CORRECT
setCount(count + 1);

// BEST for updates based on previous value
setCount(prev => prev + 1);
```

For objects and arrays, always produce a new reference.

[SHOW CODE]

```jsx
const [user, setUser] = useState({ name: 'Alice', age: 21 });

// WRONG — same reference, React skips re-render
user.age = 22;
setUser(user);

// CORRECT
setUser({ ...user, age: 22 });

// Arrays — spread, map, filter; never push or splice directly
const [items, setItems] = useState(['a', 'b', 'c']);
setItems([...items, 'd']);
setItems(items.filter(i => i !== 'b'));
```

[PAUSE — slide: useState mental model diagram]

---

## Section 8: useEffect — Side Effects and Lifecycle (16:30 – 19:30)

Side effects are operations that interact with the outside world: fetching data, setting up timers, updating the document title. `useEffect` is the hook for side effects.

[SHOW CODE]

```jsx
import { useState, useEffect } from 'react';

function StudentList() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/students')
      .then(res => res.json())
      .then(data => {
        setStudents(data);
        setLoading(false);
      })
      .catch(err => console.warn('Fetch error:', err));
  }, []);

  if (loading) return <p>Loading students...</p>;

  return (
    <ul>
      {students.map(s => (
        <li key={s.id}>{s.name} — {s.major}</li>
      ))}
    </ul>
  );
}
```

Three dependency array patterns:

- `[]` — run once after the first render. Use for initial fetches.
- `[id]` — re-run whenever `id` changes.
- No array — run after every render. Rarely the right choice.

Return a cleanup function to prevent memory leaks.

[SHOW CODE]

```jsx
useEffect(() => {
  const timerId = setInterval(() => {
    setCount(prev => prev + 1);
  }, 1000);

  return () => clearInterval(timerId);
}, []);
```

[PAUSE — slide: Component lifecycle mapped to useEffect hooks]

---

## Section 9: Component Composition and React DevTools (19:30 – 22:00)

Separate presentational components — which only render UI — from container components — which manage state and logic.

[SHOW CODE]

```jsx
// Presentational — all data via props
function TaskItem({ text, done, onToggle }) {
  return (
    <li
      style={{ textDecoration: done ? 'line-through' : 'none', cursor: 'pointer' }}
      onClick={onToggle}
    >
      {text}
    </li>
  );
}

// Container — manages state, passes data and handlers down
function TaskList() {
  const [tasks, setTasks] = useState([
    { id: 1, text: 'Read Module 09', done: false },
    { id: 2, text: 'Complete Lab 09', done: false },
    { id: 3, text: 'Post to Discussion', done: false },
  ]);

  const toggle = (id) =>
    setTasks(tasks.map(t =>
      t.id === id ? { ...t, done: !t.done } : t
    ));

  return (
    <ul>
      {tasks.map(task => (
        <TaskItem
          key={task.id}
          text={task.text}
          done={task.done}
          onToggle={() => toggle(task.id)}
        />
      ))}
    </ul>
  );
}
```

The `key` prop on mapped elements is required. Use a stable, unique ID from your data — not the array index.

React DevTools is a browser extension for Chrome and Firefox. Install it, open DevTools, and use the Components tab to inspect your component tree, props, and state in real time — no `console.log` needed.

[PAUSE — slide: React DevTools screenshot annotated]

---

## Conclusion (22:00 – 23:30)

Summary of Module 09 React Fundamentals:

- React uses the virtual DOM and reconciliation for efficient UI updates.
- JSX compiles to JavaScript — use `className`, close all tags, wrap siblings in a Fragment.
- Components are functions returning JSX — capital letter names, `export default`.
- Props pass data parent to child — read-only, one direction.
- `useState` manages changing data — always use the setter, produce new references for objects and arrays.
- `useEffect` handles side effects — dependency array controls re-runs, cleanup prevents leaks.
- Compose small focused components — separate presentational from container concerns.
- React DevTools: inspect your component tree live in the browser.

For the AWS Developer Associate exam, React SPAs deploy as static assets to S3 with CloudFront as the CDN. React app code calls API Gateway — it never holds AWS credentials directly.

Complete the reading guide before starting Lab 09, which builds a Student Dashboard using all of these concepts. I'll see you in Module 10 — state management at scale with Context API, useReducer, and React Query.

[END OF SCRIPT]
