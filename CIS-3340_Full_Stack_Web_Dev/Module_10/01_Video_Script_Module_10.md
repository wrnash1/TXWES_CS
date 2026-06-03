# Video Script: Module 10 — State Management with React

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code with React project, browser with React DevTools
- Use [SHOW CODE] for VS Code; [SHOW BROWSER] for browser; [PAUSE] for slides
- Have a multi-component React app open to demonstrate prop drilling
- React DevTools extension installed in Chrome

---

## Section 1: Introduction — The State Management Problem (0:00 – 2:00)

Welcome back. I'm Professor Nash, and this is Module 10 — State Management with React.

In Module 09 you learned that `useState` manages local component state, and that you lift state up to a common parent when siblings need to share it. That approach works well for small applications. But what happens when your application grows to dozens of components across many layers? Passing state through every intermediate component — even components that don't need it — is called prop drilling, and it is one of the most common sources of frustration in React development.

This module teaches you how to scale state management. We start with prop drilling and its consequences, then solve it with the Context API and `useReducer`. We then look at React Query, the industry standard for managing server state. We finish by discussing when React's built-in tools are enough and when a library like Redux makes sense.

[PAUSE — slide: Module 10 Learning Objectives]

---

## Section 2: Prop Drilling — The Problem (2:00 – 4:30)

Let me show you prop drilling concretely. Imagine an application with this component hierarchy:

```
App
  └── Dashboard
        └── Header
              └── UserAvatar
```

The user object lives in `App` state. `UserAvatar` needs `user.name` and `user.photoUrl`. In a drilled architecture, `App` passes `user` to `Dashboard`, `Dashboard` passes `user` to `Header`, and `Header` passes `user` to `UserAvatar`. `Dashboard` and `Header` never use `user` directly — they are just couriers.

[SHOW CODE]

```jsx
// App.jsx
function App() {
  const [user, setUser] = useState({ name: 'Alice', photoUrl: '/alice.jpg' });
  return <Dashboard user={user} />;
}

// Dashboard.jsx — doesn't use user, just passes it down
function Dashboard({ user }) {
  return <Header user={user} />;
}

// Header.jsx — same problem
function Header({ user }) {
  return (
    <nav>
      <h1>Dashboard</h1>
      <UserAvatar user={user} />
    </nav>
  );
}

// UserAvatar.jsx — finally uses it
function UserAvatar({ user }) {
  return <img src={user.photoUrl} alt={user.name} />;
}
```

This works, but it couples every intermediate component to the `user` prop. If you add a new field to `user`, you must update every component in the chain even if they do not use the new field. At scale, this becomes unmaintainable.

[PAUSE — slide: Prop drilling diagram with 5 levels]

---

## Section 3: Context API — Solving Prop Drilling (4:30 – 8:30)

The Context API lets you create a global channel that any component in the tree can tap into directly, without passing props through intermediaries.

There are three steps to using Context.

Step one: create the context.

[SHOW CODE]

```jsx
// src/context/UserContext.jsx
import { createContext, useContext, useState } from 'react';

const UserContext = createContext(null);

export function UserProvider({ children }) {
  const [user, setUser] = useState({ name: 'Alice', photoUrl: '/alice.jpg' });

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  const context = useContext(UserContext);
  if (!context) throw new Error('useUser must be used inside a UserProvider');
  return context;
}
```

Step two: wrap your component tree with the Provider.

[SHOW CODE]

```jsx
// main.jsx or App.jsx
import { UserProvider } from './context/UserContext';

ReactDOM.createRoot(document.getElementById('root')).render(
  <UserProvider>
    <App />
  </UserProvider>
);
```

Step three: consume the context anywhere in the tree.

[SHOW CODE]

```jsx
// UserAvatar.jsx — no prop drilling needed
import { useUser } from '../context/UserContext';

function UserAvatar() {
  const { user } = useUser();
  return <img src={user.photoUrl} alt={user.name} />;
}
```

`Dashboard` and `Header` no longer need to know about `user` at all. The context flows directly to `UserAvatar`.

[PAUSE — slide: Context provider tree diagram]

The custom `useUser` hook is a best practice. It validates that the consumer is inside the Provider (the error check) and gives you a named, documented API instead of raw `useContext` calls scattered across your codebase.

---

## Section 4: useReducer — Complex State Logic (8:30 – 11:30)

`useState` works well for simple values. When state transitions become complex — multiple related values, transitions that depend on previous state, or the same logic shared across many event handlers — `useReducer` is a better tool.

`useReducer` is inspired by the Redux pattern. You define a reducer function that takes the current state and an action object, and returns the next state.

[SHOW CODE]

```jsx
import { useReducer } from 'react';

// Action types — string constants prevent typos
const ACTIONS = {
  ADD_ITEM: 'ADD_ITEM',
  REMOVE_ITEM: 'REMOVE_ITEM',
  TOGGLE_DONE: 'TOGGLE_DONE',
  CLEAR_DONE: 'CLEAR_DONE',
};

// Reducer — pure function: (state, action) => newState
function todoReducer(state, action) {
  switch (action.type) {
    case ACTIONS.ADD_ITEM:
      return {
        ...state,
        items: [...state.items, { id: Date.now(), text: action.payload, done: false }],
      };

    case ACTIONS.REMOVE_ITEM:
      return {
        ...state,
        items: state.items.filter(i => i.id !== action.payload),
      };

    case ACTIONS.TOGGLE_DONE:
      return {
        ...state,
        items: state.items.map(i =>
          i.id === action.payload ? { ...i, done: !i.done } : i
        ),
      };

    case ACTIONS.CLEAR_DONE:
      return {
        ...state,
        items: state.items.filter(i => !i.done),
      };

    default:
      throw new Error(`Unknown action: ${action.type}`);
  }
}

const initialState = { items: [] };

function TodoApp() {
  const [state, dispatch] = useReducer(todoReducer, initialState);
  const [text, setText] = useState('');

  const add = () => {
    if (text.trim()) {
      dispatch({ type: ACTIONS.ADD_ITEM, payload: text.trim() });
      setText('');
    }
  };

  return (
    <div>
      <input value={text} onChange={e => setText(e.target.value)} />
      <button onClick={add}>Add</button>
      <button onClick={() => dispatch({ type: ACTIONS.CLEAR_DONE })}>
        Clear Done
      </button>
      <ul>
        {state.items.map(item => (
          <li key={item.id}>
            <span
              style={{ textDecoration: item.done ? 'line-through' : 'none' }}
              onClick={() => dispatch({ type: ACTIONS.TOGGLE_DONE, payload: item.id })}
            >
              {item.text}
            </span>
            <button onClick={() => dispatch({ type: ACTIONS.REMOVE_ITEM, payload: item.id })}>
              ×
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

[PAUSE — slide: useReducer flow diagram]

The key benefits of `useReducer`: all state transitions are centralized in one function that is easy to test in isolation, action types are documented contracts, and the state shape is explicit.

Combining `useReducer` with Context lets you build a lightweight global store without Redux.

[SHOW CODE]

```jsx
// src/context/CartContext.jsx
const CartContext = createContext(null);

export function CartProvider({ children }) {
  const [state, dispatch] = useReducer(cartReducer, { items: [] });
  return (
    <CartContext.Provider value={{ state, dispatch }}>
      {children}
    </CartContext.Provider>
  );
}

export const useCart = () => useContext(CartContext);
```

---

## Section 5: React Query — Server State (11:30 – 15:30)

There is an important distinction that many developers miss: local state (what the user has typed, which tab is open) and server state (data fetched from an API) have very different requirements. Server state is asynchronous, can become stale, can be updated by other users, and often needs caching.

React Query — now called TanStack Query — is the industry standard for managing server state. It handles caching, background refetching, loading and error states, pagination, and optimistic updates with minimal code.

[SHOW CODE]

```bash
npm install @tanstack/react-query
```

[SHOW CODE]

```jsx
// main.jsx — wrap app in QueryClientProvider
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById('root')).render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>
);
```

[SHOW CODE]

```jsx
// StudentList.jsx — useQuery replaces manual fetch + useState + useEffect
import { useQuery } from '@tanstack/react-query';

async function fetchStudents() {
  const res = await fetch('/api/students');
  if (!res.ok) throw new Error('Failed to fetch students');
  return res.json();
}

function StudentList() {
  const { data: students, isLoading, isError, error } = useQuery({
    queryKey: ['students'],
    queryFn: fetchStudents,
    staleTime: 5 * 60 * 1000, // cache fresh for 5 minutes
  });

  if (isLoading) return <p>Loading...</p>;
  if (isError) return <p>Error: {error.message}</p>;

  return (
    <ul>
      {students.map(s => (
        <li key={s.id}>{s.name}</li>
      ))}
    </ul>
  );
}
```

Compare this to the manual approach: no `useState` for loading/error/data, no `useEffect`, no cleanup function, automatic caching. The `queryKey` is the cache key — React Query deduplicates requests with the same key across components.

[PAUSE — slide: React Query request lifecycle diagram]

For mutations — creating, updating, deleting — use `useMutation`.

[SHOW CODE]

```jsx
import { useMutation, useQueryClient } from '@tanstack/react-query';

function AddStudentForm() {
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: (newStudent) =>
      fetch('/api/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newStudent),
      }).then(r => r.json()),

    onSuccess: () => {
      // Invalidate the students cache so the list refetches
      queryClient.invalidateQueries({ queryKey: ['students'] });
    },
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    mutation.mutate({ name: 'New Student', major: 'CS', gpa: 3.0 });
  };

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit" disabled={mutation.isPending}>
        {mutation.isPending ? 'Saving...' : 'Add Student'}
      </button>
      {mutation.isError && <p>Error: {mutation.error.message}</p>}
    </form>
  );
}
```

[PAUSE — slide: useMutation + invalidateQueries flow]

---

## Section 6: Redux vs Context — When to Use Each (15:30 – 18:30)

A common question: when should you use Redux instead of Context API?

Redux adds structure, middleware support, and powerful DevTools, but it also adds complexity and boilerplate. The answer depends on your application's needs.

[PAUSE — slide: Redux vs Context comparison table]

Use Context API plus `useReducer` when:

- Your team already understands React.
- Your global state is relatively simple (auth user, theme, cart).
- You do not need time-travel debugging or complex middleware.
- The application is small to medium in size.

Use Redux Toolkit when:

- Multiple developers need a strict, well-documented state contract.
- You need middleware for side effects (RTK Query, Redux Saga).
- Your state is complex with many interdependencies.
- You want time-travel debugging in Redux DevTools.
- The codebase is large and long-lived.

[SHOW CODE]

```jsx
// Context + useReducer — appropriate for auth state
const AuthContext = createContext(null);

function authReducer(state, action) {
  switch (action.type) {
    case 'LOGIN':  return { user: action.payload, isAuthenticated: true };
    case 'LOGOUT': return { user: null, isAuthenticated: false };
    default: return state;
  }
}

export function AuthProvider({ children }) {
  const [state, dispatch] = useReducer(authReducer, { user: null, isAuthenticated: false });
  const login = (user) => dispatch({ type: 'LOGIN', payload: user });
  const logout = () => dispatch({ type: 'LOGOUT' });

  return (
    <AuthContext.Provider value={{ ...state, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
```

For most applications built in this course, Context API with `useReducer` is the right choice. Redux is a valid option for large production apps, but learn the fundamentals first.

---

## Section 7: Performance Considerations (18:30 – 20:30)

Context has a performance characteristic to understand: every component that consumes a context re-renders when the context value changes. If your context value is a large object that changes frequently, this can cause unnecessary re-renders.

[SHOW CODE]

```jsx
// PROBLEM: single context with frequently-changing value
<AppContext.Provider value={{ user, theme, cart, notifications }}>

// SOLUTION: split into multiple focused contexts
<AuthContext.Provider value={{ user }}>
  <ThemeContext.Provider value={{ theme }}>
    <CartContext.Provider value={{ cart }}>
      {children}
    </CartContext.Provider>
  </ThemeContext.Provider>
</AuthContext.Provider>
```

When `cart` changes, only CartContext consumers re-render — not every component subscribed to the combined AppContext.

`React.memo` wraps a component and skips re-rendering if props have not changed by shallow comparison. Use it on expensive presentational components.

[SHOW CODE]

```jsx
const StudentCard = React.memo(function StudentCard({ student }) {
  return <div>{student.name}: {student.gpa}</div>;
});
```

`useMemo` memoizes an expensive computed value. `useCallback` memoizes a function reference — important when passing callbacks to `React.memo` children.

[SHOW CODE]

```jsx
// Derived data computed only when students changes
const honorStudents = useMemo(
  () => students.filter(s => s.gpa >= 3.5),
  [students]
);

// Stable callback reference for memo'd child
const handleDelete = useCallback((id) => {
  dispatch({ type: 'REMOVE', payload: id });
}, [dispatch]);
```

[PAUSE — slide: When to use memo, useMemo, useCallback]

---

## Conclusion (20:30 – 22:30)

Here is the summary for Module 10.

- Prop drilling passes state through intermediate components that do not need it — it works but does not scale.
- Context API eliminates prop drilling by creating a direct channel from provider to consumer.
- `useReducer` centralizes complex state transitions in a testable pure function.
- Combining Context and `useReducer` gives you a lightweight global store without Redux.
- React Query manages server state — caching, loading, errors, invalidation — with minimal code.
- Use Redux when your team and project size justify it; otherwise Context plus `useReducer` is sufficient.
- Split contexts by concern to prevent unnecessary re-renders.

For the AWS Developer Associate exam, server-state management patterns like caching and stale data map directly to CloudFront caching behaviors, TTL settings, and API Gateway caching — concepts you will encounter in the deployment modules.

Your lab this week builds a shopping cart application using Context API and `useReducer`. Complete the reading guide before starting. See you in Module 11 — Node.js and Express.

[END OF SCRIPT]
