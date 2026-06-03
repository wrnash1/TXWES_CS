# Quiz: Module 10 — State Management with React

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

---

## Instructions

Select the single best answer for each question. Questions 5, 7, and 9 include code snippets — read them carefully before answering.

---

### Question 1

What is prop drilling in React?

A. A performance optimization technique that passes only changed props to children.

B. Passing state through intermediate components that do not use it, only to reach a deeply nested child.

C. A debugging technique that traces how props flow through the component tree.

D. The process of destructuring props in a function parameter list.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — prop drilling is a problem, not an optimization.
- C is incorrect — that describes React DevTools inspection, not prop drilling.
- D is incorrect — destructuring props is a syntax convenience, unrelated to prop drilling.

---

### Question 2

Which of the following correctly describes the three steps to use the Context API in React?

A. Install a package, configure a store, and import the store hook.

B. Create a context with `createContext`, wrap the tree with a Provider, and consume with `useContext` or a custom hook.

C. Define a global variable, export it from `App.jsx`, and import it in any component that needs it.

D. Create a context, subscribe child components to it using `addEventListener`, and dispatch updates.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — the Context API is built into React; no installation is needed.
- C is incorrect — global variables are not React state; they do not trigger re-renders.
- D is incorrect — React contexts do not use `addEventListener` or an event-based subscribe model.

---

### Question 3

A React app has an `AuthContext` that provides `{ user, login, logout }`. A developer consumes it in a component that is not inside the `AuthProvider`. The custom `useAuth` hook throws `'useAuth must be used within an AuthProvider'`. What is the root cause?

A. The component must be converted to a class component before using the Auth context.

B. The component is outside the Provider's subtree, so there is no matching context value.

C. The `user` object was not initialized in `useState` before being passed to the Provider.

D. The custom hook must be called before any JSX is returned.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — context works with functional components.
- C is incorrect — uninitialized state would cause a different error, not this specific throw.
- D is incorrect — hooks must be called at the top level, but that is not what this error message indicates.

---

### Question 4

What is the signature of `useReducer`?

A. `const dispatch = useReducer(reducer, initialState)`

B. `const [state, dispatch] = useReducer(reducer, initialState)`

C. `const [state, setState] = useReducer(initialState, reducer)`

D. `const { state, dispatch } = useReducer(reducer, initialState)`

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `useReducer` returns an array of two values, not just `dispatch`.
- C is incorrect — the reducer function comes first, then the initial state.
- D is incorrect — the return value is an array, not an object.

---

### Question 5

A reducer function contains the following case:

```jsx
case 'INCREMENT':
  state.count++;
  return state;
```

What is wrong with this code?

A. The `count` property should be accessed with `this.state.count`.

B. The reducer mutates state directly instead of returning a new state object, so React may skip the re-render.

C. `case` blocks in reducers must always return `undefined` to signal no change.

D. The `++` operator is not allowed in React reducers.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `this` is not used in functional React patterns.
- C is incorrect — returning `undefined` from a reducer is not a valid pattern; it causes errors.
- D is incorrect — the `++` operator is valid JavaScript; the problem is mutation, not the operator itself.

---

### Question 6

Which statement correctly describes `useQuery` from React Query (TanStack Query)?

A. It replaces `useState` entirely for all state management in a React application.

B. It manages server state with automatic caching, background refetching, loading states, and error handling.

C. It is a React built-in hook available without installing any additional packages.

D. It can only be used once per component; multiple data needs require separate components.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — React Query manages server state specifically; client state still uses `useState` or `useReducer`.
- C is incorrect — React Query is a third-party library that must be installed.
- D is incorrect — multiple `useQuery` calls are valid in a single component.

---

### Question 7

Consider the following `useQuery` call:

```jsx
const { data } = useQuery({
  queryKey: ['student', studentId],
  queryFn: () => fetch(`/api/students/${studentId}`).then(r => r.json()),
  enabled: !!studentId,
});
```

What does the `enabled: !!studentId` option do?

A. It limits the query to only run when studentId is a positive integer.

B. It prevents the query from running when studentId is falsy (null, undefined, 0, or empty string).

C. It enables optimistic updates so the UI updates before the server responds.

D. It doubles the fetch interval by coercing studentId to a boolean.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `!!` coerces to boolean; it does not validate that the value is a positive integer.
- C is incorrect — optimistic updates are configured in `useMutation`, not `useQuery`.
- D is incorrect — `!!` is the double-negation boolean coercion operator, not related to timing.

---

### Question 8

After a `useMutation` call successfully creates a new student, the developer wants the student list to refresh. Which React Query method should be called?

A. `queryClient.resetQueries`

B. `queryClient.removeQueries`

C. `queryClient.invalidateQueries`

D. `queryClient.refetchQueries`

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — `resetQueries` removes the data and resets to the initial state, which is more aggressive than needed.
- B is incorrect — `removeQueries` deletes the cached data entirely without triggering a background refetch.
- D is technically possible but is generally used less than `invalidateQueries`, which marks data as stale and lets React Query decide when to refetch. `invalidateQueries` is the standard pattern.

---

### Question 9

A developer has this context setup:

```jsx
const AppContext = createContext(null);

export function AppProvider({ children }) {
  const [user, setUser] = useState(null);
  const [cart, setCart] = useState([]);
  const [theme, setTheme] = useState('light');

  return (
    <AppContext.Provider value={{ user, setUser, cart, setCart, theme, setTheme }}>
      {children}
    </AppContext.Provider>
  );
}
```

A performance profiler shows that the `Header` component (which only uses `theme`) re-renders every time a cart item is added. What is the most direct fix?

A. Wrap `Header` in `React.Suspense` to defer its render.

B. Split the single large context into separate `UserContext`, `CartContext`, and `ThemeContext` so each consumer only re-renders when its relevant data changes.

C. Move `cart` state into `localStorage` so it does not trigger context updates.

D. Add a `shouldComponentUpdate` lifecycle method to `Header`.

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect — `React.Suspense` is for lazy loading and async rendering, not performance optimization of context updates.
- C is incorrect — reading from `localStorage` in every render is slower, not faster, and `localStorage` changes do not trigger React re-renders.
- D is incorrect — `shouldComponentUpdate` is a class component lifecycle method; `Header` is a functional component and would use `React.memo` instead.

---

### Question 10

Your team is building a large e-commerce platform with 40+ developers and hundreds of components. The state includes complex async flows (order processing, inventory syncing), time-travel debugging is required for QA, and strict action contracts are needed to coordinate across teams. Which state management approach is most appropriate?

A. Multiple Context providers with `useReducer` in each.

B. A single global `useState` at the root component.

C. Redux Toolkit with RTK Query for async operations.

D. React Query alone, since server state is the only state that matters.

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect — multiple contexts with `useReducer` work well for small-to-medium apps, but do not provide middleware support, time-travel debugging, or the strict action contracts a 40+ developer team requires.
- B is incorrect — a single root `useState` is unmanageable at scale; every update causes the entire tree to re-render.
- D is incorrect — React Query handles server state excellently but does not address complex client state, middleware chains, or time-travel debugging.
