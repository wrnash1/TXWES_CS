# Quiz: Module 09 - CloudFront, Route 53, and Global Acceleration
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A global e-commerce company stores product images in an S3 bucket in us-east-1. Customers in Europe and Asia-Pacific report slow image load times. Which solution most effectively reduces latency for global users?
*   A) Enable S3 Transfer Acceleration on the bucket so users upload and download via CloudFront edge locations.
*   B) Create a CloudFront distribution with the S3 bucket as the origin; CloudFront caches images at edge locations worldwide, serving subsequent requests from the nearest edge.
*   C) Deploy S3 Cross-Region Replication to create bucket copies in EU and APAC Regions, then update the application to detect user location and query the nearest bucket.
*   D) Use AWS Global Accelerator to route image download requests through AWS's private network backbone to the us-east-1 bucket.
*   **Correct Answer:** B) CloudFront caches static content (images) at over 400 edge locations globally, serving users from the nearest PoP rather than the origin in us-east-1, dramatically reducing latency.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* S3 Transfer Acceleration improves upload performance by routing multipart upload requests through CloudFront edge infrastructure. It does not cache content for download — each download still goes back to the origin S3 bucket, providing minimal read latency improvement.
    *   *Why B is correct:* CloudFront is purpose-built for caching and delivering static assets like images. After the first request from any edge location, subsequent requests for the same image are served from the edge cache within that geographic area — eliminating round trips to us-east-1 for the vast majority of traffic.
    *   *Why C is incorrect:* Cross-Region Replication copies data to additional Regions but requires the application to implement geolocation detection and multi-bucket routing logic. This is operationally complex and still doesn't cache at the edge. CloudFront achieves the same result with zero application code changes.
    *   *Why D is incorrect:* AWS Global Accelerator routes TCP/UDP traffic through AWS's private backbone to the origin without caching. For static images, Global Accelerator improves routing but does not cache at the edge. CloudFront's caching is more effective for static content because cached responses are served locally without any origin traversal.

---

**Question 2**
Which of the following is the most accurate description of **Route 53 Latency-Based Routing**?
*   A) A routing policy that directs all traffic to a primary endpoint and automatically switches to a secondary endpoint when health checks detect the primary is down.
*   B) A routing policy that measures network latency between the client's DNS resolver and multiple AWS Regions, directing each query to the Region with the lowest observed latency for that resolver.
*   C) A routing policy that assigns weighted traffic percentages to multiple endpoints, enabling gradual traffic migration during blue/green deployments.
*   D) A routing policy that routes users to different endpoints based on the country or continent from which the DNS query originates.
*   **Correct Answer:** B) Latency-Based Routing directs each DNS query to the AWS Region that has the lowest measured network latency for the resolver making the query.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Failover Routing — the active-passive HA pattern with health-check-driven failover. Latency-Based Routing does not inherently do health-check failover (though it can be combined with health checks).
    *   *Why B is correct:* Route 53 maintains a database of latency measurements from DNS resolver locations to AWS Regions. Latency-Based Routing returns the record pointing to the Region with the lowest latency for each resolver. This is performance-driven routing, not geography-driven.
    *   *Why C is incorrect:* This describes Weighted Routing, where traffic percentages are explicitly configured (e.g., 90%/10% split). Weighted routing is used for canary deployments, A/B testing, and gradual migrations — not latency optimization.
    *   *Why D is incorrect:* This describes Geolocation Routing, which routes based on the geographic location of the DNS query (country or continent). Geolocation is compliance-driven or locale-content-driven; Latency-Based is performance-driven.

---

**Question 3**
A company hosts a static website on S3 behind CloudFront. They update the website's JavaScript bundle but discover that CloudFront continues to serve the old cached version. The cache TTL is 24 hours. Users need access to the updated file immediately. Which action forces CloudFront to serve the new version without waiting for TTL expiration?
*   A) Re-upload the JavaScript file to S3 with the same file name — CloudFront automatically detects content changes on the origin.
*   B) Create a CloudFront invalidation for the specific file path (e.g., `/static/app.js`) to remove it from all edge caches immediately.
*   C) Disable the CloudFront distribution, wait 5 minutes, and re-enable it to clear all cached objects.
*   D) Change the S3 bucket's CORS configuration to prevent CloudFront from caching `.js` files.
*   **Correct Answer:** B) A CloudFront cache invalidation removes the specified path from all edge caches, forcing the next request to fetch the updated file from the S3 origin.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CloudFront does not monitor S3 for content changes. It caches objects based on the request URL and TTL. Re-uploading the same file to S3 with the same name does not cause CloudFront to invalidate its cached copy — the edge cache continues serving the old version until TTL expires.
    *   *Why B is correct:* Cache invalidation is the standard CloudFront mechanism for forcing immediate cache updates. Submitting an invalidation for `/static/app.js` removes it from all edge caches within approximately 60 seconds. The first request after invalidation fetches the latest version from S3 and re-caches it. Note: the best long-term practice is versioned file names (e.g., `app.v2.js`) to avoid needing invalidations.
    *   *Why C is incorrect:* Disabling a CloudFront distribution stops serving all traffic through CloudFront — this is not a cache management operation. Disabling and re-enabling would cause an outage and does not specifically clear cached content.
    *   *Why D is incorrect:* CORS configuration controls cross-origin HTTP access policies for browsers — it has no effect on CloudFront's internal caching behavior. Modifying CORS does not cause cache invalidation.

---

**Question 4**
A financial services company runs a real-time trading application accessible from offices in North America, Europe, and Asia. The application requires the lowest possible network latency for dynamic, non-cacheable API requests. Which service best improves global network performance for this use case?
*   A) Amazon CloudFront with API Gateway as the origin and aggressive cache TTLs for all API responses.
*   B) AWS Global Accelerator, which routes user traffic through AWS edge locations to the nearest AWS endpoint over the AWS private global network, bypassing the unpredictable public internet.
*   C) Amazon Route 53 with Simple Routing returning the IP address of the primary application server in us-east-1.
*   D) S3 Transfer Acceleration to speed up data transfer between regional offices and the application's S3 data lake.
*   **Correct Answer:** B) AWS Global Accelerator routes traffic through AWS's private, optimized network backbone — avoiding public internet congestion and unpredictable routing — providing consistent low latency for dynamic TCP/UDP applications.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CloudFront caches responses at edge locations. For dynamic, non-cacheable trading API requests, aggressive caching is both impossible (stale data would be financially dangerous) and ineffective (cache misses still traverse the public internet to the origin). CloudFront is the wrong tool for non-cacheable dynamic content at scale.
    *   *Why B is correct:* Global Accelerator provides two static Anycast IPs. User traffic is directed to the nearest AWS edge PoP and then routed over AWS's high-performance private network backbone to the application, avoiding the latency and variability of the public internet. This is the SAA-C03 answer for "improve latency for dynamic, non-cacheable global traffic."
    *   *Why C is incorrect:* Route 53 Simple Routing returns a single IP and does not route traffic through the AWS network. Users still connect to the origin via the public internet, experiencing full public internet routing variability.
    *   *Why D is incorrect:* S3 Transfer Acceleration improves upload throughput to S3 by routing through CloudFront edge infrastructure. It applies to S3 operations only and has nothing to do with trading application API latency.

---

**Question 5**
A company's primary application in us-east-1 must automatically redirect traffic to a secondary deployment in us-west-2 when the primary becomes unhealthy. The DNS failover must be transparent to end users, who always use the same domain name. Which Route 53 configuration achieves this?
*   A) Configure Weighted Routing with 100% weight on us-east-1 and 0% on us-west-2 records. Manually change the weights to 0%/100% when the primary fails.
*   B) Configure Failover Routing with a health check on the us-east-1 endpoint. Route 53 automatically returns the us-west-2 record when the health check fails.
*   C) Configure Latency-Based Routing and let Route 53 automatically route to us-west-2 when us-east-1 has higher latency due to partial failure.
*   D) Use Route 53 Resolver to detect health issues and trigger a Lambda function that updates DNS records programmatically.
*   **Correct Answer:** B) Route 53 Failover Routing with a health check on the primary endpoint automatically serves the secondary record when the primary fails, with no manual intervention required.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Weighted Routing with manual weight changes requires human intervention during an outage — violating the "automatic" requirement. During the time it takes someone to notice the failure and change the weights, users experience downtime. This is not automated failover.
    *   *Why B is correct:* Route 53 Failover Routing is purpose-designed for this use case. Health checks continuously monitor the primary endpoint. When the health check fails, Route 53 stops returning the primary record and returns the secondary record instead — automatically, within the DNS TTL period. This is the active-passive DR pattern the SAA-C03 exam tests most commonly.
    *   *Why C is incorrect:* Latency-Based Routing selects the lowest-latency Region but does not guarantee failover when the primary is unhealthy. A partially-down us-east-1 that still responds (but incorrectly) may still have lower measured latency than us-west-2. Latency-Based Routing without health checks is not a failover mechanism.
    *   *Why D is incorrect:* Using Route 53 Resolver and Lambda for DNS updates is a custom, complex solution that introduces Lambda cold start latency, operational overhead, and potential failure modes in the failover path itself. Route 53 Failover Routing provides the same capability natively without custom code.

