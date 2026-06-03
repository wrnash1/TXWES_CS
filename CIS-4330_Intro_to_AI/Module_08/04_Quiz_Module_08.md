# Quiz: Module 08 — Natural Language Processing with Azure

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe features of Natural Language Processing workloads on Azure

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Submit through the course LMS.

---

## Question 1

A marketing team receives thousands of product reviews daily. They want to automatically determine whether each review is positive, negative, or neutral, and also identify which specific product features customers mention positively or negatively. Which Azure AI Language feature covers both requirements?

A. Key phrase extraction

B. Named entity recognition

C. Sentiment analysis with opinion mining enabled

D. Conversational Language Understanding

### Q1 — Correct Answer

C. Sentiment analysis with opinion mining enabled

### Q1 — Distractor Analysis

- A is incorrect: Key phrase extraction identifies important topics but does not return sentiment labels or scores.
- B is incorrect: NER identifies entity categories such as Person, Organization, and Location. It does not evaluate sentiment or associate opinions with product features.
- D is incorrect: CLU classifies user intents and extracts entities from conversational input. It is not designed for bulk review analysis.

---

## Question 2

A developer needs to extract all person names, company names, dates, and dollar amounts from a large collection of legal contracts stored as plain text. Which Azure AI Language feature is most appropriate?

A. Sentiment analysis

B. Text summarization — extractive

C. Named entity recognition

D. Conversational Language Understanding — entity extraction

### Q2 — Correct Answer

C. Named entity recognition

### Q2 — Distractor Analysis

- A is incorrect: Sentiment analysis returns emotional tone. It does not identify or categorize named entities such as person names or monetary values.
- B is incorrect: Extractive summarization selects important sentences; it does not extract structured entity data.
- D is incorrect: CLU entity extraction is designed for conversational user input, not bulk document processing. It requires a trained project with custom utterances.

---

## Question 3

What is the key difference between Azure AI Language and Azure AI Translator?

A. Azure AI Language performs translation; Azure AI Translator performs sentiment analysis

B. Azure AI Language provides NLP tasks such as sentiment analysis and NER; Azure AI Translator is a separate service focused on translating text between languages

C. They are two names for the same service and share the same endpoint

D. Azure AI Translator is a feature within Azure AI Language and uses the same API key

### Q3 — Correct Answer

B. Azure AI Language provides NLP tasks such as sentiment analysis and NER; Azure AI Translator is a separate service focused on translating text between languages

### Q3 — Distractor Analysis

- A is incorrect: The roles are reversed. Language Service handles NLP; Translator handles translation.
- C is incorrect: They are distinct Azure services with separate endpoints, pricing, and resource types.
- D is incorrect: Translator is a standalone service, not a feature of Azure AI Language. It requires its own resource and credentials.

---

## Question 4

In Conversational Language Understanding (CLU), a user sends the message: "Book me a flight to Dallas on Friday." The model should return an intent of BookFlight and extract entities for Destination and TravelDate. What is the term for this training example message used to teach the model?

A. An intent

B. An utterance

C. A feature

D. A token

### Q4 — Correct Answer

B. An utterance

### Q4 — Distractor Analysis

- A is incorrect: An intent is the label assigned to the utterance (BookFlight), not the example message itself.
- C is incorrect: A feature in CLU refers to a characteristic used by the model during training; it is not the name for a training example.
- D is incorrect: A token is a unit from tokenization (individual word or subword). A full training example sentence is an utterance.

---

## Question 5

A company builds a customer service bot. When users ask "What is your return policy?" the bot should retrieve a specific answer from the company's FAQ document. When users say "I want to cancel my order," the bot should trigger a cancellation workflow. Which combination of Azure services best handles both requirements?

A. Two separate CLU projects — one for questions, one for commands

B. Azure AI Language Question Answering for FAQ retrieval and CLU for intent-based commands

C. Azure AI Translator for FAQ retrieval and Azure AI Language for commands

D. A single CLU project with one intent per FAQ question

### Q5 — Correct Answer

B. Azure AI Language Question Answering for FAQ retrieval and CLU for intent-based commands

### Q5 — Distractor Analysis

- A is incorrect: CLU is designed for intent classification and entity extraction, not for retrieving answers from documents. Using CLU for FAQ questions would require manually creating an intent for every possible question.
- C is incorrect: Azure AI Translator handles language translation, not FAQ retrieval or intent recognition.
- D is incorrect: Creating one intent per FAQ question in CLU is an antipattern — it does not scale and is exactly the problem Question Answering solves.

---

## Question 6

Azure AI Language's sentiment analysis returns confidence scores of 0.72 positive, 0.18 neutral, and 0.10 negative for a document. What does this mean?

A. 72 words in the document are positive, 18 are neutral, and 10 are negative

B. The model is 72% confident the overall document sentiment is positive

C. The document must be labeled positive because 0.72 is greater than 0.50

D. The scores indicate the percentage of sentences in each sentiment category

### Q6 — Correct Answer

B. The model is 72% confident the overall document sentiment is positive

### Q6 — Distractor Analysis

- A is incorrect: Confidence scores are probabilities, not word counts.
- C is incorrect: While the model would label the document as positive given these scores, the explanation is wrong — the label reflects the highest probability, but the threshold is not always 0.50 and the system does not "must" assign positive.
- D is incorrect: The three scores are model confidence values for the overall document sentiment, not sentence counts.

---

## Question 7

A healthcare company wants to store anonymized patient support chat transcripts for quality analysis. Before storage, they need to remove all patient names, phone numbers, and medical record numbers from the text. Which Azure AI Language feature should they use?

A. Named entity recognition — standard output

B. Key phrase extraction

C. PII detection with text redaction enabled

D. Text summarization — abstractive

### Q7 — Correct Answer

C. PII detection with text redaction enabled

### Q7 — Distractor Analysis

- A is incorrect: Standard NER identifies entity categories but does not redact the text. You would receive the detected entities but the original text remains unchanged.
- B is incorrect: Key phrase extraction surfaces important topics. It does not identify or remove sensitive personal information.
- D is incorrect: Abstractive summarization generates a shortened version of the text but does not systematically identify or remove PII.

---

## Question 8

A CLU model is evaluated and shows 0.95 precision and 0.60 recall for the CancelOrder intent. What is the most accurate interpretation?

A. The model almost always correctly identifies CancelOrder when it predicts it, but misses 40% of actual CancelOrder utterances

B. The model catches 95% of all CancelOrder utterances but incorrectly labels many non-cancel utterances as CancelOrder

C. The model's overall accuracy is the average of 0.95 and 0.60

D. Precision and recall above 0.50 indicate the model is ready for production without further improvement

### Q8 — Correct Answer

A. The model almost always correctly identifies CancelOrder when it predicts it, but misses 40% of actual CancelOrder utterances

### Q8 — Distractor Analysis

- B is incorrect: This describes high recall and low precision, which is the opposite of the values given.
- C is incorrect: Overall accuracy is not the average of precision and recall. The harmonic mean (F1 score) is the standard combined metric, and it would be approximately 0.74 in this case.
- D is incorrect: The threshold for "production ready" depends on the use case. A recall of 0.60 means the model misses four out of ten genuine cancellation requests, which would likely be unacceptable in a commercial system.

---

## Question 9

Which of the following statements about the None intent in a CLU project is correct?

A. The None intent is optional and can be omitted if all user inputs will always match a defined intent

B. The None intent captures inputs that do not match any defined application intent, preventing false matches

C. The None intent is automatically populated by Azure and cannot be edited

D. Adding utterances to the None intent reduces the model's accuracy for other intents

### Q9 — Correct Answer

B. The None intent captures inputs that do not match any defined application intent, preventing false matches

### Q9 — Distractor Analysis

- A is incorrect: The None intent is strongly recommended in all CLU projects. Without it, the model is forced to assign every input to one of the defined intents, resulting in false positives for off-topic queries.
- C is incorrect: You must manually add diverse utterances to the None intent. It is not automatically populated.
- D is incorrect: Adding good None utterances improves the model overall by teaching it to distinguish in-scope and out-of-scope inputs. It does not reduce accuracy for other intents.

---

## Question 10

A content platform wants to automatically generate a three-sentence summary of each article that preserves exact wording from the source text and can be audited to verify accuracy. Which summarization approach should they use?

A. Abstractive summarization, because it produces more fluent sentences

B. Extractive summarization, because it selects existing sentences from the source and can be traced back to the original

C. Key phrase extraction, because it returns the most important phrases from the text

D. Opinion mining, because it identifies the most positive statements in the document

### Q10 — Correct Answer

B. Extractive summarization, because it selects existing sentences from the source and can be traced back to the original

### Q10 — Distractor Analysis

- A is incorrect: Abstractive summarization generates new sentences that may rephrase or combine source content, making exact-wording auditing impossible.
- C is incorrect: Key phrase extraction returns phrases, not complete sentences, and does not produce a coherent summary.
- D is incorrect: Opinion mining identifies aspect-level sentiment and is not a summarization technique.

---

End of Quiz — Module 08
