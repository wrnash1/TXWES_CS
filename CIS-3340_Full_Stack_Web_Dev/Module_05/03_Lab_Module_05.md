# Lab 05: Asynchronous JavaScript and the Fetch API

**Course:** CIS-3340 Full Stack Web Development
**Module:** 05 - Asynchronous JavaScript
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will build a post viewer that fetches data from the public JSONPlaceholder REST API, renders the results dynamically, implements a loading spinner, handles errors gracefully, and supports filtering and pagination. All networking is done with `async/await` and the Fetch API.

---

## Prerequisites

- Completed Module 04 JavaScript skills (DOM manipulation, event listeners)
- Google Chrome with DevTools open to Network tab
- Internet access (the lab calls `jsonplaceholder.typicode.com` — a free mock API)

---

## Starter Files

Create a new project folder called `lab05`. Inside it, create three files: `index.html`, `styles.css`, and `app.js`.

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Post Viewer | Lab 05</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <header>
    <h1>Post Viewer</h1>
    <p>Fetching from JSONPlaceholder REST API</p>
  </header>

  <main>
    <div class="controls">
      <input type="text"
             id="search-input"
             placeholder="Filter posts by title..."
             aria-label="Filter posts">
      <button id="load-btn">Load Posts</button>
      <button id="retry-btn" hidden>Retry</button>
    </div>

    <div id="loading" hidden aria-live="polite">
      <div class="spinner" aria-hidden="true"></div>
      <p>Loading posts...</p>
    </div>

    <div id="error-msg" hidden role="alert"></div>

    <div id="post-count" aria-live="polite"></div>

    <div id="post-grid" class="post-grid"></div>

    <div class="pagination" id="pagination"></div>
  </main>

  <script src="app.js" defer></script>
</body>
</html>
```

### styles.css

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  font-family: system-ui, sans-serif;
  margin: 0;
  background: #f8f9fa;
  color: #1a1a2e;
}

header {
  background: #1a1a2e;
  color: white;
  padding: 1.5rem 2rem;
}

header h1 { margin: 0; font-size: 1.5rem; }
header p  { margin: 0.25rem 0 0; opacity: 0.7; font-size: 0.9rem; }

main {
  max-width: 1100px;
  margin: 2rem auto;
  padding: 0 1.5rem;
}

.controls {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.controls input {
  flex: 1;
  min-width: 200px;
  padding: 0.6rem 1rem;
  border: 2px solid #dee2e6;
  border-radius: 6px;
  font-size: 1rem;
}

.controls input:focus {
  outline: none;
  border-color: #4361ee;
}

.controls button {
  padding: 0.6rem 1.25rem;
  background: #4361ee;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.95rem;
}

.controls button:hover { background: #3451d1; }

#loading {
  text-align: center;
  padding: 3rem;
}

.spinner {
  width: 48px;
  height: 48px;
  border: 5px solid #dee2e6;
  border-top-color: #4361ee;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin { to { transform: rotate(360deg); } }

#error-msg {
  background: #fff5f5;
  border: 2px solid #fc8181;
  border-radius: 6px;
  padding: 1rem;
  color: #c53030;
  margin-bottom: 1rem;
}

#post-count {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 1rem;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.25rem;
}

.post-card {
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.25rem;
}

.post-card h3 {
  font-size: 0.95rem;
  text-transform: capitalize;
  margin: 0 0 0.5rem;
  color: #1a1a2e;
}

.post-card p {
  font-size: 0.85rem;
  color: #555;
  margin: 0 0 0.75rem;
  line-height: 1.5;
}

.post-card .post-id {
  font-size: 0.75rem;
  color: #999;
}

.pagination {
  display: flex;
  gap: 0.5rem;
  margin-top: 2rem;
  flex-wrap: wrap;
}

.page-btn {
  padding: 0.4rem 0.85rem;
  border: 2px solid #dee2e6;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.875rem;
}

.page-btn.active {
  background: #4361ee;
  color: white;
  border-color: #4361ee;
}

.page-btn:hover:not(.active) { border-color: #4361ee; }
```

---

## Part 1: Fetch Posts from the API

### Step 1: Write the fetchPosts function

In `app.js`, write the `fetchPosts` function. It must:

- Use `async/await` and `fetch()`
- Fetch from `https://jsonplaceholder.typicode.com/posts`
- Check `response.ok` and throw an error if the status is not 2xx
- Return the parsed JSON array

Starter code:

```javascript
const API_URL = 'https://jsonplaceholder.typicode.com/posts';

const loadBtn      = document.querySelector('#load-btn');
const retryBtn     = document.querySelector('#retry-btn');
const searchInput  = document.querySelector('#search-input');
const loadingEl    = document.querySelector('#loading');
const errorEl      = document.querySelector('#error-msg');
const postGrid     = document.querySelector('#post-grid');
const postCount    = document.querySelector('#post-count');
const pagination   = document.querySelector('#pagination');

let allPosts   = [];
let currentPage = 1;
const PER_PAGE  = 12;

async function fetchPosts() {
  // TODO: fetch from API_URL
  // TODO: check response.ok — throw Error if not ok
  // TODO: parse and return JSON
}
```

### Step 2: Write the renderCards function

Write `renderCards(posts)` that:

- Clears `postGrid`
- Creates a `.post-card` `<div>` for each post in the array
- Each card shows the post's `title` (capitalized), `body`, and `id`
- Appends all cards to `postGrid`

```javascript
function renderCards(posts) {
  postGrid.innerHTML = '';

  if (posts.length === 0) {
    postGrid.innerHTML = '<p>No posts match your search.</p>';
    return;
  }

  posts.forEach(function(post) {
    const card = document.createElement('div');
    card.className = 'post-card';
    // TODO: set card.innerHTML with post.title, post.body, post.id
    // Hint: use textContent for title and body to prevent XSS
    // or sanitize before using innerHTML
    postGrid.appendChild(card);
  });
}
```

### Step 3: Write the paginated load function

Write `loadPosts()` that:

- Shows the loading indicator
- Calls `fetchPosts()`
- Stores results in `allPosts`
- Calls `displayPage(1)` to show the first page
- Hides loading, handles errors

```javascript
async function loadPosts() {
  loadingEl.hidden = false;
  errorEl.hidden   = true;
  postGrid.innerHTML = '';
  postCount.textContent = '';
  pagination.innerHTML = '';
  retryBtn.hidden = true;

  try {
    // TODO: await fetchPosts() and store in allPosts
    // TODO: call displayPage(1)
  } catch (error) {
    // TODO: show error message in errorEl
    // TODO: show retryBtn
    console.error('loadPosts failed:', error);
  } finally {
    // TODO: hide loadingEl
  }
}
```

---

## Part 2: Pagination

### Step 4: Write displayPage

Write `displayPage(page)` that:

- Accepts a page number (1-based)
- Slices `allPosts` to show `PER_PAGE` items per page
- Calls `renderCards` with the sliced array
- Updates `postCount.textContent`
- Calls `renderPagination(page, totalPages)`

```javascript
function displayPage(page) {
  currentPage = page;
  const filtered = filterPosts(searchInput.value);
  const total    = filtered.length;
  const pages    = Math.ceil(total / PER_PAGE);
  const start    = (page - 1) * PER_PAGE;
  const end      = start + PER_PAGE;
  const pageData = filtered.slice(start, end);

  renderCards(pageData);
  // TODO: update postCount with "Showing X-Y of Z posts"
  renderPagination(page, pages);
}
```

### Step 5: Write renderPagination

Write `renderPagination(currentPage, totalPages)` that:

- Clears `pagination`
- Creates a button for each page number
- Marks the current page button with `class="page-btn active"`
- Adds a click listener to each button that calls `displayPage(n)`

---

## Part 3: Search Filter

### Step 6: Write filterPosts

```javascript
function filterPosts(query) {
  if (!query.trim()) return allPosts;
  const q = query.toLowerCase();
  // TODO: return allPosts filtered where post.title includes q
}
```

### Step 7: Wire up the search input

Add an `'input'` event listener to `searchInput` that calls `displayPage(1)` whenever the value changes.

---

## Part 4: Event Wiring and Testing

### Step 8: Wire buttons

```javascript
loadBtn.addEventListener('click', loadPosts);
retryBtn.addEventListener('click', loadPosts);
```

### Step 9: Simulate a network error

In DevTools, go to the Network tab and set the throttle to "Offline." Click "Load Posts." Verify:

- The loading spinner appears
- After the error, the error message is visible with the error text
- The "Retry" button appears
- Set network back to "No throttling" and click Retry — posts load successfully

---

## Deliverables

Submit to Canvas:

1. `app.js` with all functions implemented
2. `index.html` and `styles.css`
3. Screenshot of posts grid loaded with at least 12 cards visible
4. Screenshot of the search filter showing fewer results for a query term
5. Screenshot of the error state with retry button visible (Network tab set to Offline)
6. Screenshot of pagination buttons at the bottom

---

## Grading Rubric

| Criterion | Points |
|---|---|
| `fetchPosts` uses `async/await`, checks `response.ok`, returns parsed JSON | 20 |
| `renderCards` builds DOM cards safely (no XSS via raw innerHTML with user data) | 15 |
| Loading spinner shows during fetch and hides on completion | 10 |
| Error message displays and retry button appears on network failure | 15 |
| Pagination correctly slices posts and renders page buttons | 20 |
| Search filter works and resets to page 1 on query change | 15 |
| Required screenshots submitted | 5 |
| **Total** | **100** |
