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

---

## Question 11 (5 points)

A generative AI writing assistant used in a hiring context produces job description text that consistently uses masculine pronouns and male-coded language (e.g., "he will lead the team," "a strong man for the role"). The system was trained on historical job postings without filtering for gendered language. Which bias type best describes this problem?

A. Distribution shift

B. Historical bias — the model learned gendered language patterns from historical job postings that reflected past hiring norms.

C. Label bias — human annotators labeled training examples with incorrect gender associations.

D. Feedback loop — the model's outputs are being used to retrain it, amplifying the bias.

### Q11 — Correct Answer

B. Historical bias — the model learned gendered language patterns from historical job postings that reflected past hiring norms.

### Q11 — Distractor Analysis

- A is incorrect: Distribution shift describes a mismatch between training and deployment data distributions, typically over time. The gendered language pattern is a consistent feature of the original training data, not a shift.
- C is incorrect: Label bias involves errors in how human annotators assign labels. Training on job postings doesn't involve labeling sentiment or categories — the bias is in the linguistic patterns of the source documents themselves.
- D is incorrect: A feedback loop requires the model's outputs to be fed back as future training data. The scenario describes a static training dataset, not a self-reinforcing cycle.

---

## Question 12 (5 points)

An organization deploys an AI-powered customer service chatbot that collects personal information (name, address, order history) to resolve customer inquiries. The chatbot stores complete conversation transcripts indefinitely, including sensitive health details customers share when asking about medical device returns. Which Responsible AI principle is most directly violated?

A. Fairness

B. Inclusiveness

C. Privacy and Security

D. Transparency

### Q12 — Correct Answer

C. Privacy and Security

### Q12 — Distractor Analysis

- A is incorrect: Fairness concerns equitable treatment across demographic groups. The issue described is about data collection and retention practices, not differential treatment.
- B is incorrect: Inclusiveness concerns accessibility and equitable access across abilities and languages. The issue is about how sensitive personal data is handled after collection.
- D is incorrect: Transparency concerns explainability of decisions. While disclosing data retention policies is a transparency best practice, the primary violation is storing sensitive health information beyond operational necessity without appropriate controls.

---

## Question 13 (5 points)

Which Azure tool is specifically designed to help data scientists assess and improve fairness in machine learning models by measuring disparity in model error rates across demographic groups?

A. Azure Monitor

B. Fairlearn (integrated into Azure Machine Learning Responsible AI Dashboard)

C. Azure Cognitive Services Content Filter

D. Azure Policy

### Q13 — Correct Answer

B. Fairlearn (integrated into Azure Machine Learning Responsible AI Dashboard)

### Q13 — Distractor Analysis

- A is incorrect: Azure Monitor tracks application performance, infrastructure metrics, and logs. It does not measure AI fairness metrics or demographic performance disparities.
- C is incorrect: Azure Cognitive Services Content Filter screens generative AI outputs for harmful content categories. It does not measure demographic fairness in classification or regression models.
- D is incorrect: Azure Policy enforces organizational governance rules on Azure resources. It does not assess or measure model fairness.

---

## Question 14 (5 points)

A social media platform uses AI to automatically remove posts that violate community guidelines. The system has a 12% false positive rate (incorrectly removing legitimate posts) for users who write in African American Vernacular English (AAVE), compared to 2% for standard American English. Which two Responsible AI principles are most directly violated?

A. Reliability and Safety only

B. Fairness and Inclusiveness

C. Transparency and Accountability

D. Privacy and Security and Transparency

### Q14 — Correct Answer

B. Fairness and Inclusiveness

### Q14 — Distractor Analysis

- A is incorrect: Reliability and Safety concerns consistent performance across conditions. While relevant, the specific harm here is discriminatory outcomes based on language variety, which is a fairness and inclusiveness issue.
- C is incorrect: Transparency (lack of explanation) and Accountability (no redress mechanism) may also be present, but the primary violations are the unequal error rates (Fairness) and the system's failure to work equally well for all linguistic communities (Inclusiveness).
- D is incorrect: No privacy breach is described. The issue is differential content moderation accuracy based on linguistic dialect.

---

## Question 15 (5 points)

An AI model is described as being "explainable." What does this specifically mean?

A. The model uses only simple algorithms like linear regression that are inherently understandable.

B. The model can provide a meaningful, human-understandable reason for a specific prediction — for example, identifying which input features most influenced a loan rejection decision.

C. The model's source code is publicly available for anyone to review.

D. The model has been certified by a regulatory body as producing accurate predictions.

### Q15 — Correct Answer

B. The model can provide a meaningful, human-understandable reason for a specific prediction — for example, identifying which input features most influenced a loan rejection decision.

### Q15 — Distractor Analysis

- A is incorrect: Explainability is not limited to simple algorithms. Explainability tools (SHAP, LIME, counterfactual explanations) provide post-hoc explanations for complex models including neural networks and gradient boosting.
- C is incorrect: Open-source code publication is transparency about model construction, not explainability. A model can be open source but still produce unexplainable predictions.
- D is incorrect: Regulatory certification addresses compliance and testing standards. It does not inherently mean the model explains individual predictions.

---

## Question 16 (5 points)

A municipality uses an AI system to predict which residential properties need building code inspections. Analysis reveals the system directs 73% of inspections to properties in low-income neighborhoods, compared to 18% in middle-income neighborhoods, even after controlling for known risk factors. The inspections themselves are conducted objectively. Which principle is violated and what is the likely root cause?

A. Reliability and Safety — the model is unreliable due to insufficient training data.

B. Fairness — the model likely learned a correlation between neighborhood income level and inspection history that reflects historical enforcement patterns rather than true underlying risk.

C. Transparency — residents do not know an AI is deciding inspection frequency.

D. Privacy and Security — property owner data is being processed without consent.

### Q16 — Correct Answer

B. Fairness — the model likely learned a correlation between neighborhood income level and inspection history that reflects historical enforcement patterns rather than true underlying risk.

### Q16 — Distractor Analysis

- A is incorrect: The model produces consistent predictions — the issue is not reliability but systematic disparity driven by historical bias in where inspections were previously concentrated.
- C is incorrect: Transparency is a legitimate concern, but it is not the primary violation. The core problem is inequitable targeting based on socioeconomic factors, not lack of disclosure.
- D is incorrect: Using property data for official municipal purposes does not constitute a privacy violation in most jurisdictions. The primary concern is the discriminatory allocation of enforcement activity.

---

## Question 17 (5 points)

What is the purpose of the NIST AI Risk Management Framework (AI RMF), and how does it differ from regulation?

A. The NIST AI RMF is a mandatory US federal law requiring all AI systems to be registered with the government before deployment.

B. The NIST AI RMF is a voluntary framework providing guidelines for identifying, assessing, and managing risks across the AI lifecycle; unlike regulation, compliance is not legally required but is adopted by organizations to demonstrate responsible governance.

C. The NIST AI RMF is a technical specification defining the minimum accuracy thresholds AI systems must achieve.

D. The NIST AI RMF is an international treaty signed by all UN member states governing cross-border AI data flows.

### Q17 — Correct Answer

B. The NIST AI RMF is a voluntary framework providing guidelines for identifying, assessing, and managing risks across the AI lifecycle; unlike regulation, compliance is not legally required but is adopted by organizations to demonstrate responsible governance.

### Q17 — Distractor Analysis

- A is incorrect: The NIST AI RMF is voluntary, not a mandatory federal law. US AI regulation is still evolving; no registration requirement exists at the federal level.
- C is incorrect: The AI RMF addresses governance, risk identification, and organizational practices. It does not define accuracy thresholds or technical specifications.
- D is incorrect: The NIST AI RMF is a US domestic framework, not an international treaty. The EU AI Act is the most prominent international AI regulatory instrument.

---

## Question 18 (5 points)

A large language model is used by a news organization to generate draft article summaries. The model is trained on news articles through early 2024 but is deployed in late 2025. A reader receives a confidently worded summary about a political event that the model presents as current but that actually occurred in 2023 and has since been reversed. Which responsible AI concepts are illustrated by this failure?

A. Feedback loop and representation bias

B. Knowledge cutoff (training data staleness) and hallucination risk in high-stakes publishing without human review

C. Inclusiveness failure and label bias

D. Content filter misconfiguration and jailbreak vulnerability

### Q18 — Correct Answer

B. Knowledge cutoff (training data staleness) and hallucination risk in high-stakes publishing without human review

### Q18 — Distractor Analysis

- A is incorrect: A feedback loop requires model outputs to be used as training data. A knowledge cutoff is a temporal training limitation, not a self-reinforcing cycle. Representation bias involves demographic underrepresentation.
- C is incorrect: Inclusiveness concerns accessibility across user populations. Label bias involves errors in training annotations. Neither applies to the scenario of outdated information being presented confidently.
- D is incorrect: Content filters screen for harmful content categories. Jailbreaks attempt to override safety instructions. The failure described is about outdated knowledge and lack of human review, not safety filter failure or adversarial prompting.

---

## Question 19 (5 points)

An AI system makes consequential decisions (parole recommendations, loan approvals, medical diagnoses) with no mechanism for affected individuals to request a human review or appeal the AI decision. Which Responsible AI principle is MOST directly violated?

A. Inclusiveness

B. Reliability and Safety

C. Accountability

D. Fairness

### Q19 — Correct Answer

C. Accountability

### Q19 — Distractor Analysis

- A is incorrect: Inclusiveness concerns access and usability across diverse populations. The absence of appeal mechanisms is a governance and accountability failure.
- B is incorrect: Reliability and Safety concerns whether the system performs consistently and safely. The issue here is not inconsistent performance but the absence of human review and redress pathways.
- D is incorrect: Fairness concerns equitable outcomes across demographic groups. The absence of an appeal mechanism affects all users equally — the violation is about who is answerable for AI decisions and what recourse affected individuals have, which is Accountability.

---

## Question 20 (5 points)

A university uses an AI to predict which first-year students are at risk of dropping out, and assigns additional advising resources to those students. An analysis shows the model performs well overall but has a 31% false positive rate for first-generation college students, flagging them as at-risk when they ultimately succeed. Which two principles apply, and what design change would best address both?

A. Privacy only; encrypt the student predictions.

B. Fairness and Reliability and Safety; conduct disaggregated performance evaluation by first-generation status during development and retrain with balanced representation.

C. Transparency only; publish the model's feature importance scores.

D. Accountability only; assign a faculty member to review all predictions.

### Q20 — Correct Answer

B. Fairness and Reliability and Safety; conduct disaggregated performance evaluation by first-generation status during development and retrain with balanced representation.

### Q20 — Distractor Analysis

- A is incorrect: Encrypting predictions protects data privacy but does not address the false positive rate disparity. No privacy breach is described — the concern is model accuracy equity.
- C is incorrect: Publishing feature importance is a transparency measure but does not fix the underlying performance disparity. The model needs better representation of first-generation students in training data.
- D is incorrect: Faculty review mitigates harm by adding human oversight (Accountability), but it does not fix the model's systematic misclassification of a specific group. Improving the model directly is the more effective and scalable solution.

---

End of Quiz — Module 11
