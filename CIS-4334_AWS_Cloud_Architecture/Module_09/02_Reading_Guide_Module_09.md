# Reading Guide: Module 09 - CloudFront, Route 53, and Global Acceleration
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 09 - CloudFront, Route 53, and Global Acceleration**! This module covers the AWS services that deliver content and route traffic globally with low latency. Amazon CloudFront is the AWS Content Delivery Network (CDN) that caches content at over 400 Points of Presence worldwide. Amazon Route 53 is the authoritative DNS service with advanced routing policies for high availability and geographic distribution. AWS Global Accelerator improves application performance by routing traffic through AWS's private global network rather than the public internet. These services are key components of high-availability and global-reach architectures on the SAA-C03 exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Amazon CloudFront**: A managed global CDN that caches copies of content (HTML, CSS, images, videos, API responses) at Edge Locations close to users, reducing origin server load and decreasing latency. CloudFront distributions can have multiple origins (S3 buckets, ALBs, custom HTTP origins). Cache behavior settings control which paths are cached, for how long (TTL), and which HTTP headers/cookies affect cache keys. CloudFront also provides DDoS protection via AWS Shield Standard at no extra cost, and integrates with AWS WAF for application-layer protection.

*   **Route 53 Routing Policies**: Route 53 supports seven routing policies for different traffic management needs. Simple: one record, one value. Weighted: distribute traffic proportionally across multiple endpoints (A/B testing, gradual migrations). Latency-Based: route to the Region with the lowest network latency for the client. Failover: primary and secondary endpoints with health check-based automatic failover. Geolocation: route based on the user's country or continent. Geoproximity: route based on geographic proximity with optional traffic bias. Multivalue Answer: return multiple healthy records for basic client-side load balancing.

*   **Route 53 Health Checks**: Monitors the health of endpoints (HTTP, HTTPS, TCP) and DNS failover targets. When a health check fails, Route 53 stops routing traffic to the unhealthy endpoint (for Failover routing) or adjusts weighted distributions. Health checks can also monitor CloudWatch alarms for calculated health states. Combining health checks with Failover routing is the AWS-native active-passive disaster recovery DNS pattern.

*   **AWS Global Accelerator**: A network-layer service that routes user traffic through the AWS global network (rather than the public internet) to the nearest AWS edge location, then over AWS's private backbone to the application endpoint. Global Accelerator provides two static Anycast IP addresses that serve as a fixed entry point for the application regardless of Region. It improves performance for TCP/UDP applications and provides automatic failover when an endpoint becomes unhealthy. Unlike CloudFront (which caches content), Global Accelerator does not cache — it improves network routing for dynamic, non-cacheable traffic.

*   **CloudFront Origin Access Control (OAC)**: A security mechanism that restricts direct S3 bucket access, ensuring that users can only retrieve S3 content through the CloudFront distribution (not by guessing the S3 URL). OAC replaces the older Origin Access Identity (OAI) and allows CloudFront to sign requests to S3 using AWS SigV4. Combined with S3 Block Public Access, OAC ensures the S3 bucket is never directly public-accessible.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** CloudFront, Route 53, and Global Accelerator appear primarily in Design High-Performing Architectures (24%) and Design Resilient Architectures (26%). "Reduce latency for global users" questions almost always involve CloudFront or Global Accelerator.

*   **CloudFront vs. Global Accelerator:** CloudFront caches content at edge locations — best for static assets, video, and cacheable API responses. Global Accelerator routes traffic through AWS's private backbone without caching — best for dynamic content, real-time APIs, gaming, and VoIP. The exam distinguishes these by whether caching is needed.

*   **Route 53 Failover vs. Latency-Based Routing:** Failover routing = active-passive HA with health checks (one primary, one secondary endpoint). Latency-based routing = active-active routing to the lowest-latency Region (no health-check-based failover unless combined with health checks). The exam describes a scenario and expects you to pick the correct policy.

*   **CloudFront TTL and Cache Invalidation:** Objects are cached at edge locations for the duration of the TTL. To force an update before TTL expires, create a CloudFront invalidation (costs money per path). Better practice is to use versioned file names or cache-busting query strings so CloudFront treats new versions as new objects.

*   **Geolocation vs. Latency-Based Routing:** Geolocation routes based on where the DNS query originates (country/continent) — used for serving locale-specific content or compliance-driven content restrictions. Latency-based routing routes based on actual network latency measurement — used purely for performance optimization. These are distinct features that the exam tests by scenario.

*   **Study Resource:** The CloudFront and Route 53 documentation provides comprehensive coverage of all routing policies and distribution configuration: [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/). The [Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) covers all routing policies with decision tree guidance.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the CloudFront and Route 53 chapters in the AWS Solutions Architect study materials. Review the [Amazon CloudFront FAQs page](https://aws.amazon.com/cloudfront/faqs/) and [Amazon Route 53 FAQs page](https://aws.amazon.com/route53/faqs/). The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "AWS Best Practices for DDoS Resiliency" whitepaper, which covers CloudFront's role in DDoS mitigation.

*   **Required Video:** Watch the CloudFront, Route 53, and Global Accelerator module in the official course playlist, focusing on the OAC pattern for S3 origin security and the comparison of all seven Route 53 routing policies: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create a CloudFront distribution with an S3 origin and OAC:** Deploy a static website to S3, configure a CloudFront distribution with the S3 bucket as origin, and enable Origin Access Control. Verify that direct S3 URL access is blocked while CloudFront URLs work correctly.

*   **Configure Route 53 latency-based routing across two Regions:** Deploy identical EC2 instances in us-east-1 and eu-west-1, create an Application Load Balancer in each Region, and configure Route 53 latency-based routing records pointing to each ALB. Use `dig` or online DNS tools to confirm that queries from different geographic locations resolve to the nearer Region.

*   **Set up Route 53 health checks and failover routing:** Configure a health check on the primary endpoint, create a Failover routing policy with primary and secondary records, and test by disabling the primary endpoint to observe automatic DNS failover to the secondary.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Review all seven Route 53 routing policies at [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).
- [ ] Understand CloudFront vs. Global Accelerator use cases at [https://aws.amazon.com/global-accelerator/faqs/](https://aws.amazon.com/global-accelerator/faqs/).
- [ ] Watch the CloudFront/Route 53/Global Accelerator video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab creating a CloudFront distribution with OAC and Route 53 failover routing.
- [ ] Proceed to the weekly quiz.
