# Quiz: Module 05 - Natural Language Processing (NLP) Fundamentals

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe features of Natural Language Processing workloads on Azure
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A company wants to automatically analyze thousands of customer product reviews to determine whether each review expresses satisfaction, dissatisfaction, or a neutral opinion. Which Azure service and NLP task are most appropriate?

- A) Azure Translator — Machine Translation
- B) Azure Language Service — Sentiment Analysis
- C) Azure Speech Service — Speech Recognition
- D) Azure Language Understanding — Intent Recognition

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Sentiment analysis is the NLP task that classifies text emotional tone as positive, negative, or neutral. Azure Language Service provides this as a prebuilt capability with no custom training required.
- *Why A is incorrect:* Azure Translator converts text between languages — it does not assess emotional tone.
- *Why C is incorrect:* Azure Speech Service converts audio to text. Product reviews are already text; no speech processing is needed.
- *Why D is incorrect:* Intent recognition identifies user goals in conversational utterances. Analyzing review sentiment is not an intent recognition task.

---

## Question 2

An e-commerce company receives customer messages in dozens of languages. Before routing each message to the appropriate regional support team, the system must automatically determine what language the message is written in. Which NLP task does this represent?

- A) Named Entity Recognition
- B) Key Phrase Extraction
- C) Language Detection
- D) Text Classification

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Language detection identifies the language of a text document. Azure Language Service supports detection of over 120 languages and provides a confidence score.
- *Why A is incorrect:* NER extracts entities like names and dates. It does not identify the language of the document.
- *Why B is incorrect:* Key phrase extraction identifies important topics within a document — it does not determine the document's language.
- *Why D is incorrect:* Text classification assigns a category label. While language could theoretically be a category, the specific prebuilt task for language identification is language detection.

---

## Question 3

A customer service team wants to build a chatbot that responds to requests such as "Pay my electric bill" and "Check my account balance." The chatbot needs to identify what the customer wants to do and extract the relevant details from the phrase. Which Azure service is designed for this purpose?

- A) Azure Language Service — Sentiment Analysis
- B) Azure Translator
- C) Azure Language Understanding (LUIS / CLU)
- D) Azure Language Service — Key Phrase Extraction

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* LUIS and CLU are designed specifically for intent recognition — identifying the goal (intent) behind a user's utterance and extracting relevant information (entities). "Pay my electric bill" expresses a PayBill intent with entity BillType = electric.
- *Why A is incorrect:* Sentiment analysis determines emotional tone. It cannot identify that "Pay my electric bill" means the user wants to make a payment.
- *Why B is incorrect:* Azure Translator converts text between languages. It does not analyze the meaning or intent of utterances.
- *Why D is incorrect:* Key phrase extraction identifies important words in text. It cannot recognize the intent behind a request or extract structured entities for action.

---

## Question 4

Which of the following best explains why modern NLP systems based on transformer architectures outperform older bag-of-words approaches for tasks like sentiment analysis?

- A) Transformer models require less training data than bag-of-words methods.
- B) Transformer models use contextual embeddings that represent each word differently based on surrounding context, enabling polysemy resolution and long-range dependency modeling.
- C) Transformer models run faster at inference time because they process words individually rather than as sequences.
- D) Bag-of-words models are only available for English, while transformers support all languages.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Contextual embeddings allow the same word to have different representations in different contexts. "I love this product — not!" is correctly classified as sarcastic/negative because the model processes the whole sentence simultaneously via self-attention.
- *Why A is incorrect:* Transformer models require vastly more training data than bag-of-words methods. Pretraining requires billions of text examples.
- *Why C is incorrect:* Transformers process entire sequences in parallel, which makes them faster to train but does not mean they process words individually.
- *Why D is incorrect:* Bag-of-words models can be built for any language. The limitation is not language support but the inability to capture context and word order.

---

## Question 5

A pharmaceutical research company needs to extract drug names, dosage amounts, and adverse event descriptions from clinical trial reports. Standard Azure Language Service NER does not recognize these specialized entity types. What should the company use?

- A) Azure Language Service prebuilt NER with no modifications
- B) Azure Language Service custom NER trained on labeled clinical documents
- C) Azure Translator with a clinical terminology dictionary
- D) Azure Speech Service with domain adaptation

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Custom NER in Azure Language Service lets developers define domain-specific entity types and train a model on labeled examples. This is the correct solution when the required entity types are not covered by the prebuilt model.
- *Why A is incorrect:* Prebuilt NER recognizes general entity categories (person, organization, location, date, quantity). It does not recognize clinical entities like drug names or adverse event descriptions.
- *Why C is incorrect:* Azure Translator is for language translation, not entity extraction. It cannot identify named entities.
- *Why D is incorrect:* Azure Speech Service handles audio-to-text conversion. It is not applicable to processing existing text documents.

---

## Question 6

Azure Language Service returns a sentiment score of positive=0.06, neutral=0.11, negative=0.83 for a product review. How should this output be interpreted?

- A) The review is 83% likely to be about a negative topic, such as product returns.
- B) The model is 83% confident the review expresses a negative sentiment.
- C) 83% of the words in the review are negative words.
- D) The review will be shown to 83% fewer customers than positive reviews.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Confidence scores in Azure Language Service represent the model's probability estimate for each sentiment class. A negative score of 0.83 means the model is 83% confident the text expresses negative sentiment. The three scores sum to approximately 1.
- *Why A is incorrect:* The score is a classification confidence, not a probability that the review is about a specific topic.
- *Why C is incorrect:* Confidence scores reflect the model's classification certainty, not word counts. The model uses contextual embedding, not word frequency.
- *Why D is incorrect:* API confidence scores have no connection to display frequency or business logic in a review system.

---

## Question 7

Which Azure service is specifically designed to convert written text into natural-sounding spoken audio for accessibility and voice interface applications?

- A) Azure Language Service
- B) Azure Translator
- C) Azure Speech Service — Text-to-Speech
- D) Azure Language Understanding

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Speech Service provides Text-to-Speech (TTS) synthesis, converting written text to spoken audio with configurable voices, speaking rates, and languages.
- *Why A is incorrect:* Azure Language Service performs text analysis (sentiment, NER, etc.) — it does not produce audio output.
- *Why B is incorrect:* Azure Translator converts text between languages — it produces text output, not audio.
- *Why D is incorrect:* Azure Language Understanding recognizes intents in text utterances — it does not produce speech.

---

## Question 8

A news organization wants to automatically tag each article with its three most important topics — such as "inflation," "federal reserve," and "interest rates" — to power a topic-based search feature. No predefined topic list exists. Which NLP task is most appropriate?

- A) Text Classification
- B) Intent Recognition
- C) Key Phrase Extraction
- D) Sentiment Analysis

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Key phrase extraction identifies the most important concepts in a document without requiring a predefined list. Since no topic taxonomy exists, the algorithm discovers salient terms from the text itself.
- *Why A is incorrect:* Text classification assigns documents to a predefined set of categories. Without a predefined topic list, this approach requires custom training and a defined label set.
- *Why B is incorrect:* Intent recognition identifies user goals in conversational utterances. Tagging news articles is not a conversational application.
- *Why D is incorrect:* Sentiment analysis determines emotional tone. It does not extract topic keywords.

---

## Question 9

Named Entity Recognition (NER) is applied to the sentence: "Elon Musk announced Tesla's new factory in Austin, Texas will open in March 2025." Which of the following correctly identifies the entities and their categories?

- A) Elon Musk = Person, Tesla = Organization, Austin, Texas = Location, March 2025 = DateTime
- B) Elon Musk = Location, Tesla = Person, Austin = Product, March 2025 = Currency
- C) All words are entities because every word in the sentence is important.
- D) NER cannot process this sentence because it contains proper nouns.

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* NER identifies people (Elon Musk), organizations (Tesla), locations (Austin, Texas), and date/time expressions (March 2025). These are standard entity categories in Azure Language Service.
- *Why B is incorrect:* This swaps and fabricates incorrect entity categories. NER is trained to recognize standard categories accurately.
- *Why C is incorrect:* NER extracts specific entity types, not all words. Function words like "announced" and "will" are not named entities.
- *Why D is incorrect:* NER is specifically designed to process sentences containing proper nouns. Proper nouns are the primary source of named entities.

---

## Question 10

An organization is deploying an NLP system that analyzes employee performance review documents and scores them by sentiment. An audit reveals the model assigns significantly more negative scores to reviews written about female employees than male employees with the same described performance levels. Which Microsoft responsible AI principle is most directly relevant?

- A) Reliability and Safety
- B) Transparency
- C) Fairness
- D) Inclusiveness

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The model produces inequitable outcomes for different demographic groups. Gender-based performance score disparities with equal underlying performance descriptions is a fairness violation — the model treats people unequally based on a protected characteristic.
- *Why A is incorrect:* Reliability and Safety addresses consistent performance and harm prevention. Inconsistent scores across demographic groups is specifically a fairness issue.
- *Why B is incorrect:* Transparency is about making the system's decision logic understandable. The problem described is discriminatory output, not opacity.
- *Why D is incorrect:* Inclusiveness focuses on making AI accessible to all people, particularly those with disabilities or minority language speakers. Gender bias in scoring is a fairness issue.
