# Quiz: Module 15 — Software Project Metrics and Velocity Tracking

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A Scrum Team completes Stories worth 5, 8, 3, and 13 story points in a Sprint. One additional Story estimated at 8 points was 75 percent complete at Sprint end but did not meet the Definition of Done. What is the team's velocity for this Sprint?

- A) 29 — the sum of all started stories including the partially complete one
- B) 35 — the sum of all stories including a pro-rated 6 points for the 75% complete story
- C) 29 — the sum of completed stories only, excluding the incomplete story
- D) 21 — only fully done stories with no incomplete work count at all

Correct Answer: C — Velocity is the sum of story points from Product Backlog Items that met the Definition of Done. The partially complete story contributes zero to velocity. 5 + 8 + 3 + 13 = 29.

Distractor Analysis:

- Why A is incorrect: Answer A arrives at the correct number but states an incorrect reasoning — it claims to include the partially complete story. The 29 comes from the four completed stories only.
- Why B is incorrect: Pro-rating partial completion is not how velocity is calculated. A story is either done or not done. Pro-rated credit undermines the Definition of Done's binary commitment.
- Why D is incorrect: The calculation is wrong. The four completed stories total 5 + 8 + 3 + 13 = 29, not 21.

---

## Question 2

A Scrum Team has the following velocity history: Sprint 1: 18, Sprint 2: 22, Sprint 3: 24, Sprint 4: 25, Sprint 5: 23. A new developer joins for Sprint 6. Which approach to Sprint 6 planning is most appropriate?

- A) Plan Sprint 6 for velocity 30 because the new developer adds capacity
- B) Plan Sprint 6 based on the average of Sprints 3–5 (approximately 24), acknowledging that onboarding the new developer may reduce velocity slightly
- C) Plan Sprint 6 for velocity 18 — the lowest historical velocity — to be conservative
- D) Ask the new developer how many story points they estimate they can complete individually and add it to Sprint 5's velocity

Correct Answer: B — Recent velocity (Sprints 3–5 average approximately 24) is the best baseline. Adding a new team member typically reduces velocity short-term due to onboarding overhead — so planning at the recent average rather than inflating for the new headcount is appropriate. The team should acknowledge the uncertainty.

Distractor Analysis:

- Why A is incorrect: Assuming a new developer immediately adds capacity ignores onboarding time, knowledge transfer, and the temporary drag on existing team members who must support the new person.
- Why C is incorrect: Using the minimum historical velocity from Sprint 1 — which was the team's first Sprint with a new codebase — is overly conservative and does not reflect the team's current capability.
- Why D is incorrect: Velocity is a team metric, not an individual one. Individual story point estimates do not add linearly to team velocity. This approach fragments team planning into individual capacity calculations.

---

## Question 3

A Sprint Burndown Chart shows the actual remaining work line staying nearly flat for the first eight days of a ten-day Sprint, then dropping steeply in the final two days to reach near-zero at Sprint end. What does this pattern most likely indicate?

- A) The team discovered significant scope changes during the Sprint that reduced the total work
- B) The team batched their work completion, finishing stories in the last two days rather than throughout the Sprint
- C) The team underestimated their stories, causing remaining work to appear flat until the estimates were corrected
- D) The Sprint Backlog was too small, leaving the team with little to do for most of the Sprint

Correct Answer: B — A flat burndown line followed by a steep end-of-Sprint drop is the classic batching pattern. Developers complete work internally but do not move stories to Done until the final days. This indicates that stories are not being decomposed into daily-completable units, or that the team's definition of "done" is applied in batches rather than continuously.

Distractor Analysis:

- Why A is incorrect: Scope changes typically cause the line to rise (new stories added) or cause a sudden drop without the preceding flat period. The flat-then-drop pattern is specifically about batching, not scope change.
- Why C is incorrect: Re-estimation during a Sprint would cause the line to drop or rise sharply at a specific point. The flat-then-drop pattern is more consistent with batched completion than with estimation corrections.
- Why D is incorrect: A Sprint Backlog that is too small would show the burndown reaching zero early — not staying flat for eight days.

---

## Question 4

On Day 5 of a 10-day Sprint, the Sprint Burndown shows 28 remaining story points out of the original 40. The ideal line at Day 5 would show 20 remaining points. What is the most appropriate team action?

- A) Add more stories to the Sprint Backlog to ensure the team is fully utilized
- B) Raise the concern at the Daily Scrum and discuss whether to remove lower-priority stories from the Sprint or identify what is blocking completion
- C) Extend the Sprint by two days to allow time for the remaining work
- D) Declare the Sprint a failure and begin Sprint Planning immediately

Correct Answer: B — The Scrum Team responds to burndown deviation at the Daily Scrum by inspecting the situation and adapting. Options include identifying impediments, negotiating scope reduction with the Product Owner, or adjusting the plan. The Daily Scrum is the right event for this conversation.

Distractor Analysis:

- Why A is incorrect: Adding more stories when the team is already behind the ideal line worsens the situation. The problem is not that the team lacks work — it is that they are not completing work fast enough.
- Why C is incorrect: Sprints have a fixed length. A Scrum Team does not extend a Sprint because they are behind on the Sprint Backlog. The Sprint ends on time; unfinished work returns to the Product Backlog.
- Why D is incorrect: Declaring the Sprint a failure is not a Scrum concept. A Sprint may not achieve its Sprint Goal, but the appropriate response is to communicate with the Product Owner and adapt — not restart.

---

## Question 5

A Product Owner wants to know how many more Sprints are needed before the product is ready for release. The Product Backlog contains 210 remaining story points. The team's velocity over the last four Sprints is: 30, 28, 32, 31. What is the most appropriate release forecast?

- A) Exactly 7 Sprints — calculated as 210 ÷ 30 (the first of the four velocities)
- B) Approximately 7 Sprints — calculated as 210 ÷ average velocity of 30.25, acknowledging that actual scope and velocity will vary
- C) At least 9 Sprints — always add a 30 percent buffer to any velocity-based forecast
- D) The forecast cannot be made because the Product Backlog may change

Correct Answer: B — The average velocity of the four most recent Sprints is (30 + 28 + 32 + 31) ÷ 4 = 30.25. 210 ÷ 30.25 ≈ 6.9 Sprints, rounded to approximately 7. Communicating the approximation and acknowledging that scope and velocity both vary is the correct way to present a forecast.

Distractor Analysis:

- Why A is incorrect: Using a single Sprint's velocity rather than the average ignores natural velocity variation. The average over recent Sprints is a more reliable forecasting baseline.
- Why C is incorrect: Adding a fixed 30 percent buffer is an arbitrary rule that has no basis in the team's actual data. Uncertainty should be communicated explicitly, not hidden in an unexplained buffer.
- Why D is incorrect: While the forecast will change if the Product Backlog changes, that does not make the current forecast impossible or useless. Scrum's approach is to forecast with available data and update as conditions change.

---

## Question 6

A Release Burndown Chart shows the remaining backlog line rising in Sprint 4 and Sprint 7 even though the team completed their planned work in both Sprints. What does this most likely indicate?

- A) The team under-delivered in Sprints 4 and 7 compared to their commitments
- B) The Product Owner added new items to the Product Backlog during those Sprints
- C) The team's velocity declined, causing the line to appear to rise
- D) The Definition of Done was relaxed in Sprints 4 and 7, making stories easier to complete

Correct Answer: B — In a Release Burndown, the remaining backlog line rises when new items are added to the Product Backlog. This is expected and healthy — the Product Owner continuously refines the backlog as understanding grows. The rising line is transparency about scope growth, not a failure signal.

Distractor Analysis:

- Why A is incorrect: The question states the team completed their planned work in both Sprints. Under-delivery would mean fewer points completed, which would cause slower decline — not a rise.
- Why C is incorrect: Velocity affects how quickly the line descends; it does not cause the line to rise. Rising indicates scope addition, not slower completion.
- Why D is incorrect: Relaxing the Definition of Done would make stories easier to call "done" — which would cause the line to descend faster, not rise.

---

## Question 7

Lead time for a team is 45 days. Cycle time is 12 days. What does this reveal about the team's workflow?

- A) The team takes 45 days to complete each story once they start working on it
- B) Items wait approximately 33 days in the backlog before the team begins working on them
- C) The team's throughput is insufficient — they should process 45 items per day
- D) The Sprint length should be adjusted to match the 45-day lead time

Correct Answer: B — Queue time = Lead Time − Cycle Time = 45 − 12 = 33 days. Items wait 33 days from the time they are added to the backlog until the team starts work. This is the queue time — a signal that the backlog is long or that demand exceeds the team's capacity to start new work.

Distractor Analysis:

- Why A is incorrect: That describes cycle time, not lead time. The 45 days is the total time from request to delivery, including the time the item sat in the backlog before work started.
- Why C is incorrect: Throughput is a separate metric (items completed per unit time). Lead time and cycle time do not directly prescribe a throughput target.
- Why D is incorrect: Sprint length is fixed by the team's Sprint cadence and is not derived from lead time. Sprint length typically ranges from one to four weeks regardless of lead time.

---

## Question 8

Little's Law states: Cycle Time = WIP ÷ Throughput. A team has 15 stories in progress simultaneously and completes 2 stories per day on average. What is the predicted average cycle time, and what would happen to cycle time if the team reduced WIP from 15 to 8 stories?

- A) Cycle time = 7.5 days; reducing WIP to 8 would increase cycle time to 4 days
- B) Cycle time = 7.5 days; reducing WIP to 8 would reduce cycle time to 4 days
- C) Cycle time = 30 days; reducing WIP to 8 would reduce cycle time to 16 days
- D) Cycle time = 7.5 days; reducing WIP does not affect cycle time

Correct Answer: B — Cycle Time = 15 ÷ 2 = 7.5 days. If WIP is reduced to 8 with throughput held constant: Cycle Time = 8 ÷ 2 = 4 days. Reducing WIP reduces cycle time. This is why WIP limits improve flow — fewer items in flight means each item completes faster.

Distractor Analysis:

- Why A is incorrect: The direction is wrong. Reducing WIP reduces cycle time, not increases it. Little's Law shows the direct proportional relationship — less WIP, shorter cycle time.
- Why C is incorrect: The calculation is incorrect. 15 ÷ 2 = 7.5, not 30. 30 would result from WIP = 60 at throughput = 2.
- Why D is incorrect: WIP is directly proportional to cycle time in Little's Law. Reducing WIP while holding throughput constant always reduces cycle time.

---

## Question 9

A development manager sends the following message to a Scrum Team: "I reviewed each developer's story point completion for last Sprint. Two developers only completed 5 points each while two others completed 18 points each. The lower-performing developers need to improve their individual velocity." What is the most significant problem with this approach?

- A) Story points are not the right estimation unit — the manager should use hours instead
- B) Tracking individual story point completion undermines Scrum's team model, creates incentives to claim individual ownership of stories, and misuses a team-level metric for individual evaluation
- C) The two developers who completed 18 points each should be rewarded to reinforce high performance
- D) The manager should wait until Sprint Review to discuss performance rather than reviewing it between Sprints

Correct Answer: B — Velocity and story points are team-level metrics. Scrum Teams are self-organizing collective units — the team plans together and delivers together. Measuring individual story point completion destroys collaboration (developers protect "their" stories), creates hoarding behavior, and misuses a forecasting tool as a performance evaluation instrument.

Distractor Analysis:

- Why A is incorrect: The unit of estimation (story points versus hours) is not the problem. Individual tracking is harmful regardless of the unit used.
- Why C is incorrect: Rewarding high individual story point completion compounds the problem. It reinforces the misuse of a team metric for individual evaluation.
- Why D is incorrect: The Sprint Review timing is irrelevant to whether the practice is appropriate. Individual performance evaluation using story points is problematic regardless of when it occurs.

---

## Question 10

A Cumulative Flow Diagram shows the Testing band has been widening consistently for the last three weeks, while the In Progress and Code Review bands remain stable. What does this indicate, and what action should the Scrum Master facilitate?

- A) The team is completing stories faster than expected — the wide Testing band shows strong quality assurance activity
- B) There is a bottleneck in Testing — work is arriving in Testing faster than it is being completed, causing accumulation
- C) The Definition of Done is too strict — the testing criteria should be relaxed to clear the backlog
- D) The team should stop starting new development work until Testing backlog is resolved by adding more testers

Correct Answer: B — A widening band in the CFD indicates a bottleneck at that stage. Work arrives into Testing at the rate it leaves In Progress, but the Testing completion rate is lower, causing accumulation. The Scrum Master should facilitate a Retrospective conversation about the bottleneck — options include swarming (multiple team members help with testing), decomposing stories to include testing earlier, or adjusting WIP limits.

Distractor Analysis:

- Why A is incorrect: A widening band indicates accumulation, not throughput. High quality assurance activity would show items flowing through Testing quickly, not piling up.
- Why C is incorrect: Relaxing the Definition of Done moves work downstream without solving the bottleneck — it just declares items "done" before they genuinely are, which creates hidden defect debt.
- Why D is incorrect: Adding testers is one possible response but should not be the first one. The team should first assess whether the bottleneck can be addressed by cross-training existing team members, reducing WIP upstream, or improving the testing process itself.

---

### Question 11 (5 points)

A Scrum Team has a stable average velocity of 32 points over eight Sprints. A senior developer leaves the team and is replaced by a junior developer in Sprint 9. Which adjustment to Sprint 9 planning is most appropriate?

- A) Keep Sprint 9 planned at 32 points because the team size has not changed
- B) Increase Sprint 9 to 40 points to motivate the new developer to perform at a senior level
- C) Reduce Sprint 9 capacity to account for onboarding time and the new developer's lower initial output; plan at approximately 24–28 points
- D) Skip Sprint 9 planning and run an informal Sprint until the new developer reaches full velocity

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Team composition change affects capacity even when headcount is stable. A junior replacing a senior temporarily reduces throughput due to onboarding, knowledge transfer overhead, and lower initial familiarity with the codebase.
  - Why B is incorrect: Planning at an inflated target to "motivate" a new developer is a misuse of Sprint planning. It will result in incomplete stories and an inaccurate velocity reading.
  - Why D is incorrect: Scrum requires Sprint Planning for every Sprint. Skipping planning violates the framework and removes the team's opportunity to commit to a Sprint Goal.

---

### Question 12 (5 points)

A Sprint Burndown line rises above the original starting total on Day 4. What is the most accurate interpretation?

- A) The team re-estimated stories upward or the Product Owner added items to the Sprint Backlog
- B) The team is failing to complete stories and the cumulative backlog is growing
- C) The Sprint should be cancelled because the scope has exceeded the team's capacity
- D) The burndown tool has a bug — remaining work cannot mathematically exceed its starting value

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: Incomplete stories reduce remaining points as they are finished; they do not cause the line to rise above the original total. A rise requires either re-estimation upward or scope addition.
  - Why C is incorrect: A Sprint is cancelled only when the Sprint Goal becomes obsolete — typically a change in business direction. A scope addition or re-estimate does not trigger cancellation.
  - Why D is incorrect: Remaining work can rise above its original value if stories are added to the Sprint Backlog or if an existing story is re-estimated to a larger size after work reveals more complexity.

---

### Question 13 (5 points)

A Product Owner says: "Our average cycle time is 18 days and our average lead time is 42 days. I want to improve the customer experience. Which metric should the team focus on reducing first?" What is the most appropriate recommendation?

- A) Focus on reducing cycle time first — it represents the team's execution efficiency
- B) Focus on reducing lead time first — specifically the queue time of 24 days — because customers experience the full wait from request to delivery
- C) Both metrics are equally important and should be addressed simultaneously
- D) Focus on throughput instead — neither lead time nor cycle time directly relates to customer experience

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Cycle time (18 days) is already a subset of lead time. Improving cycle time from 18 to 15 days would only reduce the customer's wait by 3 days. The 24-day queue is the larger opportunity.
  - Why C is incorrect: While both metrics matter, the queue time (24 days) is the dominant component of the customer's wait. Prioritization based on impact favors addressing the larger component first.
  - Why D is incorrect: Lead time is the most direct measure of customer experience (time from request to delivery). Throughput is about how many items complete per period, not how long any individual item takes.

---

### Question 14 (5 points)

A Scrum Team uses their Release Burndown to forecast completion. The chart shows 180 remaining points. The last four Sprint velocities were 28, 31, 27, and 30. A stakeholder asks: "Will we be done in 6 Sprints?" What is the most honest and accurate response?

- A) "Yes — 180 ÷ 29 (average velocity) = 6.2 Sprints, which rounds to 6"
- B) "Probably not — the forecast of approximately 6 Sprints assumes the backlog does not grow; if the Product Owner continues adding items as in previous Sprints, the actual delivery may be 7–8 Sprints"
- C) "We cannot forecast because the backlog may change"
- D) "Yes — we commit to delivering in exactly 6 Sprints"

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: 6.2 rounds up to 7 Sprints, not 6. More importantly, this answer does not acknowledge the risk that scope changes, which is the primary reason Release Burndown forecasts are uncertain.
  - Why C is incorrect: Uncertainty does not make forecasting impossible. The correct response is to provide a forecast with the uncertainty acknowledged, not to refuse to forecast.
  - Why D is incorrect: Scrum forecasts are probabilistic, not commitments. Committing to exactly 6 Sprints for delivery ignores variability in velocity and scope.

---

### Question 15 (5 points)

Which of the following is the best explanation for why comparing velocity across Scrum Teams is harmful?

- A) Different teams use different Agile tools, making data formats incompatible
- B) Story points are relative estimates calibrated to each team's context; a 5-point story for Team A may represent more or less work than a 5-point story for Team B, making the numbers incomparable
- C) Scrum Teams are not allowed to share velocity data with people outside the team
- D) Velocity is only meaningful when measured over 10 or more Sprints, and most teams have less history

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Data format incompatibility is a tool concern, not the reason cross-team velocity comparison is harmful. The harm is in the interpretation and organizational behavior it creates.
  - Why C is incorrect: There is no Scrum rule prohibiting sharing velocity data. The harm is not about privacy — it is about misinterpretation of relative estimates as absolute productivity measures.
  - Why D is incorrect: While more Sprint history improves reliability, the number of Sprints is not why cross-team comparison is harmful. The fundamental issue is the non-comparable nature of relative estimation.

---

### Question 16 (5 points)

A team has WIP of 20 stories and throughput of 2 stories per day. Using Little's Law, what is the average cycle time? If the team wants to reduce cycle time to 5 days without changing throughput, what WIP limit would achieve this?

- A) Cycle time = 10 days; WIP limit needed = 10 stories
- B) Cycle time = 10 days; WIP limit needed = 5 stories (since 5 ÷ 2 = 2.5, not 5 — so WIP = 10 is needed)
- C) Cycle time = 40 days; WIP limit needed = 10 stories
- D) Cycle time = 10 days; WIP limit needed = 15 stories

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: This answer contains a calculation error in the explanation. If target cycle time = 5 days and throughput = 2, then WIP = 5 × 2 = 10 stories. The answer to the WIP limit question is 10, not 5.
  - Why C is incorrect: Cycle time = 20 ÷ 2 = 10 days, not 40. The formula is WIP ÷ Throughput, not WIP × Throughput.
  - Why D is incorrect: If target cycle time = 5 days and throughput = 2, WIP = 10. A WIP limit of 15 would produce cycle time = 15 ÷ 2 = 7.5 days, not the target 5.

---

### Question 17 (5 points)

A Scrum Team's Sprint Burndown consistently shows the actual line staying exactly on or very slightly above the ideal line throughout each Sprint, ending at near-zero every Sprint. What does this burndown pattern most likely indicate?

- A) The team is gaming the burndown by artificially updating their remaining estimates to match the ideal line
- B) The team has well-calibrated Sprint Planning, effective daily inspection, and consistent delivery — the pattern is a healthy sign of predictable flow
- C) The team is completing their stories too quickly and should be given more work
- D) The team's velocity is too stable — healthy velocity should show significant variation Sprint over Sprint

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: While gaming is possible, consistently staying near the ideal line while ending at zero is the goal of good Sprint Planning and daily inspection — the most likely explanation is healthy practice, not manipulation.
  - Why C is incorrect: Completing planned work and reaching zero is the Sprint Backlog's purpose. It does not mean the team is underchallenged; it means they planned appropriately.
  - Why D is incorrect: Velocity stability is a sign of a mature team with well-calibrated estimates. Significant Sprint-to-Sprint variation is typically a sign of overcommitment, disruptions, or poor estimation — not a healthy pattern.

---

### Question 18 (5 points)

A manager proposes tracking "number of commits per developer per week" as a productivity metric. Which metric anti-pattern does this represent, and what is the most significant behavioral consequence?

- A) Velocity-as-target — developers will artificially inflate commit counts to appear productive
- B) Individual output tracking — developers optimize for commit frequency rather than value delivery, encouraging small meaningless commits and discouraging large, thoughtful refactoring work
- C) Burndown misuse — the commit count will distort the Sprint Burndown chart's accuracy
- D) Lines-of-code measurement — the metric does not differentiate between value-adding and waste code

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Velocity-as-target specifically refers to misusing story point velocity. Commit count is a different metric; the anti-pattern category here is individual output tracking.
  - Why C is incorrect: Commit count has no direct effect on the Sprint Burndown chart. The Burndown tracks remaining story points, not commit frequency.
  - Why D is incorrect: Lines-of-code measurement is a related but distinct anti-pattern; commit count and lines of code are different metrics, though both share the same fundamental flaw of measuring activity rather than value.

---

### Question 19 (5 points)

A team's Release Burndown shows that despite consistently completing 30 points per Sprint, the remaining backlog has not decreased over the past three Sprints. What does this most likely indicate?

- A) The team's velocity has been incorrectly reported — the true velocity is zero
- B) The Product Owner has been adding approximately 30 points of new items to the backlog each Sprint, keeping the total flat
- C) The team is counting incomplete stories as done, artificially inflating their velocity
- D) The Sprint Review is revealing defects that return stories to the backlog

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: If the team is completing 30 points per Sprint, velocity is real — the backlog is not decreasing because scope is growing at the same rate as completion.
  - Why C is incorrect: If incomplete stories were being counted as done, the backlog would appear to decrease (those stories would show as removed from the backlog). A flat line despite completion indicates additions, not false completions.
  - Why D is incorrect: Defects discovered at Sprint Review return as new backlog items, which would show as backlog additions. While possible, this is a less likely explanation for a flat line over three Sprints than consistent scope addition.

---

### Question 20 (5 points)

The Scrum Guide does not prescribe specific metrics. Why, then, do Scrum teams use velocity and burndown charts?

- A) They are required by SAFe and LeSS as part of the scaling frameworks built on Scrum
- B) They emerged as practical tools that support Scrum's empirical pillars — velocity supports Sprint Planning transparency, burndown supports daily inspection, and both enable adaptation when deviation is visible
- C) They are required by most enterprise organizations as compliance reporting for project governance
- D) They were added to Scrum in the 2020 Scrum Guide update as required artifacts

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Velocity and burndowns are used by single-team Scrum teams without any scaling framework. Their origin predates SAFe and LeSS.
  - Why C is incorrect: Enterprise governance requirements may reinforce their use, but teams adopt velocity and burndowns because they serve empiricism — not because of compliance.
  - Why D is incorrect: The 2020 Scrum Guide did not add velocity or burndown charts. The Guide defines commitments for each artifact but prescribes no specific metrics.

---
