# Discussion Forum: Module 02 - Modern CSS Layouts

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion asks you to connect CSS layout decisions to real development and deployment scenarios. Choose one of the three scenarios below and write an initial post addressing all three sub-questions for that scenario.

---

## Scenario A: Debugging a Broken Production Layout

A e-commerce company pushes a CSS update to their checkout page on a Friday afternoon. Within an hour, customer support receives complaints that the "Place Order" button is invisible on mobile devices but visible on desktop. The engineering team checks the deployed CSS and finds the following rule was accidentally pushed to production:

```css
.checkout-btn {
  display: flex;
  width: 250px;
}
```

On desktop (1400px wide), the button appears in the correct position. On mobile (375px wide), it disappears entirely.

Address all three of the following in your post:

1. The button is not actually gone from the DOM — it is just not visible. Propose at least two specific CSS properties that could cause a 250px element to be visually hidden on a 375px screen without `display: none`. Be specific about which property and value, and explain the mechanism.
2. The team wants to prevent this type of layout regression in the future. Propose a development practice (related to tools, workflow, or testing) that would catch this type of CSS regression before it reaches production. Explain how your proposed practice would have caught this specific bug.
3. `display: flex` was applied to the button element itself, not to a container. What does `display: flex` do when applied directly to a button? Is this semantically correct? When would you legitimately apply `display: flex` to a button?

Your initial post should be 175 to 225 words.

---

## Scenario B: Choosing Between Flexbox and Grid

A front-end developer at a SaaS company is building a new analytics dashboard. The design shows a header with a logo, search bar, and user avatar; a left sidebar with navigation icons; and a main content area containing a grid of metric cards. Each metric card has a title, a large number, and a small trend indicator. The developer opens a team discussion about whether to use Flexbox or Grid for each region.

Address all three of the following in your post:

1. For the header (logo + search bar + avatar), explain why Flexbox is the appropriate choice. What specific Flexbox properties would you apply to the header container, and what `flex` shorthand values would you assign to the search bar to make it expand to fill available space between the logo and avatar?
2. For the main content area's card grid, explain why CSS Grid with `repeat(auto-fill, minmax(220px, 1fr))` is more appropriate than a Flexbox approach with `flex: 1 1 220px`. What specific behavior is different between the two approaches that makes Grid preferable for a card dashboard?
3. A junior developer on the team suggests just using Bootstrap's grid classes instead of writing custom CSS Grid. Describe one scenario where custom CSS Grid is strongly preferable to Bootstrap's grid, and one scenario where Bootstrap's grid is a reasonable choice.

Your initial post should be 175 to 225 words.

---

## Scenario C: CloudFront Caching and CSS Deployments

A development team deploys a React application to AWS. The React app is built with `npm run build`, producing a `dist/` folder. The CSS output file is named `main.css`. This folder is uploaded to S3 and served through a CloudFront distribution. After each deploy, the team runs an AWS CLI cache invalidation.

The team lead proposes a change: instead of a single `main.css` file, the build tool should output CSS files with content hashes in their names (for example, `main.a3f9b2c.css`). The HTML file's `<link>` tag would automatically reference the correct hashed filename.

Address all three of the following in your post:

1. Explain what a CloudFront cache invalidation does at the infrastructure level. Why is it necessary after uploading new files to S3? What are the cost implications of running a `/*` invalidation on every deploy?
2. Explain the content-hash filename strategy. How does naming a CSS file `main.a3f9b2c.css` eliminate the need for a cache invalidation after each deploy, and what makes this safe to cache indefinitely at the CDN level?
3. With the content-hash strategy in place, which files still need cache invalidation after every deploy, and why? Think carefully about what changes between every deploy and what does not.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add concrete technical detail that strengthens their answer, or
- Present an alternative approach and compare trade-offs

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
| Initial post uses correct CSS and/or AWS terminology from the module | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

Flexbox and Grid are not competing tools — they are complementary. The most common mistake I see in student projects is using one exclusively. A real production layout uses Grid for the macro page structure and Flexbox inside each cell for the micro-level component alignment. Get comfortable switching between them and you will solve 90 percent of all layout problems cleanly, without hacks or workarounds.
