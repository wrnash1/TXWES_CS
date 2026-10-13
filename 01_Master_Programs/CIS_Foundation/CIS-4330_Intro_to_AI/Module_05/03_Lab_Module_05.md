# Lab Activity: Module 05 - Natural Language Processing (NLP) Fundamentals

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe features of Natural Language Processing workloads on Azure
**Points:** 100
**Submission:** Canvas LMS — Module 05 Lab Assignment

---

## Objectives

By the end of this lab, you will be able to:

- Identify the NLP task type demonstrated by a given text analysis scenario.
- Match NLP tasks to the correct Azure Cognitive Service.
- Interpret sample NLP API output including sentiment scores and named entity annotations.
- Distinguish between prebuilt and custom NLP capabilities in Azure Language Service.
- Analyze text samples for named entities, key phrases, and sentiment.

---

## Prerequisites

No Azure subscription is required. All exercises are text analysis, classification, and interpretation tasks. You will need:

- Module 05 video lecture (completed).
- Module 05 reading guide (completed), including Table 1 (NLP tasks and Azure services).

---

## Part A: NLP Task Identification (30 points)

For each scenario, identify the NLP task type from this list: Sentiment Analysis, Key Phrase Extraction, Named Entity Recognition, Language Detection, Text Classification, Question Answering, Machine Translation, Speech Recognition, Text-to-Speech, Intent Recognition.

Each task type may be used at most twice. Provide a one-sentence justification for each answer.

### Scenario 1

A hotel chain wants to analyze thousands of guest reviews submitted online to determine whether customers are generally satisfied, dissatisfied, or neutral about their stay experience.

NLP task: ________________
Justification: ________________

### Scenario 2

A law firm receives contracts in English, French, German, and Spanish. Before routing each document to the correct attorney team, the firm's system needs to automatically determine which language each contract is written in.

NLP task: ________________
Justification: ________________

### Scenario 3

A news aggregation platform wants to automatically tag each article with its main topics — such as "artificial intelligence," "climate change," or "stock market" — so users can filter by topic without reading each article.

NLP task: ________________
Justification: ________________

### Scenario 4

A global e-commerce company wants to make its English-language product descriptions available to customers in 25 additional languages, automatically.

NLP task: ________________
Justification: ________________

### Scenario 5

A financial services company processes thousands of customer support emails daily. They want to automatically extract company names, dollar amounts, account numbers, and dates from each email to route it to the right department.

NLP task: ________________
Justification: ________________

### Scenario 6

A hospital is building a voice-enabled intake system. When patients speak their symptoms aloud, the system needs to convert that spoken speech into text for processing.

NLP task: ________________
Justification: ________________

### Scenario 7

A software company's help center receives thousands of customer questions per day. The team uploads their existing FAQ documents to create a bot that can automatically find the relevant answer to each customer's question.

NLP task: ________________
Justification: ________________

### Scenario 8

A call center is building a virtual agent that responds to customer requests like "Check my account balance," "Transfer $200 to savings," and "Report a lost card." The system needs to understand the goal behind each phrase and extract the relevant details.

NLP task: ________________
Justification: ________________

### Scenario 9

A research firm wants to automatically sort 50,000 medical research abstracts into one of eight disease categories (cardiovascular, oncology, neurology, etc.) so researchers can filter the database by specialty.

NLP task: ________________
Justification: ________________

### Scenario 10

A screen reader application needs to speak out loud the text on a website for visually impaired users, converting the written web page content into natural-sounding audio.

NLP task: ________________
Justification: ________________

---

## Part B: Azure Service Matching (20 points)

For each scenario, identify the most appropriate Azure service from this list: Azure Language Service (prebuilt), Azure Language Service (custom), Azure Translator, Azure Speech Service, Azure Language Understanding (LUIS / CLU).

Each service may be used more than once.

### Scenario 11

A startup wants to add real-time English-to-Japanese translation to its chat support platform with no ML expertise. They need a solution deployable via REST API call.

Azure service: ________________
Justification: ________________

### Scenario 12

A pharmaceutical company wants to extract drug names, dosages, and adverse event descriptions from clinical trial reports. Standard NER does not recognize these domain-specific entities.

Azure service: ________________
Justification: ________________

### Scenario 13

A podcasting platform wants to generate automatic transcripts of all uploaded audio files so the content is searchable by keyword.

Azure service: ________________
Justification: ________________

### Scenario 14

A retailer wants to analyze 10,000 product reviews to determine the overall sentiment — positive, negative, or neutral — without any custom model training.

Azure service: ________________
Justification: ________________

### Scenario 15

A bank is building a voice assistant that should understand commands like "Pay my credit card bill" or "Show my last three transactions." The assistant needs to identify the banking action requested and the relevant account details.

Azure service: ________________
Justification: ________________

---

## Part C: Interpreting NLP API Output (30 points)

The following JSON represents the output from Azure Language Service for a customer review. Read the output carefully and answer the questions below.

```json
{
  "id": "review_001",
  "sentiment": "mixed",
  "confidenceScores": {
    "positive": 0.46,
    "neutral": 0.08,
    "negative": 0.46
  },
  "sentences": [
    {
      "text": "The hotel room was spotlessly clean and the view was breathtaking.",
      "sentiment": "positive",
      "confidenceScores": { "positive": 0.97, "neutral": 0.02, "negative": 0.01 }
    },
    {
      "text": "However, the check-in process took over two hours and the staff were unhelpful.",
      "sentiment": "negative",
      "confidenceScores": { "positive": 0.03, "neutral": 0.04, "negative": 0.93 }
    }
  ],
  "keyPhrases": ["hotel room", "check-in process", "staff", "breathtaking view"],
  "entities": [
    { "text": "two hours", "category": "Quantity", "subcategory": "Duration", "confidenceScore": 0.99 }
  ]
}
```

### Question 16 (8 points)

The overall sentiment is "mixed" with equal positive and negative scores of 0.46. Based on the sentence-level sentiment, explain precisely why the overall result is "mixed" rather than "positive" or "negative." Which aspect of the hotel experience drove each sentiment direction?

Your answer: ________________

### Question 17 (6 points)

The key phrases extracted are: "hotel room," "check-in process," "staff," "breathtaking view." A product manager reads this output and says "the key phrases don't tell me enough — I need to know which ones are positive and which are negative." Is this a limitation of key phrase extraction? What would they need to do to get this combined insight?

Your answer: ________________

### Question 18 (8 points)

The entity "two hours" was recognized with category "Quantity" and subcategory "Duration" with a confidence score of 0.99. Why is recognizing this entity potentially valuable to the hotel's operations team — what business action might they take based on this extracted information?

Your answer: ________________

### Question 19 (8 points)

The confidence score for the positive sentiment in sentence 2 ("the check-in process took over two hours and the staff were unhelpful") is 0.03. Explain what a confidence score represents in the context of sentiment analysis. If the hotel receives 10,000 reviews per week, why is high confidence on negative reviews particularly important for the operations team?

Your answer: ________________

---

## Part D: Prebuilt vs Custom NLP (20 points)

For each scenario, determine whether a prebuilt Azure Language Service capability is sufficient, or whether a custom NLP solution is required. Write "Prebuilt" or "Custom" and provide a two-sentence justification.

### Scenario 20

A travel agency wants to analyze the sentiment of customer reviews about their vacation packages. The reviews are standard English-language text expressing satisfaction or dissatisfaction.

Prebuilt or Custom: ________________
Justification: ________________

### Scenario 21

A cybersecurity company wants to classify security incident reports into one of 12 internal severity tiers based on their proprietary risk taxonomy. The standard text classification categories do not match their internal system.

Prebuilt or Custom: ________________
Justification: ________________

### Scenario 22

A hospital wants to extract patient names, physician names, and diagnosis codes from discharge summaries. Standard NER recognizes general person names but does not specifically recognize ICD-10 diagnosis codes.

Prebuilt or Custom: ________________
Justification: ________________

### Scenario 23

A marketing agency wants to detect the language of incoming social media comments so they can route non-English comments to the appropriate regional team.

Prebuilt or Custom: ________________
Justification: ________________

---

## Answer Key and Grading Rubric

### Part A (3 points per scenario = 30 points)

Scenario 1: Sentiment Analysis. Goal is to determine emotional tone (satisfied/dissatisfied/neutral) of text.

Scenario 2: Language Detection. Goal is to identify the language each document is written in.

Scenario 3: Key Phrase Extraction. Goal is to extract the main topics from articles for tagging — not a full classification into predefined categories.

Scenario 4: Machine Translation. Goal is to convert text from English into 25 other languages.

Scenario 5: Named Entity Recognition. Goal is to identify and classify specific entity types (company names, amounts, dates) from free text.

Scenario 6: Speech Recognition (Speech-to-Text). Converting spoken audio to text.

Scenario 7: Question Answering. Matching customer questions to answers from uploaded FAQ documents.

Scenario 8: Intent Recognition. Identifying the banking action (intent) and account details (entities) from natural language commands.

Scenario 9: Text Classification. Sorting documents into predefined categories (eight disease specialties).

Scenario 10: Text-to-Speech. Converting written text to spoken audio output.

Scoring: 3 pts = correct task with accurate justification. 1 pt = correct task with weak justification. 0 pts = incorrect task.

### Part B (4 points per scenario = 20 points)

Scenario 11: Azure Translator. Real-time translation via REST API with no training.

Scenario 12: Azure Language Service (custom). Domain-specific entities (drug names, dosages) require custom NER training.

Scenario 13: Azure Speech Service. Audio-to-text transcription.

Scenario 14: Azure Language Service (prebuilt). Standard English sentiment analysis requires no custom training.

Scenario 15: Azure Language Understanding (LUIS / CLU). Intent recognition with entity extraction for conversational commands.

### Part C (8+6+8+8 = 30 points)

Q16: The first sentence about room cleanliness and the view is strongly positive (0.97). The second sentence about check-in time and unhelpful staff is strongly negative (0.93). The overall "mixed" result averages these opposing sentence-level scores.

Q17: Yes, this is a limitation. Key phrase extraction identifies topics but does not assign sentiment to them. To get sentiment per topic, the team would need aspect-based sentiment analysis, which analyzes sentiment toward specific aspects or entities within the text.

Q18: The "two hours" duration entity flags an unusually long check-in wait time. The operations team could use this to identify bottlenecks, set service level targets, or trigger an automatic follow-up with the affected guest.

Q19: Confidence score represents the model's certainty in its classification. High confidence on negative reviews means the operations team can trust automated alerts without manually reviewing every flagged review — critical at 10,000 reviews per week volume.

### Part D (5 points per scenario = 20 points)

Scenario 20: Prebuilt. Standard English sentiment analysis is covered by the prebuilt Language Service capability without custom training.

Scenario 21: Custom. The 12 proprietary severity tiers are not standard categories; custom text classification with labeled training examples is required.

Scenario 22: Custom. ICD-10 diagnosis codes are domain-specific entities not covered by standard NER; custom NER training is needed.

Scenario 23: Prebuilt. Language detection is a prebuilt Language Service capability supporting 120+ languages with no training required.

---

## Deliverable

Submit a single document (PDF or Word) containing all answers and justifications. Include your name, course section, and date at the top. For Part C, include the full text of your responses alongside the relevant JSON excerpt from the question. Upload to the Module 05 Lab Assignment in Canvas by the posted due date.

## Part 9 — Challenge Exercise

### Challenge 1: NLP Pipeline with NLTK and scikit-learn

1. Using Python, install `nltk` and download `punkt`, `stopwords`, and `wordnet`. Write a function that accepts a string of text and returns: (a) a list of tokens, (b) the tokens with stopwords removed, and (c) the lemmatized form of each remaining token using `WordNetLemmatizer`.
2. Apply your function to three sentences of your choice that express positive, negative, and neutral sentiment respectively. Display the output of each preprocessing step side by side.
3. Using scikit-learn's `TfidfVectorizer`, fit it on a list of at least 10 short sentences you write yourself (mix of positive and negative). Print the vocabulary and identify which 5 terms received the highest average TF-IDF weight.
4. Explain in two sentences why TF-IDF down-weights common words and how this property makes it useful for tasks like key phrase extraction.

### Challenge 2: Bias Audit of a Sentiment Classifier

1. Using scikit-learn, train a `LogisticRegression` sentiment classifier on the `movie_reviews` corpus from NLTK (`nltk.corpus.movie_reviews`). Split 80/20 train/test and report accuracy.
2. Write 6 test sentences of your own — 3 describing the same positive experience using male-coded language (e.g., "led," "decisive," "drove results") and 3 using female-coded language (e.g., "collaborated," "nurturing," "supportive"). Run all 6 through the classifier and record the predicted sentiment and confidence score.
3. Compare the results. Do the male-coded and female-coded sentences receive the same or different sentiment scores for equivalent content?
4. Write a 3-4 sentence reflection explaining what this experiment reveals about NLP model bias and which responsible AI principle it relates to.

### Reflection Questions

1. Based on Challenge 1, what would happen to classification accuracy if you skipped the tokenization and stopword removal steps and fed raw sentence strings directly to the TF-IDF vectorizer? Why?
2. Based on Challenge 2, propose one concrete step a team could take during NLP model development to detect and mitigate gender-coded language bias before the model is deployed.
