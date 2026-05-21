# Quiz: Module 14 - Generative Models: GANs and VAEs
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
In a Generative Adversarial Network, what is the role of the Generator and how does it receive training signal?
*   A) The generator classifies input images as real or fake and sends that classification label back to the discriminator as a training signal.
*   B) The generator produces synthetic samples from random noise and is trained by trying to maximize the discriminator's error — it improves when the discriminator incorrectly labels its outputs as real.
*   C) The generator compresses real training images into a compact latent representation and is trained by minimizing reconstruction loss against the original images.
*   D) The generator selects the most representative samples from the training set and passes them to the discriminator, which learns to generalize from those hard examples.
*   **Correct Answer:** B) The generator never sees real data directly. Its only feedback comes from the discriminator — when the discriminator correctly identifies a fake, the generator's loss is high. The generator gradient-descends to produce samples that increasingly fool the discriminator into outputting a "real" label.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Classification of real vs. fake is the discriminator's role, not the generator's. The generator only produces samples; it does not evaluate anything.
    *   *Why B is correct:* In the GAN training loop: (1) train discriminator on real samples (label=1) and generator fakes (label=0); (2) train generator by passing its fakes through the discriminator and computing loss as if the fakes were labeled real. Implemented with two separate `tf.GradientTape()` contexts.
    *   *Why C is incorrect:* This describes an Autoencoder or VAE encoder — compressing real images to a latent representation is a fundamentally different architecture. The GAN generator does the opposite: it maps from latent noise to images.
    *   *Why D is incorrect:* The generator creates entirely new synthetic samples from random noise — it does not select or curate from the training set.

---

**Question 2**
Which of the following is the most accurate definition of a **Variational Autoencoder (VAE)**?
*   A) A two-network adversarial system where a generator produces fake images and a discriminator tries to detect them, trained simultaneously until the generator produces photorealistic outputs.
*   B) A generative model with an encoder that maps input data to a probability distribution (mean and variance) in a latent space, and a decoder that reconstructs data from samples drawn from that distribution — enabling smooth interpolation and new sample generation.
*   C) A dimensionality reduction technique that projects high-dimensional data onto the two or three principal components that explain the most variance, used to visualize embedding clusters.
*   D) A sequence-to-sequence model that encodes an input sequence with an LSTM and decodes it into an output sequence of different length, used for machine translation tasks.
*   **Correct Answer:** B) Unlike a standard autoencoder (which maps inputs to fixed latent vectors), a VAE maps inputs to distributions. The reparameterization trick — `z = μ + σ * ε` where `ε ~ N(0,1)` — makes sampling differentiable so backpropagation can train the encoder. This gives the latent space smooth, continuous structure suitable for generation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a GAN, not a VAE. GANs use adversarial training between a generator and discriminator; VAEs use a single encoder-decoder with a KL divergence regularization term.
    *   *Why B is correct:* VAE loss = reconstruction loss + KL divergence penalty. The KL divergence term forces the learned latent distribution to stay close to a standard Gaussian, which enables new sample generation by sampling from N(0,1) and decoding.
    *   *Why C is incorrect:* This describes PCA (Principal Component Analysis), an unsupervised linear dimensionality reduction method — conceptually related to representation learning but architecturally unrelated to VAEs.
    *   *Why D is incorrect:* This describes a sequence-to-sequence (seq2seq) model used in NLP. The encoder-decoder terminology overlaps, but seq2seq models are not generative in the probabilistic sense and do not learn a latent space distribution.

---

**Question 3**
Why do GANs require a custom training loop with `tf.GradientTape()` instead of the standard `model.fit()` API?
*   A) `model.fit()` does not support binary cross-entropy loss, which is required for the GAN discriminator's real/fake classification objective.
*   B) GANs involve two networks with separate loss functions that must be updated alternately — the discriminator is updated first on real and fake samples, then the generator is updated by treating its outputs as if they were real. This two-stage update cannot be expressed as a single `model.compile()`/`model.fit()` call.
*   C) `model.fit()` automatically shuffles training data, which would destroy the temporal ordering that GANs require to generate sequential image frames.
*   D) `tf.GradientTape()` trains faster than `model.fit()` because it bypasses Python overhead in the Keras training loop, which is necessary for GAN convergence within a reasonable training time.
*   **Correct Answer:** B) In each training step, the discriminator must be trained on real samples (label=1) and the generator's fakes (label=0) — updating discriminator weights. Then the generator must be trained by generating new fakes, passing them through the frozen discriminator, and minimizing the loss as if they were real — updating only generator weights. Two separate gradient computations and two separate `optimizer.apply_gradients()` calls are required.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `model.fit()` fully supports `loss='binary_crossentropy'`. The limitation is not the loss function but the need for alternating two-network updates within a single training step.
    *   *Why B is correct:* The custom loop: `with tf.GradientTape() as disc_tape: disc_loss = ...` then `disc_optimizer.apply_gradients(...)` — followed by `with tf.GradientTape() as gen_tape: gen_loss = ...` then `gen_optimizer.apply_gradients(...)`. This is the standard TF GAN training pattern.
    *   *Why C is incorrect:* GANs do not require temporally ordered batches — they are trained on static image datasets. The need for a custom loop has nothing to do with data ordering.
    *   *Why D is incorrect:* Performance is not the reason — `model.fit()` compiles to XLA and is highly optimized. The custom loop is needed for architectural reasons (alternating updates), not speed.

---

**Question 4**
What is "mode collapse" in GAN training, and which symptom most clearly identifies it?
*   A) The discriminator's loss drops to zero because it becomes too strong and the generator cannot produce good enough fakes to fool it — training is stuck.
*   B) The generator produces only a narrow set of very similar outputs (or a single output), failing to cover the diversity of the training distribution — all generated samples look nearly identical regardless of the input noise.
*   C) The GAN training loop crashes with a NaN loss because the learning rate is too high, causing gradient explosion in the generator's transposed convolution layers.
*   D) Both the generator and discriminator losses oscillate between 0 and 1 without converging, indicating that the two networks are perfectly balanced and no further training is needed.
*   **Correct Answer:** B) Mode collapse occurs when the generator discovers one or a few outputs that reliably fool the discriminator and exploits them repeatedly. The generator ignores most of the latent space. Visual symptom: all generated images look nearly identical. Mitigation strategies include using Wasserstein GAN loss, minibatch discrimination, or reducing the discriminator learning rate relative to the generator.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A discriminator that becomes too strong (discriminator loss → 0) is a related but distinct problem — the generator receives near-zero gradient and cannot improve. This is "discriminator dominance," not mode collapse, though both can stall training.
    *   *Why B is correct:* Mode collapse is diagnosed by inspecting generated samples for diversity. If 100 different noise vectors all produce nearly the same output, mode collapse has occurred. The generator has collapsed its output distribution to a single mode.
    *   *Why C is incorrect:* NaN loss from gradient explosion is a numerical stability issue unrelated to mode collapse. It is addressed with gradient clipping (`clipnorm` or `clipvalue` in the optimizer), not by addressing output diversity.
    *   *Why D is incorrect:* Oscillating losses in a GAN are often normal during training — the discriminator and generator are competing, so their losses naturally fluctuate. Oscillation is not the defining symptom of mode collapse.

---

**Question 5**
What is the purpose of the KL divergence term in the VAE loss function?
*   A) It measures how well the decoder reconstructs the original input by computing the pixel-wise difference between the input and the decoded output.
*   B) It penalizes the encoder for producing a latent distribution that deviates from a standard Gaussian — this regularization forces the latent space to be continuous and well-organized, enabling new sample generation by sampling from N(0,1).
*   C) It measures the adversarial distance between the generator's output distribution and the training data distribution, replacing binary cross-entropy in Wasserstein GANs.
*   D) It computes the gradient norm of the decoder network to detect and prevent vanishing gradients in the VAE's deep decoding layers.
*   **Correct Answer:** B) Without the KL divergence term, the encoder learns arbitrary latent distributions with no structure — the latent space has "holes" where decoding produces garbage. KL divergence forces the learned distribution to stay close to N(0,1), ensuring that any point sampled from the latent space at inference time decodes to a valid, meaningful output.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Reconstruction quality is measured by the reconstruction loss term (typically binary cross-entropy or MSE between input and decoded output). KL divergence is the regularization term, not the reconstruction term — the VAE total loss is reconstruction_loss + β * KL_divergence.
    *   *Why B is correct:* KL divergence between the encoder's output distribution N(μ, σ²) and the prior N(0,1) is: `KL = -0.5 * sum(1 + log(σ²) - μ² - σ²)`. At inference, you can generate new samples by sampling `z ~ N(0,1)` and passing through the decoder because the training KL term has aligned the latent space with this prior.
    *   *Why C is incorrect:* This describes the Wasserstein distance used in Wasserstein GANs (WGANs), not VAE KL divergence. These are entirely different models using different loss functions.
    *   *Why D is incorrect:* Gradient norms and vanishing gradient detection are not part of the VAE loss function. KL divergence is a probability-theoretic measure of distribution similarity, not a gradient diagnostic.
