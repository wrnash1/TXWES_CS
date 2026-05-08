### 2. Reading Guide: Scaling Spanner
**High-Yield Concepts:** 
*   **Nodes vs. Processing Units:** You scale Spanner by adding compute capacity. 1 Node = 1000 Processing Units.
*   **Interleaving Tables:** A physical schema design technique in Spanner where child rows are stored physically adjacent to parent rows on the hard drive, massively speeding up JOIN queries.
