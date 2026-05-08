### 4. Lab 3: Generating and Exchanging Keys
**Objective:** Use GPG to generate asymmetric key pairs, export public keys, and encrypt a message.
**Instructions:**
1. Boot your Kali Linux VM.
2. Open a terminal and generate a new GPG key pair: `gpg --full-generate-key` (Select RSA, 2048 bit, and enter your details).
3. Export your public key to an armor-encoded file: `gpg --armor --export your.email@txwes.edu > public.key`
4. Exchange `public.key` files with a lab partner (or simulate by creating a second user).
5. Import your partner's public key: `gpg --import partner_public.key`
6. Encrypt a text file using their public key: `gpg --encrypt --recipient partner.email@txwes.edu secret.txt`
**Deliverable:** Take a screenshot of the terminal output showing the successful encryption of `secret.txt` resulting in the `secret.txt.gpg` file. Submit to Blackboard.

---
