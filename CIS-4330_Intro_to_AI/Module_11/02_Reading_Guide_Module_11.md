# Reading Guide: Module 11 — AI Ethics and Responsible AI Principles

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe responsible AI considerations and Microsoft's Responsible AI principles

---

## Overview

This reading guide covers Microsoft's six Responsible AI principles, bias detection and mitigation, model cards, AI impact assessments, and the regulatory landscape. This module is directly and heavily tested on AI-900. Estimated reading time: 50–65 minutes.

---

## Section 1: Microsoft's Six Responsible AI Principles

### The Framework

Microsoft's Responsible AI principles were formalized in 2018 and have since been embedded in product design, procurement requirements, and developer guidance across Azure AI services. Every Azure AI service — Custom Vision, Face API, Azure OpenAI, Language Service — has been evaluated against these principles, and several product decisions (such as Face API Limited Access) are direct results of applying them.

### Principle Definitions and Examples

| Principle | Core Definition | Concrete Example |
|-----------|----------------|-----------------|
| Fairness | AI should treat all groups equitably and not produce discriminatory outcomes | A hiring AI that rates candidates equally regardless of gender, race, or name |
| Reliability and Safety | AI should perform consistently and minimize harm across varied conditions | A medical diagnostic AI that performs equally well on patients of all ages and imaging equipment types |
| Privacy and Security | AI should collect minimum necessary data and protect it from misuse | A voice assistant that discards audio recordings after processing rather than storing them |
| Inclusiveness | AI should be accessible and work well for all people across abilities, languages, and contexts | An OCR system that handles both Latin and Arabic scripts with equal accuracy |
| Transparency | AI's capabilities, limitations, and decision processes should be understandable | A loan decision system that provides a plain-language explanation of why an application was declined |
| Accountability | Humans and organizations should be answerable for AI behavior and outcomes | A hospital that designates a named clinician as responsible for any AI-assisted diagnosis |

### Principle Interactions

The principles frequently interact and sometimes create tensions.

**Transparency vs. Privacy**: Publishing full model details for transparency may reveal information about training data, compromising individual privacy.

**Fairness vs. Accuracy**: Applying equal false positive rates across demographic groups may reduce overall accuracy compared to an unconstrained model.

**Reliability vs. Inclusiveness**: A highly reliable model for majority groups may be less reliable for minority groups due to representation gaps in training data.

These tensions do not mean the principles conflict — they mean that responsible AI requires careful engineering trade-offs rather than simple solutions.

---

## Section 2: Bias — Technical Deep Dive

### Types of Bias

| Bias Type | Description | Example |
|-----------|-------------|---------|
| Historical bias | Training data reflects past discriminatory practices | Credit model trained on historical loans that excluded minority applicants |
| Representation bias | Some groups are underrepresented in training data | Face recognition system with 80% lighter-skinned training images |
| Measurement bias | Data collection methods are less accurate for some groups | Activity tracker that measures steps less accurately on darker-skin tones |
| Aggregation bias | A single model is applied to groups with fundamentally different characteristics | Medical model trained on male patients applied to female patients |
| Label bias | Human annotators apply labels inconsistently across groups | Resumé screeners who rate identical applications differently based on applicant name |
| Feedback loop bias | Biased model outputs become future training data, amplifying the bias | Recidivism model that over-predicts risk for one group, leading to longer sentences, which become features in future models |

### Bias Detection Tools

| Tool | Type | What It Does |
|------|------|-------------|
| Fairlearn | Python library / Azure ML integration | Computes fairness metrics across demographic groups; supports mitigation algorithms |
| Responsible AI Dashboard (Azure ML) | Visual tool | Group-level performance analysis, error distribution, counterfactuals, causal inference |
| InterpretML | Python library | Model explainability via SHAP values and other methods |
| Azure ML model evaluation | Built-in | Confusion matrices, precision/recall by class |

### Fairness Metrics

Different fairness metrics capture different aspects of equitable treatment. No single metric is universally correct — the right metric depends on the harm being prevented.

| Metric | Definition | When to Use |
|--------|-----------|-------------|
| Demographic parity | Equal positive prediction rates across groups | When historical exclusion of a group must be corrected |
| Equal opportunity | Equal true positive rates across groups | When being identified as positive is a benefit (e.g., loan approval) |
| Predictive parity | Equal precision across groups | When false positives cause harm (e.g., security screening) |
| Equalized odds | Equal true positive AND false positive rates | Strict fairness; often hardest to achieve |

### Mitigation Strategies

**Pre-processing approaches** modify training data before model training.

- Reweighting: assign higher sample weights to underrepresented groups
- Resampling: oversample underrepresented groups or undersample overrepresented groups
- Relabeling: audit and correct biased labels

**In-processing approaches** modify the training objective.

- Adversarial debiasing: train a model that is good at the task but poor at predicting the protected attribute
- Fairness constraints: add a fairness penalty to the loss function

**Post-processing approaches** modify model outputs after training.

- Threshold adjustment: apply different decision thresholds per group to achieve equal error rates
- Calibration: adjust confidence scores so they are equally reliable across groups

---

## Section 3: Reliability and Safety in Practice

### Failure Mode Categories

| Failure Type | Description | Example |
|-------------|-------------|---------|
| Distribution shift | Real-world data differs from training data | Medical model deployed in a new country with different patient demographics |
| Edge cases | Rare inputs the model was not trained on | Autonomous vehicle encountering a construction zone type not in training data |
| Adversarial attacks | Deliberately crafted inputs to cause failure | Stop sign with a small adversarial sticker that makes the AI misclassify it |
| Model degradation | Performance declines as world changes but model is static | Fraud detection model trained before a new type of fraud emerged |

### Safety Practices

- **Model monitoring**: Track production performance metrics continuously; alert on degradation
- **A/B testing before full rollout**: Deploy to a small user segment first
- **Human-in-the-loop for high stakes**: Always require human review for medical, legal, financial, and safety decisions
- **Kill switch**: Design every AI system with the ability to revert to non-AI fallback behavior
- **Red teaming**: Deliberately attempt to break the system before deployment

---

## Section 4: Governance Tools

### Model Cards

A model card is a short document that communicates essential information about a trained model to users, evaluators, and the public. The concept was introduced in Google's 2019 paper "Model Cards for Model Reporting" and has been widely adopted.

| Model Card Section | Content |
|-------------------|---------|
| Model overview | What the model does; intended use cases |
| Model type and architecture | Algorithm family; key design choices |
| Training data | Source, size, preprocessing; known gaps or biases |
| Evaluation data | Test sets used; how representative they are |
| Performance metrics | Overall and per-subgroup accuracy, precision, recall |
| Limitations | What the model should NOT be used for; known failure modes |
| Ethical considerations | Fairness analysis results; bias mitigations applied |
| Recommendations | Guidance for deployers; context where caution is needed |

Microsoft publishes model cards for Azure AI Face API, Custom Vision, and other services. They are available on the Azure AI documentation site and on the Microsoft Research model card page.

### AI Impact Assessments

An AI impact assessment (AIIA) is a structured pre-deployment evaluation. It is analogous to an environmental impact assessment for construction projects — a structured analysis of potential harms conducted before a decision is made.

#### Core AIIA Questions

1. What is the AI system designed to do, and what decisions will it influence?
2. Who will be affected — directly (subjects of AI decisions) and indirectly (communities, third parties)?
3. What potential harms could result — to individuals, groups, and society?
4. What is the severity and reversibility of potential harms?
5. Have affected communities or stakeholders been consulted?
6. What safeguards, human oversight, and audit mechanisms are in place?
7. What is the process for monitoring the system after deployment?
8. What is the remediation plan if harms occur?

#### When AIIAs Are Required

| Context | Requirement |
|---------|-------------|
| EU AI Act high-risk systems | Mandatory (called "conformity assessment") |
| US federal agency AI | Required by Executive Order guidance |
| Microsoft internal AI deployment | Required by Microsoft Responsible AI Standard |
| General enterprise best practice | Strongly recommended by NIST AI RMF |

---

## Section 5: The Regulatory Landscape Reference

### Key Frameworks

| Framework | Jurisdiction | Type | Key AI Provisions |
|-----------|-------------|------|------------------|
| EU AI Act | European Union | Binding law | Risk-based classification; high-risk requirements; prohibited AI |
| GDPR | European Union | Binding law | Right to explanation for automated decisions; data minimization |
| NIST AI Risk Management Framework | United States | Voluntary | Govern, Map, Measure, Manage risk framework |
| AI Executive Order (2023) | United States | Federal directive | Safety reporting for powerful AI; agency standards |
| UK AI Principles | United Kingdom | Guidance | Sector-based regulation via existing regulators |
| China AI Regulations | China | Binding law | Algorithmic recommendation and generative AI specific rules |

### EU AI Act Risk Tiers

| Risk Level | Examples | Requirements |
|-----------|----------|-------------|
| Unacceptable (banned) | Social scoring by governments; real-time biometric surveillance in public spaces | Prohibited |
| High risk | Recruitment, credit scoring, critical infrastructure, law enforcement, medical devices | Conformity assessment; transparency; human oversight; data governance |
| Limited risk | Chatbots, deepfakes | Transparency disclosure (must disclose AI nature) |
| Minimal risk | Spam filters, recommendation engines | No specific requirements |

---

## Section 6: Service-Level Responsible AI in Azure

### How Principles Map to Product Decisions

| Product Decision | Responsible AI Principle |
|----------------|-------------------------|
| Face API Limited Access program | Accountability; Fairness |
| Azure OpenAI content filters (always on) | Reliability and Safety |
| PII detection and redaction in Language Service | Privacy and Security |
| Responsible AI Dashboard in Azure ML | Fairness; Transparency |
| Model cards for Azure AI services | Transparency; Accountability |
| Orchestration Workflow confidence threshold | Reliability and Safety |
| Bot Framework disclosure guidelines | Transparency |
| Custom Vision export for offline use | Inclusiveness (access in low-connectivity contexts) |

---

## Section 7: AI-900 Exam Tips

### High-Frequency Topics

**Topic 1 — Name all six principles.** This is directly tested. Memorize: Fairness, Reliability and Safety, Privacy and Security, Inclusiveness, Transparency, Accountability.

**Topic 2 — Match scenario to principle.** A scenario describes an AI system causing a specific type of harm — map it to the correct principle. Demographic disparity → Fairness. Unpredictable failures → Reliability and Safety. Leaked private data → Privacy and Security. Works only in English → Inclusiveness. No explanation available → Transparency. Nobody held responsible → Accountability.

**Topic 3 — Model card contents.** Know the sections and their purpose.

**Topic 4 — Bias types.** Know historical, representation, and label bias. Know that training data is the primary source.

**Topic 5 — AI impact assessment purpose.** Know that it is a pre-deployment evaluation for identifying and mitigating potential harms.

### Common Exam Traps

- Transparency is about explainability and honest communication — not about publishing all model details publicly.
- Accountability does not mean the AI is responsible for its actions — humans and organizations are accountable for the AI they deploy.
- Fairness is not the same as accuracy. A highly accurate model can still be unfair if errors are concentrated in one demographic group.
- Inclusiveness is broader than disability accessibility — it includes language coverage, cultural context, and economic access.

---

## Section 8: Key Term Glossary

| Term | Definition |
|------|-----------|
| Fairness | AI treats all groups equitably without discriminatory outcomes |
| Reliability and Safety | AI performs consistently and minimizes harm across varied conditions |
| Privacy and Security | AI collects minimum necessary data and protects it from unauthorized access |
| Inclusiveness | AI is accessible and works well for all people across abilities, languages, and contexts |
| Transparency | AI capabilities, limitations, and decisions are understandable to users and affected parties |
| Accountability | Humans and organizations are answerable for AI behavior and outcomes |
| Bias | Systematic error in model predictions that unfairly disadvantages a group |
| Historical bias | Bias arising from training data that reflects past discriminatory practices |
| Representation bias | Bias from underrepresentation of groups in training data |
| Feedback loop | Cycle where biased AI outputs become future training data, amplifying bias |
| Model card | Document communicating a model's purpose, training data, performance, and limitations |
| AI impact assessment | Pre-deployment evaluation of potential harms and safeguards |
| Fairlearn | Microsoft open-source Python library for AI fairness assessment and mitigation |
| EU AI Act | EU legislation classifying AI systems by risk level and imposing requirements |
| NIST AI RMF | US voluntary AI risk management framework |
| Explainability | Ability to provide a meaningful explanation for a model's specific prediction |

---

## Section 9: Study Checklist

Work through this checklist before the quiz.

- [ ] I can name all six Microsoft Responsible AI principles from memory
- [ ] For each principle, I can give one concrete example of an AI system violating it
- [ ] I can describe three types of bias in AI training data
- [ ] I know what a feedback loop is in the context of AI bias
- [ ] I can name two Azure tools for detecting or mitigating AI fairness issues
- [ ] I understand what a model card contains and why it supports transparency and accountability
- [ ] I know the purpose and key questions of an AI impact assessment
- [ ] I can describe the EU AI Act risk tiers and give one example at each level
- [ ] I can map a real-world AI harm scenario to the specific Responsible AI principle it violates
- [ ] I know why the Face API Limited Access policy was implemented and which principles it serves

---

## 10. Supplemental Resources

**1. Microsoft Responsible AI Resource Center**
<https://www.microsoft.com/en-us/ai/responsible-ai>
Microsoft's central hub for responsible AI guidance, tools, and case studies. Includes links to the Responsible AI Standard document, Fairlearn, InterpretML, and Azure Machine Learning Responsible AI Dashboard — directly supporting every principle covered in Module 11.

**2. Fairlearn — Fairness Assessment and Mitigation for Machine Learning (official documentation)**
<https://fairlearn.org/v0.10/user_guide/index.html>
The official user guide for Fairlearn, Microsoft's open-source Python library. Covers fairness metrics (demographic parity, equalized odds), disparity visualization, and mitigation algorithms (ExponentiatedGradient, GridSearch). Hands-on supplement to the Module 11 bias analysis exercises.

**3. NIST AI Risk Management Framework (AI RMF 1.0)**
<https://airc.nist.gov/RMF>
The US National Institute of Standards and Technology's AI Risk Management Framework, covering Govern, Map, Measure, and Manage functions. Directly relevant to the EU AI Act and NIST comparison content in Module 11 and a key reference for the AI impact assessment in Part D of the lab.

---

End of Reading Guide — Module 11
