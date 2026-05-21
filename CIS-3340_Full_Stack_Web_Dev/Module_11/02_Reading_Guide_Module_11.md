# Reading Guide: Module 11 - Frontend Frameworks (React)
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 11 - Frontend Frameworks (React)**! This module introduces React — Facebook's open-source JavaScript library for building component-based user interfaces. You will learn the core mental model behind React: breaking a UI into reusable, isolated components, describing the UI with JSX syntax, and letting React efficiently update only the changed parts of the DOM through its Virtual DOM reconciliation algorithm. React is the dominant front-end framework for AWS full-stack applications and is the basis for the state management and hooks topics covered in Module 12.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **Single Page Application (SPA)**: A web application that loads a single HTML document and dynamically updates the visible content using JavaScript — without navigating to a new URL or triggering a full browser page reload. React applications are SPAs: React Router intercepts navigation events and renders different components based on the URL path while the HTML shell and JavaScript bundle remain loaded in memory.
*   **React Virtual DOM**: An in-memory JavaScript representation of the real DOM tree. When component state or props change, React re-renders the affected components into the Virtual DOM first, computes a diff between the previous and new Virtual DOM trees (reconciliation), and applies only the minimal set of real DOM changes required. This avoids expensive full-page repaints and makes React highly performant for frequent UI updates.
*   **Components**: The fundamental building blocks of a React application — self-contained, reusable JavaScript functions (or classes) that accept input data via `props` and return JSX describing what the UI should look like. A component can be as small as a styled button or as large as a full-page layout. Components compose together to build the complete application tree.
*   **JSX syntax**: A JavaScript syntax extension that allows writing HTML-like markup directly inside JavaScript code. JSX is compiled to `React.createElement()` calls by Babel during the build step. Key JSX rules: use `className` instead of `class`, use `htmlFor` instead of `for`, close all tags (including self-closing ones like `<img />`), and wrap multiple elements in a single parent element or Fragment (`<>`).
*   **Build pipelines**: The automated toolchain that transforms React JSX and modern JavaScript into optimized, browser-compatible static files (HTML, CSS, JS bundles) ready for deployment. `create-react-app` uses Webpack + Babel internally; Vite is the modern alternative. `npm run build` produces the production `build/` directory that is deployed to AWS S3, CloudFront, or Amplify as a static site.

---

### 2. Certification Exam Tips
*   **React Build Artifacts and AWS S3 + CloudFront:** The DVA-C02 exam tests static site deployment on AWS. A React application built with `npm run build` produces a `build/` folder of static files. These are uploaded to an S3 bucket configured for static website hosting, and a CloudFront distribution is placed in front for HTTPS and CDN caching. Know the steps: S3 bucket policy, CloudFront origin, and cache invalidation after deployments.
*   **AWS Amplify Simplifies React Deployment:** The exam includes scenarios about AWS Amplify Hosting — a service that automates the S3 + CloudFront deployment pipeline with git-based CI/CD. Connecting a GitHub repository to Amplify automatically builds and deploys on every push to the main branch.
*   **Study Resource:** The official React documentation was completely rewritten in 2023 and is now the best free reference for learning React. [React.dev — Quick Start](https://react.dev/learn) covers components, JSX, props, and state with interactive code sandboxes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Part 1 covering **React Fundamentals** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part1) — this section introduces components, JSX, and the basic React rendering model.
*   **Required Video:** Watch the React introduction section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering component creation, JSX syntax, and the Virtual DOM concept.

---

### Lab & Command Integration
In this week's hands-on lab, you will set up and build your first React application:
*   **Setup base React project skeleton**: Run `npm create vite@latest my-app -- --template react` (Vite) or `npx create-react-app my-app` to scaffold a new React project, then `cd my-app && npm install && npm run dev` to start the development server.
*   **Convert HTML blocks to JSX component templates**: Take an existing static HTML page section (e.g., a header and card grid) and refactor it into reusable React functional components — replacing `class` with `className` and ensuring all tags are properly closed.
*   **Inspect Virtual DOM structures**: Open React DevTools (browser extension) while the development server is running to visualize the component tree, inspect props values, and observe how re-renders occur when you interact with the UI.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Part 1 covering **React Fundamentals** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part1).
- [ ] Watch the React section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Install the [React Developer Tools](https://react.dev/learn/react-developer-tools) browser extension before starting the lab.
- [ ] Proceed to the weekly hands-on lab activity.
