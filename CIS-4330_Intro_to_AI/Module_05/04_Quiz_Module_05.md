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

---

### Question 11 (5 points)

What does tokenization accomplish as the first step in an NLP pipeline?

- A) It translates the input text into a numerical embedding vector that the model can process.
- B) It splits raw text into smaller units (words, subwords, or characters) that the model treats as discrete inputs.
- C) It removes all stopwords and punctuation from the document to reduce noise.
- D) It assigns a sentiment score to each word based on a predefined sentiment lexicon.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Tokenization is the process of splitting text into tokens — the atomic units the model processes. Modern tokenizers (e.g., WordPiece, BPE) split at the subword level, allowing models to handle unseen or rare words by breaking them into known subword components.
  - *Why A is incorrect:* Converting tokens to numerical vectors is embedding, which occurs after tokenization. Tokenization produces discrete tokens, not vectors.
  - *Why C is incorrect:* Removing stopwords is a separate optional preprocessing step, not the definition of tokenization. Modern transformer-based NLP often retains stopwords.
  - *Why D is incorrect:* Assigning sentiment values per word describes lexicon-based sentiment analysis, a distinct older approach unrelated to tokenization.

---

### Question 12 (5 points)

A travel company wants to enable customers to type questions like "What is the baggage allowance for economy class?" into their website and receive answers drawn from the airline's existing FAQ documents. No custom ML training is planned. Which Azure service is most appropriate?

- A) Azure Language Understanding (LUIS)
- B) Azure Custom Question Answering
- C) Azure Language Service — Sentiment Analysis
- D) Azure Machine Learning AutoML

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Custom Question Answering (part of Azure Language Service) ingests existing FAQ documents and automatically extracts question-answer pairs. It then matches user questions to the closest stored answer — no custom model training is required.
  - *Why A is incorrect:* LUIS is for intent recognition and entity extraction in conversational applications. It does not answer questions from documents.
  - *Why C is incorrect:* Sentiment analysis determines emotional tone. It does not retrieve answers from FAQ documents.
  - *Why D is incorrect:* Azure Machine Learning AutoML trains custom models from scratch and requires labeled training data. This scenario explicitly requires no custom training.

---

### Question 13 (5 points)

What is the primary difference between Azure Translator and Azure Language Service in the context of multilingual applications?

- A) Azure Translator processes audio; Azure Language Service processes text.
- B) Azure Translator converts text between languages; Azure Language Service analyzes text for sentiment, entities, and key phrases within a language.
- C) Azure Translator requires custom training data; Azure Language Service uses prebuilt models for all tasks.
- D) Azure Translator is only available in North America; Azure Language Service is a global service.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Translator is a machine translation service that converts text from a source language to a target language. Azure Language Service analyzes text — extracting meaning, sentiment, entities, and structure — within the given language. They serve complementary but distinct purposes.
  - *Why A is incorrect:* Both services process text, not audio. Audio processing is Azure Speech Service's domain.
  - *Why C is incorrect:* Both services offer prebuilt capabilities. Azure Translator has no custom training mode (unlike Custom Translator, which is a related but separate product).
  - *Why D is incorrect:* Both services are globally available Azure services. Geographic availability is not the distinction.

---

### Question 14 (5 points)

An application processes spoken customer complaint calls and needs to: (1) convert speech to text, (2) detect the customer's language, and (3) analyze the sentiment of the transcribed text. Which combination of Azure services should be used?

- A) Azure Language Service for all three steps.
- B) Azure Speech Service (step 1), Azure Language Service (steps 2 and 3).
- C) Azure Translator (steps 1 and 2), Azure Language Service (step 3).
- D) Azure Bot Service for all three steps.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Speech Service handles speech-to-text transcription (step 1). Azure Language Service handles language detection (step 2) and sentiment analysis (step 3). This is the correct pairing of services by capability.
  - *Why A is incorrect:* Azure Language Service processes text — it cannot transcribe audio. Step 1 requires the Speech Service.
  - *Why C is incorrect:* Azure Translator translates text between languages but does not transcribe audio. Step 1 still requires the Speech Service.
  - *Why D is incorrect:* Azure Bot Service is for building conversational bots, not for audio transcription or text analysis pipelines.

---

### Question 15 (5 points)

In NLP, what is a "word embedding" and why is it important?

- A) A word embedding is a rule that maps each word to a unique integer ID; it ensures no two words share the same numerical code.
- B) A word embedding is a dense numerical vector that represents a word's meaning in a continuous space, where semantically similar words have similar vectors.
- C) A word embedding is a compression technique that removes duplicate words from a training corpus before model training.
- D) A word embedding is a dictionary lookup table that returns the definition of each word in the input sentence.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Word embeddings (e.g., Word2Vec, GloVe, contextual embeddings from BERT) represent words as dense vectors in a high-dimensional space. Words with similar meanings cluster together, enabling models to reason about semantic similarity. This is foundational to modern NLP.
  - *Why A is incorrect:* Mapping words to unique integer IDs describes integer/index encoding, not embeddings. Integer IDs carry no semantic information — they are arbitrary numbers.
  - *Why C is incorrect:* Removing duplicate words describes deduplication or vocabulary construction, not embedding. Embeddings are representations, not compression methods.
  - *Why D is incorrect:* Returning definitions describes a dictionary lookup, not a numerical embedding. Embeddings capture distributional semantics, not dictionary definitions.

---

### Question 16 (5 points)

A healthcare company processes doctors' notes and needs to identify whether each note mentions a medication name, and if so, whether it was administered or prescribed. Standard Azure Language Service NER supports medication as an entity but does not distinguish administration context. Which approach extends this capability?

- A) Use Azure Translator to translate all notes to English before applying NER.
- B) Use Azure Language Service Custom NER to define additional labels for administration context and train on labeled clinical documents.
- C) Use Azure Speech Service to re-read the notes aloud and apply sentiment analysis.
- D) Use Azure Machine Learning to train a simple logistic regression model on raw text.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Custom NER extends Azure Language Service to support domain-specific entity types and sub-types. Training on labeled clinical documents where medication context is annotated gives the model the distinction it needs.
  - *Why A is incorrect:* Translation is only relevant for multilingual content. The scenario describes English doctors' notes. Translation does not add entity context.
  - *Why C is incorrect:* Re-reading notes as audio and applying sentiment analysis is irrelevant. Sentiment measures emotional tone, not medication context.
  - *Why D is incorrect:* While a custom logistic regression model could work, it would require significant feature engineering and is not the Azure-native, purpose-built solution for entity extraction extension.

---

### Question 17 (5 points)

Which term describes the process by which a transformer model like BERT learns to understand language by training on massive unlabeled text corpora before being fine-tuned on a specific task?

- A) Supervised classification
- B) Reinforcement learning from human feedback (RLHF)
- C) Pretraining
- D) Data augmentation

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Pretraining involves training a model on a large general-purpose dataset (typically using self-supervised objectives like masked language modeling) before task-specific fine-tuning. BERT, GPT, and Azure Language Service's underlying models all undergo pretraining.
  - *Why A is incorrect:* Supervised classification requires labeled input-output pairs and trains a task-specific model. Pretraining is self-supervised on unlabeled text — no human-assigned labels are required.
  - *Why B is incorrect:* RLHF is a technique used to align large language models with human preferences through reward modeling. It is a post-pretraining step, not the pretraining itself.
  - *Why D is incorrect:* Data augmentation creates additional training examples through transformations (e.g., synonym replacement, back-translation). It is a training data strategy, not the pretraining paradigm.

---

### Question 18 (5 points)

An NLP model for resume screening systematically scores resumes containing female-coded language (e.g., "collaborative," "supportive") lower than resumes with identical qualifications using male-coded language (e.g., "led," "executed"). What is the root cause of this bias?

- A) The model's tokenizer splits words incorrectly, losing semantic information.
- B) The training data reflects historical gender imbalances in hiring, causing the model to associate certain language patterns with less-favorable hiring outcomes.
- C) The sentiment analysis component incorrectly classifies positive adjectives as negative.
- D) Azure Language Service does not support gender-neutral language.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* If the training data consisted of past successful-hire resumes from a historically male-dominated field, the model would learn that male-coded language correlates with positive outcomes — not because of skill, but because of historical bias. This is a documented real-world NLP fairness problem (notably seen in Amazon's hiring tool).
  - *Why A is incorrect:* Tokenization errors do not systematically produce gender-based scoring differences. The bias is in learned patterns from training data, not in text splitting.
  - *Why C is incorrect:* The scenario is about resume scoring, not sentiment analysis. Even if sentiment played a role, miscategorizing adjectives would not explain the systematic gender correlation.
  - *Why D is incorrect:* Azure Language Service supports gender-neutral and diverse language. The bias described is a model training data issue, not a service limitation.

---

### Question 19 (5 points)

Which of the following best describes how Azure Cognitive Search uses NLP to enhance document search beyond simple keyword matching?

- A) Azure Cognitive Search replaces all documents with summarized versions before indexing.
- B) Azure Cognitive Search applies NLP skills such as entity extraction, key phrase extraction, and language detection to enrich documents at index time, enabling semantic and metadata-driven search.
- C) Azure Cognitive Search translates all indexed documents into English regardless of their original language.
- D) Azure Cognitive Search uses sentiment analysis to sort search results by emotional positivity.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Cognitive Search's AI enrichment pipeline applies NLP skills (built on Azure Language Service and Cognitive Services) to extract structured metadata from unstructured content during indexing. This enables faceted, semantic, and entity-based search that goes far beyond keyword matching.
  - *Why A is incorrect:* Azure Cognitive Search indexes the original documents with enriched metadata. It does not replace documents with summaries.
  - *Why C is incorrect:* Azure Cognitive Search supports multilingual content and does not force translation to English. Language detection identifies content language; translation is optional.
  - *Why D is incorrect:* While sentiment could theoretically be indexed as a field, this is not a built-in default behavior of Azure Cognitive Search and is not a standard search ranking mechanism.

---

### Question 20 (5 points)

A mobile app needs to translate spoken Spanish into written English in real time. Which combination of Azure services achieves this?

- A) Azure Language Understanding → Azure Translator
- B) Azure Speech Service (Speech-to-Text with Spanish) → Azure Translator (Spanish to English)
- C) Azure Language Service → Azure Speech Service (Text-to-Speech)
- D) Azure Translator → Azure Speech Service (Speech-to-Text)

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The pipeline requires (1) transcribing spoken Spanish to text using Azure Speech Service's Spanish speech recognition model, then (2) translating the Spanish text to English using Azure Translator. Azure Speech Service also supports direct speech translation as a single-step option.
  - *Why A is incorrect:* Azure Language Understanding recognizes intents in text — it does not transcribe audio. This pipeline skips the audio-to-text step entirely.
  - *Why C is incorrect:* This pipeline analyzes text then converts text to speech — producing audio output, not written English. The steps are reversed and incorrect for this use case.
  - *Why D is incorrect:* Azure Translator translates text, not audio. You cannot feed audio directly into Azure Translator — transcription must happen first.
