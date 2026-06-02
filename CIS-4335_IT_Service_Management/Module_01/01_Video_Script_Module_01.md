# Video Script: Module 01 — Introduction to ITIL 4 and Service Management

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** ITIL 4 Foundation

---

## [00:00 – 01:30] Opening and Module Overview

Hello, everyone, and welcome to Module 01 of CIS-4335 IT Service Management. I am Professor Nash, and I am glad you are here. This is the first module of the course, and it is also one of the most important — because what we cover today forms the conceptual foundation for everything that follows for the next fifteen weeks.

By the end of this video, you will be able to define IT service management and explain why organizations adopt it, describe the evolution of ITIL from its origins through ITIL 4, explain the core concept of value co-creation, and identify the key components of the ITIL 4 framework at a high level.

These are not just academic definitions. The ITIL 4 Foundation certification exam will test you on every term we discuss today, and industry employers expect IT professionals to speak this language fluently. Let us get started.

---

## [01:30 – 04:30] What Is a Service? What Is IT Service Management?

Before we can talk about ITIL, we need to agree on what a service actually is. In everyday language, people use the word loosely. ITIL 4 is very precise about it.

ITIL 4 defines a **service** as a means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks.

Let me unpack that definition carefully, because each phrase matters.

First: "enabling value co-creation." Notice it does not say "delivering value to" the customer. It says co-creation. That is a deliberate and significant choice of words. Value is not a package you hand off. It is something that emerges from the relationship between the provider and the consumer. When you use a navigation app on your phone, the app developer creates the software, maintains the servers, and updates the maps — but you co-create the value by providing your location, choosing your destination, and making the decisions that get you where you need to go. Neither party creates value in isolation.

Second: "outcomes that customers want to achieve." ITIL distinguishes sharply between outputs and outcomes. An **output** is a tangible or intangible deliverable. An **outcome** is a result for a stakeholder enabled by one or more outputs. The email server being available is an output. The salesperson closing a deal because they received a client's message on time is an outcome. ITIL 4 tells us to keep our focus on outcomes, not just outputs.

Third: "without managing specific costs and risks." This is the value of specialization. When your organization uses a cloud provider instead of running its own data center, you are transferring the risks and costs of hardware failure, power management, and physical security to a specialist. That transfer is part of what makes the service valuable.

**IT Service Management**, or ITSM, is the set of policies, practices, and capabilities an organization uses to design, deliver, manage, and improve IT services in ways that are aligned to business needs. ITSM is not about configuring routers or writing code — it is about ensuring that IT activity creates genuine value for the people and organizations it serves.

ITIL 4 is the world's most widely adopted ITSM framework. It is not a law or a standard. It is a body of best-practice guidance that organizations adapt to fit their specific context.

---

## [04:30 – 08:00] The Evolution of ITIL: From ITIL v1 to ITIL 4

Understanding where ITIL came from helps you understand why it is structured the way it is today.

**ITIL Version 1** was developed in the 1980s by the UK government's Central Computer and Telecommunications Agency, the CCTA. The government had observed enormous variation in the quality and cost-effectiveness of IT services purchased from vendors, and they wanted a set of guidelines for what good IT service management looked like. The result was a library of about 40 books covering everything from network management to software development. It was thorough, but it was also dense and difficult to implement.

**ITIL Version 2** arrived in the early 2000s and consolidated that library into a more manageable structure. It organized guidance primarily around Service Support and Service Delivery — the two most operationally relevant areas. V2 gained wide adoption globally. Many organizations built their service desks and change management processes directly from ITIL v2 guidance.

**ITIL Version 3**, published in 2007 and refined in 2011, reorganized the framework around a **service lifecycle** with five phases: Service Strategy, Service Design, Service Transition, Service Operation, and Continual Service Improvement. This was a more holistic and strategically grounded model. It introduced the idea that IT services needed to be designed and managed from their conception to their retirement, not just operated day-to-day. ITIL v3 also rebranded guidance units from "processes" to something closer to disciplines, though the word "practice" was not formally adopted until ITIL 4.

**ITIL 4** was published in 2019. It was a fundamental re-architecture of the framework — not just an update. The five lifecycle phases were retired. In their place came the **Service Value System** and the **Service Value Chain**. ITIL 4 was explicitly designed to work alongside modern approaches like Agile, DevOps, Lean, and organizational change management. The term "practices" replaced "processes" to signal that effective service management requires people, technology, information, and partners working together — not just documented flowcharts.

The exam will sometimes present a scenario involving an outdated ITIL v3 concept and ask you to identify the ITIL 4 equivalent. Know these distinctions cold.

---

## [08:00 – 11:00] Utility, Warranty, and Value

ITIL 4 defines value through two complementary lenses: **utility** and **warranty**.

**Utility** is what a service does — its functionality. It answers the question: does this service do what the customer needs it to do? ITIL 4 describes utility as "fit for purpose." A service has utility if it either supports the performance of the consumer or removes constraints from the consumer.

Think of a word processing application. Its utility is the ability to create, edit, format, and save documents. If the application cannot do those things, it has no utility for a writer, regardless of how stable or secure it is.

**Warranty** is how the service performs — its reliability, availability, capacity, and security. ITIL 4 describes warranty as "fit for use." A service has warranty if it meets agreed levels of availability, capacity, continuity, and security.

Using the same word processor: if the application crashes every thirty minutes, loses documents randomly, or is available only forty percent of the time, it has poor warranty — even if its features are excellent.

A service must have both utility and warranty to deliver value. A service that does the right things but does it unreliably fails. A service that is always available but does nothing useful also fails.

Here is a phrase that is worth memorizing: **Utility is fit for purpose; warranty is fit for use. Both are required for value.**

The exam frequently presents scenarios that ask you to classify a characteristic of a service as a utility or warranty concern. Practice identifying which one is being described.

---

## [11:00 – 15:00] The ITIL 4 Service Value System — Overview

[SHOW DIAGRAM]

Now let us introduce the ITIL 4 Service Value System, or SVS. This is the top-level model in ITIL 4, and it describes how all the components of an organization work together to enable value creation.

At the left side of the SVS diagram you will see two inputs: **Opportunity** and **Demand**. Opportunity represents possibilities for value creation. Demand represents the need for products and services from internal and external consumers. These are the triggers that set the SVS in motion.

At the right side of the diagram is the output: **Value**. Everything in between exists to convert opportunity and demand into value.

Inside the SVS, there are five core components. I will introduce each one briefly here and we will explore each in depth in later modules.

**Component 1: Guiding Principles.** These are seven recommendations that guide an organization's decisions and actions in all circumstances. They are: Focus on Value; Start Where You Are; Progress Iteratively with Feedback; Collaborate and Promote Visibility; Think and Work Holistically; Keep It Simple and Practical; and Optimize and Automate. The Guiding Principles are universal — they apply across the organization, across all practices, and in every situation.

**Component 2: Governance.** This is the means by which an organization directs and controls its activities. Governance ensures that policies, objectives, and accountability are established and followed.

**Component 3: Service Value Chain.** This is the operational heart of the SVS — the model that defines how an organization creates, delivers, and continuously improves services. The Service Value Chain consists of six activities: Plan, Improve, Engage, Design and Transition, Obtain/Build, and Deliver and Support. These activities combine in flexible patterns called value streams.

**Component 4: Practices.** ITIL 4 defines 34 management practices — sets of organizational resources designed to perform work or accomplish an objective. These practices are grouped into three categories: General Management Practices (14), Service Management Practices (17), and Technical Management Practices (3). You will study the most exam-relevant practices in Modules 6 through 15.

**Component 5: Continual Improvement.** This is the ongoing activity embedded throughout the entire SVS. Every component of the SVS is subject to continual improvement. ITIL 4 provides a seven-step Continual Improvement Model to guide these efforts.

The SVS is the framework that holds all of ITIL 4 together. When you are answering exam scenario questions, always ask yourself: where does this fit in the SVS?

---

## [15:00 – 18:00] The Four Dimensions of Service Management

ITIL 4 states that every service, practice, and system must be considered across **four dimensions** to ensure it is balanced, realistic, and effective. Neglecting any one dimension creates risk.

[SHOW DIAGRAM]

**Dimension 1: Organizations and People.** This dimension covers the roles, responsibilities, culture, and skills of everyone involved in service management. It includes the formal organizational structure as well as informal culture and communication. A technically perfect system can fail if the people who use it lack training, if accountability is unclear, or if organizational culture resists adoption.

**Dimension 2: Information and Technology.** This dimension covers the information assets, knowledge, and technology infrastructure required to deliver services. It includes data management, AI tools, automation platforms, application architecture, and collaboration tools. It also includes information security — how data is protected and governed.

**Dimension 3: Partners and Suppliers.** Almost no organization delivers services entirely on its own. This dimension covers the relationships with external parties — cloud vendors, outsourced support providers, hardware manufacturers, and software licensors. It addresses how those relationships are contracted, managed, and evaluated.

**Dimension 4: Value Streams and Processes.** This dimension covers the workflows, procedures, and activities that transform inputs into outputs. It is where process design and workflow optimization live within ITIL 4. A value stream is a series of steps an organization takes to create and deliver products and services to a service consumer.

Surrounding all four dimensions in the ITIL 4 model are **external factors** — political, economic, social, technological, legal, and environmental forces that organizations cannot control but must account for. This is sometimes called the PESTLE model.

The exam tests the four dimensions regularly. When you read a scenario question, identify which dimension is the primary focus before selecting an answer.

---

## [18:00 – 20:30] ITIL 4 Key Stakeholder Roles

ITIL 4 uses precise terminology for the people and organizations involved in service relationships. Knowing these terms is important for both the exam and for practical communication.

A **service provider** is an organization that delivers services to consumers. A **service consumer** is an organization that uses services. These terms are generic — the consumer could be another business unit within the same company.

Within the service consumer organization, ITIL 4 identifies three distinct roles.

A **customer** is a person who defines the requirements for a service and takes responsibility for the outcomes of service consumption. Customers make purchasing or adoption decisions and define what success looks like.

A **user** is a person who uses services on a day-to-day basis. Users may or may not be the same as customers. When a manager purchases a software license for their team, the manager is the customer; the team members who use the software are the users.

A **sponsor** is a person who authorizes the budget for service consumption. The sponsor may be the same person as the customer or may be a more senior stakeholder.

Understanding these distinctions matters because ITIL practices are designed to engage different stakeholders in different ways. The Service Desk interacts primarily with users. Service Level Management negotiates primarily with customers. Financial decisions involve sponsors.

---

## [20:30 – 22:30] Connecting It All: Why ITIL 4 Matters in Practice

I want to spend a few minutes making this concrete before we wrap up.

Think about a university campus — a context all of you know well. The campus IT department is a service provider. The students, faculty, and administrative staff are users. The academic departments are customers who define what services they need. The provost's office is the sponsor that approves the IT budget.

The services include the learning management system, email, the library database, wireless network access, and the student information system. Each of these services must have utility — they must do what users need them to do — and warranty — they must be available, reliable, and secure when needed.

When the learning management system goes down the night before finals, that is an incident that disrupts user outcomes. The IT team's response to that incident, their investigation into its root cause, and their actions to prevent recurrence are all service management activities guided by ITIL practices.

When the university evaluates whether to migrate from its on-premise email system to a cloud provider, that decision involves all four dimensions: the people who will be affected, the technology being adopted, the vendor relationship, and the workflows that will change.

ITIL 4 gives us a shared vocabulary and a coherent framework for making all of these decisions and activities more consistent, more effective, and more aligned to the outcomes that matter.

---

## [22:30 – 24:00] Module Summary and What Is Next

Let us review what we covered today.

We defined a service as a means of enabling value co-creation, and we established that value requires both utility and warranty.

We traced the evolution of ITIL from its government origins in the 1980s through ITIL 4 in 2019, noting the shift from a lifecycle model to the Service Value System.

We introduced the five components of the SVS: Guiding Principles, Governance, Service Value Chain, Practices, and Continual Improvement.

We introduced the four dimensions of service management: Organizations and People; Information and Technology; Partners and Suppliers; and Value Streams and Processes.

And we clarified the key stakeholder roles: service provider, service consumer, customer, user, and sponsor.

In Module 02, we will go deep into the Service Value System and examine how its components interact. In Module 03, we will return to the four dimensions in detail.

Before next week, complete the Reading Guide, work through the Lab Activity, and take the Module Quiz. The discussion prompt this week asks you to apply today's concepts to a real-world scenario — I encourage you to think carefully and engage with your classmates' ideas.

For additional study, Axelos maintains the official ITIL 4 Foundation resources at axelos.com. That is your authoritative source for exam-aligned definitions.

I will see you in Module 02. Good luck, and do the reading.

---

End of Module 01 Video Script
