# Discussion: Module 09 — Big Data Technologies

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 10 (6 initial post + 4 peer responses)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 1: Data Concepts and Environments

---

## Instructions

Choose ONE of the three scenarios below and write an initial post of 175–225 words. Then respond substantively to at least TWO classmates who chose different scenarios. Peer responses must be at least 75 words — extend the analysis, ask a probing question, or offer an alternative approach.

Initial posts are due by Thursday at 11:59 PM. Peer responses are due by Sunday at 11:59 PM.

---

## Scenario A: The Media Streaming Platform

A video streaming company has 80 million monthly active users. Every time a user plays, pauses, skips, searches, or rates a video, an event is logged. This generates approximately 4 billion events per day — roughly 320 TB of raw JSON log data. The data engineering team must design a storage and processing architecture to support three use cases simultaneously:

- A recommendation engine that must re-rank a user's personalized feed within 500 milliseconds of each viewing action
- A weekly content performance report used by studio executives to evaluate show renewals
- A data science team that experiments with new recommendation algorithms by training models on 12 months of historical viewing behavior

In your initial post, address the following:

- Which of the 5 V's are most relevant to this company's data challenges? Identify at least two and explain how each one specifically manifests in this scenario.
- Should this company use a data lake, a data warehouse, or a data lakehouse as its primary storage architecture? Justify your recommendation by explaining how it serves all three use cases — not just the dominant one.
- The 500-millisecond recommendation requirement means batch processing is insufficient for one component of this system. Explain what streaming technology would handle this, and describe how it would coexist with batch processing in the same overall architecture (hint: think lambda or kappa).

---

## Scenario B: The Public Utility Grid

A regional electric utility monitors 2.4 million smart meters that transmit readings every 15 minutes. Each reading includes meter ID, timestamp, kilowatt-hours consumed, voltage level, and any fault codes. The utility's existing Oracle database is struggling to handle the insert volume and the analytical queries simultaneously, causing reporting delays and data loss during peak transmission windows.

The utility's IT director asks the analytics team to evaluate Apache Hadoop and Apache Spark as replacement technologies. The IT director has a traditional database background and is skeptical: "We already have a perfectly good database. Why do we need a completely different system?"

In your initial post, address the following:

- Explain, in language appropriate for a non-technical IT director, why a traditional relational database is architecturally limited for this workload. Reference at least one specific characteristic of the 5 V's to justify why a distributed system is needed.
- Compare HDFS and a traditional disk-based database in terms of how each handles node failure. What would happen to the utility's meter readings if a traditional database server failed vs. an HDFS DataNode?
- The utility runs monthly usage reports for billing that require joining 18 months of meter history — roughly 6 billion rows. Should this use MapReduce, Hive, or Apache Spark? Justify your choice, and explain the trade-off you are making by choosing it over the alternatives.

---

## Scenario C: The National Retailer Data Strategy

A national retail chain with 1,400 stores is consolidating its data infrastructure. Currently, data exists in three separate systems: a transactional SQL database for point-of-sale data, a marketing platform with customer behavioral data in CSV and JSON formats, and a supply chain system with XML shipment records. The Chief Data Officer wants a single unified platform where analysts can query all three sources together, data scientists can train machine learning models on raw historical data, and the BI team can produce governed, certified metrics for board presentations.

A vendor is proposing a data lake solution. A second vendor is proposing a data warehouse. A third vendor is proposing a data lakehouse.

In your initial post, address the following:

- The CDO's requirements span three different user groups with different needs. Map each user group (analysts, data scientists, BI team) to the storage architecture most suited to their specific requirements. Does one architecture satisfy all three groups, or do different groups need different approaches?
- The data lake vendor warns that "a data lake gives you maximum flexibility." The data warehouse vendor warns that "a data lake will become a data swamp within 18 months." Who is more correct for this organization's situation, and what specific governance practices would determine whether the data lake vendor's prediction or the data warehouse vendor's warning comes true?
- The CDO asks whether batch processing or streaming processing is appropriate for a use case where inventory levels must be visible to store managers within 5 minutes of a sale completing. Justify your recommendation and identify what the latency trade-off would be if the organization chose the opposite approach.

---

## Peer Response Guidelines

When responding to classmates, consider:

- Did they correctly identify the relevant V's for the scenario?
- Did they accurately describe the data lake vs. data warehouse trade-offs?
- Did they match the processing paradigm (batch vs. streaming) to the latency requirement?
- Is there a technology, governance practice, or architectural trade-off they overlooked?

---

## Grading Rubric (10 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Technical accuracy | 3 | Correct application of big data concepts, architectures, and processing paradigms |
| Scenario-specific reasoning | 2 | Recommendations tied to specific requirements in the scenario |
| Depth of analysis | 2 | Addresses trade-offs and limitations, not just definitions |
| Peer response quality | 2 | Substantive engagement; extends the analysis or challenges assumptions |
| Writing clarity | 1 | Clear, organized, professional; within word count |

---

## Professor Nash Note

Big data architecture decisions are among the most expensive and long-lasting choices an organization makes. A poorly chosen architecture can cost millions to correct. The scenarios here reflect real decisions made at real companies — and in each case, the right answer depends on understanding the specific requirements, not just knowing which technology sounds most impressive. As you write and respond, resist the temptation to say "use Spark for everything" — instead, demonstrate that you understand when the complexity of distributed systems is warranted and when it is not.

---

End of Module 09 Discussion
