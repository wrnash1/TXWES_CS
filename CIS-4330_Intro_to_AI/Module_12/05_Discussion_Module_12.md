# Discussion Forum: Module 12 — AI in Business: Use Cases and ROI

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Due Dates:** Initial post by Wednesday 11:59 PM | Peer responses by Sunday 11:59 PM

**Total Points:** 10

---

## Instructions

Read all three scenarios below. Choose one scenario for your initial post. Identify your scenario choice (A, B, or C) at the top of your post.

---

## Scenario A: The Misclassified Use Case

A regional hospital is planning an AI initiative to help radiologists review chest X-rays. The project sponsor describes the initiative to the board as follows: "We are automating radiology. This AI will read X-rays and free up our radiologists to focus on other work." The technology lead, however, describes the same system differently: "The AI flags regions of interest for the radiologist to prioritize. Radiologists still review and sign off on every scan."

The board approves the project based on the sponsor's description and expects a 40 percent reduction in radiology staffing costs within two years. After deployment, radiologists are more efficient and catch more findings, but no staff reductions occur — the same team is now reviewing more scans per shift with fewer missed findings.

In your initial post (175–225 words), address all of the following:

- Identify the correct AI use case category for this deployment based on what the system actually does, and explain why the sponsor's description represents a different category entirely. Use the definitions from the reading guide.

- The board's ROI expectation (40 percent staffing cost reduction) was built on a misclassified use case. Describe what the actual value proposition of an Enhancement use case looks like in this context, and explain how the organization should have framed the ROI case to the board.

- This misalignment between business expectation and technical design is a governance failure. Identify the specific point in the AI project lifecycle where this misalignment should have been caught, and name the type of documentation that would have formalized the correct use case classification before board approval.

---

## Scenario B: The Build vs Buy Standoff

A mid-sized insurance company is launching a claims triage project. When a claim is submitted, the system should automatically route it to one of seven internal processing queues based on the nature of the claim. The seven queue categories are proprietary to the company — they map to internal business units and are not standard insurance categories used by any commercial software.

Two teams disagree on the approach:

Team A argues for Azure AI Language CLU. They say: "CLU can learn any intent categories we define. We just label utterances for our seven queues and train the model."

Team B argues for Azure OpenAI with a detailed system message. They say: "GPT-4 is powerful enough to understand claim descriptions and route them correctly with a well-designed prompt. No training data needed."

The company has 12,000 labeled historical claim descriptions already categorized into the seven queues.

In your initial post (175–225 words), address all of the following:

- Evaluate both teams' arguments using the build-versus-buy decision framework from the reading guide. Which team's approach is better aligned with the framework for this specific scenario? Justify your answer by citing at least two factors from the framework.

- Identify one scenario in which Team B's approach (Azure OpenAI with prompt engineering) would be the better choice. What specific condition would need to be different about this project for that to be true?

- Both approaches have ongoing cost implications. Name one ongoing cost component that is different between CLU and Azure OpenAI prompt engineering for this use case, and explain which approach has the lower long-term maintenance burden for this specific case.

---

## Scenario C: The ROI Dispute

A logistics company deployed an Azure Machine Learning demand forecasting model eight months ago. The model predicts weekly parcel volume by region, which the company uses to optimize driver staffing and vehicle routing.

The data science team reports a positive ROI: they cite $280,000 in annualized labor savings from more efficient driver scheduling and $95,000 in avoided overtime costs. Total investment was $210,000 in Year 1 (development, compute, and data labeling). They calculate ROI at 178 percent.

The CFO challenges the ROI claim: "We did not actually reduce headcount. No one was laid off. The same number of drivers are working. Where is the savings?" The data science team responds: "We're doing the same volume with 11 percent fewer overtime hours. The savings are real — we're just not seeing them in the headcount line."

In your initial post (175–225 words), address all of the following:

- Explain which ROI value component (from Table 4 in the reading guide) each side of the dispute is talking about. Is the data science team's ROI claim valid? Justify your answer using the definitions.

- The CFO's challenge reveals that no baseline metrics were established before deployment. Explain what baseline data the team should have captured before launch and how those baselines would have made the ROI calculation indisputable.

- Identify one AI investment cost component that the data science team may have underestimated in their $210,000 figure, given that the model has been in production for eight months and is being used for operational decisions every week.

---

## Peer Response Guidelines

Reply to at least two classmates who chose different scenarios than you. Each peer response must be at least 50 words and must add substantive analysis beyond agreement.

Suggested peer response approaches:

- Identify a value component your peer did not mention that is also relevant to the ROI case they analyzed.

- Challenge the build-versus-buy recommendation your peer made and provide a counter-argument using one factor from the framework they did not address.

- Add a specific detail about the maturity stage implied by your peer's scenario that they did not address in their post.

- Evaluate the governance mechanism your peer proposed — is it sufficient to prevent recurrence of the described problem?

---

## Grading Rubric (10 Points Total)

### Initial Post — 6 Points

6 pts: Use case category, ROI components, or build-versus-buy framework applied accurately and with specificity. Framework terms used correctly. All three sub-questions addressed. Meets 175–225 word requirement. Demonstrates original reasoning beyond restating the scenario.

4–5 pts: Most concepts applied correctly. One sub-question underdeveloped or uses imprecise terminology. Word count met.

2–3 pts: Significant errors in use case classification, ROI component identification, or framework application. One or more sub-questions missing. May not meet word count.

0–1 pts: Post missing or does not engage substantively with the scenario.

### Peer Responses — 4 Points

4 pts: Substantive responses to at least two peers from different scenarios. Each adds new analysis or challenges a specific claim. Minimum 50 words each.

2–3 pts: Responds to two peers with limited new substance, or responds to only one peer.

0–1 pts: No responses or all responses are superficial agreement.

---

## Professor Nash Note

Scenario C is the most common failure mode I see in real AI projects. Teams calculate ROI using cost savings that are technically real but organizationally invisible — no one was let go, no budget line changed, and the CFO cannot see the number. The lesson is not that the ROI is fake; operational efficiency savings from avoided overtime and optimized scheduling are real dollar values. The lesson is that without a baseline, you cannot prove it to anyone who was not already convinced. Before any production AI deployment, capture the current state: average overtime hours per week, average labor cost per scheduled route, average error rate. Keep those numbers. When the model is running and you want to make the case, you subtract the new number from the old number and multiply by cost. That is how you win the CFO conversation. Strong posts will engage with the baseline question specifically rather than just restating that baselines are important.
