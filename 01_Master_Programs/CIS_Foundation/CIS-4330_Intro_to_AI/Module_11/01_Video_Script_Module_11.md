# Video Script: Module 11 — AI Ethics and Responsible AI Principles

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure AI Fundamentals (AI-900)

---

## INTRO SEGMENT (0:00 – 2:00)

Welcome to Module 11. I'm Professor Nash. This is our final content module, and I have saved the most important topic for last: AI ethics and responsible AI.

Everything we have built in this course — computer vision, language understanding, chatbots, generative AI — carries the potential to cause harm if designed or deployed carelessly. The same technology that helps a nurse triage patients faster can also misidentify a patient's race and skew their treatment. The same model that writes your marketing copy can produce and spread disinformation at scale. The same facial recognition system that unlocks your phone can wrongfully identify an innocent person to a law enforcement officer.

These are not hypothetical risks. They are documented harms that have occurred in production systems.

By the end of this module you will be able to name and define Microsoft's six Responsible AI principles, explain the concepts of bias in AI and how it propagates from data to decisions, describe model cards and AI impact assessments as governance tools, and discuss the regulatory landscape around AI.

This module aligns directly to AI-900 Objective 6: Describe responsible AI considerations.

---

## SECTION 1: The Microsoft Responsible AI Framework (2:00 – 5:00)

Microsoft has articulated six principles that guide how it designs AI systems and how it expects customers to use Azure AI services. These principles are not aspirational marketing — they are embedded in product decisions like the Face API Limited Access policy and the Azure OpenAI content filters we explored in earlier modules.

The six principles are:

**Fairness**: AI systems should treat all people equitably and not produce discriminatory outcomes based on characteristics such as race, gender, religion, national origin, disability, or age.

**Reliability and Safety**: AI systems should perform as expected across intended use cases, behave predictably under varied conditions, and have safeguards to prevent and minimize harm.

**Privacy and Security**: AI systems should respect data privacy laws and norms, collect only the minimum necessary data, and protect that data from unauthorized access.

**Inclusiveness**: AI systems should be accessible to and designed for all people, including those with disabilities, across diverse languages, cultures, and socioeconomic contexts.

**Transparency**: AI systems and their limitations should be understandable to the people who use them and the people they affect. Decision-making processes should be explainable.

**Accountability**: People and organizations deploying AI systems should be answerable for how those systems behave. There should be mechanisms for redress when AI causes harm.

**[SHOW DEMO]** Navigate to microsoft.com/ai/responsible-ai. Show the Responsible AI framework page. Point out the principle icons, the Tools and Practices section, and the link to the AI Impact Assessment guide.

These six principles provide the ethical compass for every decision in AI development. When you encounter a design choice in the lab, in your career, or on the AI-900 exam, ask yourself which principles are at stake.

---

## SECTION 2: Fairness — Bias in AI Systems (5:00 – 9:00)

Fairness is perhaps the most technically complex and socially consequential of the six principles.

### What Is Bias?

In machine learning, **bias** refers to systematic errors in predictions that unfairly advantage or disadvantage particular groups. This is different from the statistical concept of bias (error from wrong assumptions) and different from personal prejudice. Machine learning bias typically emerges from one of three sources.

**Historical bias in training data**: If the training data reflects historical inequities, the model learns and perpetuates those inequities. A credit scoring model trained on historical lending data will encode the discriminatory practices of the past.

**Representation bias**: If certain groups are underrepresented in the training data, the model will perform worse for those groups. A face recognition system trained mostly on lighter-skinned faces will have higher error rates on darker-skinned faces.

**Label bias**: If the labels attached to training examples reflect human prejudice, the model learns that prejudice. If human labelers rate certain resumes as "unqualified" based on names that signal race or gender, a model trained on those labels will encode that bias.

### How Bias Propagates

Bias in AI can cause harm through a chain of effects.

Training data reflects past inequities. The model learns from that data. The model makes biased predictions. Those predictions drive decisions. Those decisions perpetuate or amplify the original inequity.

This is called a **feedback loop**. A credit model that denies loans to people from certain zip codes reduces wealth in those communities, which reduces creditworthiness metrics in future training data, which reinforces the bias in the next model version.

### Detecting Bias

**[SHOW DEMO]** Navigate to Azure Machine Learning Studio. Show the Responsible AI dashboard. Point out the Fairness section — it computes model performance metrics broken down by demographic groups. Show how accuracy, precision, recall, and error rate can all differ across groups.

Tools for detecting and measuring bias include:

- **Fairlearn** — open-source Python library for assessing and mitigating bias, integrated into Azure ML
- **Responsible AI Dashboard** in Azure ML — visual tool for group-level performance analysis
- **Counterfactual Analysis** — "What would the prediction be if only this one attribute changed?"

### Mitigating Bias

After detecting bias, you have several options.

**Pre-processing**: Modify the training data — resample underrepresented groups, relabel biased labels, or remove protected attributes (noting that this is often insufficient because proxy variables can still encode the same information).

**In-processing**: Modify the training objective to include a fairness constraint — for example, requiring equal true positive rates across demographic groups.

**Post-processing**: Adjust model outputs by applying different decision thresholds for different groups to achieve statistical parity.

All of these involve trade-offs. Improving fairness for one group on one metric often reduces overall accuracy or fairness on another metric. These are genuine engineering and policy trade-offs, not problems with a clean solution.

---

## SECTION 3: Reliability and Safety (9:00 – 11:00)

Reliability means the system does what it is supposed to do, consistently, across the range of conditions it will encounter in production.

Safety means the system does not cause harm, including unintended harm, when it fails or when it encounters unexpected inputs.

For AI systems, reliability and safety considerations include:

**Distribution shift**: The model was trained on data from one distribution but encounters different data in production. A medical imaging model trained on images from hospital A may perform poorly on images from hospital B that uses different equipment and imaging protocols.

**Edge cases**: Inputs the model was not trained on. A self-driving car model trained on sunny California highways may not reliably handle icy roads in Minnesota.

**Adversarial inputs**: Deliberately crafted inputs designed to cause the model to fail. An autonomous vehicle model can be fooled by a small sticker on a stop sign that humans ignore but causes the model to misclassify it.

**Cascading failures**: The AI is one component in a larger system. A failure in the AI component may cascade through the system in ways that are hard to predict.

Reliability and safety are why **human oversight** is so critical for high-stakes applications. For decisions affecting health, safety, liberty, or financial welfare, a human should always be in the loop — either reviewing every decision or serving as an escalation path when the AI is uncertain.

---

## SECTION 4: Privacy and Security (11:00 – 13:00)

AI systems are voracious consumers of data. Training and deploying AI systems involves collecting, storing, and processing enormous amounts of information — much of it personal.

Privacy principles for AI include:

**Data minimization**: Collect only the data strictly necessary for the AI task. Do not collect data "just in case" it might be useful later.

**Purpose limitation**: Use data only for the purpose for which it was collected. Training data gathered for one application should not be repurposed for a different application without re-evaluation.

**Retention limits**: Delete data when it is no longer needed for the stated purpose.

**User control**: Where possible, give individuals control over whether their data is used to train or improve AI systems.

Security considerations include protecting models themselves. A model can leak information about its training data through a technique called **membership inference** — inferring whether a specific individual was in the training dataset. For models trained on sensitive data like medical records, this is a serious privacy risk.

**[SHOW DEMO]** In the Azure portal, show Azure AI Services diagnostic settings and how audit logging captures API calls, inputs, and outputs. Show how Azure Key Vault is used to store API keys rather than hardcoding them in application code.

---

## SECTION 5: Inclusiveness and Transparency (13:00 – 15:30)

### Inclusiveness

AI systems should work for everyone, not just the majority or the most economically powerful users.

Inclusiveness challenges in AI include:

**Language coverage**: Most large AI models perform best in English and Western European languages. Performance degrades significantly for lower-resource languages — those with less training data. Users who primarily speak Swahili, Tamil, or Quechua are systematically underserved.

**Disability access**: AI applications should be designed with accessibility in mind — screen reader compatibility, voice interfaces for users who cannot type, high-contrast UI for users with visual impairments.

**Digital access**: AI solutions that require high-speed internet or expensive devices exclude populations in areas with poor connectivity or lower economic resources.

**Cultural context**: AI models trained predominantly on Western content may perform poorly or produce culturally inappropriate outputs for users from other cultural contexts.

### Transparency

Transparency has two dimensions: transparency about the AI system's capabilities and limitations (product transparency), and transparency about how the AI makes specific decisions (decision transparency).

**Product transparency** means users should know:

- That they are interacting with an AI system
- What the system is designed to do and not do
- What data it uses and retains
- What its known error rates and limitations are

**Decision transparency** — also called **explainability** — means being able to provide a meaningful explanation for why the AI produced a specific output for a specific input. This is technically difficult for deep learning models, which are often called "black boxes."

---

## SECTION 6: Accountability and Governance Tools (15:30 – 18:30)

### Accountability

Accountability means someone is responsible for the AI system's behavior and answerable when it causes harm.

In practice, this means:

- Clear ownership: Who is responsible for the system's design, deployment, and monitoring?
- Audit trails: Can you reconstruct what the system did and why for any given decision?
- Redress mechanisms: If someone is harmed by an AI system's decision, is there a pathway for appeal and correction?
- Incident response: Is there a plan for when the system makes a serious mistake?

Accountability is why purely automated AI decision-making for consequential decisions is problematic. If a machine makes a decision that harms someone and there is no human in the loop, accountability is diffuse and redress is nearly impossible.

### Model Cards

A **model card** is a document accompanying a trained AI model that transparently communicates:

- What the model is designed to do
- What data it was trained on and what biases may be present
- How it performs overall and across demographic subgroups
- Known limitations and failure modes
- Intended and out-of-scope use cases
- Ethical considerations and recommendations for deployment

Microsoft publishes model cards for the models in Azure AI services. They are a tool for both transparency (the public understands what the model does) and accountability (the developer has documented their design choices and tested their model).

**[SHOW DEMO]** Search "Microsoft model card" or navigate to the Azure AI Face API model card. Walk through its sections: intended use, evaluation data, performance metrics by demographic, limitations, and recommendations.

### AI Impact Assessments

An **AI impact assessment** is a structured evaluation conducted before deploying an AI system. It asks:

- What decisions will this system influence?
- Who will be affected, and how?
- What are the potential harms — to individuals, groups, and society?
- Have affected communities been consulted?
- What safeguards are in place?
- What is the plan if harms occur?

Microsoft provides a template for AI impact assessments on its Responsible AI website. Several governments have made some form of AI impact assessment mandatory for public sector AI deployments.

---

## SECTION 7: The Regulatory Landscape (18:30 – 20:30)

AI regulation is evolving rapidly. You do not need deep legal knowledge for AI-900, but you should understand the general landscape.

**European Union AI Act**: Entered into force in 2024. Classifies AI systems by risk level — unacceptable risk (banned), high risk (strict requirements), limited risk (transparency obligations), minimal risk (no specific requirements). High-risk applications include recruitment, credit scoring, critical infrastructure, and law enforcement.

**GDPR (EU General Data Protection Regulation)**: Applies to any AI system processing personal data of EU residents. Key provisions relevant to AI include the right to explanation for automated decisions and restrictions on profiling.

**Executive Order on AI (US, 2023)**: Directed federal agencies to develop AI safety standards and required developers of powerful AI models to report to the government.

**NIST AI Risk Management Framework (US)**: A voluntary framework for managing AI risk, widely adopted in US federal agencies and recommended for private sector use.

**Sector-specific regulations**: Healthcare AI is subject to FDA oversight. Financial services AI is subject to fair lending laws. Employment AI is subject to equal opportunity laws. These apply regardless of AI-specific legislation.

**[SHOW DEMO]** Navigate to the Microsoft Responsible AI website. Show the section on regulatory resources and the link to the EU AI Act resources.

The key takeaway is that the regulatory environment is tightening worldwide. Building AI responsibly is not just ethically correct — it is increasingly legally required.

---

## SECTION 8: AI-900 Exam Alignment and Course Recap (20:30 – 23:00)

Let's connect Module 11 to AI-900 objectives and wrap up the full course.

The exam tests your ability to name all six Microsoft Responsible AI principles and match each to its definition, explain why bias occurs and how it can be mitigated, describe what a model card is and what it communicates, and explain what an AI impact assessment is used for.

Key terms for the exam:

- **Fairness** — equitable treatment across demographic groups
- **Reliability and Safety** — consistent, predictable, harm-minimizing behavior
- **Privacy and Security** — data minimization, purpose limitation, user control
- **Inclusiveness** — designing for all people across languages, abilities, and contexts
- **Transparency** — explainability and honest communication about AI capabilities
- **Accountability** — human responsibility for AI outcomes and mechanisms for redress
- **Bias** — systematic error that unfairly disadvantages a group
- **Model card** — documentation of a model's purpose, data, performance, and limitations
- **AI impact assessment** — pre-deployment evaluation of potential harms and safeguards
- **Fairlearn** — Microsoft open-source tool for assessing and mitigating fairness issues
- **Responsible AI Dashboard** — Azure ML visualization tool for fairness, explainability, and error analysis

For the exam: every scenario question about a real-world harm maps back to one or more of the six principles. Identify which principle is implicated and you will find the answer.

And with that, you have completed the primary content of CIS-4330. You have gone from AI fundamentals all the way through computer vision, NLP, conversational AI, generative AI, and now the ethical framework that should guide everything you build.

The certification exam is your next milestone. Good luck. I am proud of everything you have learned this semester.

---

## OUTRO (23:00 – 24:00)

The lab this week asks you to conduct a mini AI impact assessment on a real or proposed AI system of your choosing. The quiz covers the six Responsible AI principles and the governance tools from this module.

This has been Module 11 and the final lecture of CIS-4330. Thank you for showing up every week, asking hard questions, and engaging seriously with this material. Go build something responsible.

---

End of Script — Module 11. Estimated delivery: 23 minutes with demos.
