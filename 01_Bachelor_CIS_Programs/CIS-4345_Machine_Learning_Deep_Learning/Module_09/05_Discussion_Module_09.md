# Discussion Forum: Module 09 — Natural Language Processing with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Instructions

Post your initial response by Wednesday at 11:59 PM. Reply to at least two peers by Sunday at 11:59 PM. Each reply must be at least 60 words and contribute a new idea, counterpoint, or concrete example beyond simply agreeing.

---

## Scenario 1 — The Vocabulary Size Tradeoff

A team at a financial services company is building a complaint-routing classifier. Their corpus contains 2.3 million customer complaint tickets spanning 12 routing categories (billing, fraud, account access, etc.). The corpus vocabulary — after lowercasing and punctuation removal — contains 87,000 unique words. The lead data scientist wants to set `num_words=5000` to keep the model small and fast, arguing that the top 5,000 most frequent words capture all the discriminative signal needed. A junior engineer disagrees, pointing out that financial domain terms like "arbitration," "escrow," and "collateralized" are low-frequency but highly predictive of specific routing categories. The junior engineer advocates for `num_words=30000` and a larger embedding dimension of 128.

Respond to the following in 175–225 words:

Who has the stronger technical argument, and why? Describe specifically how `num_words` affects the behavior of the `Tokenizer` and what happens to low-frequency domain terms when `num_words` is set too small. If you were leading this project, what `num_words` value would you choose and why? How would you empirically validate your choice?

---

## Scenario 2 — Legacy Pipeline vs. Portable Model

A data science team at a healthcare company trained a clinical notes classifier using `Tokenizer`, `pad_sequences`, and a Sequential model with an `Embedding` layer. The model achieves 91% accuracy on the validation set. When they hand it off to the deployment team, the deployment engineer discovers that the model file alone does not contain the tokenizer — it was saved separately as a JSON file using `tokenizer_to_json()`. During a subsequent model update, a teammate retrained the model with different `num_words` settings and forgot to re-export the tokenizer JSON. The result was that the deployed inference service was using the old tokenizer vocabulary with the new model weights, producing silent garbage predictions for six hours before the error was caught.

Respond to the following in 175–225 words:

Explain precisely why this failure occurred — what is the technical incompatibility between the old tokenizer and the new model? What architectural change (covered in Module 09) would have prevented this failure entirely? Write a two-sentence description of the preventive pattern, naming the specific Keras API. What organizational process change would you also recommend to prevent this class of error in the future?

---

## Scenario 3 — Choosing the Right Encoder

A startup is building three different NLP products simultaneously and has limited GPU compute:

Product A — Spam detection for short SMS messages (average 12 words per message, binary label).

Product B — Legal contract clause classification (average 350 words per clause, 8 mutually exclusive categories).

Product C — Real-time comment toxicity detection that must return a result within 50 milliseconds on a CPU server.

The team wants to use a single architecture for all three products to minimize engineering complexity. They are debating between: (1) `Embedding` + `GlobalAveragePooling1D` + `Dense`, and (2) `Embedding` + `Bidirectional LSTM` + `Dense`.

Respond to the following in 175–225 words:

Is a single architecture the right call for all three products? For each product, identify which encoder (`GlobalAveragePooling1D` or Bidirectional LSTM) you would recommend and justify your choice based on the sequence length, label type, and latency constraint. For Product C, what specific steps beyond model architecture could you take to meet the 50-millisecond latency requirement?

---

## Peer Response Guidelines

When responding to a classmate, go beyond agreement. You must do at least one of the following:

- Challenge a specific technical claim with evidence or a counter-example.
- Offer a concrete Keras code snippet (no more than 5 lines) that demonstrates an alternative approach.
- Draw a parallel to a different NLP domain (legal, medical, social media, code review) where their recommendation would or would not apply.

---

## Grading Rubric — 10 Points Total

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted on time | 1 | Posted by Wednesday 11:59 PM |
| Addresses all three prompt questions | 2 | All sub-questions answered with relevant detail |
| Technical accuracy | 2 | Correct use of TF/Keras API names and NLP concepts from Module 09 |
| Depth of analysis | 2 | Goes beyond surface-level description; explains the "why" |
| Word count (175–225 words) | 1 | Within the specified range |
| Peer response 1 (substantive, 60+ words) | 1 | Adds new idea, code, or counter-example |
| Peer response 2 (substantive, 60+ words) | 1 | Adds new idea, code, or counter-example |
| **Total** | **10** | |

---

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.
