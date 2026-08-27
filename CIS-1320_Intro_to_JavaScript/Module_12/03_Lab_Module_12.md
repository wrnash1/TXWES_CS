# Lab Activity: Module 12 — Event Handling and Listeners

## Course: CIS-1320 Introduction to JavaScript

**Certification Alignment:** JSE — Certified Associate in JavaScript Programming (OpenEDG / JS Institute)

---

## Lab Overview

This lab builds interactive behavior into web pages using the full event model: `addEventListener`, the event object, `preventDefault`, event bubbling, `stopPropagation`, and event delegation. The final part builds a functional task list application using delegation.

**Environment:** VS Code + Live Server extension + Chrome or Firefox DevTools

---

## Setup

Create a project folder called `module12_lab`. Inside it, create these files:

**`index.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module 12 Lab</title>
  <style>
    body { font-family: sans-serif; max-width: 700px; margin: 2rem auto; padding: 0 1rem; }
    h1, h2 { color: #333; }
    button { padding: 0.4rem 0.8rem; margin: 0.25rem; cursor: pointer; }
    input[type="text"] { padding: 0.4rem; width: 250px; }
    .box { width: 200px; height: 120px; background: #d0e8ff; border: 2px solid #3a8dde;
           display: flex; align-items: center; justify-content: center;
           cursor: pointer; user-select: none; margin: 0.5rem 0; }
    .outer { background: #ffd0d0; border: 2px solid #de3a3a; width: 260px; height: 180px;
             display: flex; align-items: center; justify-content: center; }
    .inner { background: #d0ffd0; border: 2px solid #3ade3a; width: 180px; height: 120px;
             display: flex; align-items: center; justify-content: center; }
    .btn-bubble { padding: 0.4rem 0.8rem; }
    #task-input { padding: 0.4rem; width: 220px; }
    #task-list { list-style: none; padding: 0; }
    #task-list li { display: flex; justify-content: space-between; align-items: center;
                    padding: 0.5rem 0.75rem; margin: 0.25rem 0; border: 1px solid #ccc;
                    border-radius: 4px; background: #fafafa; }
    #task-list li.done { text-decoration: line-through; color: #888; background: #f0f0f0; }
    #task-list li .task-text { flex: 1; cursor: pointer; }
    #task-list li .del-btn { background: #e55; color: white; border: none;
                              padding: 0.2rem 0.5rem; border-radius: 3px; cursor: pointer; }
    #log { background: #f8f8f8; border: 1px solid #ddd; padding: 0.5rem;
           font-family: monospace; font-size: 0.85rem; max-height: 150px;
           overflow-y: auto; margin-top: 0.5rem; }
    .selected { background: #fffbcc !important; }
  </style>
</head>
<body>
  <h1>Module 12: Event Handling</h1>

  <h2>Part 1 — addEventListener</h2>
  <button id="multi-btn">Click Me</button>
  <button id="once-btn">Click Once</button>
  <div id="log-p1"></div>

  <h2>Part 2 — Event Object</h2>
  <div class="box" id="mouse-box">Move / Click Me</div>
  <input type="text" id="key-input" placeholder="Type here (keydown demo)">
  <br><br>
  <input type="text" id="live-input" placeholder="Live input demo">
  <p id="live-output"></p>
  <form id="demo-form">
    <input type="text" id="form-field" placeholder="Form field">
    <button type="submit">Submit (intercepted)</button>
  </form>
  <div id="log-p2"></div>

  <h2>Part 3 — Bubbling and stopPropagation</h2>
  <div class="outer" id="outer">
    OUTER
    <div class="inner" id="inner">
      INNER
      <button class="btn-bubble" id="bubble-btn">BUTTON</button>
    </div>
  </div>
  <button id="stop-btn">Add stopPropagation to button</button>
  <div id="log-p3"></div>

  <h2>Part 4 — Event Delegation (Task List)</h2>
  <div>
    <input type="text" id="task-input" placeholder="New task...">
    <button id="add-task-btn">Add Task</button>
  </div>
  <ul id="task-list"></ul>
  <p id="task-status"></p>

  <script src="lab12.js"></script>
</body>
</html>
```

**`lab12.js`** — start empty, add code section by section.

Open with Live Server. Confirm the page loads. Open DevTools Console.

---

## Part 1 — `addEventListener` and Multiple Listeners

**Learning objectives:** Add multiple independent listeners to the same element; use `removeEventListener` with a named function; observe that inline arrows cannot be removed.

### Section 1.1 — Multiple Listeners on One Element

```javascript
// --- Part 1: addEventListener ---

// 1.1 — Multiple independent listeners
const multiBtn = document.getElementById('multi-btn');
const logP1 = document.getElementById('log-p1');

function logEvent(msg) {
  const line = document.createElement('p');
  line.style.margin = '2px 0';
  line.textContent = msg;
  logP1.prepend(line);
}

multiBtn.addEventListener('click', () => logEvent('Listener A fired'));
multiBtn.addEventListener('click', () => logEvent('Listener B fired'));
multiBtn.addEventListener('click', () => logEvent('Listener C fired'));
```

Save. Click "Click Me" several times. Confirm all three messages appear for each click — none overwrites the others.

### Section 1.2 — `removeEventListener` with a Named Function

```javascript
// 1.2 — removeEventListener requires a named function reference
function onceHandler() {
  logEvent('onceHandler fired — will now remove itself');
  document.getElementById('once-btn').removeEventListener('click', onceHandler);
}

document.getElementById('once-btn').addEventListener('click', onceHandler);
```

Save. Click "Click Once" — the message appears. Click again — nothing. The listener removed itself on first execution.

### Section 1.3 — Why Inline Arrows Cannot Be Removed

```javascript
// 1.3 — Attempting to remove an inline arrow listener (this does nothing)
const arrowHandler = () => logEvent('Arrow listener (cannot be removed by anonymous ref)');
multiBtn.addEventListener('click', arrowHandler);

// This line does nothing — different function object:
// multiBtn.removeEventListener('click', () => logEvent('...'));

// This DOES work — same reference:
// multiBtn.removeEventListener('click', arrowHandler);
// Uncomment above to test; arrowHandler fires will stop after that.
```

Observe: `arrowHandler` fires on each click because its reference (`arrowHandler`) is retained. If you use an anonymous inline arrow directly in `addEventListener`, you cannot remove it at all.

---

## Part 2 — The Event Object

**Learning objectives:** Log `event.type`, `event.target`, mouse coordinates, keyboard properties; use `preventDefault` on a form and a link.

### Section 2.1 — Mouse Events

```javascript
// --- Part 2: Event Object ---

const mouseBox = document.getElementById('mouse-box');
const logP2 = document.getElementById('log-p2');

function logP2Event(msg) {
  const line = document.createElement('p');
  line.style.margin = '2px 0';
  line.textContent = msg;
  logP2.prepend(line);
}

// 2.1 — Click: target and coordinates
mouseBox.addEventListener('click', (e) => {
  logP2Event(`click — target: ${e.target.id}, x: ${e.clientX}, y: ${e.clientY}`);
});

// 2.2 — mouseenter / mouseleave (do not bubble)
mouseBox.addEventListener('mouseenter', () => logP2Event('mouseenter — mouse entered the box'));
mouseBox.addEventListener('mouseleave', () => logP2Event('mouseleave — mouse left the box'));
```

Save. Move the mouse into and out of the blue box. Click it. Confirm the three event types log correctly.

### Section 2.2 — Keyboard Events

```javascript
// 2.3 — keydown: key and modifier keys
const keyInput = document.getElementById('key-input');

keyInput.addEventListener('keydown', (e) => {
  logP2Event(`keydown — key: "${e.key}", code: ${e.code}, shift: ${e.shiftKey}, ctrl: ${e.ctrlKey}`);
});
```

Save. Click inside the text input and press several keys including Enter, Escape, Shift+A, and Ctrl+Z. Observe the key values logged.

### Section 2.3 — `input` vs `change`

```javascript
// 2.4 — input fires on every character; change fires on blur
const liveInput = document.getElementById('live-input');
const liveOutput = document.getElementById('live-output');

liveInput.addEventListener('input', (e) => {
  liveOutput.textContent = `Live: "${e.target.value}"`;
});

liveInput.addEventListener('change', (e) => {
  logP2Event(`change fired — committed value: "${e.target.value}"`);
});
```

Save. Type in the live input field — the paragraph updates on every keystroke. Click away (blur) — the `change` event fires once with the final value.

### Section 2.4 — `preventDefault`

```javascript
// 2.5 — Prevent form submission page reload
const demoForm = document.getElementById('demo-form');

demoForm.addEventListener('submit', (e) => {
  e.preventDefault();   // without this, the page would reload
  const value = document.getElementById('form-field').value;
  logP2Event(`Form submitted (intercepted) — value: "${value}"`);
  document.getElementById('form-field').value = '';
});
```

Save. Type text in the form field and press Enter or click Submit. The page must not reload — the value appears in the log. If the page reloads, `preventDefault` is not working.

---

## Part 3 — Event Bubbling and `stopPropagation`

**Learning objectives:** Observe the bubbling order; identify `event.target` vs `event.currentTarget`; use `stopPropagation`; observe it interrupting the chain.

### Section 3.1 — Observing Bubbling

```javascript
// --- Part 3: Bubbling ---

const logP3 = document.getElementById('log-p3');

function logP3Event(msg) {
  const line = document.createElement('p');
  line.style.margin = '2px 0';
  line.textContent = msg;
  logP3.prepend(line);
}

// 3.1 — Add listeners at all three levels
document.getElementById('bubble-btn').addEventListener('click', (e) => {
  logP3Event(`BUTTON — target: ${e.target.id}, currentTarget: ${e.currentTarget.id}`);
});

document.getElementById('inner').addEventListener('click', (e) => {
  logP3Event(`INNER — target: ${e.target.id}, currentTarget: ${e.currentTarget.id}`);
});

document.getElementById('outer').addEventListener('click', (e) => {
  logP3Event(`OUTER — target: ${e.target.id}, currentTarget: ${e.currentTarget.id}`);
});
```

Save. Click the BUTTON. All three listeners fire. Confirm the log shows:

- `target` is always `bubble-btn` (where the click originated)
- `currentTarget` changes for each listener (`bubble-btn`, `inner`, `outer`)

Also click the INNER div (not the button) — two listeners fire (inner, outer). Click OUTER — only one fires.

### Section 3.2 — `stopPropagation`

```javascript
// 3.2 — Toggle stopPropagation on the button
let stopEnabled = false;

document.getElementById('stop-btn').addEventListener('click', () => {
  stopEnabled = !stopEnabled;
  document.getElementById('stop-btn').textContent =
    stopEnabled ? 'Remove stopPropagation from button' : 'Add stopPropagation to button';
  logP3Event(`stopPropagation on button: ${stopEnabled}`);
});

// Replace the button's listener with one that conditionally stops propagation
document.getElementById('bubble-btn').addEventListener('click', (e) => {
  if (stopEnabled) {
    e.stopPropagation();
    logP3Event('BUTTON — stopPropagation called — inner and outer will NOT fire');
  } else {
    logP3Event('BUTTON — no stopPropagation — event will bubble');
  }
});
```

Save. Click "Add stopPropagation to button", then click BUTTON. Only the button's listeners fire — inner and outer are suppressed. Toggle it off — bubbling resumes.

---

## Part 4 — Event Delegation: Task List

**Learning objectives:** Use a single delegated listener to handle clicks on dynamically added elements; distinguish actions by CSS class or data attribute.

### Section 4.1 — Add Tasks

```javascript
// --- Part 4: Event Delegation ---

const taskInput = document.getElementById('task-input');
const taskList  = document.getElementById('task-list');
const taskStatus = document.getElementById('task-status');

let taskIdCounter = 0;

function addTask(text) {
  if (!text.trim()) return;

  const li = document.createElement('li');
  li.dataset.id = ++taskIdCounter;

  const span = document.createElement('span');
  span.classList.add('task-text');
  span.textContent = text;

  const delBtn = document.createElement('button');
  delBtn.classList.add('del-btn');
  delBtn.textContent = 'Delete';
  delBtn.dataset.action = 'delete';

  li.appendChild(span);
  li.appendChild(delBtn);
  taskList.appendChild(li);

  updateTaskStatus();
}

document.getElementById('add-task-btn').addEventListener('click', () => {
  addTask(taskInput.value);
  taskInput.value = '';
  taskInput.focus();
});

taskInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    addTask(taskInput.value);
    taskInput.value = '';
  }
});

// Seed with a few tasks
addTask('Buy groceries');
addTask('Call dentist');
addTask('Walk the dog');
```

Save. Confirm three tasks appear. Add a new task using the button and using Enter.

### Section 4.2 — Delegated Listener for Toggle and Delete

```javascript
// 4.2 — One delegated listener handles ALL interactions
taskList.addEventListener('click', (e) => {
  const li = e.target.closest('li');
  if (!li) return;

  // Delete button clicked
  if (e.target.dataset.action === 'delete') {
    li.remove();
    updateTaskStatus();
    return;
  }

  // Task text clicked — toggle done state
  if (e.target.classList.contains('task-text')) {
    li.classList.toggle('done');
    updateTaskStatus();
  }
});
```

Save. Click on task text to mark tasks done (strikethrough). Click the red Delete button to remove. Add new tasks after — the delegated listener handles them automatically with no additional JavaScript.

### Section 4.3 — Status Counter

```javascript
// 4.3 — Status line: counts total and done
function updateTaskStatus() {
  const total = taskList.querySelectorAll('li').length;
  const done  = taskList.querySelectorAll('li.done').length;
  taskStatus.textContent = `${done} of ${total} tasks complete`;
}

updateTaskStatus();
```

Save. Toggle tasks done and delete tasks — the counter updates accurately.

### Section 4.4 — Verify Delegation with Dynamically Added Tasks

```javascript
// 4.4 — Add a task programmatically after the listener was registered
// The delegated listener handles it with no changes needed
setTimeout(() => {
  addTask('This task was added 2 seconds after page load');
}, 2000);
```

Save. Two seconds after page load a fourth task appears. Click its text and delete button — the delegated listener handles it correctly.

---

## Part 9 — Challenge Exercise

This section is **optional**. It extends the lab with advanced problems that apply event handling and delegation in more demanding scenarios.

### Step 9.1 — Keyboard Shortcut Manager

Add a `<div id="shortcut-log"></div>` to your HTML. Implement a keyboard shortcut system that maps key combinations to actions:

```javascript
const shortcuts = {
  'ctrl+s':     () => console.log('Save triggered'),
  'ctrl+z':     () => console.log('Undo triggered'),
  'ctrl+shift+f': () => console.log('Find triggered'),
  'escape':     () => console.log('Escape pressed — close modals'),
};

function getShortcutKey(e) {
  const parts = [];
  if (e.ctrlKey)  parts.push('ctrl');
  if (e.shiftKey) parts.push('shift');
  if (e.altKey)   parts.push('alt');
  parts.push(e.key.toLowerCase());
  return parts.join('+');
}

document.addEventListener('keydown', e => {
  const key = getShortcutKey(e);
  const action = shortcuts[key];

  if (action) {
    e.preventDefault();
    action();
    document.getElementById('shortcut-log').textContent = `Last shortcut: ${key}`;
  }
});
```

Test each shortcut in the browser. Extend the system by allowing dynamic registration:

```javascript
function registerShortcut(combo, handler) {
  shortcuts[combo.toLowerCase()] = handler;
}

registerShortcut('ctrl+b', () => {
  document.body.style.background =
    document.body.style.background === 'black' ? '' : 'black';
});
```

Verify `Ctrl+B` toggles the background color.

### Step 9.2 — Debounced Input Handler

Add a `<input id="debounced-input" placeholder="Type here...">` and `<p id="debounced-output"></p>`. Implement a `debounce` utility function, then apply it to a live search input so the handler only fires after the user stops typing for 300ms:

```javascript
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

const handleSearch = debounce(e => {
  document.getElementById('debounced-output').textContent =
    `Searching for: "${e.target.value}"`;
  console.log('Search fired:', e.target.value);
}, 300);

document.getElementById('debounced-input').addEventListener('input', handleSearch);
```

Observe the difference: type rapidly and confirm the output only updates after you pause. Compare with an un-debounced version on a second input that fires on every keystroke.

### Step 9.3 — Custom Event System

Implement a minimal event emitter that supports subscribing to, emitting, and unsubscribing from named custom events — without using the DOM:

```javascript
class EventEmitter {
  constructor() {
    this._listeners = {};
  }

  on(event, handler) {
    if (!this._listeners[event]) {
      this._listeners[event] = [];
    }
    this._listeners[event].push(handler);
    return this;   // enable chaining
  }

  off(event, handler) {
    if (!this._listeners[event]) return this;
    this._listeners[event] = this._listeners[event].filter(h => h !== handler);
    return this;
  }

  emit(event, ...args) {
    (this._listeners[event] || []).forEach(h => h(...args));
    return this;
  }
}
```

Test the emitter with a shopping cart scenario:

```javascript
const cart = new EventEmitter();

function onItemAdded(item) {
  console.log(`Added: ${item.name} — $${item.price}`);
}

cart.on('item:add', onItemAdded);
cart.on('item:add', item => console.log(`Cart total items: ${item.quantity}`));

cart.emit('item:add', { name: 'Widget', price: 9.99, quantity: 1 });
cart.emit('item:add', { name: 'Gadget', price: 24.99, quantity: 2 });

cart.off('item:add', onItemAdded);
cart.emit('item:add', { name: 'Doohickey', price: 4.99, quantity: 3 });
// After off: only the quantity listener fires
```

Extend the emitter with an `once(event, handler)` method that auto-removes the handler after it fires once.

---

## Lab Completion Checklist

- [ ] Three `click` listeners on `multi-btn` all fire independently
- [ ] `onceHandler` fires once then removes itself via `removeEventListener`
- [ ] Mouse click on blue box logs `target`, `clientX`, `clientY`
- [ ] `mouseenter` and `mouseleave` log when mouse enters and leaves the box
- [ ] Keyboard `keydown` logs `key`, `code`, `shiftKey`, `ctrlKey`
- [ ] `input` event updates live output on every keystroke
- [ ] `change` event fires once on blur with the final value
- [ ] `preventDefault` on form submission prevents page reload
- [ ] Clicking BUTTON logs all three bubbling levels in order
- [ ] `event.target` stays constant (the clicked element); `event.currentTarget` changes per listener
- [ ] `stopPropagation` on button prevents inner/outer listeners from firing
- [ ] Task list renders three initial tasks
- [ ] Clicking task text toggles `done` class (strikethrough)
- [ ] Clicking Delete removes the task
- [ ] Adding new tasks — delegated listener handles them without extra code
- [ ] Dynamically added task (setTimeout) is handled correctly
- [ ] Status counter updates accurately after each toggle and delete
