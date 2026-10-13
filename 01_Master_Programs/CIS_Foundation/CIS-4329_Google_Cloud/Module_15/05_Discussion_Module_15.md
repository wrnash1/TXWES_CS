# Discussion Forum: Module 15 — GCP Cost Management and Billing

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Discussion Prompt

Cloud cost management is one of the most visible operational responsibilities of a GCP administrator. Every decision — choosing a VM machine type, selecting a storage class, deciding whether to purchase committed use discounts — has a measurable cost impact. This week's discussion asks you to apply the cost management frameworks from Module 15 to a real-world scenario and engage with your classmates' proposed solutions.

### Scenario

You are the GCP administrator for a mid-size e-commerce company. The company's GCP bill has increased 40% over the past three months without a corresponding increase in traffic. Your manager has asked you to identify the causes and propose a cost reduction plan.

You pull the Cloud Billing BigQuery export and find:

- Compute Engine costs have doubled — 60 VMs are running in the development environment 24/7, including on nights and weekends
- 15 VMs in production have low CPU and memory utilization according to the VM Rightsizing Recommender (averaging 8% CPU, 12% memory)
- 200 TB of log data is stored in Cloud Storage Standard class — logs older than 30 days are never accessed
- 5 reserved static IP addresses have no attached resources and have been unattached for 4 months
- No committed use discounts are in place for the 40 production VMs that have been running continuously for 18 months

---

### Your Tasks

**Initial Post (Due Wednesday at 11:59 PM)**

In 200–250 words, propose a cost reduction plan for this scenario. Your post must:

1. Identify the two highest-priority cost reduction actions from the five issues listed. Explain your prioritization — why are these two the highest priority? Consider both the magnitude of potential savings and the implementation effort or risk.

2. For your two priority actions, specify the exact GCP tool or feature that implements each action (use the correct tool name — "Object Lifecycle Management" not "storage transitions"; "VM Rightsizing Recommender" not "recommender tool"), and describe the specific configuration or command needed.

3. Identify one issue from the list that carries implementation risk if handled incorrectly, and explain what could go wrong and how to mitigate the risk.

---

**Peer Responses (Due Sunday at 11:59 PM)**

Write substantive replies of at least 75 words each to at least two classmates. In your replies, engage with one of the following:

- Do you agree with your peer's prioritization? If you prioritized differently, explain why based on the cost data provided.
- Did your peer specify the correct GCP tool for their proposed action? If not, identify the correct tool and explain the difference.
- Did your peer identify a risk? If so, evaluate their mitigation strategy — is it sufficient? Would you add anything?

---

## Instructor Notes for Grading

Strong initial posts will:

- Use correct, specific GCP tool names from the module (not generic descriptions)
- Show prioritization reasoning based on the data in the scenario — for example, 60 dev VMs running 24/7 likely represents a larger absolute cost than 5 unattached IPs, so it should rank higher
- Identify a genuine implementation risk — for example, releasing a reserved IP that a team is using as a DNS record target, or downsizing a VM based on average CPU without accounting for peak load

Strong peer responses will challenge or refine the peer's reasoning, not just validate it.

---

## Discussion Rubric

| Component | Points | Criteria |
|---|---|---|
| Initial Post — Prioritization | 3 | Two actions identified with explicit cost-magnitude reasoning; higher-value actions correctly ranked |
| Initial Post — Tool Specificity | 2 | Correct GCP tool names used; specific configuration or command described |
| Initial Post — Risk Analysis | 2 | Genuine implementation risk identified; mitigation strategy is practical and specific |
| Peer Response 1 | 1.5 | Engages with prioritization, tool accuracy, or risk; at least 75 words; adds substantive analysis |
| Peer Response 2 | 1.5 | Engages with prioritization, tool accuracy, or risk; at least 75 words; adds substantive analysis |
| **Total** | **10** | |

---

## Optional Extension

If you want to go deeper, consider this extension question (not graded):

The scenario mentions that no committed use discounts are in place for 40 production VMs running continuously for 18 months. The VMs are n2-standard-8 in us-central1. Based on the discount types covered in this module, what is the difference in annual cost between receiving only Sustained Use Discounts versus purchasing 1-year resource-based CUDs for the same vCPU and memory commitment? What additional information would you need to calculate this precisely?

Post your analysis as a reply to any classmate who also engaged with the extension.
