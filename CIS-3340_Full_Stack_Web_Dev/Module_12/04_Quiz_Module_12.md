# Quiz: Module 12 - React State & Props
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which React Hook is used to add local state variables to functional components?
*   A) `useEffect`
*   B) `useContext`
*   C) `useState`
*   D) `useStateVariable`
*   **Correct Answer:** C) `useState` returns a tuple of `[currentValue, setterFunction]` — calling the setter with a new value schedules a component re-render with the updated state.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `useEffect` is used to perform side effects (API calls, subscriptions, DOM mutations) after renders — not to declare state variables.
    *   *Why B is incorrect:* `useContext` reads the current value of a React context created with `createContext()` — it is used for global state access, not local component state.
    *   *Why C is correct:* `useState` is the hook specifically designed to add reactive, local state to functional components.
    *   *Why D is incorrect:* `useStateVariable` is not a React API — it does not exist.

---

**Question 2**
Which of the following is the most accurate definition of **immutable props** in React?
*   A) CSS custom properties (`--variable-name`) defined in the `:root` selector that cannot be changed after the stylesheet is loaded.
*   B) Read-only data objects that parent components pass to child components via JSX attributes — the receiving child component cannot modify them; communication back to the parent uses callback functions passed as props.
*   C) React state variables declared with `const` that are frozen with `Object.freeze()` to prevent accidental mutation.
*   D) The fixed initial values provided to `useState()` that cannot be changed after the component first mounts.
*   **Correct Answer:** B) Read-only data objects that parent components pass to child components via JSX attributes — the receiving child component cannot modify them; communication back to the parent uses callback functions passed as props.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CSS custom properties are a styling mechanism — unrelated to React component props.
    *   *Why B is correct:* React enforces a unidirectional data flow where props flow from parent to child and cannot be mutated by the child — this is the core definition of immutable props.
    *   *Why C is incorrect:* State variables declared with `const` in JavaScript cannot be reassigned (the variable binding is fixed), but the state value itself is updated by calling the setter function — this is separate from props immutability.
    *   *Why D is incorrect:* The initial value passed to `useState()` is only used for the first render — the state can subsequently be updated by calling the setter function. This is a description of state initialization, not props.

---

**Question 3**
A React component needs to fetch data from an API when it first renders and store the result for display. Which hook combination is most appropriate?
*   A) `useRef` to store the data and `useMemo` to trigger the fetch on mount.
*   B) `useState` to store the fetched data and `useEffect` with an empty dependency array (`[]`) to trigger the fetch once on mount.
*   C) `useContext` to store the data globally and `useReducer` to dispatch the fetch action.
*   D) Two `useState` hooks — one for triggering the fetch and one for storing the result.
*   **Correct Answer:** B) `useState` to store the fetched data and `useEffect` with an empty dependency array (`[]`) to trigger the fetch once on mount.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `useRef` stores mutable values that do not trigger re-renders — it is not appropriate for display data. `useMemo` memoizes computed values, not side effects.
    *   *Why B is correct:* This is the standard React data-fetching pattern: `useEffect(() => { fetch(...).then(...).then(data => setData(data)) }, [])` runs the fetch once on mount and `useState` holds the result for rendering.
    *   *Why C is incorrect:* `useContext` is for consuming shared context — it does not initiate fetch calls. `useReducer` is for complex state transitions, not the primary pattern for simple API fetches.
    *   *Why D is incorrect:* A boolean "trigger" state is an anti-pattern — `useEffect` with `[]` runs once on mount without needing a trigger state variable.

---

**Question 4**
A parent component passes `count={5}` as a prop to a `Counter` child component. Inside `Counter`, the developer calls `props.count = 10`. What happens?
*   A) The parent component's state updates to `10` and re-renders.
*   B) React throws a runtime error because props are read-only and cannot be directly mutated.
*   C) The `Counter` component's local `props.count` updates to `10` for the current render only, without affecting the parent.
*   D) The assignment is silently ignored in strict mode — in development, React shows a console warning but the prop is not changed.
*   **Correct Answer:** B) React enforces props as read-only objects. Attempting to directly assign to `props.count` throws a `TypeError` because React freezes the props object in development mode (and the frozen object throws on mutation in strict mode).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Modifying `props.count` in the child does not communicate back to the parent — React's data flow is unidirectional (top-down only).
    *   *Why B is correct:* Props are immutable by design — direct mutation throws a TypeError because the props object is frozen.
    *   *Why C is incorrect:* The props object is frozen — direct assignment throws an error rather than creating a temporary local mutation.
    *   *Why D is incorrect:* The error is not silently ignored — it throws in strict mode. If outside strict mode, the assignment fails silently on a frozen object, but the prop value does not change.

---

**Question 5**
A React component conditionally renders a loading spinner while data is being fetched and the results table after the fetch completes. Which pattern correctly implements this?
*   A) Use two separate components on two different pages — one shows the spinner and the other shows the table.
*   B) Use `useState` to track a `loading` boolean and the `data` array; render `{loading ? <Spinner /> : <Table data={data} />}` in the JSX return.
*   C) Use `document.getElementById('spinner').style.display = 'none'` inside `useEffect` to hide the spinner after the fetch completes.
*   D) Define the spinner and the table in separate CSS classes and toggle their `visibility` using a prop passed down from the router.
*   **Correct Answer:** B) Use `useState` to track a `loading` boolean and the `data` array; render `{loading ? <Spinner /> : <Table data={data} />}` in the JSX return.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Splitting into separate pages defeats the purpose of conditional rendering — SPA UX requires transitioning between views within the same component without navigation.
    *   *Why B is correct:* Conditional rendering with a `loading` state flag is the standard React pattern — JSX ternary expressions render different UI based on current state.
    *   *Why C is incorrect:* Direct DOM manipulation with `getElementById` bypasses React's rendering model — it is an anti-pattern that causes React's Virtual DOM to get out of sync with the real DOM.
    *   *Why D is incorrect:* Toggling `visibility` via CSS hides the element visually but keeps it in the DOM and in the accessibility tree — conditional rendering is the correct React approach.
