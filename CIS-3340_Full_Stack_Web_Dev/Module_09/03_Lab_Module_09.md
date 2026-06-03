# Lab 09: React Student Dashboard

## Course: CIS-3340 Full Stack Web Development

## Texas Wesleyan University | Professor Nash

## Estimated Time: 90–120 minutes

---

## Objectives

By completing this lab you will:

- Scaffold a React project with Vite
- Write JSX with conditional rendering and list rendering
- Build functional components with props
- Manage state with `useState`
- Fetch data with `useEffect`
- Compose multiple components into a complete Student Dashboard

---

## Prerequisites

- Node.js 18+ installed (`node --version` to verify)
- Module 09 video lecture and reading guide completed
- VS Code with the ES7+ React/Redux/React-Native Snippets extension (optional but helpful)

---

## Part 1: Project Setup (10 minutes)

### Step 1 — Scaffold the project

Open a terminal in your development folder and run:

```bash
npm create vite@latest lab09-dashboard -- --template react
cd lab09-dashboard
npm install
npm run dev
```

Open `http://localhost:5173` in your browser. You should see the default Vite + React page.

### Step 2 — Clean the starter files

Replace the contents of `src/App.jsx` with:

```jsx
function App() {
  return (
    <div>
      <h1>Student Dashboard</h1>
    </div>
  );
}

export default App;
```

Replace the contents of `src/index.css` with:

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Arial, sans-serif; background: #f4f6f9; color: #222; }
.container { max-width: 1100px; margin: 0 auto; padding: 24px; }
.card {
  background: #fff;
  border: 1px solid #dde1e7;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
}
.badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: bold;
}
.badge-green { background: #d4edda; color: #155724; }
.badge-yellow { background: #fff3cd; color: #856404; }
.badge-red { background: #f8d7da; color: #721c24; }
```

Delete `src/App.css` and `src/assets/react.svg`. Remove any imports for those files from `App.jsx` and `main.jsx`.

---

## Part 2: Static Data and Component Structure (20 minutes)

### Step 3 — Create the data file

Create `src/data/students.js`:

```js
export const students = [
  { id: 1, name: 'Alice Johnson', major: 'Computer Science', gpa: 3.8, status: 'active', enrolled: 2022 },
  { id: 2, name: 'Bob Martinez', major: 'Information Systems', gpa: 2.9, status: 'probation', enrolled: 2021 },
  { id: 3, name: 'Carol Chen', major: 'Computer Science', gpa: 3.5, status: 'active', enrolled: 2023 },
  { id: 4, name: 'David Kim', major: 'Cybersecurity', gpa: 3.1, status: 'active', enrolled: 2022 },
  { id: 5, name: 'Emma Davis', major: 'Information Systems', gpa: 1.8, status: 'at-risk', enrolled: 2023 },
];
```

### Step 4 — Build the StatusBadge component

Create `src/components/StatusBadge.jsx`:

```jsx
function StatusBadge({ status }) {
  const classes = {
    active: 'badge badge-green',
    probation: 'badge badge-yellow',
    'at-risk': 'badge badge-red',
  };

  return (
    <span className={classes[status] || 'badge'}>
      {status}
    </span>
  );
}

export default StatusBadge;
```

### Step 5 — Build the StudentCard component

Create `src/components/StudentCard.jsx`:

```jsx
import StatusBadge from './StatusBadge';

function StudentCard({ name, major, gpa, status, enrolled }) {
  return (
    <div className="card">
      <h3>{name}</h3>
      <p>Major: {major}</p>
      <p>GPA: {gpa.toFixed(2)} &nbsp; <StatusBadge status={status} /></p>
      <p style={{ fontSize: '0.85rem', color: '#666' }}>Enrolled: {enrolled}</p>
    </div>
  );
}

export default StudentCard;
```

---

## Part 3: Rendering a List (15 minutes)

### Step 6 — Build the StudentList component

Create `src/components/StudentList.jsx`:

```jsx
import StudentCard from './StudentCard';

function StudentList({ students }) {
  if (students.length === 0) {
    return <p>No students match your filter.</p>;
  }

  return (
    <div>
      {students.map(student => (
        <StudentCard key={student.id} {...student} />
      ))}
    </div>
  );
}

export default StudentList;
```

### Step 7 — Wire up App.jsx

Update `src/App.jsx` to import the data and render the list:

```jsx
import { students } from './data/students';
import StudentList from './components/StudentList';

function App() {
  return (
    <div className="container">
      <h1>Student Dashboard</h1>
      <p>{students.length} students enrolled</p>
      <StudentList students={students} />
    </div>
  );
}

export default App;
```

Save and verify all five student cards render in the browser.

---

## Part 4: Adding State — Filter and Search (25 minutes)

### Step 8 — Add filter state to App.jsx

Update `src/App.jsx` to add a status filter:

```jsx
import { useState } from 'react';
import { students } from './data/students';
import StudentList from './components/StudentList';

function App() {
  const [filter, setFilter] = useState('all');
  const [search, setSearch] = useState('');

  const visible = students.filter(s => {
    const matchesFilter = filter === 'all' || s.status === filter;
    const matchesSearch = s.name.toLowerCase().includes(search.toLowerCase())
      || s.major.toLowerCase().includes(search.toLowerCase());
    return matchesFilter && matchesSearch;
  });

  return (
    <div className="container">
      <h1>Student Dashboard</h1>

      <div style={{ marginBottom: '16px', display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
        <input
          type="text"
          placeholder="Search by name or major..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          style={{ padding: '8px', borderRadius: '4px', border: '1px solid #ccc', flexGrow: 1 }}
        />
        <select
          value={filter}
          onChange={e => setFilter(e.target.value)}
          style={{ padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
        >
          <option value="all">All Statuses</option>
          <option value="active">Active</option>
          <option value="probation">Probation</option>
          <option value="at-risk">At Risk</option>
        </select>
      </div>

      <p>Showing {visible.length} of {students.length} students</p>
      <StudentList students={visible} />
    </div>
  );
}

export default App;
```

Test: type "Computer Science" in the search box. Type "alice". Change the status dropdown to "At Risk".

---

## Part 5: useEffect — Simulated Data Fetch (20 minutes)

### Step 9 — Create a mock API utility

Create `src/api/mockFetch.js`:

```js
import { students } from '../data/students';

// Simulates a network delay of 800ms
export function fetchStudents() {
  return new Promise((resolve) => {
    setTimeout(() => resolve([...students]), 800);
  });
}
```

### Step 10 — Use useEffect in App.jsx

Replace the static import of `students` with a `useEffect` fetch. Update `src/App.jsx`:

```jsx
import { useState, useEffect } from 'react';
import { fetchStudents } from './api/mockFetch';
import StudentList from './components/StudentList';

function App() {
  const [allStudents, setAllStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filter, setFilter] = useState('all');
  const [search, setSearch] = useState('');

  useEffect(() => {
    fetchStudents()
      .then(data => {
        setAllStudents(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const visible = allStudents.filter(s => {
    const matchesFilter = filter === 'all' || s.status === filter;
    const matchesSearch =
      s.name.toLowerCase().includes(search.toLowerCase()) ||
      s.major.toLowerCase().includes(search.toLowerCase());
    return matchesFilter && matchesSearch;
  });

  if (loading) return <div className="container"><p>Loading students...</p></div>;
  if (error) return <div className="container"><p style={{ color: 'red' }}>Error: {error}</p></div>;

  return (
    <div className="container">
      <h1>Student Dashboard</h1>

      <div style={{ marginBottom: '16px', display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
        <input
          type="text"
          placeholder="Search by name or major..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          style={{ padding: '8px', borderRadius: '4px', border: '1px solid #ccc', flexGrow: 1 }}
        />
        <select
          value={filter}
          onChange={e => setFilter(e.target.value)}
          style={{ padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
        >
          <option value="all">All Statuses</option>
          <option value="active">Active</option>
          <option value="probation">Probation</option>
          <option value="at-risk">At Risk</option>
        </select>
      </div>

      <p>Showing {visible.length} of {allStudents.length} students</p>
      <StudentList students={visible} />
    </div>
  );
}

export default App;
```

Verify that the loading state appears for approximately 800ms before the list renders.

---

## Expected Output

When complete, your application should display:

- A "Loading students..." message for ~800ms on initial load
- Five student cards after loading
- Each card shows: name, major, GPA formatted to two decimal places, a color-coded status badge, and enrollment year
- The search input filters cards in real time by name or major
- The status dropdown filters cards by status
- The count above the list updates as filters change

---

## Deliverables

Submit a zip file containing your entire `lab09-dashboard` project folder (excluding `node_modules`). Your submission must include:

1. `src/App.jsx` — with `useState`, `useEffect`, filter logic
2. `src/components/StudentCard.jsx`
3. `src/components/StudentList.jsx`
4. `src/components/StatusBadge.jsx`
5. `src/api/mockFetch.js`
6. `src/data/students.js`

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Project scaffolds and runs without errors | 15 |
| All five student cards render with correct data | 20 |
| StatusBadge renders correct color for each status | 15 |
| Search input filters list in real time | 15 |
| Status dropdown filter works correctly | 15 |
| useEffect used for data loading with loading state | 15 |
| Code quality: no console errors, no direct state mutation | 5 |
| **Total** | **100** |
