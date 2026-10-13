# Discussion Forum: Module 03 - Unsupervised Learning: Clustering and Dimensionality Reduction

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Due Dates:** Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM
**Total Points:** 10

---

## Instructions

Read all three scenarios below. Choose one scenario for your initial post. Identify your scenario choice (A, B, or C) at the top of your post.

---

## Scenario A: The Hospital Patient Segmentation Project

A large regional hospital wants to use machine learning to better understand its patient population. The analytics team has electronic health record data for 400,000 patients, including age, body mass index, number of prior hospitalizations, number of chronic conditions, average length of stay, and insurance type. No outcome labels are available — the team is not trying to predict readmission or any specific event. They simply want to know whether distinct patient profiles exist within the data.

A junior analyst suggests training a logistic regression model because "it is more powerful than clustering." A senior data scientist pushes back and argues that clustering is the right tool here.

In your initial post (175-225 words), address all of the following:

- Why is clustering the correct approach for this scenario? Explain specifically why logistic regression cannot be applied here.

- The team runs K-means with K=2 through K=8 and uses the elbow method to select K=4. Describe what the team would need to do after the algorithm finishes to make the results useful to hospital administrators.

- Identify one responsible AI concern that arises when clustering patient data and segmenting people into groups based on health characteristics.

---

## Scenario B: The Music Recommendation Dimensionality Problem

A music streaming company has 80 million songs in its catalog. Each song is described by 450 audio features including tempo, key, danceability, energy, acousticness, loudness, valence, and speechiness. The company wants to build a recommendation engine that finds songs similar to a user's recently played tracks. A data scientist notes that computing distances in 450-dimensional space is extremely slow and suffers from the curse of dimensionality.

The data scientist proposes using PCA to reduce the 450 features to 20 principal components before running K-means clustering to group similar songs together.

In your initial post (175-225 words), address all of the following:

- Explain the curse of dimensionality in this scenario. What specific problem does it cause for a distance-based algorithm like K-means?

- Evaluate the proposed two-step pipeline: PCA then K-means. Is this a reasonable approach? What is lost in the PCA step?

- After clustering, the data scientist finds 12 song clusters and asks the music curation team to name them. What does this naming process illustrate about unsupervised learning outputs?

---

## Scenario C: The Retail Customer Segmentation Audit

A regional grocery chain used K-means clustering two years ago to segment its 1.5 million loyalty card customers into five groups: Premium Shoppers, Deal Seekers, Convenience Buyers, Family Stockers, and Infrequent Visitors. The marketing team built targeted promotions for each segment and saw a 14% lift in redemption rates.

An analytics intern now notices that the Infrequent Visitors cluster — which receives the fewest promotions — is disproportionately composed of elderly customers in low-income zip codes. The marketing team argues the algorithm had no demographic information, so no bias is possible.

In your initial post (175-225 words), address all of the following:

- The algorithm had no demographic data, yet clusters correlate with demographics. Explain how this can happen using your knowledge of feature selection and unsupervised learning.

- Identify which Microsoft responsible AI principle is most relevant and explain how it applies.

- Should the company redesign the segmentation? If yes, propose one concrete change. If no, defend your reasoning using responsible AI principles.

---

## Peer Response Guidelines

Reply to at least two classmates who chose different scenarios than you. Each peer response must be at least 50 words and must add substantive analysis beyond simple agreement.

Suggested peer response approaches:

- Challenge or extend the responsible AI analysis in your peer's post.

- Point out an alternative unsupervised algorithm that might work better in their scenario.

- Raise a technical limitation of the approach your peer recommended.

- Provide a real-world analogy that reinforces or complicates their argument.

---

## Grading Rubric (10 Points Total)

### Initial Post — 6 Points

**6 pts:** Addresses all required sub-questions with accurate course vocabulary. Meets 175-225 word requirement. Demonstrates original reasoning beyond restating definitions.

**4-5 pts:** Addresses most sub-questions with generally correct analysis. Minor vocabulary errors or one sub-question underdeveloped. Word count met.

**2-3 pts:** Fewer than half the sub-questions addressed, significant factual errors, or word count not met.

**0-1 pts:** Post missing or does not substantively engage with the scenario.

### Peer Responses — 4 Points

**4 pts:** Substantive responses to at least two peers from different scenarios. Each adds new analysis or a counterpoint. Minimum 50 words each.

**2-3 pts:** Responds to two peers with limited substance, or responds to only one peer.

**0-1 pts:** No responses submitted or all responses are superficial.

---

## Professor Nash Note

Scenario C is the most nuanced because it asks you to reason about how an algorithm with no demographic information can still produce demographically correlated outputs. This is a real and well-documented phenomenon in machine learning, with real consequences for affected people. Before concluding that "no demographic data means no bias," consider what proxy variables in behavioral data might correlate with demographics.
