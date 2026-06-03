# Discussion Forum: Module 05 — TensorFlow and Keras Fundamentals

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Instructions

Post your **initial response** to one of the three scenarios below by **Wednesday at 11:59 PM**. Your initial post must be **175–225 words** written in complete sentences. Respond to **at least two classmates** by **Sunday at 11:59 PM** with a minimum of **60 words each**. Peer responses must add substance — extend the argument, propose an alternative design, or connect the idea to a different application domain.

---

## Scenario A — Sequential vs. Functional in a Real System

A team of data scientists at a health insurance company is building a risk scoring model. The model must combine two separate data streams: structured claims history (45 numeric features) and demographic data (12 numeric features). They want to process each stream through its own hidden layer before combining them, then pass the merged representation through two more layers to predict a binary risk score.

One team member argues they should use the Sequential API because it is simpler and faster to write. Another says the Sequential API cannot express this architecture at all.

Evaluate both positions. Explain precisely why one of them is correct using the specific limitations of the Sequential API. Describe how you would construct this model using the Functional API, naming the specific Keras layer type you would use to merge the two streams and explaining why you chose it over alternatives. Your response should demonstrate understanding of the architectural difference between the two APIs, not just restate their definitions.

---

## Scenario B — Tensor Shape Debugging

A junior developer on your team submits the following code for code review. They report it raises a shape error at the `tf.matmul` line but they cannot figure out why.

```python
features = tf.constant([[1.0, 2.0, 3.0],
                         [4.0, 5.0, 6.0]])   # shape (2, 3)
weights = tf.constant([[0.1, 0.2],
                        [0.3, 0.4],
                        [0.5, 0.6]])           # shape (3, 2)
bias = tf.constant([0.1, 0.2, 0.3])           # shape (3,)
result = tf.matmul(features, weights) + bias
```

Identify all errors in this code — there may be more than one. For each error, explain what the shape mismatch is, why it causes a failure, and provide the corrected line. Then explain the general rule for matrix multiplication shape compatibility that a developer should memorize to avoid this class of error. Your response should be specific enough that the junior developer could fix their code and understand why it was wrong.

---

## Scenario C — Model Compilation Trade-offs

A data science intern at a retail company is building a product recommendation model. The model predicts which of 200 product categories a customer is most likely to purchase next. The training labels are stored as integers from 0 to 199. The intern writes this compilation call:

```python
model.compile(
    optimizer='sgd',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```

A senior engineer reviews the code and flags two problems. Identify both problems, explain precisely why each is wrong for this use case, and write the corrected `model.compile()` call. Then explain your optimizer choice: is `'adam'` always better than `'sgd'` for every problem, or are there situations where SGD is preferable? Support your position with at least one concrete reason.

---

## Peer Response Requirements

Your two peer responses must each:

- Be at least 60 words in complete sentences
- Add a new perspective, counterexample, or alternative approach — not just agreement
- Reference a specific technical concept from this module (tensor shapes, API differences, compilation, or model architecture)

Responses that only say "Great explanation" or summarize what the peer already wrote receive no credit.

---

## Grading Rubric (10 Points Total)

| Criterion | Points |
|---|---|
| Initial post is 175–225 words in complete sentences | 1 |
| All errors or design choices identified correctly | 2 |
| Technical explanation is accurate and uses correct terminology | 3 |
| Response connects concepts to the practical scenario | 2 |
| Two peer responses of 60+ words with substantive new content | 2 |
| **Total** | **10** |

---

## Professor Nash — Closing Note

Scenario B is the kind of problem you will hit within the first hour of writing TensorFlow code — and it trips up experienced developers just as often as beginners. Learning to read shape errors methodically, rather than guessing, is one of the most valuable debugging skills in deep learning.

Scenario A matters because the architecture decision you make at the start of a project is much harder to change later. Choosing the wrong API because you were in a hurry is a debt you pay back slowly across the entire project lifecycle.

Scenario C highlights that model compilation is not a formality — the wrong loss function will silently train a broken model, and you will not know until you see inexplicably bad validation performance. Developing the habit of verifying your compile call is as important as verifying your architecture.

Read what your classmates wrote carefully. The scenarios were designed to have multiple defensible approaches, and you will often learn more from someone who solved the same problem differently than from any lecture slide.
