# Video Script: Module 05 — Service Value Chain Activities

**Course:** CIS-4335 IT Service Management — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20–24 minutes
**Certification Alignment:** ITIL 4 Foundation

---

## [00:00 – 01:30] Opening and Module Objectives

Welcome to Module 05. I am Professor Nash. In Module 02 we introduced the Service Value Chain as the operating model at the heart of the SVS. Today we go much deeper. We will examine each of the six SVC activities in detail, understand what inputs and outputs each activity works with, and explore how activities combine into value streams that serve specific organizational purposes.

By the end of this module you will be able to describe the purpose, inputs, and outputs of each of the six SVC activities; explain how the Improve activity differs from the others; describe how value streams combine SVC activities for specific scenarios; and connect SVC activities to specific ITIL 4 practices.

This module is essential for the Foundation exam. The exam will ask questions at several levels of depth: which activity does a described action belong to, what does a specific activity output, and what value stream pattern applies to a described scenario. Let us work through it.

---

## [01:30 – 04:30] The Service Value Chain — Architecture Review

[SHOW DIAGRAM]

Before we go into each activity, let us review the overall architecture.

The Service Value Chain is surrounded by the other SVS components. Governance sits above it, setting the direction within which the SVC operates. The Guiding Principles inform how every activity is performed. Practices provide the capabilities that enable SVC activities. And Continual Improvement applies to all activities from within.

The SVC has two directions of flow. Demand and opportunity enter from the outside world and drive the SVC. Value exits the SVC in the form of products, services, and outcomes for consumers.

Inside the SVC, all six activities are connected to each other and to the Improve activity in particular. This means that improvement information flows continuously across all activities — when Deliver and Support identifies a recurrent problem, that insight should flow through Improve and potentially back into Design and Transition or Obtain/Build.

The SVC does not have a front door and a back door. It has six interconnected activities that can be entered from multiple points depending on the type of work being done.

---

## [04:30 – 07:00] Activity 1: Plan

The Plan activity ensures a shared understanding of the vision, current status, and improvement direction for all four dimensions and all products and services across the organization.

The purpose of Plan is alignment. Alignment between organizational leadership and operational teams. Alignment between what services currently exist and what services are needed. Alignment between strategy and execution.

Inputs to Plan include demand from stakeholders, policies from governance, improvement status reports from Improve, and service performance data from Deliver and Support.

Outputs of Plan include strategic plans, portfolios of services and projects, architectural decisions, policies for the other activities to follow, and improvement plans.

A critical exam point about Plan: it is not a one-time activity that happens at the beginning of a project. It is an ongoing activity that produces strategic and operational guidance that all other SVC activities rely on. Every other activity receives input from Plan in some form.

---

## [07:00 – 09:30] Activity 2: Improve

The Improve activity ensures continual improvement of products, services, and practices across all value chain activities and across the four dimensions of service management. It is unique among the six activities because it connects to all of the others simultaneously.

Every activity in the SVC both contributes to Improve and receives outputs from it. Deliver and Support generates incident and performance data that feeds improvement analysis. Design and Transition generates lessons learned that feed back into Design improvements. The Improve activity synthesizes these inputs and produces improvement initiatives, plans, and performance evaluations.

The Improve activity is supported by the Continual Improvement practice, which provides the seven-step improvement model and the Continual Improvement Register. We will cover the Continual Improvement practice in depth in Module 06.

For the exam: every SVC activity has a bidirectional relationship with Improve. No activity is exempt from contributing to improvement or receiving improvement guidance.

---

## [09:30 – 12:30] Activity 3: Engage

The Engage activity provides a good understanding of stakeholder needs, sets the direction for service delivery and continuous engagement, and establishes good relationships with all stakeholders.

Engage is how the organization stays connected to the outside world. It captures demand from consumers and translates it into requirements. It communicates service performance back to customers. It manages ongoing relationships with users, customers, sponsors, and partners.

Inputs to Engage include demand from consumers, service performance data, improvement status, contracts and agreements, and information about third-party services.

Outputs of Engage include stakeholder requirements, change requests, service performance reports to customers, feedback and insights from consumers, and engagement data that informs other activities.

A practical way to understand Engage: it is the voice of the customer inside the SVC. Without Engage, the SVC would produce services based on assumptions rather than actual consumer needs. Every other activity relies on Engage to provide the demand signal.

For the exam: when a scenario describes collecting stakeholder requirements, communicating service status to users, managing customer relationships, or responding to consumer feedback, the Engage activity is involved.

---

## [12:30 – 15:30] Activities 4 and 5: Design and Transition, Obtain/Build

The Design and Transition activity ensures that products and services continually meet stakeholder expectations for quality, costs, and time to market. This is where new or changed services are designed, tested, and handed off to operational teams.

Design and Transition covers the entire lifecycle of a service from concept to live deployment. It produces service designs, tested service components, transition plans, and updated service documentation. It draws on requirements from Engage, architectural decisions from Plan, and components from Obtain/Build.

A key point: Design and Transition is not the same as the ITIL v3 Service Design phase. In ITIL 4, design and transition are a single integrated activity because ITIL 4 recognizes that in modern DevOps environments, design and deployment can happen in days or weeks, not months.

The Obtain/Build activity ensures that service components are available when and where they are needed and meet agreed specifications. This covers both obtaining components from external sources and building them internally.

Obtain/Build is where the actual work of acquiring or creating service components happens. If the organization is deploying a new monitoring tool, Obtain/Build covers purchasing the licenses, installing the software, configuring it, and confirming it meets specifications. If the organization is developing custom software, Obtain/Build covers the development work.

---

## [15:30 – 18:30] Activity 6: Deliver and Support

The Deliver and Support activity ensures that services are delivered and supported according to agreed specifications and stakeholders' expectations. This is where day-to-day service operation happens.

Deliver and Support is where the service desk operates, where incidents are resolved, where service requests are fulfilled, and where ongoing monitoring and event management occur. It is the activity that most users experience directly.

Inputs to Deliver and Support include deployed services from Design and Transition, service components from Obtain/Build, improvement plans from Improve, and stakeholder requirements from Engage.

Outputs of Deliver and Support include delivered services, resolved incidents, fulfilled service requests, performance data, and improvement opportunities that feed back into Improve.

The Deliver and Support activity depends on a strong set of practices: Incident Management, Service Desk, Service Request Management, Monitoring and Event Management, and others. These practices enable the activity — they provide the defined ways of working that make consistent service delivery possible.

---

## [18:30 – 21:00] Value Streams in Action

Let us look at how these six activities combine into value streams for specific types of work.

Value stream example 1: Resolving a user-reported incident.

A user calls the service desk to report that their workstation cannot connect to the corporate VPN. The Engage activity captures the incident report and translates it into a service desk ticket. The Deliver and Support activity takes ownership of the ticket, diagnoses the problem, implements a fix, and confirms resolution with the user. The Improve activity receives data about this incident type and identifies whether it represents a pattern worth investigating. If a pattern is detected, Plan may receive a recommendation for a change to the VPN configuration.

Value stream example 2: Deploying a new collaboration tool.

The business requests a new project collaboration platform. Engage captures the requirements: 500 users, integration with email, real-time document collaboration, mobile access. Plan incorporates this into the service portfolio and allocates resources. Design and Transition designs the implementation, integration points, and user onboarding plan. Obtain/Build procures the cloud platform licenses and configures the environment. Deliver and Support launches the service, configures helpdesk procedures for the new tool, and begins handling user questions. Improve monitors adoption and performance and feeds that data back into future design decisions.

The exam may present a scenario and ask which SVC activities are involved. Practice mapping scenarios to activities.

---

## [21:00 – 23:00] Connecting Practices to SVC Activities

Practices do not map one-to-one to SVC activities, but there are strong associations.

Incident Management and Service Desk primarily enable Deliver and Support. Service Request Management primarily enables Deliver and Support. Change Enablement primarily enables Design and Transition. Deployment Management primarily enables Obtain/Build. Service Level Management primarily enables Engage and Deliver and Support. Continual Improvement primarily enables Improve.

The word "primarily" is important here. Most practices contribute to multiple SVC activities. Knowledge Management, for example, contributes to Deliver and Support (agents use knowledge articles to resolve incidents) and to Improve (knowledge gaps become improvement opportunities) and to Design and Transition (new service documentation is produced during design).

---

## [23:00 – 24:00] Module Summary and What Is Next

The six SVC activities are Plan, Improve, Engage, Design and Transition, Obtain/Build, and Deliver and Support. Each has a defined purpose, specific inputs, and specific outputs. They connect to each other and to the Improve activity in flexible patterns called value streams.

In Module 06 we cover the Continual Improvement practice — the seven-step model that structures the Improve activity. In Modules 07 through 15 we cover the specific ITIL 4 practices in depth.

Complete the Reading Guide, Lab, and Quiz. The discussion this week asks you to map a real service scenario to SVC activities.

For authoritative SVC content, see axelos.com.

---

End of Module 05 Video Script
