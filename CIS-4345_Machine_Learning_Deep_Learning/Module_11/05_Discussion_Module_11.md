# Discussion Forum: Module 11 — Transfer Learning and Fine-Tuning

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Forum Instructions

Read all three scenarios below. Choose **one scenario** to respond to in your initial post. Your initial post must be 175–225 words and directly address the scenario prompt. Then reply to at least **one peer** who chose a different scenario with a substantive response of 60 or more words.

Initial posts are due by **Thursday at 11:59 PM**. Peer responses are due by **Sunday at 11:59 PM**.

---

## Scenario A — Choosing the Right Pretrained Model for a Specific Deployment

A startup is building a mobile app that identifies 50 species of birds from photos taken on a smartphone. The app must run inference on-device (iOS and Android) without sending images to a server. The team has collected 300 labeled photos per species (15,000 total). They are debating between three architectures: VGG16, ResNet50, and MobileNetV2.

The lead developer argues for ResNet50 because "it has the best accuracy-to-parameter ratio." The mobile engineer argues for MobileNetV2 because "the model needs to fit on a phone and run in under 200 milliseconds." A third team member suggests they should evaluate all three with a quick feature extraction experiment before committing.

Respond to the following: Which architecture would you recommend for this specific use case, and what is your reasoning? How does the on-device deployment constraint change the decision compared to a server-side deployment? Is the third team member's evaluation suggestion worth the time given the team's data volume and constraints? What transfer learning strategy (feature extraction only vs. fine-tuning) would you recommend for 300 images per class?

### Sample Response — Scenario A

For on-device mobile deployment with 15,000 training images and a 200-millisecond inference budget, I would recommend MobileNetV2. The mobile engineer's argument is correct and decisive here. VGG16 at 528 MB is simply not viable for a mobile app — it exceeds the recommended model size for on-device inference on most smartphones, and its inference speed on mobile CPUs is too slow. ResNet50 at 98 MB is borderline, but MobileNetV2 at 14 MB is specifically designed for exactly this constraint.

The on-device deployment requirement is a hard constraint, not a preference. Server-side deployment would open the door to ResNet50 or even EfficientNet variants without any size concerns. On-device changes the decision fundamentally.

The third team member's evaluation suggestion is worthwhile but should be time-boxed. A quick feature extraction experiment across all three architectures — train just the head for 5 epochs each — takes perhaps two hours and gives empirical accuracy data for this specific bird dataset. Bird photography differs enough from generic ImageNet images (lighting, background clutter, similar fine-grained categories) that the accuracy ordering may not match the ImageNet benchmark rankings.

For 300 images per class, I would start with feature extraction only. Fine-tuning the last 10–15 layers of MobileNetV2 could then be attempted as a second phase if accuracy does not meet the product requirement.

---

## Scenario B — Diagnosing Poor Fine-Tuning Results

A data scientist fine-tunes VGG16 on a satellite image classification task with 8 classes and 2,000 images per class (16,000 total). After Phase 1 feature extraction, validation accuracy reaches 87%. She then runs Phase 2 fine-tuning by unfreezing all 19 convolutional layers at once and training with the same learning rate she used in Phase 1 (`1e-3`). After 10 epochs of fine-tuning, validation accuracy has dropped to 61% — worse than a simpler baseline she tested earlier.

She is confused because she expected fine-tuning to improve on Phase 1. She asks her team: "Did I do something wrong, or does fine-tuning just not work for satellite images?"

Respond to the following: What went wrong, and what specific changes would you make to her fine-tuning procedure? In what order would you apply those changes? Why does fine-tuning sometimes make things worse rather than better? Is there a general principle for deciding how many layers to unfreeze and at what learning rate?

### Sample Response — Scenario B

The data scientist encountered catastrophic forgetting — the most common fine-tuning failure mode. Using the same `1e-3` learning rate for Phase 2 that she used for Phase 1 produced gradient updates large enough to overwrite VGG16's pretrained weights within the first few epochs. By epoch 10, the convolutional layers contained essentially random weights relative to the ImageNet features, and 16,000 examples were insufficient to re-learn those representations from scratch. The drop from 87% to 61% is the signature of this failure.

I would make three specific changes in this order. First, reduce the learning rate to `1e-5` — approximately 100 times smaller than the Phase 1 rate. This is the single most impactful fix and should be applied before anything else. Second, avoid unfreezing all 19 layers at once. Start by unfreezing only the last 4 convolutional layers (block5 in VGG16), which are the most task-specific. Early layers encode generic edges and textures that transfer well without modification. Third, add `EarlyStopping` with `restore_best_weights=True` and a patience of 5 to prevent the model from drifting past its validation peak.

The general principle: unfreeze from the top down, use learning rates 10–100x smaller than the head phase, and freeze more aggressively when the dataset is small or domain-distant from ImageNet.

---

## Scenario C — Transfer Learning Across Domains

A hospital research team wants to use transfer learning to classify histopathology slides (microscope images of tissue samples) into malignant and benign categories. They have 800 labeled slides per class. A radiologist on the team is skeptical: "These microscopy images look nothing like the natural photos in ImageNet. How can features trained on dogs and cars help classify cancer cells?"

A deep learning researcher responds: "Transfer learning works even across very different domains because early CNN layers learn universal features that are useful everywhere."

Both make reasonable points. The reality is nuanced.

Respond to the following: Who is more correct, and under what conditions? What does the research literature say about transfer learning to medical imaging domains? How would you design the transfer learning strategy (which model, how many layers to freeze, what learning rate) given the domain difference and the dataset size? What would you do differently if the team had 10,000 labeled slides instead of 1,600?

### Sample Response — Scenario C

Both the radiologist and the researcher make valid points, and the research literature supports a nuanced position closer to the researcher's. Studies by Raghu et al. (2019) and Tajbakhsh et al. (2016) demonstrated that ImageNet pretrained weights consistently outperform random initialization on medical imaging tasks, even with apparent domain mismatch. The reason is precisely what the researcher said: early convolutional layers learn edge detectors and texture filters that are genuinely universal — they detect boundaries and patterns in histopathology slides just as in natural photos.

However, the radiologist's skepticism is not entirely wrong. Domain gap is real. The deeper layers of a model pretrained on ImageNet encode high-level features tied to natural image objects — "fur texture," "wheel shape" — that do not exist in microscopy. These deeper layers need more adaptation than in a natural-image fine-tuning scenario.

My strategy for 800 slides per class: use MobileNetV2 or ResNet50, freeze all but the last 10–15 layers in Phase 2 fine-tuning, use learning rate `5e-6`, and apply strong augmentation (rotation up to 90 degrees, vertical flips, color jitter) since histopathology slides can appear in any orientation.

With 10,000 slides per class, I would unfreeze more aggressively — perhaps the last 30–40% of layers — and use a slightly higher fine-tuning learning rate of `1e-5`. The additional data can support meaningful adaptation of the mid-level features while still benefiting from the generic early-layer features.

---

## Peer Response Examples

### Peer Response to Scenario A (63 words)

You made a strong case for MobileNetV2, and I agree with the on-device constraint being decisive. I want to add one consideration you did not mention: MobileNetV2 also integrates natively with TensorFlow Lite, which is the standard pipeline for deploying TF models to iOS and Android. That ecosystem support is another practical argument for MobileNetV2 beyond just model size and inference speed.

### Peer Response to Scenario B (61 words)

Your diagnosis is correct, but I would add one more fix to your list: after applying the low learning rate, consider training for more epochs with a longer EarlyStopping patience. In my own experience with VGG16 fine-tuning, the improvement from fine-tuning can be slow to appear — validation accuracy sometimes dips slightly for the first 3–4 epochs before recovering. Short patience can terminate training prematurely.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post is 175–225 words (counted) | 2 |
| Addresses all parts of the chosen scenario prompt | 3 |
| Demonstrates accurate understanding of transfer learning concepts from Module 11 | 3 |
| Peer response is 60 or more words and adds substantive new content | 2 |
| **Total** | **10** |

---

## Professor Nash — Discussion Note

Scenario C reflects one of the most active areas of applied deep learning research right now — medical imaging AI. The question of how much pretrained features transfer across domains is not just academic: it directly affects whether smaller hospitals with limited labeled data can deploy effective diagnostic tools.

Scenario B is worth studying carefully because catastrophic forgetting is a mistake I have seen made repeatedly by engineers who learned fine-tuning from a quick tutorial and missed the learning rate nuance. The difference between `1e-3` and `1e-5` is not a small detail — it is the difference between fine-tuning working and not working.

Strong responses to any of these scenarios will demonstrate that you understand the *mechanism* behind the recommendations, not just the rules. Anyone can memorize "use a low learning rate for fine-tuning." I want to see that you understand why.

---

*End of Discussion Forum — Module 11*
