# Lab 01: Building a Semantic HTML5 Page

**Course:** CIS-3340 Full Stack Web Development
**Module:** 01 - HTML5 Semantics & SEO
**Texas Wesleyan University | Professor Nash**
**Total Points:** 100

---

## Overview

In this lab you will build a complete, valid HTML5 page using semantic elements and correct SEO metadata. You will write all markup by hand in a plain text editor or VS Code. No CSS, JavaScript, or frameworks are used in this lab — the focus is entirely on correct document structure.

By the end of this lab you will have a page that passes the W3C Nu HTML Checker with zero errors, demonstrates a correct heading hierarchy, and includes all required `<head>` metadata.

---

## Prerequisites

- A text editor (VS Code is recommended) or any plain-text editor
- A modern web browser (Chrome or Firefox)
- Internet access to run the W3C Nu HTML Checker at validator.w3.org
- No installations or command-line tools are required for this lab

---

## Scenario

You are a front-end developer building the department homepage for the fictional Ramsey College of Technology at a regional university. The page must be accessible, SEO-ready, and structurally correct before the design team applies CSS styles in the next sprint.

---

## Part 1: Build the HTML Structure

### Step 1: Create the project file

Create a new file named `index.html`. Do not use any template from your editor — start with a completely blank file.

### Step 2: Add the document skeleton

Type the following skeleton exactly. Do not copy-paste — typing forces you to think about each declaration.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="">
  <title></title>
</head>
<body>

</body>
</html>
```

Fill in the `<meta name="description">` content with a 150 to 160 character description of the Ramsey College of Technology. Fill in `<title>` with a page title under 60 characters following the pattern: `Page Name | Site Name`.

### Step 3: Add the page header

Inside `<body>`, add a `<header>` element containing your single `<h1>` and a tagline paragraph.

```html
<header>
  <h1>Ramsey College of Technology</h1>
  <p>Preparing the next generation of technology professionals.</p>
</header>
```

### Step 4: Add primary navigation

Below the `<header>`, add a `<nav>` element with an `aria-label` of "Primary navigation". Include an unordered list with at least four links.

```html
<nav aria-label="Primary navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/programs">Programs</a></li>
    <li><a href="/faculty">Faculty</a></li>
    <li><a href="/admissions">Admissions</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

### Step 5: Add the main content area

Add a `<main>` element. Inside it, add an `<article>` for the primary editorial content and an `<aside>` for supplementary links.

```html
<main>
  <article>
    <h2>Welcome to Ramsey College of Technology</h2>
    <p>Our college offers bachelor and master degree programs in computer science,
       information technology, cybersecurity, and data analytics. Our curriculum
       is aligned to industry certifications and real-world project experience.</p>

    <h3>Featured Programs</h3>
    <ul>
      <li>
        <h4>Bachelor of Science in Computer Science</h4>
        <p>A four-year program covering software engineering, algorithms, and
           cloud computing. Aligned to the AWS Certified Developer Associate
           certification in the senior year.</p>
      </li>
      <li>
        <h4>Bachelor of Science in Cybersecurity</h4>
        <p>Hands-on training in network defense, penetration testing, and
           security operations center procedures.</p>
      </li>
      <li>
        <h4>Master of Science in Data Analytics</h4>
        <p>Advanced coursework in statistical modeling, machine learning,
           and enterprise data visualization.</p>
      </li>
    </ul>

    <h3>Upcoming Events</h3>
    <ul>
      <li>
        <time datetime="2025-09-15">September 15, 2025</time> — Fall Open House
      </li>
      <li>
        <time datetime="2025-10-01">October 1, 2025</time> — Career Fair
      </li>
    </ul>
  </article>

  <aside>
    <h2>Quick Resources</h2>
    <ul>
      <li><a href="/schedule">Class Schedule</a></li>
      <li><a href="/advising">Academic Advising</a></li>
      <li><a href="/tutoring">Tutoring Center</a></li>
      <li><a href="/labs">Computer Labs</a></li>
    </ul>
  </aside>
</main>
```

### Step 6: Add an image with correct alt text

Inside the `<article>`, after the welcome paragraph, add an image element. Use a placeholder URL for the `src` attribute. Write descriptive `alt` text that describes what the image shows — not the filename.

```html
<figure>
  <img src="images/campus-lab.jpg"
       alt="Students collaborating at workstations in the Ramsey College computer lab"
       width="900"
       height="500">
  <figcaption>Students in the advanced networking lab, Building C.</figcaption>
</figure>
```

### Step 7: Add a decorative separator image

After the events list, add a decorative horizontal divider image with the correct empty `alt` attribute.

```html
<img src="images/divider.png" alt="" role="presentation">
```

### Step 8: Add the footer

Below `<main>`, add a `<footer>` element with copyright text, a contact address, and at least two footer navigation links.

```html
<footer>
  <address>
    Ramsey College of Technology<br>
    1234 University Boulevard<br>
    Fort Worth, TX 76105<br>
    <a href="mailto:rct@university.edu">rct@university.edu</a>
  </address>
  <nav aria-label="Footer navigation">
    <ul>
      <li><a href="/privacy">Privacy Policy</a></li>
      <li><a href="/accessibility">Accessibility Statement</a></li>
      <li><a href="/sitemap">Sitemap</a></li>
    </ul>
  </nav>
  <p>&copy; 2025 Ramsey College of Technology. All rights reserved.</p>
</footer>
```

### Step 9: Add Open Graph metadata

Return to the `<head>` section and add Open Graph tags below your `<meta name="description">` line.

```html
<meta property="og:title" content="Ramsey College of Technology">
<meta property="og:description"
      content="Degree programs in CS, cybersecurity, and data analytics.">
<meta property="og:image"
      content="https://university.edu/images/rct-og.jpg">
<meta property="og:url" content="https://university.edu/rct">
<meta property="og:type" content="website">
```

---

## Part 2: Validate and Test

### Step 10: Browser preview

Open `index.html` in Chrome. The page will be unstyled — that is expected. Verify:

- The page title appears in the browser tab
- All headings render with the browser's default size hierarchy (h1 largest, h4 smallest)
- All navigation links are visible and underlined
- The image placeholder area shows a broken-image icon (the `src` file does not exist, but the `alt` text should be readable)
- The footer contact information and copyright text are visible

### Step 11: W3C Nu HTML Checker validation

Navigate to validator.w3.org in your browser.

Choose the "Validate by text input" option.

Copy the entire contents of your `index.html` file and paste it into the text area.

Click "Check."

A passing result shows a green banner reading "Document checking completed. No errors or warnings to show."

If you see errors, read each message carefully. Common beginner errors include:

- Missing `alt` attribute on an `<img>` element
- Heading level skipped (for example, `<h4>` used without a preceding `<h3>` in the same section)
- Duplicate `id` attribute values
- A `<meta>` tag placed after non-metadata elements in `<head>`

Fix each error and re-validate until the checker passes with zero errors.

### Step 12: Accessibility check with browser DevTools

In Chrome, open DevTools (F12), click the "Elements" panel, then select any landmark element (`<header>`, `<nav>`, `<main>`, `<footer>`). In the right panel, click "Accessibility."

Verify each landmark has the correct role listed:

- `<header>` should show role: banner
- `<nav>` should show role: navigation
- `<main>` should show role: main
- `<footer>` should show role: contentinfo

---

## Deliverables

Submit the following to the Canvas assignment portal:

1. Your completed `index.html` file (attach the file, do not paste the code into the text box)
2. A screenshot showing the W3C Nu HTML Checker passing with zero errors (the green success banner must be visible along with the URL or the pasted source in the background)
3. A screenshot of the rendered, unstyled page in your browser showing visible headings, navigation, and footer content

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Correct document skeleton: DOCTYPE, html lang, charset, viewport, description, title | 15 |
| All six required landmark elements present and correctly nested | 20 |
| Correct heading hierarchy — no skipped levels, one h1 only | 15 |
| At least one informational image with descriptive alt text | 10 |
| At least one decorative image with empty alt and role="presentation" | 5 |
| Open Graph metadata present and complete | 10 |
| Footer includes address, navigation, and copyright | 10 |
| W3C Nu HTML Checker passes with zero errors (screenshot required) | 10 |
| Browser DevTools accessibility roles verified (screenshot required) | 5 |
| **Total** | **100** |
