# Reading Guide: Module 12 - React State & Props
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 12 - React State & Props**! This module deepens your React knowledge by covering the two core data mechanisms: **props** (data passed from a parent component to a child) and **state** (data managed internally within a component that, when changed, triggers a re-render). You will learn the `useState` hook for local state management, the `useEffect` hook for side effects like API calls, and how data flows unidirectionally through the component tree. These patterns are the foundation for building interactive, data-driven React applications that consume AWS API Gateway endpoints.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Functional components**: React components defined as plain JavaScript functions that accept `props` as their argument and return JSX. Since React 16.8, functional components can use hooks (`useState`, `useEffect`, etc.) to manage state and side effects — making them the preferred component style over class-based components. A minimal functional component: `function Button({ label }) { return <button>{label}</button>; }`.
*   **React hooks**: Special functions provided by React (prefixed with `use`) that let functional components access React features like state, context, and lifecycle. Built-in hooks include `useState` (local state), `useEffect` (side effects), `useContext` (global context), `useRef` (mutable references), and `useMemo`/`useCallback` (performance optimization). Hooks must be called at the top level of a component function — not inside loops, conditionals, or nested functions.
*   **useState**: The React hook for adding local state to a functional component. `const [value, setValue] = useState(initialValue)` returns the current state value and a setter function. Calling `setValue(newValue)` schedules a re-render with the new value. State updates are asynchronous — React batches them for performance — so the new value is not immediately available after calling the setter.
*   **Immutable props**: The read-only data objects that parent components pass to child components via JSX attributes. Props flow downward through the component tree (parent → child) and cannot be modified by the receiving component. If a child needs to communicate a change back to a parent, the parent passes a callback function as a prop that the child calls — this is called "lifting state up."
*   **Event handling**: The pattern of attaching JavaScript handler functions to React elements via JSX event props — such as `onClick`, `onChange`, `onSubmit`, and `onKeyDown`. React synthetic events normalize browser differences and provide the same event API across all browsers. Event handlers commonly call state setter functions to update component state in response to user interactions.

---

### 2. Certification Exam Tips
*   **State Management Patterns in AWS Applications:** The DVA-C02 exam tests full-stack application architectures where a React front-end fetches and displays data from DynamoDB via API Gateway + Lambda. Understanding how `useEffect` triggers a `fetch()` call on component mount, stores the result in `useState`, and renders the data in JSX is the React side of this architecture.
*   **Unidirectional Data Flow:** React's one-way data binding (props down, events up) is a design principle that makes applications predictable and debuggable. The exam may present scenarios about state management in multi-component applications — know when to lift state up vs. use Context vs. use a state management library.
*   **Study Resource:** The official React documentation covers hooks exhaustively with interactive examples. [React.dev — useState](https://react.dev/reference/react/useState) and [React.dev — useEffect](https://react.dev/reference/react/useEffect) are the most precise references for the hooks covered in this module.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Parts 1 and 2 covering **React State and Data Fetching** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part1) and [Part 2](https://fullstackopen.com/en/part2) — covering `useState`, component communication, and fetching data from an API.
*   **Required Video:** Watch the React state and hooks section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering `useState`, `useEffect`, props, and event handlers.

---

### Lab & Command Integration
In this week's hands-on lab, you will build interactive React components with state and props:
*   **Configure useState hook controls to manage component arrays**: Build a to-do list component where `const [items, setItems] = useState([])` tracks the list items — adding new items with `setItems([...items, newItem])` and removing them by filtering.
*   **Pass props to nested child elements**: Refactor the to-do list into separate `TodoList`, `TodoItem`, and `AddTodoForm` components — passing the `items` array and an `onDelete` callback function as props from the parent to each child.
*   **Handle button interactions to update view state**: Add a "Mark Complete" button to each `TodoItem` that calls a parent-provided `onToggle(id)` callback, which updates the parent's state array to flip the `completed` boolean on the matching item.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Parts 1–2 covering **React State and Data Fetching** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/).
- [ ] Watch the React state and hooks section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Build a simple counter component using `useState` before starting the lab to confirm your understanding of state updates and re-renders.
- [ ] Proceed to the weekly hands-on lab activity.
