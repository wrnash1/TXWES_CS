# Quiz: Module 11 — AI Ethics and Responsible AI Principles

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe responsible AI considerations and Microsoft's Responsible AI principles

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Submit through the course LMS.

---

## Question 1

A company deploys a loan approval AI that has a 5% false negative rate (incorrectly denying qualified applicants) overall, but analysis shows the false negative rate is 18% for Hispanic applicants and 3% for white applicants. Which Responsible AI principle is primarily violated?

A. Reliability and Safety

B. Privacy and Security

C. Fairness

D. Inclusiveness

### Q1 — Correct Answer

C. Fairness

### Q1 — Distractor Analysis

- A is incorrect: Reliability and Safety concerns the system performing consistently and preventing harm across general conditions. The issue here is not a random failure — it is a systematic disparity across demographic groups, which is a fairness violation.
- B is incorrect: Privacy and Security concerns data collection, storage, and protection. No privacy breach is described here.
- D is incorrect: Inclusiveness concerns designing for people with disabilities, diverse languages, and varying economic access. While related, the specific failure — discriminatory error rates by ethnicity — is most precisely described as a Fairness violation.

---

## Question 2

An autonomous vehicle company deploys a self-driving system. After deployment, the company discovers the system performs poorly on roads covered with snow or ice because the training data contained almost no winter driving examples. Which Responsible AI principle is primarily at issue?

A. Transparency

B. Reliability and Safety

C. Accountability

D. Fairness

### Q2 — Correct Answer

B. Reliability and Safety

### Q2 — Distractor Analysis

- A is incorrect: Transparency concerns the explainability of AI decisions and honest communication about capabilities. The issue here is not that users lack explanation — it is that the system fails to perform safely in real-world conditions.
- C is incorrect: Accountability concerns who is responsible for AI outcomes. While accountability would become relevant after harm occurs, the primary design failure is a reliability and safety problem.
- D is incorrect: Fairness concerns equitable treatment across demographic groups. Poor performance in winter conditions is a coverage gap in training data, not a demographic disparity.

---

## Question 3

A healthcare AI that recommends treatment plans does not provide any explanation of why it recommended a specific treatment. Physicians cannot understand the reasoning behind recommendations and must either trust or ignore the AI blindly. Which Responsible AI principle is most directly implicated?

A. Inclusiveness

B. Accountability

C. Fairness

D. Transparency

### Q3 — Correct Answer

D. Transparency

### Q3 — Distractor Analysis

- A is incorrect: Inclusiveness addresses accessibility and diversity of user populations. The issue here is not about who can use the system — it is about whether anyone can understand how it makes decisions.
- B is incorrect: Accountability addresses who is responsible for outcomes. Lack of explainability is a transparency issue; accountability would come into play in determining who bears responsibility when the unexplainable recommendation causes harm.
- C is incorrect: Fairness addresses equitable treatment across groups. The absence of explanation is not inherently a fairness concern — it could affect all physicians equally.

---

## Question 4

Which of the following best describes what a model card communicates?

A. The source code and training scripts used to build the model

B. The model's purpose, training data, performance metrics (including by demographic subgroup), limitations, and ethical considerations

C. The legal terms under which the model may be used commercially

D. The API endpoint and authentication credentials for accessing the model

### Q4 — Correct Answer

B. The model's purpose, training data, performance metrics (including by demographic subgroup), limitations, and ethical considerations

### Q4 — Distractor Analysis

- A is incorrect: Source code and training scripts are separate technical artifacts. Model cards are human-readable documentation, not code.
- C is incorrect: Legal terms are covered in service agreements and licenses, not model cards.
- D is incorrect: API documentation and credentials are developer resources. Model cards are transparency and accountability documents, not technical reference guides.

---

## Question 5

A predictive policing AI directs additional police patrols to neighborhoods based on crime predictions. More patrols lead to more arrests in those areas. Those new arrests are added to the training data for the next version of the model, which predicts even higher crime in those same areas. What is this phenomenon called?

A. Representation bias

B. A feedback loop

C. Distribution shift

D. Label bias

### Q5 — Correct Answer

B. A feedback loop

### Q5 — Distractor Analysis

- A is incorrect: Representation bias refers to some groups being underrepresented in training data. While the feedback loop creates representation problems, the cycle itself is specifically called a feedback loop.
- C is incorrect: Distribution shift occurs when the deployment environment differs from the training environment. The described scenario is a self-reinforcing cycle in which the AI's outputs influence its own future training data.
- D is incorrect: Label bias occurs when human annotators apply labels inconsistently. The scenario describes a structural cycle, not a labeling problem.

---

## Question 6

An organization deploys an AI recruitment screener that uses name analysis as a feature. The AI was trained on historical hiring data from a period when the company's workforce was 90% male. Male-sounding names receive higher scores. No explanation is given to candidates, and no human reviews the AI's rejections. Which list correctly identifies ALL principles violated?

A. Fairness only

B. Fairness and Transparency

C. Fairness, Transparency, and Accountability

D. Fairness, Transparency, Accountability, and Privacy and Security

### Q6 — Correct Answer

C. Fairness, Transparency, and Accountability

### Q6 — Distractor Analysis

- A is incorrect: While Fairness is violated (discriminatory scoring based on gender-associated names), the lack of explanation also violates Transparency, and the absence of human review and redress violates Accountability.
- B is incorrect: This correctly identifies Fairness and Transparency but omits Accountability. Deploying consequential decisions with no human oversight and no mechanism for candidates to appeal is an accountability failure.
- D is incorrect: Privacy and Security concerns data collection and protection. No privacy breach is described in the scenario — the violation is about discriminatory scoring, lack of explanation, and absent oversight.

---

## Question 7

Which of the following is the correct definition of an AI impact assessment?

A. A performance benchmark comparing the AI model to industry-standard accuracy thresholds

B. A security audit evaluating whether the AI system is vulnerable to adversarial attacks

C. A pre-deployment evaluation of the potential harms an AI system could cause and the safeguards needed to mitigate them

D. A post-deployment analysis of actual harms the AI system caused during its first year of operation

### Q7 — Correct Answer

C. A pre-deployment evaluation of the potential harms an AI system could cause and the safeguards needed to mitigate them

### Q7 — Distractor Analysis

- A is incorrect: Performance benchmarking compares accuracy metrics. An AI impact assessment is a governance and ethics evaluation, not a performance comparison.
- B is incorrect: Security auditing for adversarial attacks is a specific technical security activity. An AI impact assessment is broader, covering social, ethical, and fairness harms.
- D is incorrect: An AI impact assessment occurs before deployment to prevent harms proactively. Post-deployment incident analysis is a different (though also important) activity.

---

## Question 8

A voice recognition AI is highly accurate for adult male speakers in North American English but has significantly higher error rates for speakers with accents, elderly speakers, and children. Which Responsible AI principle does this performance gap most directly violate?

A. Privacy and Security

B. Accountability

C. Inclusiveness

D. Transparency

### Q8 — Correct Answer

C. Inclusiveness

### Q8 — Distractor Analysis

- A is incorrect: Privacy and Security concerns data protection. No privacy violation is described — the issue is unequal system performance across user groups.
- B is incorrect: Accountability concerns who is responsible for AI outcomes. The described issue is a design and coverage problem, not an absence of human oversight.
- D is incorrect: Transparency concerns explainability of decisions. The system's differential performance is not a transparency problem — it is an inclusiveness problem because the system was not designed to work equally well for all people.

---

## Question 9

Under the European Union AI Act, which of the following AI applications would be classified as high risk?

A. A spam filter for a personal email account

B. A movie recommendation engine on a streaming platform

C. An AI system used by a bank to evaluate creditworthiness of loan applicants

D. An AI feature that auto-completes text messages on a smartphone

### Q9 — Correct Answer

C. An AI system used by a bank to evaluate creditworthiness of loan applicants

### Q9 — Distractor Analysis

- A is incorrect: Spam filters are minimal-risk systems under the EU AI Act. They do not make consequential decisions affecting individuals' rights or economic circumstances.
- B is incorrect: Recommendation engines are generally classified as minimal or limited risk. They influence content consumption but do not determine access to financial products, employment, or housing.
- D is incorrect: Text autocomplete is minimal risk. It assists a user but does not make binding decisions affecting that user's rights or opportunities.

---

## Question 10

Microsoft's Responsible AI principle of Accountability means which of the following?

A. The AI model itself is programmed to apologize when it makes an error

B. The AI system logs every prediction it makes so errors can be traced in audit records

C. Humans and organizations deploying AI are answerable for how those systems behave, and mechanisms exist for redress when AI causes harm

D. The AI vendor guarantees 100% accuracy and pays financial penalties for incorrect predictions

### Q10 — Correct Answer

C. Humans and organizations deploying AI are answerable for how those systems behave, and mechanisms exist for redress when AI causes harm

### Q10 — Distractor Analysis

- A is incorrect: AI models do not have moral responsibility or the capacity to "apologize" in any meaningful sense. Accountability is a property of humans and organizations, not of the model itself.
- B is incorrect: Audit logging is a technical mechanism that supports accountability, but it is not the definition of the principle. Accountability is about human answerability and redress, not just logging.
- D is incorrect: Vendors do not typically guarantee 100% accuracy, and financial penalties are not the definition of accountability in the Responsible AI framework. Accountability is about governance structure and redress pathways, not contractual liability.

---

End of Quiz — Module 11
