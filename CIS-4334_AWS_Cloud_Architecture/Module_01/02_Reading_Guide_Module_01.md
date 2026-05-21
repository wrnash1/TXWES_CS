# Reading Guide: Module 01 - AWS Global Infrastructure and Core Services Overview
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 01 - AWS Global Infrastructure and Core Services Overview**! This module establishes the physical and logical foundation of the AWS cloud platform. You will learn how AWS organizes its global network of data centers, how fault isolation works between geographic zones, and how core AWS services are categorized. This knowledge underpins every architectural decision you will make for the SAA-C03 exam and in professional practice.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **AWS Regions**: A geographic area containing two or more Availability Zones. Each Region is physically isolated from other Regions and has completely independent power, networking, and connectivity. When designing for global fault tolerance, you choose which Region(s) to deploy workloads in based on latency, data residency, and service availability.

*   **Availability Zones (AZs)**: One or more discrete data centers within a Region, each with redundant power, networking, and cooling, connected to other AZs in the same Region via high-bandwidth, low-latency fiber links. AZs are physically separated far enough apart to minimize correlated failures while remaining close enough for synchronous replication. Deploying across multiple AZs is the primary strategy for high availability within a Region.

*   **Edge Locations**: AWS Points of Presence (PoPs) distributed globally that are used by services such as Amazon CloudFront and Route 53 to cache content and answer DNS queries as close to end users as possible. There are significantly more Edge Locations than Regions, enabling low-latency content delivery worldwide.

*   **AWS Global Infrastructure**: The complete worldwide network of Regions, Availability Zones, Local Zones, Wavelength Zones, and Edge Locations. This distributed infrastructure allows architects to design systems that are highly available, fault tolerant, and low latency for users anywhere in the world.

*   **Shared Responsibility Model**: The AWS security framework that divides security obligations between AWS and the customer. AWS is responsible for security "of" the cloud (physical hardware, hypervisor, managed service infrastructure), while customers are responsible for security "in" the cloud (operating system patches, application code, IAM configuration, data encryption). Understanding this boundary is essential for both the SAA-C03 exam and real-world compliance.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Coverage:** The exam is divided into four domains — Design Secure Architectures (30%), Design Resilient Architectures (26%), Design High-Performing Architectures (24%), and Design Cost-Optimized Architectures (20%). Global infrastructure knowledge is foundational to all four.

*   **AZ vs. Region Trap:** The exam frequently asks whether a solution achieves "high availability" or "fault tolerance." Deploying across multiple AZs in one Region provides high availability but not full regional fault tolerance. For disaster recovery, you must deploy across multiple Regions. Know the difference.

*   **Shared Responsibility Exam Trap:** Questions about "who is responsible for patching the guest OS on an EC2 instance" always point to the customer. AWS patches the underlying hypervisor. For managed services like RDS, AWS patches the database engine — but the customer still controls encryption keys, IAM permissions, and network access.

*   **Local Zones vs. Wavelength Zones:** Local Zones extend AWS infrastructure to metro areas for single-digit millisecond latency. Wavelength Zones embed AWS compute inside 5G carrier networks. Know which use case each solves — the exam tests scenario-based selection.

*   **Study Resource:** The AWS Global Infrastructure overview explains Region and AZ design principles relevant to SAA-C03: [AWS Global Infrastructure Overview](https://aws.amazon.com/about-aws/global-infrastructure/). The AWS Shared Responsibility Model whitepaper is required reading: [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Review the AWS Shared Responsibility Model and Global Infrastructure sections in the AWS documentation and whitepapers. The AWS Whitepapers portal contains the official "Overview of Amazon Web Services" document that describes all core service categories: [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/). Search for "Overview of Amazon Web Services" to find the foundational whitepaper.

*   **Required Video:** Watch the AWS SAA-C03 foundations lecture covering global infrastructure, AZs, and the Shared Responsibility Model in the official course playlist: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s). Pay particular attention to the segments on Region selection criteria and fault isolation boundaries.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Inspect global AWS Availability Zones using the AWS CLI:** Run `aws ec2 describe-availability-zones --region us-east-1` to list all AZs in a Region and observe their state and zone IDs.

*   **Locate regional service availability:** Use the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) to identify which services are available in which Regions and consider how that affects architecture decisions.

*   **Map out a multi-AZ service architecture:** Sketch a simple 3-tier web application (load balancer, EC2, RDS) deployed across two AZs and identify which components the customer manages vs. which AWS manages per the Shared Responsibility Model.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Review the AWS Shared Responsibility Model page at [https://aws.amazon.com/compliance/shared-responsibility-model/](https://aws.amazon.com/compliance/shared-responsibility-model/).
- [ ] Read the "Overview of Amazon Web Services" whitepaper at [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/).
- [ ] Watch the video lecture on AWS Global Infrastructure in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab exploring Regions and AZs.
- [ ] Proceed to the weekly quiz.
