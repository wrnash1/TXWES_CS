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

---

### Question 11 (5 points)

A `useReducer` reducer receives an unrecognized `action.type`. According to the best-practice pattern shown in the reading guide, what should the default case do?

- A) Return `undefined` to signal that no state change occurred.
- B) Return the current state unchanged, or throw an error for unknown action types.
- C) Automatically log the unknown action to the console and reset state to `initialState`.
- D) Call `dispatch` recursively with a `RESET` action type.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Returning `undefined` from a reducer replaces state with `undefined`, causing the next render to crash. The default case must always return a valid state value.
  - Why B is correct: In permissive reducers, returning the current state is safe. In strict reducers (like the one in the lab), throwing an error on unknown types surfaces bugs early — both are acceptable depending on the team's discipline preference.
  - Why C is incorrect: The default case should not reset state automatically — that would silently discard state on every typo in an action type.
  - Why D is incorrect: Calling `dispatch` inside a reducer creates an infinite loop and is never a valid pattern.

---

### Question 12 (5 points)

`React.memo(Component)` is a higher-order component. What does it do?

- A) It memoizes the return value of all `useState` calls inside the component.
- B) It wraps a component and skips re-rendering if the props passed to it have not changed (shallow comparison).
- C) It replaces `useEffect` for components that need to cache API responses.
- D) It converts a class component into a functional component automatically.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `React.memo` does not affect `useState` — state changes always trigger re-renders of the component that owns the state.
  - Why B is correct: `React.memo` performs a shallow prop comparison before re-rendering. If all props are reference-equal to the previous render, the component is skipped.
  - Why C is incorrect: API caching is `useQuery`'s responsibility — `React.memo` is purely about rendering, not data fetching.
  - Why D is incorrect: `React.memo` only wraps functional components — it does not convert class components and does not work with them.

---

### Question 13 (5 points)

`useCallback(fn, deps)` is used to stabilize a function reference. Why is this important when passing a callback to a child wrapped in `React.memo`?

- A) Without `useCallback`, the callback function re-executes every time the parent renders.
- B) Without `useCallback`, a new function object is created on every parent render. Since `React.memo` uses shallow comparison, the new function reference causes the child to re-render even if the logic is identical.
- C) `useCallback` is required for any function used inside JSX event handlers, or React will throw an error.
- D) Without `useCallback`, async functions inside event handlers lose their `this` binding.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A new function reference does not cause extra executions of the callback — it causes extra re-renders of components that receive the function as a prop.
  - Why B is correct: Every render creates a new function object at a new memory address. A `React.memo` child sees a different reference for the callback prop and re-renders. `useCallback` returns the same reference across renders when dependencies have not changed.
  - Why C is incorrect: Passing functions to JSX event handlers without `useCallback` is valid JavaScript — it does not throw an error.
  - Why D is incorrect: Arrow functions in JSX do not use `this`, so `this` binding is not relevant here.

---

### Question 14 (5 points)

React Query's `staleTime` option controls how long fetched data is considered fresh. If `staleTime` is set to `0` (the default), what happens when the user switches to another browser tab and returns to the app?

- A) The query is immediately cleared from cache and the component shows a loading spinner.
- B) Nothing — React Query never re-fetches automatically.
- C) The data is considered stale immediately. When `refetchOnWindowFocus` is `true` (the default), React Query triggers a background refetch when the tab regains focus.
- D) React Query calls `window.location.reload()` to ensure fresh data.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: The existing cached data continues to be displayed while the background refetch runs — there is no loading spinner for a background refetch.
  - Why B is correct in isolation — but only if `refetchOnWindowFocus` is set to `false`. With default settings, C is correct.
  - Why C is correct: With `staleTime: 0`, data is always stale. Combined with `refetchOnWindowFocus: true` (both defaults), returning to the tab triggers an automatic background refetch.
  - Why D is incorrect: React Query never reloads the page — it updates state through React's rendering pipeline.

---

### Question 15 (5 points)

A developer builds a `NotificationContext` that provides a list of notifications and a `dismiss` function. The value object is re-created on every render: `value={{ notifications, dismiss }}`. Which change stabilizes the context value to prevent unnecessary consumer re-renders?

- A) Move the Provider to a separate file so React caches its renders automatically.
- B) Wrap the value object in `useMemo` with `notifications` and `dismiss` as dependencies.
- C) Use `useRef` instead of `useState` to store the notifications array.
- D) Replace `createContext(null)` with `createContext({})` to provide a stable default.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The file location of the Provider has no effect on render behavior — the value object is still recreated each render.
  - Why B is correct: `useMemo(() => ({ notifications, dismiss }), [notifications, dismiss])` returns the same object reference as long as `notifications` and `dismiss` are unchanged, preventing all consumers from re-rendering unnecessarily.
  - Why C is incorrect: `useRef` does not trigger re-renders when its value changes, making it unsuitable for state that should update the UI.
  - Why D is incorrect: The default value of `createContext` only applies when no Provider is above the consumer — it does not affect the Provider's value object stability.

---

### Question 16 (5 points)

In an optimistic update pattern with `useMutation`, what is the purpose of the `onError` callback receiving the `context` returned by `onMutate`?

- A) To log the error to an external monitoring service before re-throwing it.
- B) To roll back the optimistic cache update by restoring the previous data that was saved in `context` before the mutation ran.
- C) To retry the mutation automatically with an exponential backoff algorithm.
- D) To redirect the user to an error page when the server returns a non-200 response.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: While logging is a valid use, the primary purpose of `context` in `onError` is rollback — not logging.
  - Why B is correct: `onMutate` snapshots the current cache data and returns it as `context`. If the mutation fails, `onError` uses `queryClient.setQueryData` with the snapshot to undo the optimistic update.
  - Why C is incorrect: Retry logic is configured separately via the `retry` option on `useMutation` — it is not the purpose of `onError`.
  - Why D is incorrect: Navigation is a side effect that can be placed in `onError`, but receiving `context` is specifically for rollback, not navigation.

---

### Question 17 (5 points)

A component calls `useContext(CartContext)` and returns `null` because no Provider wraps it. A developer adds a null-check: `if (!cart) return null`. What is wrong with this approach compared to throwing an error in a custom hook?

- A) Returning `null` from a component is a syntax error in React.
- B) Returning `null` silently renders nothing, hiding the misconfiguration. Throwing an error in the custom hook surfaces the bug immediately with a descriptive message during development.
- C) `useContext` never returns `null` — the question is based on a false premise.
- D) The `null` check prevents the component from ever rendering again, even after a Provider is added.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Returning `null` from a component is perfectly valid React — it renders nothing.
  - Why B is correct: Silent failures are harder to debug than explicit errors. The custom hook pattern — `if (!ctx) throw new Error('...')` — immediately tells the developer what is wrong and where to fix it, rather than showing a blank component with no explanation.
  - Why C is incorrect: `useContext` returns the context's default value when no Provider is present. If `createContext(null)` was used, the default value is `null`, so the component does receive `null`.
  - Why D is incorrect: The component re-evaluates on every render — once wrapped in a Provider, the null check would pass and render normally.

---

### Question 18 (5 points)

What does the `queryKey` array `['students', { status: 'active', page: 2 }]` do differently from `['students']` in React Query?

- A) It is invalid — React Query query keys must contain only primitive strings.
- B) It caches the filtered, paginated result separately from `['students']`, so changing the filter or page fetches new data without overwriting the unfiltered cache entry.
- C) It causes the query to run twice in parallel — once for `'students'` and once for the filter object.
- D) The object in the array is ignored — only the first string element is used as the cache key.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: React Query query keys can contain any serializable value including objects and numbers — not just strings.
  - Why B is correct: React Query serializes the entire `queryKey` array and uses the result as the cache key. Different keys produce independent cache entries, enabling separate caching of paginated and filtered results.
  - Why C is incorrect: A single `useQuery` call with one key runs one query — not two.
  - Why D is incorrect: React Query deep-serializes the entire array for cache key comparison — the object is not ignored.

---

### Question 19 (5 points)

A developer wraps the entire application in a single `AppContext` that provides `user`, `cart`, `theme`, and `notifications`. Every state update (even a notification being dismissed) re-renders every context consumer. Which architectural change is most effective?

- A) Replace `useContext` with `useRef` in all consumer components to avoid subscribing to context updates.
- B) Split `AppContext` into four separate contexts (`UserContext`, `CartContext`, `ThemeContext`, `NotificationContext`) so each consumer only re-renders when its relevant slice changes.
- C) Move all state into `localStorage` and read it synchronously in each component's render.
- D) Upgrade to React 19 which automatically prevents unnecessary context re-renders with no code changes.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `useRef` does not subscribe to context updates — components using `useRef` for context data would not re-render when the data changes, which breaks the UI.
  - Why B is correct: Splitting into focused contexts is the canonical React solution. A component consuming only `ThemeContext` does not re-render when cart items change because it is not subscribed to `CartContext`.
  - Why C is incorrect: `localStorage` is synchronous but not reactive — reads during render do not automatically trigger re-renders when `localStorage` values change.
  - Why D is incorrect: React 19 does not automatically resolve coarse-grained context subscriptions — code architecture changes are still required.

---

### Question 20 (5 points)

The `gcTime` (garbage collection time) option in React Query controls what behavior?

- A) How long React Query waits before retrying a failed request.
- B) How long data that has no active subscribers (no component is currently mounted that uses the query) remains in the cache before being garbage collected.
- C) The maximum time allowed for a `queryFn` to resolve before React Query marks the query as failed.
- D) The interval at which React Query automatically refetches all active queries in the background.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Retry delay is controlled by the `retryDelay` option — not `gcTime`.
  - Why B is correct: `gcTime` (formerly `cacheTime`) determines how long inactive query data persists in memory. When a component that used the query unmounts, the data stays cached for `gcTime` milliseconds before being removed, allowing fast re-mounts without a loading flash.
  - Why C is incorrect: There is no built-in timeout option for individual `queryFn` execution — that would be implemented with `AbortController` inside the function itself.
  - Why D is incorrect: Background refetch intervals are controlled by `refetchInterval` — not `gcTime`.
