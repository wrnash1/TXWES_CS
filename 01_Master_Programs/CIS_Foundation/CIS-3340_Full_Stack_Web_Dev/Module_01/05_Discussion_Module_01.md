# Discussion Forum: Module 01 - HTML5 Semantics & SEO

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion asks you to connect HTML5 semantic structure and SEO principles to real production scenarios. Choose one of the three scenarios below and write an initial post that addresses all three sub-questions for that scenario. You do not need to respond to all three scenarios — choose the one that interests you most or aligns most closely with your professional goals.

---

## Scenario A: Accessibility Audit for a University Website

Your university's web team discovers that the main academic department pages are built entirely from `<div>` and `<span>` elements with CSS class names like `class="header"`, `class="nav-wrapper"`, and `class="content-block"`. A third-party accessibility audit flags the site as non-compliant with WCAG 2.1 Level AA — a legal requirement under Section 508 of the Rehabilitation Act for federally funded institutions.

Address all three of the following in your post:

1. Explain specifically why `<div class="nav-wrapper">` is not equivalent to `<nav>` from an accessibility standpoint, even if both look identical in the browser. What information does the semantic element provide that the `div` does not?
2. The development team argues that refactoring hundreds of existing pages to use semantic HTML will take too long. Propose a prioritization strategy — which pages or elements would you fix first, and why?
3. Identify one WCAG POUR principle (Perceivable, Operable, Understandable, or Robust) that is most directly violated by the current non-semantic markup, and explain your reasoning.

Your initial post should be 175 to 225 words. Posts outside this range will receive partial credit on the length criterion.

---

## Scenario B: SEO Strategy for an E-Commerce Launch

A startup is launching an online marketplace. The engineering team has built all product listing pages using React with server-side rendering (SSR). The marketing team reports that product pages are not appearing in Google search results even two weeks after launch. An SEO consultant reviews the HTML source and finds that every page has the same `<title>Texas Marketplace</title>` and the same generic `<meta name="description" content="Buy products online.">`. Product images have `alt=""` on all of them. The `<h1>` on every product page reads "Product Details."

Address all three of the following in your post:

1. Identify the three specific HTML problems the consultant found, and explain why each one harms search engine indexing.
2. Propose specific content for the `<title>`, `<meta name="description">`, and `<h1>` for a product page selling a 65-inch 4K television. Use realistic placeholder values.
3. Explain the business impact of empty `alt` attributes on product images beyond just SEO ranking — consider at least one non-search impact.

Your initial post should be 175 to 225 words. Posts outside this range will receive partial credit on the length criterion.

---

## Scenario C: Deploying a Static Site to AWS S3

A developer on your team has built a company marketing site using only HTML5, CSS, and JavaScript. The site has ten pages. She uploads all files to an S3 bucket and enables static website hosting. The site looks correct when she navigates from the homepage, but directly typing a URL like `company-site.s3-website.amazonaws.com/about` returns a 403 error. She also notices that when a page link is shared on LinkedIn, LinkedIn displays a generic globe icon instead of the company's hero image.

Address all three of the following in your post:

1. Explain the root cause of the 403 error when navigating directly to `company-site.s3-website.amazonaws.com/about`. What does S3 expect to find at `/about` and why does it fail?
2. Identify which HTML `<head>` tag controls the image LinkedIn displays when a URL is shared, and explain the value requirements for that tag (format, URL type, size recommendation).
3. Explain the difference between setting the S3 "Error document" to `index.html` vs. creating an actual `about.html` file for each page. Which approach is more appropriate for a multi-page static site (as opposed to a React SPA), and why?

Your initial post should be 175 to 225 words. Posts outside this range will receive partial credit on the length criterion.

---

## Peer Response Instructions

After your initial post is submitted, read through your classmates' posts and write a substantive reply to at least two peers whose scenarios differ from yours.

Each peer response must be at least 75 words and must do one of the following:

- Correct a technical inaccuracy in their post with a specific explanation
- Add a concrete example or AWS-specific context that strengthens their point
- Offer an alternative approach with a comparison of the trade-offs involved

Responses such as "Great post!" or "I agree with everything you said" do not earn credit regardless of length.

---

## Due Dates

- Initial post: Wednesday by 11:59 PM
- Peer responses (at least two): Sunday by 11:59 PM

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses all three sub-questions with technical accuracy | 3 |
| Initial post meets the 175 to 225 word count requirement | 1 |
| Initial post uses correct technical terminology from the module | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

HTML structure is not just a best practice — it is the contract between your code and every machine that reads it: browsers, crawlers, screen readers, and AI indexers. When I review the AWS deployment labs in Module 14, I always look at the HTML source first. A poorly structured page deployed to the world's most reliable cloud infrastructure is still a poorly structured page. Build the foundation right in Module 01, and every module that follows becomes easier.
