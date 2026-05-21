# Reading Guide: Module 12 - Cloud Analytics – AWS Athena, Google BigQuery
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 12 - Cloud Analytics: AWS Athena and Google BigQuery**! Cloud analytics platforms have fundamentally changed how organizations analyze large datasets — eliminating the need to provision and maintain dedicated database servers and enabling analysts to query terabytes of data stored in object storage using standard SQL. This module covers the cloud analytics concepts tested on the **CompTIA Data+** exam: cloud storage and compute separation, serverless query execution, scalability on demand, and the shared responsibility model for data security in the cloud.

Understanding cloud analytics is essential for any modern analyst role. Most enterprise data teams now run analytics on cloud-native platforms, and the Data+ exam specifically tests your knowledge of how cloud environments differ from on-premises systems and what responsibilities shift to the customer under cloud service models.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cloud service models (IaaS, PaaS, SaaS)**: Infrastructure as a Service (IaaS) provides raw compute, storage, and networking — the customer manages the OS, middleware, and applications (e.g., AWS EC2). Platform as a Service (PaaS) provides a managed platform where the customer deploys applications without managing the underlying infrastructure (e.g., Google Cloud Run). Software as a Service (SaaS) delivers fully managed software over the internet — the customer only manages data and user access (e.g., Salesforce, Google Sheets).
*   **Serverless query execution (AWS Athena and Google BigQuery)**: Serverless analytics services allow analysts to run SQL queries directly against files stored in object storage (Amazon S3 or Google Cloud Storage) without provisioning, managing, or scaling a database server. The platform automatically allocates compute resources for each query and charges based on the amount of data scanned. This separates storage cost from compute cost.
*   **Columnar storage and query performance**: Cloud analytical databases store data in columnar format — each column is stored contiguously on disk rather than each row. When a query accesses only two of twenty columns, the engine reads only those two columns, dramatically reducing I/O. Columnar storage is the reason BigQuery and Redshift are fast for analytical queries that aggregate a few columns across billions of rows.
*   **Shared responsibility model**: In cloud environments, security responsibilities are divided between the cloud provider and the customer. The provider secures the physical infrastructure, hypervisor, and network (security of the cloud). The customer is responsible for configuring access controls, encrypting data, managing user permissions, and protecting their data (security in the cloud). Misconfigured S3 buckets with public access are a classic example of customer-side responsibility failure.
*   **Scalability and elasticity**: Cloud platforms scale compute and storage independently on demand. Elasticity means resources are provisioned automatically when demand increases and released when it decreases — users are billed only for what they consume. This contrasts with on-premises infrastructure, where capacity must be provisioned in advance for peak load.

---

### 2. Certification Exam Tips
*   **Domain weight:** Cloud analytics concepts appear in Domain 2 (Data Collection and Management, ~25%) and Domain 4 (Analytics and Reporting, ~23%) of the Data+ DA0-001 exam. Questions about cloud service models, storage architecture, and the shared responsibility model are high-frequency.
*   **Exam trap — IaaS vs. PaaS vs. SaaS responsibilities:** The exam will describe a scenario and ask who is responsible for a specific component. IaaS: customer manages OS upward. PaaS: customer manages only the application and data. SaaS: customer manages only data and user access. The provider always owns physical infrastructure.
*   **Exam trap — serverless vs. server-based:** AWS Athena and Google BigQuery are serverless — no servers to provision or manage. The exam may contrast these with services like Amazon Redshift (a provisioned cluster) or traditional on-premises databases. If the question describes "no infrastructure to manage" and "pay per query," the answer is a serverless service.
*   **Exam trap — shared responsibility:** A data breach caused by an S3 bucket configured with public access is the customer's responsibility, not the cloud provider's. The provider secures the physical infrastructure; the customer configures access controls. The exam frequently tests this boundary.
*   **Study Resource:** The data engineering and cloud chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/) cover the conceptual foundations of cloud-scale data storage and querying. The [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) demonstrates loading and querying datasets in Python using patterns that parallel cloud SQL workflows in Athena and BigQuery.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the cloud computing and large-scale data chapters in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Focus on the sections covering cloud storage architectures, query execution at scale, and the separation of storage from compute.
*   **Required Video:** Watch the data engineering and cloud analytics sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238), which demonstrates querying large datasets using SQL-style operations in Python that mirror the experience of using BigQuery or Athena.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Classify a set of cloud services by model (IaaS, PaaS, SaaS)**: Given a list of six services (including EC2, BigQuery, Salesforce, and Cloud Run), identify which model each belongs to and explain what the customer is responsible for in each case.
*   **Write a SQL query for a serverless analytics scenario**: Given a description of a dataset stored as Parquet files in cloud object storage, write the SELECT statement that would retrieve total revenue by region, and estimate the cost impact of selecting only two columns vs. SELECT *.
*   **Identify shared responsibility violations**: Review three cloud configuration scenarios and classify each as provider responsibility, customer responsibility, or both — including a public S3 bucket, an unpatched hypervisor, and an unrotated encryption key.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the cloud computing chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.
