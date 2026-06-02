# Video Script: Module 01 - HTML5 Semantics & SEO

**Course:** CIS-3340 Full Stack Web Development
**Estimated Duration:** 22 minutes
**Certification Alignment:** AWS Certified Developer - Associate (DVA-C02)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Professor Nash on-screen for introductions and transitions
- Screen capture: VS Code + Chrome browser side by side during live coding
- Use [SHOW CODE] cue to switch to full-screen VS Code
- Use [SHOW BROWSER] cue to switch to full-screen Chrome
- Highlight active lines with VS Code cursor; narrate every keystroke
- Keep terminal visible in lower panel throughout

---

## Section 1: Introduction and Why Semantics Matter [00:00 - 04:00]

Welcome to Module 01 of CIS-3340 Full Stack Web Development at Texas Wesleyan University. I am Professor Nash, and today we are building the foundation that every other module in this course depends on: HTML5 semantic structure and search engine optimization.

Before we write a single line of CSS or JavaScript, we need to understand what the browser, the search crawler, and the screen reader all see when they receive an HTML document. They do not see a visual layout. They see a tree of elements, and the names of those elements carry meaning.

This module aligns to the AWS Certified Developer Associate exam because every full-stack application we deploy to AWS serves HTML. Whether we host static files in S3, run server-side rendering on Elastic Beanstalk, or return HTML fragments from Lambda, the quality of that markup affects our users, our SEO ranking, and our legal accessibility compliance.

**AWS Exam Tip:** The DVA-C02 exam does not directly test HTML syntax, but exam scenarios frequently describe static web applications hosted on S3 and distributed through CloudFront. Understanding what a "static site build" contains — HTML, CSS, and JavaScript files — is assumed background knowledge in those questions.

Let me show you what we are going to build today.

[SHOW BROWSER]

Here is a finished semantic HTML5 page for a fictional university department. Notice the clear visual hierarchy. Now let me show you the page source.

[SHOW CODE]

Every structural container has a name that tells you exactly what it is: `header`, `nav`, `main`, `article`, `aside`, `footer`. Compare that to a page built entirely from `div` elements — functionally identical in the browser, but invisible to anything that reads meaning rather than pixels.

---

## Section 2: The Semantic Element Reference [04:00 - 09:30]

[SHOW CODE]

Let us open a new file called `index.html` and build the skeleton from scratch.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Texas Wesleyan Computer Science Department homepage.">
  <title>Computer Science | Texas Wesleyan University</title>
</head>
<body>

  <header>
    <h1>Texas Wesleyan University</h1>
    <p>Department of Computer Science</p>
  </header>

  <nav aria-label="Primary navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/programs">Programs</a></li>
      <li><a href="/faculty">Faculty</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
  </nav>

  <main>
    <article>
      <h2>Welcome to Computer Science at TXWES</h2>
      <p>Our programs prepare students for careers in software development,
         cloud computing, and data science.</p>
    </article>

    <aside>
      <h2>Quick Links</h2>
      <ul>
        <li><a href="/schedule">Course Schedule</a></li>
        <li><a href="/advising">Advising</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2024 Texas Wesleyan University. All rights reserved.</p>
  </footer>

</body>
</html>
```

Walk through each element:

- `<!DOCTYPE html>` declares the HTML5 document type. Without this, browsers enter quirks mode and rendering becomes unpredictable.
- `<html lang="en">` — the `lang` attribute is required for screen readers to select the correct language voice engine. This is a WCAG 3.1.1 Level A requirement.
- `<meta charset="UTF-8">` prevents character encoding errors for international characters.
- `<meta name="viewport">` is the single most important tag for mobile rendering. Without it, mobile browsers render your page at 980px and scale it down — users see tiny text. We cover this in depth in Module 03.
- `<meta name="description">` is the text snippet search engines display below your page title in results. Write it as 150 to 160 characters of compelling plain language about the page content.
- `<title>` is the single highest-weight on-page SEO signal. Keep it unique per page, under 60 characters, and place the most important keyword near the front.

**AWS Exam Tip:** When a DVA-C02 question describes uploading a static site to S3, the `index.html` file with its `<head>` metadata is the entry point that gets served. The S3 bucket's website endpoint setting maps `/` to `index.html` by default.

Now let us look at the body semantic elements.

`<header>` represents the introductory content of the nearest sectioning ancestor — in this case, the whole page. It commonly holds the site logo, the `<h1>`, and the primary navigation. Do not confuse `<header>` with `<head>` — `<head>` is invisible metadata, `<header>` is visible page content.

`<nav>` wraps a major block of navigation links. Adding `aria-label` to the `<nav>` element is important when a page has multiple navigation regions — it lets screen reader users distinguish between primary navigation, breadcrumbs, and footer navigation.

`<main>` identifies the primary content area unique to this page. There should be exactly one `<main>` per document. Screen reader users can jump directly to `<main>` to skip repeated headers and navigation.

`<article>` is for self-contained content that could be redistributed or syndicated independently — a blog post, a news story, a product listing, a forum reply. Ask yourself: could this content stand alone and still make sense? If yes, `<article>` is appropriate.

`<aside>` marks content that is tangentially related to the surrounding content — a sidebar, a callout box, a related-links widget, an advertisement.

`<footer>` is the footer of the nearest sectioning ancestor. At the page level it typically holds copyright notices, legal links, and contact information.

[SHOW BROWSER]

Let us open this in Chrome and inspect the Accessibility panel in DevTools. You can see the browser has built an accessibility tree from our semantic markup — the roles are inferred directly from element names.

---

## Section 3: Heading Hierarchy and SEO [09:30 - 14:30]

[SHOW CODE]

The heading tags `<h1>` through `<h6>` do double duty: they create the document outline that both search crawlers and screen reader users navigate, and they signal content importance.

The rule is strict: one `<h1>` per page, and heading levels must not skip. Never jump from `<h2>` to `<h4>` to add visual size — use CSS for size, headings for structure.

Here is a correct heading hierarchy:

```html
<h1>Computer Science Department</h1>
  <h2>Undergraduate Programs</h2>
    <h3>Bachelor of Science in Computer Science</h3>
    <h3>Bachelor of Science in Information Systems</h3>
  <h2>Graduate Programs</h2>
    <h3>Master of Science in Data Science</h3>
```

And here is a broken hierarchy that fails WCAG 1.3.1:

```html
<h1>Computer Science Department</h1>
<h3>Undergraduate Programs</h3>  <!-- skipped h2 — violation -->
<h5>Bachelor of Science</h5>     <!-- skipped h4 — violation -->
```

**AWS Exam Tip:** WCAG compliance is increasingly a contractual requirement for enterprise AWS deployments. When a DVA-C02 scenario mentions deploying a public-facing application for a government agency or healthcare organization, assume accessibility standards apply and that they flow down to the HTML the server returns.

Now let me show you how to validate your heading structure.

[SHOW BROWSER]

Open Chrome DevTools, go to the Elements panel, and look at the Accessibility tab. Alternatively, install the axe DevTools browser extension — it will flag heading-order violations directly on the rendered page.

Another tool you should bookmark is the W3C Nu HTML Checker at validator.w3.org. Let me paste our markup in and show you a clean validation result.

---

## Section 4: Images, Alt Text, and Open Graph Metadata [14:30 - 19:00]

[SHOW CODE]

Every `<img>` element requires an `alt` attribute. The value should describe the informational content of the image for someone who cannot see it.

```html
<!-- Correct: descriptive alt text -->
<img src="campus-quad.jpg"
     alt="Students gathered on the Texas Wesleyan campus quad on a sunny afternoon"
     width="800"
     height="400">

<!-- Correct: decorative image — empty alt tells screen readers to skip it -->
<img src="divider-line.png" alt="" role="presentation">

<!-- Wrong: filename as alt text -->
<img src="campus-quad.jpg" alt="campus-quad.jpg">

<!-- Wrong: missing alt attribute entirely -->
<img src="campus-quad.jpg">
```

Always include `width` and `height` attributes on images. This reserves layout space before the image loads, preventing the Cumulative Layout Shift that Google's Core Web Vitals score penalizes.

Now let us add Open Graph metadata so the page generates rich previews when shared on LinkedIn, Slack, or Teams:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Texas Wesleyan Computer Science Department homepage.">
  <title>Computer Science | Texas Wesleyan University</title>

  <!-- Open Graph tags for social sharing previews -->
  <meta property="og:title" content="Computer Science | Texas Wesleyan University">
  <meta property="og:description" content="Prepare for careers in software, cloud, and data science.">
  <meta property="og:image" content="https://txwes.edu/images/cs-og.jpg">
  <meta property="og:url" content="https://txwes.edu/cs">
  <meta property="og:type" content="website">
</head>
```

**AWS Exam Tip:** Open Graph image URLs must be absolute paths. When a React app is hosted on S3 + CloudFront, the `og:image` must point to the full CloudFront domain — not a relative path. This is a common deployment gotcha.

---

## Section 5: Lab Preview and End Card [19:00 - 22:00]

[SHOW CODE]

Before I let you loose on the lab, let me walk through the deliverable you will submit.

You are going to build a complete semantic HTML5 page for a fictional department or organization of your choosing. The requirements are:

- Exactly one `<h1>` at the page level
- At minimum: `<header>`, `<nav>`, `<main>`, one `<article>`, one `<aside>`, and `<footer>`
- At least two images with descriptive `alt` text
- A complete `<head>` section including charset, viewport, description, and title
- Pass the W3C Nu HTML Checker with zero errors

You will not be writing CSS in this lab — we tackle that in Module 02. Focus entirely on correct structure and meaningful content.

[SHOW BROWSER]

Here is what the unstyled page looks like in the browser. It is plain, but it is correct. Every element serves a purpose. Every heading is in the right place. Every image has meaningful alt text. This is the foundation everything else is built on.

Thank you for watching. Complete the reading guide before the quiz, and work through the lab before our next session. I will see you in Module 02 where we apply CSS Flexbox and Grid to make this page look as good as it is structured.

---

## Additional Resources

- developer.mozilla.org — search "HTML elements reference" for the complete semantic element specification
- aws.amazon.com/certification — official AWS Certified Developer Associate exam guide and sample questions
