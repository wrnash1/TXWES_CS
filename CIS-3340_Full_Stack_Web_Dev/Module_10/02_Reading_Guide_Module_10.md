# Reading Guide: Module 10 — State Management with React

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Certified Developer — Associate (DVA-C02)

---

## Overview

This guide covers state management patterns beyond `useState`: the Context API for global state, `useReducer` for complex transitions, React Query for server state, and the decision between Context and Redux. Work through every code example in your editor.

---

## 1. Understanding State Categories

React applications deal with two fundamentally different types of state.

### 1.1 Client State vs Server State

| Category | Description | Examples | Best Tool |
|---|---|---|---|
| **Client state** | Lives in the browser, owned by the app | UI open/close, current tab, form input, cart | `useState`, `useReducer`, Context |
| **Server state** | Originates on a server, can be stale | API data, user profiles, product lists | React Query (TanStack Query) |

A very common mistake is managing server state with `useState` and `useEffect`. This works but requires you to manually handle caching, loading, errors, refetching, and synchronization. React Query handles all of this automatically.

### 1.2 Prop Drilling

Prop drilling occurs when a value must be passed through multiple layers of components that do not use it directly, only forwarding it further down.

```text
App (user state)
  └── Layout (passes user down, doesn't use it)
        └── Sidebar (passes user down, doesn't use it)
              └── UserMenu (finally uses user)
```

Signs that prop drilling is hurting you:

- A component receives a prop only to pass it to a child.
- Adding a field to a shared object requires touching 4+ files.
- Refactoring a component requires updating every parent in the chain.

---

## 2. Context API Deep Dive

### 2.1 createContext and Provider Pattern

```jsx
// src/context/ThemeContext.jsx
import { createContext, useContext, useState } from 'react';

const ThemeContext = createContext(null);

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  const toggleTheme = () => setTheme(t => t === 'light' ? 'dark' : 'light');

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// Custom hook — validates usage and provides named API
export function useTheme() {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error('useTheme must be used within a ThemeProvider');
  return ctx;
}
```

### 2.2 Context Default Value

The `createContext(defaultValue)` argument is used only when a component consumes the context without a matching Provider above it in the tree. In production code, set it to `null` and throw an error in the custom hook — this surfaces misconfigured trees immediately during development.

### 2.3 Nesting Multiple Providers

Compose multiple providers at the app root. Order matters only when providers depend on each other.

```jsx
// main.jsx
ReactDOM.createRoot(document.getElementById('root')).render(
  <QueryClientProvider client={queryClient}>
    <AuthProvider>
      <ThemeProvider>
        <CartProvider>
          <App />
        </CartProvider>
      </ThemeProvider>
    </AuthProvider>
  </QueryClientProvider>
);
```

---

## 3. useReducer Reference

### 3.1 Reducer Function Rules

A reducer must be a pure function:

- Same inputs always produce the same output.
- No side effects (no API calls, no `console.log`, no `localStorage` writes).
- Never mutate the state argument — always return a new object.

```jsx
// CORRECT — new object each time
case 'INCREMENT':
  return { ...state, count: state.count + 1 };

// WRONG — mutates state directly
case 'INCREMENT':
  state.count++;
  return state;
```

### 3.2 Action Shape Convention

```jsx
// Standard Flux Standard Action shape
const action = {
  type: 'ADD_ITEM',     // required: string, usually SCREAMING_SNAKE_CASE
  payload: { ... },     // optional: data needed to process the action
  error: false,         // optional: true if payload is an Error
  meta: { ... },        // optional: metadata (timestamps, request IDs)
};
```

### 3.3 useReducer vs useState Comparison

| Scenario | Prefer |
|---|---|
| Single boolean toggle | `useState` |
| Single string / number | `useState` |
| Object with 2–3 related fields | Either |
| Object with many fields and complex transitions | `useReducer` |
| Multiple event handlers updating the same state | `useReducer` |
| State machine (defined set of valid transitions) | `useReducer` |
| Need to test state logic in isolation | `useReducer` |

### 3.4 Context + useReducer Pattern

This combination creates a lightweight global store.

```jsx
// src/context/CartContext.jsx
import { createContext, useContext, useReducer } from 'react';

const CartContext = createContext(null);

function cartReducer(state, action) {
  switch (action.type) {
    case 'ADD': {
      const existing = state.items.find(i => i.id === action.payload.id);
      if (existing) {
        return {
          ...state,
          items: state.items.map(i =>
            i.id === action.payload.id ? { ...i, qty: i.qty + 1 } : i
          ),
        };
      }
      return { ...state, items: [...state.items, { ...action.payload, qty: 1 }] };
    }
    case 'REMOVE':
      return { ...state, items: state.items.filter(i => i.id !== action.payload) };
    case 'CLEAR':
      return { items: [] };
    default:
      return state;
  }
}

export function CartProvider({ children }) {
  const [state, dispatch] = useReducer(cartReducer, { items: [] });

  const total = state.items.reduce((sum, i) => sum + i.price * i.qty, 0);

  return (
    <CartContext.Provider value={{ items: state.items, total, dispatch }}>
      {children}
    </CartContext.Provider>
  );
}

export const useCart = () => {
  const ctx = useContext(CartContext);
  if (!ctx) throw new Error('useCart must be used within a CartProvider');
  return ctx;
};
```

---

## 4. React Query (TanStack Query) Reference

### 4.1 Setup

```bash
npm install @tanstack/react-query @tanstack/react-query-devtools
```

```jsx
// main.jsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000, // 1 minute default
      retry: 2,
    },
  },
});

ReactDOM.createRoot(document.getElementById('root')).render(
  <QueryClientProvider client={queryClient}>
    <App />
    <ReactQueryDevtools initialIsOpen={false} />
  </QueryClientProvider>
);
```

### 4.2 useQuery Options Reference

| Option | Default | Description |
|---|---|---|
| `queryKey` | required | Array used as cache key; changes trigger refetch |
| `queryFn` | required | Async function that returns data or throws |
| `staleTime` | 0 | How long (ms) data is considered fresh |
| `gcTime` | 5 min | How long unused data stays in cache |
| `refetchOnWindowFocus` | `true` | Refetch when user returns to tab |
| `enabled` | `true` | Set to `false` to disable automatic fetching |
| `retry` | 3 | Number of retries on failure |

### 4.3 Dynamic Query Keys

When your query depends on a variable, include it in the `queryKey` array. React Query re-fetches whenever the key changes.

```jsx
// Fetches /api/students/42 when studentId is 42
const { data: student } = useQuery({
  queryKey: ['student', studentId],
  queryFn: () => fetch(`/api/students/${studentId}`).then(r => r.json()),
  enabled: !!studentId,  // don't fetch if studentId is null
});
```

### 4.4 useMutation and Cache Invalidation

```jsx
const queryClient = useQueryClient();

const deleteMutation = useMutation({
  mutationFn: (id) =>
    fetch(`/api/students/${id}`, { method: 'DELETE' }).then(r => {
      if (!r.ok) throw new Error('Delete failed');
    }),

  // Optimistic update — remove from cache before server confirms
  onMutate: async (id) => {
    await queryClient.cancelQueries({ queryKey: ['students'] });
    const previous = queryClient.getQueryData(['students']);
    queryClient.setQueryData(['students'], (old) =>
      old.filter(s => s.id !== id)
    );
    return { previous };
  },

  // Rollback on error
  onError: (_err, _id, context) => {
    queryClient.setQueryData(['students'], context.previous);
  },

  // Refetch to confirm server state
  onSettled: () => {
    queryClient.invalidateQueries({ queryKey: ['students'] });
  },
});
```

### 4.5 React Query vs Manual Fetch Comparison

| Feature | Manual (useEffect + useState) | React Query |
|---|---|---|
| Loading state | Manual `useState(true)` | `isLoading` built-in |
| Error state | Manual `useState(null)` | `isError` / `error` built-in |
| Caching | None by default | Automatic with `staleTime` |
| Deduplication | None | Automatic for same `queryKey` |
| Background refetch | Manual | `refetchOnWindowFocus` etc. |
| Pagination | Manual | `useInfiniteQuery` built-in |
| Optimistic updates | Complex manual implementation | `onMutate` / rollback pattern |

---

## 5. Redux vs Context — Decision Guide

### 5.1 When Context + useReducer Is Enough

- Application has fewer than 10–15 components sharing global state.
- State shape is well-understood and changes infrequently.
- No complex async side effects that need middleware.
- Team size is 1–3 developers.

### 5.2 When to Reach for Redux Toolkit

- Large team where strict action contracts prevent coordination problems.
- Complex async flows (RTK Query, saga, thunk chains).
- Need for time-travel debugging in production.
- Existing codebase already uses Redux.

### 5.3 Redux Toolkit Quick Comparison

```jsx
// Context + useReducer version
const AuthContext = createContext(null);
export function AuthProvider({ children }) { ... }
export const useAuth = () => useContext(AuthContext);

// Redux Toolkit equivalent
import { createSlice } from '@reduxjs/toolkit';

const authSlice = createSlice({
  name: 'auth',
  initialState: { user: null, isAuthenticated: false },
  reducers: {
    login: (state, action) => {
      state.user = action.payload;
      state.isAuthenticated = true;
    },
    logout: (state) => {
      state.user = null;
      state.isAuthenticated = false;
    },
  },
});

export const { login, logout } = authSlice.actions;
export default authSlice.reducer;
```

RTK uses Immer under the hood, so the "mutation" syntax in reducers is safe — Immer converts it to immutable updates.

---

## 6. Performance Optimization Reference

### 6.1 Context Re-render Problem

Every component that calls `useContext(MyContext)` re-renders when the context value changes, even if the part of the value it uses did not change.

**Solutions:**

1. Split into multiple focused contexts (most common).
2. Use `React.memo` on consumer components.
3. Use `useMemo` to stabilize the context value object.

```jsx
// Stabilize context value with useMemo
export function CartProvider({ children }) {
  const [state, dispatch] = useReducer(cartReducer, { items: [] });

  const value = useMemo(() => ({ items: state.items, dispatch }), [state.items]);

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
}
```

### 6.2 Memoization Quick Reference

| Hook | Purpose | Use When |
|---|---|---|
| `React.memo(Component)` | Skip re-render if props unchanged | Expensive component that often receives same props |
| `useMemo(fn, deps)` | Cache computed value | Expensive calculation; new array/object reference each render |
| `useCallback(fn, deps)` | Cache function reference | Passing callbacks to `React.memo` children |

---

## 7. AWS DVA-C02 Exam Connections

- **Caching and stale data**: React Query's `staleTime` / `gcTime` mirrors CloudFront TTL and cache invalidation logic tested on the exam.
- **Optimistic updates**: Similar to DynamoDB conditional writes and error rollback patterns.
- **Context API for auth**: AWS Amplify and Cognito SDKs expose user state through a React context-like pattern.
- **Redux middleware (Thunk/Saga)**: Conceptually similar to Lambda function chaining and Step Functions for async workflows.

---

## 8. Study Checklist

- [ ] Explain what prop drilling is and when it becomes a problem
- [ ] Create a context with `createContext`, a Provider, and a custom `use` hook
- [ ] Wrap an app tree with multiple providers in the correct order
- [ ] Write a `useReducer` reducer with at least 3 action types
- [ ] Combine Context and `useReducer` into a global store pattern
- [ ] Use `useQuery` to fetch and display data with loading and error states
- [ ] Use `useMutation` with `invalidateQueries` to create or delete data
- [ ] Explain when to use Redux Toolkit instead of Context
- [ ] Apply `React.memo`, `useMemo`, and `useCallback` to prevent unnecessary re-renders
- [ ] Split a single large context into multiple focused contexts

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 10 topics:

**1. React Official Documentation — Context**
[https://react.dev/learn/passing-data-deeply-with-context](https://react.dev/learn/passing-data-deeply-with-context)
The official React guide to `createContext`, Provider nesting, and `useContext` — including worked examples of when to use context versus lifting state, directly aligned to the AuthContext and CartContext patterns in Lab 10.

**2. TanStack Query (React Query) Documentation**
[https://tanstack.com/query/latest/docs/framework/react/overview](https://tanstack.com/query/latest/docs/framework/react/overview)
The complete reference for `useQuery`, `useMutation`, cache invalidation, optimistic updates, and the `QueryClientProvider` setup used in Lab 10 — the authoritative source for every option in the `useQuery` options reference table in this guide.

**3. React Official Documentation — useReducer**
[https://react.dev/reference/react/useReducer](https://react.dev/reference/react/useReducer)
The official `useReducer` API reference with worked examples of the reducer pattern, action shapes, initialization strategies, and the Context + useReducer global store combination — covers all reducer concepts in Section 3 of this guide.

**4. Redux Toolkit Official Documentation — Why Redux Toolkit**
[https://redux-toolkit.js.org/introduction/why-rtk-is-redux-today](https://redux-toolkit.js.org/introduction/why-rtk-is-redux-today)
The Redux team's explanation of when to use Redux Toolkit versus the Context API, covering `createSlice`, Immer-powered mutation syntax, and RTK Query — directly relevant to the Context vs Redux decision framework in Section 5.
