# Discussion Forum: Module 09 — React Fundamentals

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

---

## Instructions

Choose **one** of the three scenarios below and write a 175–225 word response in complete sentences. Your initial post is due by Thursday at 11:59 PM. Reply to at least one classmate's post by Sunday at 11:59 PM. Your reply must be substantive — at least 75 words that engage with their specific argument or code example.

---

## Scenario A — The useState Mutation Bug

A classmate shares the following React code in a group project. It is supposed to add a new student to a list, but clicking the "Add" button does not update the UI.

```jsx
const [students, setStudents] = useState([
  { id: 1, name: 'Alice', gpa: 3.8 }
]);

function addStudent() {
  students.push({ id: 2, name: 'Bob', gpa: 3.5 });
  setStudents(students);
}
```

Explain in your own words why this code does not work. Describe what React does (and does not do) when it receives a state update. Provide a corrected version of `addStudent` and explain why your fix triggers a re-render while the original does not. Discuss at least one other pattern — such as updating an existing item or removing an item — where the same mutation mistake appears.

### Sample Response — Scenario A

The problem with this code is that it mutates the existing `students` array by calling `push` directly on it, then passes that same array reference to `setStudents`. React performs a shallow reference comparison when it receives a state update — if the reference is identical to the previous state, React concludes nothing changed and skips the re-render entirely. Because `push` modifies the array in place rather than creating a new one, `students` and the updated array point to the same memory address, so React sees no change.

The corrected version creates a brand-new array using the spread operator: `setStudents([...students, { id: 2, name: 'Bob', gpa: 3.5 }])`. This allocates a new array with all existing elements plus the new one, giving React a different reference. React detects the change and re-renders the component with the updated list displayed.

The same mutation trap appears with object updates. Writing `user.gpa = 4.0; setUser(user)` passes the same object reference, so React skips the re-render. The fix is `setUser({ ...user, gpa: 4.0 })`. For removal, never use `splice` on the original array — use `setStudents(students.filter(s => s.id !== targetId))` to produce a new filtered array. Immutability is a non-negotiable rule in React state management.

### Sample Peer Reply — Scenario A

Your explanation of shallow reference comparison was clear and accurate. I want to add that the functional updater form is even safer for additions: `setStudents(prev => [...prev, newStudent])`. If `addStudent` were called rapidly — say, by a double-click — using `prev` ensures each call builds on the latest queued state rather than the stale `students` variable captured in the closure. This pattern is especially important in async contexts where multiple state updates can batch together.

---

## Scenario B — useEffect and the Missing Dependency

A developer writes the following component to display a student profile. It works when the component first loads, but switching to a different student ID in the URL does not update the displayed profile.

```jsx
function StudentProfile({ studentId }) {
  const [student, setStudent] = useState(null);

  useEffect(() => {
    fetch(`/api/students/${studentId}`)
      .then(r => r.json())
      .then(data => setStudent(data));
  }, []);

  if (!student) return <p>Loading...</p>;
  return <h2>{student.name}</h2>;
}
```

Explain what is wrong with the dependency array. Describe what a stale closure is and how it causes this bug. Provide the corrected `useEffect` call. Then discuss one additional concern with this code — specifically what happens if the component unmounts while the fetch is in-flight — and show how to address it with a cleanup function.

### Sample Response — Scenario B

The bug is the empty dependency array `[]`. By passing an empty array, the developer instructs React to run the effect only once after the initial render and never again, even when `studentId` changes. This creates a stale closure — the effect function captures the value of `studentId` at the time it was created, but because the effect never re-runs, that captured value never updates when the prop changes.

The fix is simple: add `studentId` to the dependency array — `useEffect(() => { ... }, [studentId])`. Now React re-runs the fetch every time `studentId` changes, and the profile updates correctly.

There is a second problem: if the user navigates away before the fetch completes, the component unmounts, but the `then` callback still calls `setStudent` on an unmounted component. This causes a React warning and can mask bugs in larger applications. The solution is a cancellation flag in the cleanup function. Initialize `let cancelled = false` inside the effect, check `if (!cancelled) setStudent(data)` inside the `then` callback, and return `() => { cancelled = true; }` as the cleanup function. React calls this cleanup before the next effect run or when the component unmounts, preventing the stale state update.

### Sample Peer Reply — Scenario B

Your description of stale closures was excellent. I would add that when the API call is replaced with `async/await`, developers sometimes make the effect itself `async` — writing `useEffect(async () => { ... }, [studentId])`. This is a mistake because an async function returns a Promise, and React interprets that as the cleanup function. Instead, declare an inner `async function fetchStudent()` inside the effect and call it immediately. That keeps the cleanup return synchronous and avoids the warning.

---

## Scenario C — Choosing Component Architecture

Your team is building a university registration portal in React. The portal has three main sections: a course catalog (read-only list of 200 courses), a shopping cart (courses the student has selected), and a checkout form (student info, payment). A teammate suggests putting all state — catalog search filters, cart items, and form data — in the root `App` component. Another teammate says each section should manage its own state independently.

Describe the tradeoffs between centralizing state in `App` versus keeping state local to each section. Explain which pieces of state should be local and which benefit from being lifted up. Identify at least one concrete problem that each approach causes if taken to an extreme. Conclude with your recommendation for this specific portal.

### Sample Response — Scenario C

Centralizing all state in `App` creates a single source of truth, which sounds clean in theory. The concrete problem is that every time any state changes — even typing a character in the search box — the entire component tree potentially re-renders, including the cart and form. This causes performance degradation and makes the codebase harder to reason about because a single change in the form accidentally triggers re-renders in unrelated components. `App.jsx` also becomes a massive file that is difficult to test or maintain.

Keeping all state local to each section solves the re-render problem but creates a different issue: the cart and checkout form need to share the same data. If the cart manages its own list of selected courses and the checkout form manages its own copy, the two can get out of sync. Resolving this with a callback chain through multiple layers of components — called prop drilling — quickly becomes unmanageable.

My recommendation is a hybrid approach. Catalog search filters belong locally in the catalog section — nothing else needs them. Form validation state belongs locally in the checkout form. But the cart items need to be lifted up to a common ancestor of both the cart and checkout form, since both sections must display and act on the same list. This pattern — lift state only as high as necessary — is the standard React approach before reaching for a global state solution like Context API, which we will cover in Module 10.

### Sample Peer Reply — Scenario C

Your hybrid approach is exactly right. I would add that the catalog's filtered results should also stay local — 200 courses filtered client-side is not expensive, and centralizing the filter state in `App` would couple an unrelated concern to the global state. One pattern I have used successfully is colocating state with the component that owns it: if only one component reads and writes a piece of state, that state belongs in that component. Only lift when two or more siblings need the same value.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses the chosen scenario directly and accurately | 3 |
| Technical explanation is correct (React behavior, hooks, JSX rules) | 3 |
| Response is 175–225 words in complete sentences | 1 |
| Peer reply is substantive (75+ words, engages with specific points) | 2 |
| Peer reply posted by Sunday 11:59 PM | 1 |
| **Total** | **10** |

---

## Professor Nash Note

Strong responses go beyond restating the problem. They explain the underlying mechanism — why React behaves the way it does — and generalize to similar situations. For Scenario A, the strongest posts will mention the functional updater form and at least one array pattern beyond `push`. For Scenario B, the strongest posts will handle both the missing dependency and the unmount cleanup. For Scenario C, the best posts will give a concrete architectural recommendation with clear reasoning rather than saying "it depends."
