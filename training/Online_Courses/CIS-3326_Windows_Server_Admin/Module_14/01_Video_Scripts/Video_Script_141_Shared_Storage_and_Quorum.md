**Video Script 14.1: Shared Storage and Quorum**
*Audio:* "To ensure a database never goes down, we cluster servers. Two physical servers connect to the same SAN storage. If Node A crashes, Node B instantly takes over the IP address and storage disk. To prevent 'Split Brain' (where both nodes think they are in charge), we use a Quorum witness."
