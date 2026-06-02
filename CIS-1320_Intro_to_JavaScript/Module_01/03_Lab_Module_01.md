# Lab Activity: Module 01 — JavaScript Introduction and Execution

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Overview

In this lab you will write your first JavaScript programs, connect them to HTML pages, and observe them running in the browser. You will use VS Code as your editor and Chrome (or Firefox) as your browser. No installation beyond VS Code is needed for this module — JavaScript runs directly in every browser.

By the end of this lab you will have:

- Created an HTML page with an embedded JavaScript script block
- Used `console.log()` to print values to the browser console
- Explored the browser DevTools Console interactively
- Refactored to an external `.js` file linked via the `src` attribute
- Observed and fixed the classic script-placement null-reference error using `defer`

---

## Prerequisites

- VS Code installed on your computer
- Google Chrome or Mozilla Firefox installed
- The Module 01 reading guide completed

---

## Lab Setup

Create a dedicated folder for this lab. In VS Code, open a new folder named `module01-lab`. All files for this lab go inside that folder.

If you have not installed the **Live Server** extension for VS Code, install it now: open the Extensions panel (Ctrl+Shift+X), search for "Live Server" by Ritwick Dey, and click Install. Live Server lets you open HTML files in a browser with automatic reload on save, which simplifies development.

---

## Part 1 — Your First JavaScript Page

### Step 1.1 — Create the HTML File

Inside `module01-lab`, create a new file named `index.html`. Type the following exactly — do not copy-paste; typing it once helps you remember the structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module 01 Lab</title>
</head>
<body>
  <h1>CIS-1320 — Module 01 Lab</h1>
  <p>Open DevTools (F12) and click the Console tab to see output.</p>

  <script>
    console.log('Hello, World!');
    console.log('My name is [your name]');
    console.log('CIS-1320 Module 01 Lab');
  </script>
</body>
```

Replace `[your name]` with your actual first name.

### Step 1.2 — Open in the Browser

Right-click `index.html` in VS Code and choose **Open with Live Server**. Chrome should open automatically. If it does not, find the address bar at the bottom of VS Code that says something like `Port: 5500` and navigate to `http://127.0.0.1:5500/index.html` in your browser.

### Step 1.3 — Open DevTools

Press **F12** (or Fn+F12 on some laptops) to open Chrome DevTools. Click the **Console** tab. You should see your three `console.log()` lines printed.

### Step 1.4 — Log More Data Types

Add these lines inside the `<script>` block, below your existing `console.log` calls. Save the file and observe the console update automatically via Live Server:

```javascript
console.log(42);
console.log(3.14);
console.log(true);
console.log(false);
console.log(null);
console.log(2 + 3);
console.log('JavaScript' + ' ' + 'is' + ' ' + 'fun');
```

Notice how each data type is displayed differently in the console — numbers are shown in blue, strings in black, booleans in blue, `null` in gray.

### Screenshot 1

Take a screenshot of the browser with DevTools open on the Console tab showing all your `console.log()` output from Steps 1.1 through 1.4. Your HTML page should be visible in the background. Label this screenshot **Lab01-Part1**.

---

## Part 2 — Interactive DevTools Console

The console is not just for displaying output from your script. It is an interactive JavaScript REPL (Read-Eval-Print Loop) — you can type expressions directly and evaluate them.

### Step 2.1 — Type Expressions Directly

Click inside the Console input area (the line starting with `>`). Type each of the following and press Enter after each one. Do not type the `>` — that is already there:

```text
> 10 + 5
> 100 - 37
> 4 * 8
> 20 / 4
> 7 % 3
> 2 ** 10
```

Observe the result of each expression printed on the line below.

### Step 2.2 — String Expressions

```text
> 'Hello, ' + 'World!'
> 'Texas Wesleyan'.length
> 'javascript'.toUpperCase()
> 'PROFESSOR NASH'.toLowerCase()
```

### Step 2.3 — Declare Variables

```text
> let score = 95
> score
> score + 5
> let name = 'Alice'
> 'Hello, ' + name
```

Note that when you declare a variable with `let`, the console shows `undefined` — that is the return value of the declaration statement itself. The variable is created. On the next line, typing `score` evaluates to `95`.

### Step 2.4 — Test `console.error` and `console.warn`

Type these in the console:

```text
> console.error('This is an error message')
> console.warn('This is a warning')
> console.log('This is normal output')
```

Observe the different colors and icons: red for error, yellow for warning, plain for log.

### Screenshot 2

Take a screenshot showing the results of your interactive console session from Part 2. The console should show the arithmetic results, string results, variable declarations, and the error/warn/log styling. Label this screenshot **Lab01-Part2**.

---

## Part 3 — External JavaScript File

### Step 3.1 — Create `app.js`

Inside `module01-lab`, create a new file named `app.js`. Add the following content:

```javascript
// app.js — external JavaScript file for Module 01 Lab

console.log('app.js is loaded and running!');

const course = 'CIS-1320 Introduction to JavaScript';
const module = 'Module 01';
const student = '[your name]';    // replace with your name

console.log('Course:', course);
console.log('Module:', module);
console.log('Student:', student);

// Arithmetic expressions
const a = 15;
const b = 4;
console.log('Sum:', a + b);
console.log('Product:', a * b);
console.log('Quotient:', a / b);
console.log('Remainder:', a % b);
```

Replace `[your name]` with your first name.

### Step 3.2 — Link the External File

Update `index.html` to use the external file. Remove the internal `<script>` block (the whole `<script>...</script>` section including all its contents) and replace it with a single `<script>` tag that links `app.js`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module 01 Lab</title>
</head>
<body>
  <h1>CIS-1320 — Module 01 Lab</h1>
  <p>Open DevTools (F12) and click the Console tab to see output.</p>

  <script src="app.js"></script>
</body>
```

Note that the `<script src="app.js">` tag is placed **at the bottom of `<body>`**, just before `</body>`. This is one valid approach for ensuring the DOM is available when the script runs.

### Step 3.3 — Verify

Save both files. The browser should reload automatically (Live Server). Open DevTools and confirm the Console tab shows the output from `app.js`.

### Screenshot 3

Take a screenshot showing the DevTools console output from the external `app.js` file. The URL bar should show `127.0.0.1:5500` (or similar). Label this screenshot **Lab01-Part3**.

---

## Part 4 — Script Placement and the `defer` Attribute

This part demonstrates the classic null-reference error caused by incorrect script placement, and then fixes it with `defer`.

### Step 4.1 — Create the Demo Page

Create a new file in `module01-lab` named `placement.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Placement Demo</title>
  <script src="placement.js"></script>
</head>
<body>
  <h1>Placement Demo</h1>
  <p id="output">This paragraph is in the body.</p>
</body>
</html>
```

Create a second new file named `placement.js`:

```javascript
// placement.js

const el = document.getElementById('output');
console.log('Element found:', el);

if (el === null) {
  console.error('ERROR: Element is null — script ran before DOM was ready.');
} else {
  console.log('Element text:', el.textContent);
}
```

### Step 4.2 — Observe the Error

Open `placement.html` in Live Server (right-click → Open with Live Server, or navigate to `http://127.0.0.1:5500/placement.html`).

Open DevTools (F12) and look at the Console tab. You should see:

```text
Element found: null
ERROR: Element is null — script ran before DOM was ready.
```

This is the problem: the `<script>` in `<head>` runs before the browser has parsed the `<body>`. The `<p id="output">` element does not exist yet when `document.getElementById('output')` runs, so it returns `null`.

### Step 4.3 — Fix with `defer`

Edit `placement.html`. Add the `defer` attribute to the `<script>` tag:

```html
<script src="placement.js" defer></script>
```

Save and reload. The console should now show:

```text
Element found: <p id="output">...</p>
Element text: This paragraph is in the body.
```

With `defer`, the browser downloads `placement.js` in parallel while parsing the HTML, but does not execute it until the entire HTML document has been parsed. When the script runs, the `<p>` element already exists.

### Step 4.4 — Verify the Fix

Confirm the console shows the element and its text content, with no null error.

### Screenshot 4

Take a side-by-side screenshot (or two separate screenshots) showing:

1. The console output **without** `defer` (showing `null` and the error message)
2. The console output **with** `defer` (showing the element and its text content)

Label these **Lab01-Part4a** (without defer) and **Lab01-Part4b** (with defer).

---

## Deliverables

Submit the following to the Module 01 Lab assignment in Canvas:

| Item | Description |
|---|---|
| `index.html` | Final version using `<script src="app.js">` |
| `app.js` | External JavaScript file with your name and arithmetic expressions |
| `placement.html` | Final version with `defer` attribute |
| `placement.js` | The placement demo script |
| Lab01-Part1.png | Console output from Part 1 |
| Lab01-Part2.png | Interactive console session from Part 2 |
| Lab01-Part3.png | External file output from Part 3 |
| Lab01-Part4a.png | Console showing null error (without defer) |
| Lab01-Part4b.png | Console showing successful element read (with defer) |

---

## Reflection Questions

Answer these in the text box on the Canvas submission page (two to three sentences each):

1. In your own words, what is the difference between an internal script block and an external JavaScript file? When would you choose one over the other?

2. Explain what happened in Part 4 when the script was in `<head>` without `defer`. Why did the element come back as `null`?

3. What is one thing you discovered by typing expressions directly in the browser console that you did not expect?

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Console shows nothing | DevTools not open or wrong tab | Press F12, click Console tab |
| "Cannot find module" or 404 in console | `app.js` path wrong or file not saved | Check that `app.js` is in the same folder as `index.html` |
| Live Server not reloading | File not saved | Press Ctrl+S in VS Code |
| Console shows `null` in Part 3 | Script is in `<head>` without `defer` | Move script to end of `<body>` or add `defer` |
| `console.log` output not visible | Output may be filtered | Click the "All levels" filter button in the DevTools Console |
