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

---

## Question 11 (5 points)

Azure AI Language's opinion mining feature is enabled when calling the sentiment analysis endpoint. What additional information does opinion mining return compared to standard sentiment analysis?

A. The language of the document and the detected dialect region.

B. Aspect-level sentiment — which specific features or attributes of a subject are evaluated positively or negatively, along with who expressed the opinion.

C. A count of positive, negative, and neutral words in each sentence.

D. A translation of the document into English before sentiment scoring.

### Q11 — Correct Answer

B. Aspect-level sentiment — which specific features or attributes of a subject are evaluated positively or negatively, along with who expressed the opinion.

### Q11 — Distractor Analysis

- A is incorrect: Language detection is a separate feature and is not what opinion mining adds. Dialect information is not returned.
- C is incorrect: Standard sentiment analysis and opinion mining both use contextual embeddings, not word counts. Neither returns a count of sentiment-labeled individual words.
- D is incorrect: Translation is Azure AI Translator's function. Sentiment analysis operates on the text in its original language; translation is not part of the pipeline.

---

## Question 12 (5 points)

A developer builds a CLU model with four intents: BookFlight, CancelFlight, CheckStatus, and None. During testing, the model frequently predicts BookFlight for utterances that should match CancelFlight. What is the most likely cause and best remedy?

A. The CLU service has a known bug that confuses flight-related intents.

B. The utterances for BookFlight and CancelFlight are too similar; adding more varied and distinctive training utterances for each intent will help the model distinguish them.

C. The None intent has too many utterances, causing the model to ignore the flight intents.

D. Four intents exceed the maximum supported by CLU.

### Q12 — Correct Answer

B. The utterances for BookFlight and CancelFlight are too similar; adding more varied and distinctive training utterances for each intent will help the model distinguish them.

### Q12 — Distractor Analysis

- A is incorrect: The described confusion is a standard model training quality issue, not a service bug.
- C is incorrect: The None intent should contain diverse out-of-scope utterances. Having sufficient None utterances improves the model; it does not cause confusion between in-scope intents.
- D is incorrect: CLU supports hundreds of intents. Four intents is well within the supported range.

---

## Question 13 (5 points)

What is entity linking in Azure AI Language, and how does it differ from standard NER?

A. Entity linking assigns a custom label to any word in the text; NER only finds proper nouns.

B. Entity linking disambiguates recognized entities by connecting them to a knowledge base entry (e.g., linking "Paris" to the Wikipedia article for Paris, France vs. Paris, Texas); NER only identifies and categorizes entity mentions without disambiguation.

C. Entity linking extracts only numerical entities such as dates and prices; NER extracts person names and organizations.

D. Entity linking and NER are synonyms for the same operation in Azure AI Language.

### Q13 — Correct Answer

B. Entity linking disambiguates recognized entities by connecting them to a knowledge base entry (e.g., linking "Paris" to the Wikipedia article for Paris, France vs. Paris, Texas); NER only identifies and categorizes entity mentions without disambiguation.

### Q13 — Distractor Analysis

- A is incorrect: NER recognizes a broad range of entity types (not just proper nouns), and entity linking is not about assigning custom labels.
- C is incorrect: NER covers many types including people, organizations, locations, dates, and quantities. Entity linking covers recognized entities that map to knowledge base entries, not exclusively numbers.
- D is incorrect: They are distinct features. NER produces category labels; entity linking produces knowledge base identifiers (URLs). Both are available in Azure AI Language but return different data.

---

## Question 14 (5 points)

A legal firm processes thousands of contracts containing names, dates, and monetary amounts. They need a solution that can automatically detect and replace all person names with the placeholder `[REDACTED]` before the documents are stored. Which feature of Azure AI Language should they use?

A. Named entity recognition — the detected entities can be used to filter sensitive content.

B. Key phrase extraction — important phrases including names will be returned.

C. PII entity recognition with redaction — the API returns both the detected PII and a redacted version of the text.

D. Abstractive summarization — the summary will omit personally identifiable information.

### Q14 — Correct Answer

C. PII entity recognition with redaction — the API returns both the detected PII and a redacted version of the text.

### Q14 — Distractor Analysis

- A is incorrect: Standard NER identifies entity categories but does not produce a redacted version of the text. The firm would need to implement their own find-and-replace logic from NER output.
- B is incorrect: Key phrase extraction returns important phrases for understanding content; it does not identify or redact PII specifically.
- D is incorrect: Abstractive summarization generates shortened versions of text. It does not systematically identify PII or guarantee that names are excluded from the output.

---

## Question 15 (5 points)

A news media organization wants to build a chatbot that answers readers' questions about breaking news stories. The knowledge base will be updated hourly from articles. Which Azure AI Language service is most appropriate?

A. CLU — train intents for each article topic.

B. Azure AI Language Question Answering — import articles as knowledge sources and query against extracted Q&A pairs.

C. Azure AI Translator — translate questions to match stored article language.

D. Azure AI Language PII detection — scan articles for sensitive information before storing.

### Q15 — Correct Answer

B. Azure AI Language Question Answering — import articles as knowledge sources and query against extracted Q&A pairs.

### Q15 — Distractor Analysis

- A is incorrect: Training CLU intents for thousands of articles is impractical and would require constant retraining. Question Answering is designed for knowledge retrieval at scale.
- C is incorrect: Translation is for converting between languages. If the reader and articles share the same language, translation is irrelevant. Even if languages differ, translation alone does not answer questions.
- D is incorrect: PII detection protects personal data. It does not answer reader questions or build a chatbot knowledge base.

---

## Question 16 (5 points)

Which of the following NLP preprocessing steps is MOST important before training a traditional machine learning text classifier (not a transformer-based model)?

A. Applying PII redaction to remove personal information from training documents.

B. Tokenization, stopword removal, and TF-IDF vectorization to convert text into numerical feature vectors the model can process.

C. Running abstractive summarization to shorten all training documents to 100 words.

D. Translating all training documents into English using Azure AI Translator.

### Q16 — Correct Answer

B. Tokenization, stopword removal, and TF-IDF vectorization to convert text into numerical feature vectors the model can process.

### Q16 — Distractor Analysis

- A is incorrect: PII redaction is a privacy preprocessing step for sensitive data, not a requirement for training a text classifier. It does not convert text into numerical features.
- C is incorrect: Summarizing training documents to 100 words would lose the signals needed for accurate classification. Preprocessing for traditional ML focuses on feature representation, not compression.
- D is incorrect: Translating to English is relevant only for multilingual scenarios. Traditional ML classifiers can be trained in any language as long as the feature representation is consistent.

---

## Question 17 (5 points)

A CLU model's training evaluation shows F1 scores of 0.95 for BookRoom and 0.62 for CancelRoom. A developer examines the labeled utterances and finds that CancelRoom has only 8 training examples while BookRoom has 47. What action will most likely improve CancelRoom's F1 score?

A. Lower the probability threshold for the CancelRoom intent specifically.

B. Add more labeled training utterances for CancelRoom (at least 20-30 diverse examples).

C. Delete the CancelRoom intent and combine it with the None intent.

D. Retrain the model without any training data changes.

### Q17 — Correct Answer

B. Add more labeled training utterances for CancelRoom (at least 20-30 diverse examples).

### Q17 — Distractor Analysis

- A is incorrect: Lowering the probability threshold increases recall but also increases false positives (predicting CancelRoom when other intents should match). The root cause — insufficient training data — is not addressed by threshold changes.
- C is incorrect: Merging CancelRoom into None would make the bot unable to recognize and respond to genuine cancellation requests.
- D is incorrect: Retraining without any data changes will produce the same model. The training data imbalance is the root cause and must be addressed.

---

## Question 18 (5 points)

An Azure AI Language sentiment analysis call processes a customer complaint: "The product arrived on time, but the packaging was completely damaged and the manual was missing." Which sentiment output best represents this document?

A. Positive sentiment — the product arrived on time.

B. Negative sentiment — the complaint outweighs the positive aspect.

C. Mixed sentiment — with sentence-level scores: first sentence positive (on-time delivery), second and third sentences negative (packaging and missing manual).

D. Neutral sentiment — the document contains both positive and negative words in equal measure.

### Q18 — Correct Answer

C. Mixed sentiment — with sentence-level scores: first sentence positive (on-time delivery), second and third sentences negative (packaging and missing manual).

### Q18 — Distractor Analysis

- A is incorrect: The document contains significant negative content. A positive overall label would misrepresent the customer's experience.
- B is incorrect: While negative aspects dominate, the Azure AI Language service also provides sentence-level and aspect-level detail. Simply labeling the document negative loses the distinction that timely delivery was a positive experience.
- D is incorrect: Neutral sentiment indicates lack of positive or negative opinion. This document expresses clear positive and negative opinions. Neutral applies to factual or opinion-free text.

---

## Question 19 (5 points)

Custom Translator differs from the standard Azure AI Translator service in which important way?

A. Custom Translator is used for speech translation; the standard service only translates text.

B. Custom Translator allows organizations to upload domain-specific parallel text to fine-tune translation quality for specialized vocabulary (e.g., legal, medical, engineering terminology).

C. Custom Translator is free for all Azure customers; the standard service requires a paid plan.

D. Custom Translator replaces CLU for intent recognition tasks.

### Q19 — Correct Answer

B. Custom Translator allows organizations to upload domain-specific parallel text to fine-tune translation quality for specialized vocabulary (e.g., legal, medical, engineering terminology).

### Q19 — Distractor Analysis

- A is incorrect: Both services handle text translation. Azure AI Speech Service handles speech translation. Neither Custom Translator nor the standard Translator is for speech.
- C is incorrect: Custom Translator has training compute costs. It is not free. The standard Translator has a free tier for general translation; Custom Translator is a premium offering.
- D is incorrect: Custom Translator is purely for language translation. CLU handles conversational intent recognition. These are completely different capabilities.

---

## Question 20 (5 points)

A compliance officer needs to identify every email address, phone number, and credit card number in 50,000 customer service transcripts stored in Azure Blob Storage. The officer wants automated detection reports without modifying the original files. Which approach best meets this need?

A. Use Azure AI Language PII entity recognition to scan the transcripts and return detected PII entities with their positions — without enabling redaction.

B. Use Azure AI Language NER with the standard pre-built categories.

C. Use Azure AI Language sentiment analysis to flag emotionally sensitive conversations.

D. Use Azure AI Language extractive summarization to condense each transcript before manual review.

### Q20 — Correct Answer

A. Use Azure AI Language PII entity recognition to scan the transcripts and return detected PII entities with their positions — without enabling redaction.

### Q20 — Distractor Analysis

- A is correct because PII detection specifically targets sensitive data types like email addresses, phone numbers, and credit card numbers. The redaction feature can be disabled so the original files remain unchanged while the compliance report captures entity positions.
- B is incorrect: Standard NER detects general entity categories (Person, Organization, Location). It does not specifically target PII data types like credit card numbers or phone numbers.
- C is incorrect: Sentiment analysis measures emotional tone. It does not identify PII data types.
- D is incorrect: Summarization condenses content. It does not detect or report PII entity locations for compliance purposes.

---

End of Quiz — Module 08
