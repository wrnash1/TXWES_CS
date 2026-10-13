# Video Script: Module 03 — The Four Dimensions of Service Management

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** ITIL 4 Foundation

---

## [00:00 – 01:30] Opening and Module Objectives

Welcome back. This is Module 03, and today we cover the Four Dimensions of Service Management — one of the most consistently tested topic areas on the ITIL 4 Foundation exam.

By the end of this module you will be able to name and describe all four dimensions of service management, explain why each dimension must be considered for every service and practice, apply the four dimensions to real-world scenarios to identify which dimension a problem belongs to, and describe the role of external factors — the PESTLE model — in shaping service management decisions.

Let us get started.

---

## [01:30 – 04:30] Why Four Dimensions?

ITIL 4 teaches that every service, every practice, and every component of the Service Value System must be considered across four dimensions. The reason for this is straightforward: services fail when organizations focus exclusively on one area while neglecting others.

Here is a scenario we see constantly in real organizations. A team designs a technically excellent system — the architecture is sound, the code is clean, the platform is scalable. They go live. Within two months, the service is failing. Why? Because no one trained the users, roles and responsibilities were unclear, the vendor providing a key integration was not onboarded properly, or the workflows the system was supposed to support were never mapped.

The four dimensions are ITIL 4's way of ensuring that organizations look at every service through four different lenses simultaneously: the people, the technology, the external partners, and the work itself.

Neglecting any single dimension creates gaps. The exam will present scenarios that describe a failure and ask you to identify which dimension was neglected. That is a question pattern you will see multiple times on the Foundation exam, so developing fluency with the four dimensions is essential.

---

## [04:30 – 09:00] Dimension 1: Organizations and People

[SHOW DIAGRAM]

The first dimension is Organizations and People. This dimension covers the human and organizational elements required to deliver services effectively.

It includes the formal organizational structure — how teams are organized, what reporting relationships exist, how authority and accountability are distributed. It includes roles and responsibilities — who owns what, who approves what, who does the work, who escalates when problems arise.

It also includes something that formal org charts do not capture: organizational culture. Culture encompasses the shared values, assumptions, and behaviors that shape how people actually work. A technically well-designed practice can fail completely if the organizational culture does not support it. For example, if an organization's culture is heavily siloed and politically competitive, a practice like knowledge management — which requires people to freely share information — will struggle regardless of how well the technology platform is configured.

The Organizations and People dimension also covers skills and capabilities. Employees need to know what ITIL 4 is, understand the practices relevant to their roles, and have the soft skills required for stakeholder engagement. An IT department that has never trained its staff in service management principles will deliver inconsistent results even with the best tools.

For the exam: when a scenario describes confusion about who is responsible, teams not working together, resistance to a new practice, or a culture mismatch, the answer likely involves the Organizations and People dimension.

---

## [09:00 – 13:00] Dimension 2: Information and Technology

The second dimension is Information and Technology. This dimension covers the information assets and the technology infrastructure required to deliver services.

The information side includes the data that services create, use, and depend on. This means data governance — how data is created, stored, managed, protected, and used. It means knowledge management — how the organization captures and shares expertise. It means information security — how data is protected from unauthorized access, modification, or loss.

The technology side includes the hardware, software, applications, platforms, and tools that support service delivery. This ranges from server infrastructure and networking to cloud platforms, automation tools, artificial intelligence, and the service management platform itself.

For modern organizations, this dimension is increasingly dominated by questions about cloud adoption, automation, AI integration, and data management at scale. ITIL 4 was written with these realities in mind, and the Information and Technology dimension explicitly accounts for them.

Key questions that belong to this dimension include: is the right technology available to deliver this service? Is data properly managed and secured? Do teams have access to the information they need to do their work effectively? Are technology choices integrated with each other in a way that supports the service?

For the exam: when a scenario describes technology failures, data problems, tool incompatibilities, or knowledge gaps, the Information and Technology dimension is likely the primary focus.

---

## [13:00 – 17:00] Dimension 3: Partners and Suppliers

The third dimension is Partners and Suppliers. This dimension covers the relationships an organization has with external parties — the vendors, contractors, managed service providers, cloud platforms, and other organizations that contribute to service delivery.

Almost no organization delivers services entirely on its own. A typical IT service may rely on a cloud infrastructure provider, a software vendor's platform, a managed security operations center, a hardware maintenance contractor, and a professional services firm for implementation support. Each of these is a partner or supplier, and each relationship must be actively managed.

This dimension covers how supplier relationships are contracted — the agreements, SLAs, and performance metrics that govern what suppliers are expected to deliver. It covers supplier selection — how the organization chooses between providers. It covers ongoing supplier management — monitoring performance, managing risks, and maintaining the relationship over time.

ITIL 4 also distinguishes between different types of supplier relationships based on the strategic importance and degree of dependency. Some suppliers provide commodity services that could easily be replaced; others provide highly integrated capabilities that are deeply embedded in service delivery and would be very difficult to change.

For the exam: when a scenario describes vendor performance problems, unclear supplier contracts, outsourcing decisions, or dependency on a third-party service, the Partners and Suppliers dimension is likely the primary focus.

---

## [17:00 – 20:30] Dimension 4: Value Streams and Processes

The fourth dimension is Value Streams and Processes. This dimension covers the workflows, procedures, and activities that define how work is done — how inputs are transformed into outputs that enable value.

A value stream is the end-to-end series of steps an organization takes to create and deliver a service to a consumer. A process is a specific set of interrelated activities that transform inputs into defined outputs. The Value Streams and Processes dimension is where organizations design, document, and optimize how work flows.

This dimension connects directly to the Service Value Chain. The SVC defines what activities exist; the Value Streams and Processes dimension defines how those activities are performed in specific contexts.

Key questions that belong to this dimension include: how does a request move from submission to fulfillment? What are the steps in our incident resolution process? Where are the bottlenecks in our change approval workflow? What is the sequence of activities when we onboard a new customer?

This dimension is also where Lean thinking applies most directly. Lean is the discipline of identifying and eliminating waste in workflows. Value stream mapping — a Lean technique that ITIL 4 explicitly references — is the practice of drawing out all the steps in a workflow and identifying which steps add value and which represent waste.

For the exam: when a scenario describes inefficient workflows, unclear process steps, bottlenecks, or the need to redesign how work is done, the Value Streams and Processes dimension is likely the primary focus.

---

## [20:30 – 22:30] External Factors: The PESTLE Model

Surrounding the four dimensions in the ITIL 4 model are external factors that organizations cannot control but must account for. ITIL 4 uses the PESTLE model to categorize these factors.

PESTLE stands for: Political, Economic, Social, Technological, Legal, and Environmental factors.

Political factors include government policies, regulatory environments, and geopolitical stability. A financial services company must design its IT services to comply with financial regulations that vary by country.

Economic factors include market conditions, budget constraints, and economic cycles. An IT department facing budget cuts must make different decisions about technology investments than one in a growth period.

Social factors include demographic trends, user expectations, and workforce characteristics. The expectation that services should be available via mobile devices is a social factor that shapes service design requirements.

Technological factors include the pace of technology change, emerging platforms, and technology availability. Cloud computing fundamentally changed what is possible for small and large organizations alike.

Legal factors include data protection laws, contractual obligations, and intellectual property requirements. The General Data Protection Regulation in Europe is a legal factor with direct implications for how IT services manage personal data.

Environmental factors include climate considerations, sustainability requirements, and physical environment risks. Data center energy consumption and geographic risk (flood zones, earthquake-prone regions) are environmental factors in service design.

The PESTLE factors affect all four dimensions. They set the context within which the four dimensions must operate.

---

## [22:30 – 24:00] Module Summary and What Is Next

Let us recap Module 03.

The four dimensions of service management are: Organizations and People; Information and Technology; Partners and Suppliers; and Value Streams and Processes. Every service and practice must be considered across all four.

Organizations and People covers roles, culture, skills, and accountability. Information and Technology covers data assets, tools, platforms, and security. Partners and Suppliers covers external relationships, contracts, and vendor management. Value Streams and Processes covers workflows, procedures, and work design.

Surrounding the four dimensions are external PESTLE factors — Political, Economic, Social, Technological, Legal, and Environmental — that shape the context within which services must operate.

In Module 04 we go deep on the seven Guiding Principles. Complete the Reading Guide, Lab, and Quiz for Module 03. The discussion this week asks you to apply the four dimensions to a real organizational scenario.

For authoritative content on the four dimensions, see axelos.com.

---

End of Module 03 Video Script
