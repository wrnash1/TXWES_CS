# Video Script: Module 12 — Software Design Patterns

## Course: CIS-3350 Software Engineering and Agile

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Scrum.org PSM I / Software Engineering Best Practices

---

### Production Notes

- Camera: Instructor on screen for introduction and all section transitions
- Slides: Title cards for each section heading; UML diagrams shown alongside code
- [SHOW CODE] tags indicate cuts to code panels (JavaScript examples)
- [PAUSE] tags indicate natural stopping points for student reflection
- [SHOW DIAGRAM] tags indicate cuts to UML class diagrams

---

### Introduction (0:00 – 1:30)

Welcome back. I'm Professor Nash, and this is Module 12 of CIS-3350 Software Engineering and Agile.

Today's topic is **software design patterns** — reusable solutions to recurring design problems that experienced engineers have documented, named, and shared over decades.

Design patterns are one of the most important vocabulary sets you will carry in your professional career. When an architect says "use the Observer pattern here" or "this is a Strategy," the whole team understands immediately — no lengthy explanation required. That shared language is one of design patterns' most practical values.

By the end of this module you will be able to:

- Identify the three Gang of Four pattern categories and explain the purpose of each
- Implement Singleton, Factory, and Builder creational patterns with code examples
- Apply Adapter, Decorator, and Facade structural patterns to design problems
- Use Observer, Strategy, and Command behavioral patterns in realistic scenarios
- Select the appropriate pattern given a design constraint

[PAUSE — title slide with objectives]

---

### Section 1: The Gang of Four and Three Categories (1:30 – 4:00)

In 1994, four authors — Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides — published a book called *Design Patterns: Elements of Reusable Object-Oriented Software*. They catalogued 23 patterns and organized them into three categories. Software engineers universally call these authors the Gang of Four, and their framework remains the definitive vocabulary of object-oriented design.

[SHOW DIAGRAM — three-category taxonomy tree]

The three categories are based on what kind of problem the pattern addresses:

**Creational patterns** concern how objects are created. They decouple the instantiation process from the clients that need objects, making systems flexible and independent of specific classes.

**Structural patterns** concern how classes and objects are composed into larger structures. They identify efficient ways to realize relationships between entities — how to build bigger things from smaller pieces.

**Behavioral patterns** concern how objects communicate and how responsibility is distributed among them. They define the protocols for interaction between components.

Today we'll cover three patterns from each category — nine patterns total — with JavaScript code examples throughout.

---

### Section 2: Creational Patterns (4:00 – 9:00)

### The Singleton Pattern

The Singleton ensures a class has exactly one instance and provides a global access point to it.

Classic use cases: a logger that all modules write to, a configuration manager, a database connection pool, a cache.

[SHOW CODE]

```javascript
// singleton.js
class AppConfig {
  constructor() {
    this.theme = 'light';
    this.apiUrl = 'https://api.example.com';
    this.logLevel = 'warn';
  }

  static getInstance() {
    if (!AppConfig._instance) {
      AppConfig._instance = new AppConfig();
    }
    return AppConfig._instance;
  }
}

AppConfig._instance = null;

module.exports = AppConfig;

// Usage — both references point to the same object
const configA = AppConfig.getInstance();
const configB = AppConfig.getInstance();
console.log(configA === configB); // true
```

[PAUSE]

The `_instance` is stored as a class-level property. The first call to `getInstance()` creates it; every subsequent call returns the same object. Notice the constructor is not private here — JavaScript doesn't enforce that — but the convention is to always use `getInstance()` and never call `new AppConfig()` directly.

The critical concern: **thread safety**. In multi-threaded environments, two threads could simultaneously check `_instance === null`, both find it null, and both create instances. JavaScript's single-threaded event loop avoids this for browser/Node code, but in multi-threaded environments you need a lock around the initialization check.

### The Factory Method Pattern

Factory Method defines an interface for creating objects but lets subclasses decide which class to instantiate.

[SHOW CODE]

```javascript
// factory.js — payment processor factory
class PaymentProcessor {
  process(amount) {
    throw new Error('process() must be implemented');
  }
}

class CreditCardProcessor extends PaymentProcessor {
  process(amount) {
    return `Charged $${amount} to credit card`;
  }
}

class PayPalProcessor extends PaymentProcessor {
  process(amount) {
    return `Sent $${amount} via PayPal`;
  }
}

class BankTransferProcessor extends PaymentProcessor {
  process(amount) {
    return `Initiated $${amount} bank transfer`;
  }
}

// Factory function
function createPaymentProcessor(method) {
  const processors = {
    creditCard: CreditCardProcessor,
    paypal: PayPalProcessor,
    bankTransfer: BankTransferProcessor,
  };

  const ProcessorClass = processors[method];
  if (!ProcessorClass) {
    throw new Error(`Unknown payment method: ${method}`);
  }
  return new ProcessorClass();
}

// Client code never uses 'new CreditCardProcessor()' directly
const processor = createPaymentProcessor('paypal');
console.log(processor.process(49.99)); // "Sent $49.99 via PayPal"
```

[PAUSE]

Adding a new payment method means adding a new class and one entry in the `processors` map. No existing code changes. This is the Open/Closed Principle: open for extension, closed for modification.

### The Builder Pattern

Builder constructs complex objects step by step, separating construction from representation.

[SHOW CODE]

```javascript
// builder.js — query builder
class QueryBuilder {
  constructor(table) {
    this.table = table;
    this.conditions = [];
    this.selectedColumns = ['*'];
    this.limitValue = null;
    this.orderByColumn = null;
  }

  select(...columns) {
    this.selectedColumns = columns;
    return this;  // enables method chaining
  }

  where(condition) {
    this.conditions.push(condition);
    return this;
  }

  orderBy(column) {
    this.orderByColumn = column;
    return this;
  }

  limit(n) {
    this.limitValue = n;
    return this;
  }

  build() {
    let query = `SELECT ${this.selectedColumns.join(', ')} FROM ${this.table}`;
    if (this.conditions.length > 0) {
      query += ` WHERE ${this.conditions.join(' AND ')}`;
    }
    if (this.orderByColumn) {
      query += ` ORDER BY ${this.orderByColumn}`;
    }
    if (this.limitValue) {
      query += ` LIMIT ${this.limitValue}`;
    }
    return query;
  }
}

const query = new QueryBuilder('orders')
  .select('id', 'customer', 'total')
  .where('status = "pending"')
  .where('total > 100')
  .orderBy('created_at')
  .limit(25)
  .build();

console.log(query);
// SELECT id, customer, total FROM orders
// WHERE status = "pending" AND total > 100
// ORDER BY created_at LIMIT 25
```

[PAUSE]

The key insight of Builder: `return this` on each method enables **fluent method chaining**, and `build()` produces the final object. Each optional part of the construction can be included or omitted independently.

---

### Section 3: Structural Patterns (9:00 – 14:00)

### The Adapter Pattern

Adapter converts the interface of a class into another interface clients expect.

[SHOW CODE]

```javascript
// adapter.js — adapting a legacy logger to a new interface
class LegacyLogger {
  writeLog(severity, message) {
    console.log(`[${severity.toUpperCase()}] ${new Date().toISOString()} ${message}`);
  }
}

// New interface the application expects
class ModernLoggerAdapter {
  constructor() {
    this.legacy = new LegacyLogger();
  }

  info(message) {
    this.legacy.writeLog('info', message);
  }

  warn(message) {
    this.legacy.writeLog('warn', message);
  }

  error(message) {
    this.legacy.writeLog('error', message);
  }
}

// Application code uses the modern interface
const logger = new ModernLoggerAdapter();
logger.info('Application started');
logger.warn('Low disk space');
logger.error('Database connection failed');
```

[PAUSE]

The adapter wraps the legacy system and exposes the modern interface. Application code is completely decoupled from the legacy implementation — swap out the legacy logger and only the adapter changes.

### The Decorator Pattern

Decorator attaches additional responsibilities to an object dynamically.

[SHOW CODE]

```javascript
// decorator.js — HTTP request decorators
class BaseRequest {
  send(url) {
    return fetch(url);
  }
}

class LoggingDecorator {
  constructor(request) {
    this.request = request;
  }

  send(url) {
    console.log(`Sending request to: ${url}`);
    return this.request.send(url);
  }
}

class RetryDecorator {
  constructor(request, maxRetries = 3) {
    this.request = request;
    this.maxRetries = maxRetries;
  }

  async send(url) {
    for (let attempt = 1; attempt <= this.maxRetries; attempt++) {
      try {
        return await this.request.send(url);
      } catch (err) {
        if (attempt === this.maxRetries) throw err;
        console.log(`Retry ${attempt} of ${this.maxRetries}`);
      }
    }
  }
}

// Stack decorators — logging + retry
const request = new RetryDecorator(new LoggingDecorator(new BaseRequest()));
request.send('https://api.example.com/data');
```

[PAUSE]

Each decorator wraps the object before it and adds one layer of behavior. You can stack any combination — logging, retry, caching, authentication headers — without modifying `BaseRequest`. New behaviors are new decorators, not modifications to existing classes.

### The Facade Pattern

Facade provides a simplified interface to a complex subsystem.

[SHOW CODE]

```javascript
// facade.js — home theater system
class Amplifier {
  on() { console.log('Amp on'); }
  setVolume(v) { console.log(`Volume: ${v}`); }
}

class Projector {
  on() { console.log('Projector on'); }
  setInput(input) { console.log(`Input: ${input}`); }
}

class StreamingPlayer {
  on() { console.log('Player on'); }
  play(movie) { console.log(`Playing: ${movie}`); }
}

// Facade — one simple interface for the whole system
class HomeTheaterFacade {
  constructor() {
    this.amp = new Amplifier();
    this.projector = new Projector();
    this.player = new StreamingPlayer();
  }

  watchMovie(movie) {
    this.amp.on();
    this.amp.setVolume(20);
    this.projector.on();
    this.projector.setInput('HDMI');
    this.player.on();
    this.player.play(movie);
  }
}

// Client code — one method call instead of six
const theater = new HomeTheaterFacade();
theater.watchMovie('Inception');
```

[PAUSE]

The Facade is especially useful when a complex subsystem needs a simple entry point for most common use cases, while still allowing direct access to subsystem components when needed.

---

### Section 4: Behavioral Patterns (14:00 – 19:30)

### The Observer Pattern

Observer defines a one-to-many dependency so that when one object changes state, all dependents are notified automatically.

[SHOW CODE]

```javascript
// observer.js — stock price notification system
class StockTicker {
  constructor(symbol) {
    this.symbol = symbol;
    this.price = 0;
    this.observers = [];
  }

  subscribe(observer) {
    this.observers.push(observer);
  }

  unsubscribe(observer) {
    this.observers = this.observers.filter(o => o !== observer);
  }

  setPrice(price) {
    this.price = price;
    this._notify();
  }

  _notify() {
    for (const observer of this.observers) {
      observer.update(this.symbol, this.price);
    }
  }
}

class PriceAlertObserver {
  constructor(threshold) { this.threshold = threshold; }
  update(symbol, price) {
    if (price < this.threshold) {
      console.log(`ALERT: ${symbol} dropped to $${price}`);
    }
  }
}

class PortfolioObserver {
  update(symbol, price) {
    console.log(`Portfolio update: ${symbol} = $${price}`);
  }
}

const aapl = new StockTicker('AAPL');
aapl.subscribe(new PriceAlertObserver(150));
aapl.subscribe(new PortfolioObserver());

aapl.setPrice(175);  // Portfolio update: AAPL = $175
aapl.setPrice(145);  // Portfolio update + ALERT
```

[PAUSE]

The subject — `StockTicker` — knows nothing specific about its observers. It only knows they have an `update()` method. New observer types can be added in future Sprints without changing the subject at all. This loose coupling is one of Observer's defining strengths.

### The Strategy Pattern

Strategy defines a family of algorithms, encapsulates each one, and makes them interchangeable.

[SHOW CODE]

```javascript
// strategy.js — sorting strategies
class BubbleSortStrategy {
  sort(data) {
    const arr = [...data];
    for (let i = 0; i < arr.length - 1; i++) {
      for (let j = 0; j < arr.length - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        }
      }
    }
    return arr;
  }
}

class QuickSortStrategy {
  sort(data) {
    if (data.length <= 1) return data;
    const pivot = data[Math.floor(data.length / 2)];
    const left = data.filter(x => x < pivot);
    const mid = data.filter(x => x === pivot);
    const right = data.filter(x => x > pivot);
    return [...this.sort(left), ...mid, ...this.sort(right)];
  }
}

class DataSorter {
  constructor(strategy) {
    this.strategy = strategy;
  }

  setStrategy(strategy) {
    this.strategy = strategy;
  }

  sort(data) {
    return this.strategy.sort(data);
  }
}

const sorter = new DataSorter(new QuickSortStrategy());
console.log(sorter.sort([5, 3, 8, 1, 9])); // [1, 3, 5, 8, 9]

// Swap strategies at runtime
sorter.setStrategy(new BubbleSortStrategy());
console.log(sorter.sort([5, 3, 8, 1, 9])); // same result, different algorithm
```

[PAUSE]

### The Command Pattern

Command encapsulates a request as an object, allowing requests to be queued, logged, or undone.

[SHOW CODE]

```javascript
// command.js — text editor with undo
class TextEditor {
  constructor() { this.text = ''; }
  insert(text) { this.text += text; }
  delete(count) { this.text = this.text.slice(0, -count); }
}

class InsertCommand {
  constructor(editor, text) {
    this.editor = editor;
    this.text = text;
  }
  execute() { this.editor.insert(this.text); }
  undo() { this.editor.delete(this.text.length); }
}

class CommandHistory {
  constructor() { this.history = []; }

  execute(command) {
    command.execute();
    this.history.push(command);
  }

  undo() {
    const command = this.history.pop();
    if (command) command.undo();
  }
}

const editor = new TextEditor();
const history = new CommandHistory();

history.execute(new InsertCommand(editor, 'Hello'));
history.execute(new InsertCommand(editor, ', World'));
console.log(editor.text); // "Hello, World"

history.undo();
console.log(editor.text); // "Hello"
```

[PAUSE]

Command makes operations first-class objects that can be stored, queued, logged, and reversed. The undo functionality in every text editor, graphics program, and database uses a variant of this pattern.

---

### Section 5: Pattern Selection and Scrum Context (19:30 – 23:00)

How do you choose which pattern to apply? Here is a practical decision framework:

- If you need exactly one instance of something shared across the app — **Singleton**
- If you're creating objects but want to defer the specific class choice — **Factory**
- If you're building a complex object with many optional parts — **Builder**
- If you need to make two incompatible interfaces work together — **Adapter**
- If you want to add behaviors to objects without subclassing — **Decorator**
- If you want to simplify access to a complex subsystem — **Facade**
- If you need one change to notify many dependents automatically — **Observer**
- If you need interchangeable algorithms at runtime — **Strategy**
- If you need operations that can be queued, logged, or undone — **Command**

[PAUSE]

In Scrum, design patterns directly support **Agile Manifesto Principle 9**: continuous attention to technical excellence and good design enhances agility. A codebase built on well-chosen patterns absorbs Sprint-over-Sprint feature additions without constant rework. New features become new Strategy classes, new Observer implementations, new Factory branches — not modifications to existing, tested code.

The Retrospective is the right forum to discuss whether the team's current design is creating friction for future Sprints. If every Sprint requires changing the same class, the team may need a pattern-based refactoring as a backlog item.

---

### Closing Summary (23:00 – 24:00)

Design patterns fall into three Gang of Four categories: Creational (Singleton, Factory, Builder), Structural (Adapter, Decorator, Facade), and Behavioral (Observer, Strategy, Command).

Each pattern solves a specific recurring problem: Singleton controls shared instances, Factory decouples object creation, Builder assembles complex objects step-by-step, Adapter bridges incompatible interfaces, Decorator adds behavior dynamically, Facade simplifies subsystems, Observer notifies dependents automatically, Strategy makes algorithms swappable, and Command encapsulates operations for undo and queuing.

Patterns are a shared vocabulary and a set of proven solutions — use them when they fit, not as a requirement to apply for every problem.

In Module 13 we'll turn to code quality and refactoring — how to identify problems in existing code and systematically improve it, often by applying the patterns we learned today.

See you there.

[END OF SCRIPT]
