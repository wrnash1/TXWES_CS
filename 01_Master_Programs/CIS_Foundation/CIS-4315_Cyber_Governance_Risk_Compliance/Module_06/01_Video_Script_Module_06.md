# Video Script: Module 06 — Information Security Program Development

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## CISM Domain Alignment: Domain 3 — Information Security Program

---

## Pre-Roll Slide

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Introduction (0:00–1:30)

[SHOW SLIDE: Module 06 Title Card — Information Security Program Development]

Welcome back, everyone. I'm Professor Nash, and this is Module 06 of CIS-4315, Cyber Governance, Risk, and Compliance.

Over the last five modules, we've built a solid foundation in governance frameworks, risk assessment, and compliance requirements. Now we shift gears into something deeply practical: how do you actually build an information security program from the ground up?

[PAUSE]

This module is one of the most hands-on in the entire course. Whether you're preparing for the CISM exam or stepping into a security manager role, understanding program development is non-negotiable. We're going to walk through four major areas today.

First, the security program charter — what it is, why it matters, and how to write one that actually gets used. Second, the policy hierarchy — how policies, standards, procedures, and guidelines relate to each other. Third, security strategy alignment — connecting your security investments to business objectives. And fourth, resource planning — budgets, staffing, and making the business case.

[SHOW SLIDE: Module 06 Learning Objectives]

By the end of this module, you should be able to develop a program charter, construct a multi-tier policy hierarchy, align security strategy to business goals, and build a basic resource plan. Let's get started.

---

## Section 1: The Information Security Program Charter (1:30–6:00)

[SHOW SLIDE: What Is a Security Program Charter?]

Let's start with the charter. A security program charter is the founding document of your information security function. Think of it as the constitution of your security program. It defines why the program exists, what authority it holds, and who is accountable.

[PAUSE]

Without a charter, your security program has no formal standing in the organization. You might have a security team doing great work, but if there's no documented mandate, leadership can — and will — deprioritize, defund, or ignore security when it conflicts with business velocity.

[SHOW SLIDE: Charter Components — Six Elements]

A well-constructed charter typically contains six elements.

One: Purpose and scope. What does the security program protect, and what is explicitly out of scope? Scope creep is real, and vague charters invite it.

Two: Authority. Who grants the CISO or security program manager the authority to enforce policy? This usually traces back to the board or a C-suite executive. No authority equals no enforcement capability.

Three: Roles and responsibilities. Who is accountable for what? The charter should clearly distinguish between the security team's responsibilities and those of business unit owners.

[PAUSE]

Four: Alignment to business objectives. This is where many organizations fail. The charter should explicitly connect the security program to the company's mission. For a financial services firm, that might be protecting customer trust and regulatory compliance. For a healthcare company, it's HIPAA compliance and patient safety.

Five: Reporting structure. Where does security sit in the organizational hierarchy? Does the CISO report to the CEO, CTO, or CFO? This matters enormously for independence and authority.

Six: Review cycle. How often is the charter updated? Annual review at minimum. After significant organizational changes, immediately.

[SHOW SLIDE: Charter vs. Policy — Know the Difference]

Here's a critical exam point. The charter is NOT a policy. A policy tells people what they must do. The charter tells the organization what the security program is empowered to do. This distinction shows up on the CISM exam regularly.

[PAUSE]

Let me give you a real-world analogy. The charter is like the city council's resolution creating a police department — it establishes authority, funding, and jurisdiction. The policies are like the laws the police department enforces. You need both, but they serve completely different purposes.

---

## Section 2: The Policy Hierarchy (6:00–11:00)

[SHOW SLIDE: The Four-Tier Policy Hierarchy]

Now let's talk about the policy hierarchy. Organizations that get this right have coherent, enforceable security requirements. Organizations that get it wrong end up with a pile of disconnected documents that nobody reads and nobody follows.

[PAUSE]

The standard hierarchy has four tiers. From top to bottom: Policies, Standards, Procedures, and Guidelines.

[SHOW SLIDE: Tier 1 — Policies Defined]

Tier 1: Policies. These are the highest-level mandatory requirements. They state what must be done without specifying how. Examples include an Acceptable Use Policy, an Access Control Policy, or an Information Classification Policy.

Key characteristics of good policies: they are technology-neutral, they reference regulatory drivers, and they are signed off by executive leadership. A policy that says "all data must be encrypted" is appropriate. A policy that says "use AES-256 on all laptops" is stepping into standards territory.

[SHOW SLIDE: Tier 2 — Standards Defined]

Tier 2: Standards. Standards are mandatory technical specifications that implement policy requirements. They answer the "how specifically" question that policies deliberately leave open.

[PAUSE]

If the policy says "all data at rest must be encrypted," the standard says "use AES-256 with PBKDF2 key derivation for data at rest on all endpoints." Standards can be updated more frequently than policies because technology evolves. This architectural decision — keeping policies technology-neutral and putting specifics in standards — is deliberate and important.

[SHOW SLIDE: Tier 3 — Procedures Defined]

Tier 3: Procedures. Procedures are step-by-step operational instructions for implementing standards. If the standard says use AES-256, the procedure tells an IT admin exactly how to enable BitLocker with AES-256 on a Windows 11 device.

Procedures are the most granular tier. They change most frequently because they track operational reality — software versions, interface changes, vendor tools. Procedures are often owned by IT operations rather than the security team itself.

[PAUSE]

[SHOW SLIDE: Tier 4 — Guidelines Defined]

Tier 4: Guidelines. These are the only non-mandatory documents in the hierarchy. Guidelines offer recommended practices, helpful suggestions, and context. They're important for user adoption and culture, but violations don't trigger the same disciplinary process as policy violations.

Think of a guideline as a best practice document for developers on how to write secure code. Following it is strongly encouraged. Not following it doesn't land you in front of HR.

[SHOW SLIDE: Policy Hierarchy — Connected Example]

Let me show you how these four tiers connect in practice.

Policy: "All remote access to corporate systems must use multi-factor authentication."

Standard: "Remote access shall use hardware tokens or authenticator app TOTP with a minimum 6-digit code. SMS-based OTP is not approved."

Procedure: "To configure your authenticator app for VPN access: Step 1, download the approved app from the corporate portal. Step 2, scan the QR code displayed in the user provisioning portal."

Guideline: "When choosing between hardware tokens and authenticator apps, consider that hardware tokens are recommended for employees handling Tier 1 data."

[PAUSE]

You see how each tier adds specificity while the top tier stays broad enough to remain stable? That's the design principle.

---

## Section 3: Security Strategy Alignment (11:00–16:30)

[SHOW SLIDE: Why Strategy Alignment Matters]

Let's move to security strategy alignment. This is where security managers often struggle, especially early in their careers. It's tempting to build a security program based purely on threats and vulnerabilities. But if your security strategy isn't connected to what the business is trying to achieve, you will constantly fight for resources, face executive skepticism, and lose the argument every time.

[PAUSE]

The CISM exam tests this heavily. Security programs exist to enable business objectives, not to block them. That's the mindset shift. Your job is to protect the organization's ability to operate, grow, and meet its mission.

[SHOW SLIDE: Business-Driven Security Planning — Four Steps]

Here's the framework for aligning security strategy to business objectives.

Step one: Understand the business strategy. What markets is the company entering? What is the growth plan? What are the critical business processes? You cannot align security to a strategy you don't understand.

Step two: Identify business-critical assets. Every business has information assets that, if compromised, would materially harm the organization. For a retailer, it's payment card data and customer PII. For a defense contractor, it's intellectual property and controlled unclassified information. Security strategy must prioritize protecting these assets.

[PAUSE]

Step three: Map threats to business impact. Don't just list threats — express them in business terms. "A ransomware attack could halt manufacturing for 72 hours, costing $4.2 million in lost production." That sentence gets executive attention. "We're at risk of ransomware" does not.

Step four: Define security objectives that support business objectives. If the business objective is to expand into European markets, a supporting security objective is achieving GDPR compliance. If the business is acquiring a competitor, a security objective is integrating the acquired company's security controls within 18 months.

[SHOW SLIDE: The Security Strategy Document Components]

A formal security strategy document typically covers three to five years and includes these components.

Current state assessment — where are we today in terms of security maturity?

Target state — what does the security program look like when fully built out?

Gap analysis — what's missing between current and target state?

Roadmap — what initiatives, in what sequence, close the gaps?

[PAUSE]

Resource requirements — what budget, people, and tools are needed to execute the roadmap?

[SHOW SLIDE: Maturity Models as Strategy Tools]

One highly effective tool for communicating security strategy is a maturity model. The CMMI-based approach defines five levels: Initial, Managed, Defined, Quantitatively Managed, and Optimizing.

When you can show the board a heatmap of your security domains against a maturity model — "We're at Level 1 in vulnerability management and need to reach Level 3 in 24 months" — you've turned an abstract security discussion into a project management conversation that executives understand.

[PAUSE]

This is also where NIST CSF comes in, which we'll cover in depth in Module 07. The CSF's five functions — Identify, Protect, Detect, Respond, Recover — provide a natural structure for maturity assessment and strategy communication.

---

## Section 4: Resource Planning (16:30–21:00)

[SHOW SLIDE: Resource Planning — Budget, People, Tools]

The final section of this module is resource planning. Even the best security strategy fails without adequate resources. As a security manager, you need to understand how to estimate, justify, and manage the resources your program requires.

[PAUSE]

[SHOW SLIDE: Three Resource Categories]

Resources fall into three categories: people, technology, and budget.

Let's start with people. A useful benchmark is that security headcount typically ranges from 5 to 10 percent of total IT staff in mature organizations. But headcount alone doesn't tell the story. You need to consider skill sets, coverage gaps, and the build-versus-buy decision.

Many organizations fill skill gaps with managed security service providers or specialized consulting firms. This is a legitimate strategy, but it requires careful vendor management and clear service-level agreements.

[PAUSE]

[SHOW SLIDE: Security Budget Benchmarks]

On the budget side, industry benchmarks vary by sector. According to Gartner and similar research firms, security spending typically represents 10 to 15 percent of the total IT budget, though this varies significantly by industry. Financial services and healthcare tend to spend more; manufacturing and retail tend to spend less.

What matters more than the percentage is whether your budget is risk-informed. You should be able to trace every major budget item to a risk it mitigates or a compliance requirement it satisfies.

[SHOW SLIDE: Building the Business Case — Four Elements]

Here's the practical skill you need: building the business case for security investment. This is a competency that separates effective CISOs from ineffective ones.

A strong business case includes four elements.

One: Problem statement. What risk or gap are you addressing? Be specific and quantitative where possible.

Two: Solution options. Present two or three options with pros and cons. Decision-makers don't like being told there's only one option.

Three: Cost-benefit analysis. What does each option cost? What risk reduction does it provide? Can you express the benefit in financial terms using something like Annualized Loss Expectancy?

[PAUSE]

Four: Recommendation with implementation timeline. Tell them what you think they should do and when it can be done.

[SHOW SLIDE: ALE in Resource Planning]

Let me spend a moment on Annualized Loss Expectancy, or ALE, because it bridges risk management and resource planning.

ALE equals Single Loss Expectancy multiplied by Annual Rate of Occurrence. If a data breach would cost the company $2 million in remediation, legal, and reputational damage, and you estimate it has a 20 percent chance of occurring in any given year, the ALE is $400,000.

[PAUSE]

If a security control costs $150,000 per year and reduces the probability to 5 percent, the new ALE is $100,000. You've reduced ALE by $300,000 at a cost of $150,000. That's a clear return. This kind of analysis resonates with CFOs and boards.

---

## Section 5: Putting It All Together (21:00–23:30)

[SHOW SLIDE: The Program Development Lifecycle]

Let me close by connecting all four elements into a program development lifecycle.

The charter establishes authority. The policy hierarchy creates enforceable requirements. The strategy alignment ensures the program serves the business. And resource planning makes execution possible.

[PAUSE]

These four elements are interdependent. A charter without resources is meaningless. A strategy without a policy framework to enforce it fails. Policies without executive authority behind the charter won't be followed.

[SHOW SLIDE: CISM Exam Connection — Domain 3]

For your CISM exam preparation, Domain 3 covers information security program development extensively. Pay particular attention to the relationship between governance (Domain 1) and program development (Domain 3). Governance sets the direction; the program executes it.

Key exam areas from this module include the purpose and components of a security program charter, the four-tier policy hierarchy and when each tier applies, how to align security strategy to business objectives, and how to calculate and present ALE for resource justification.

[PAUSE]

[SHOW SLIDE: Module 06 Summary]

Let's recap Module 06.

We covered the security program charter — its six components and its role as the founding document of your security function. We walked through the four-tier policy hierarchy: policies, standards, procedures, and guidelines, with clear distinctions between mandatory and advisory tiers.

We explored security strategy alignment — why security must serve business objectives and how to structure a multi-year strategy document. And we examined resource planning, including budget benchmarking, the build-versus-buy decision, and building the business case using ALE.

[PAUSE]

Your lab this week asks you to draft a security program charter for a fictional mid-size company. Take your time with the authority and scope sections — those are where most students lose points. Your quiz covers the policy hierarchy and strategy alignment concepts. The discussion this week asks you to evaluate a scenario where a CISO failed to align security to business strategy.

See you in Module 07, where we go deep into security architecture and controls.

[SHOW SLIDE: End Card]

---

*End of Video Script — Module 06*
