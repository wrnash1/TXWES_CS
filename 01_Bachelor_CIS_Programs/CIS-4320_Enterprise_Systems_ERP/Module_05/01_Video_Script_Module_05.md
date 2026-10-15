# Video Script: Module 05 - Financial Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 22-24 minutes

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Simplilearn &bull; Enterprise Resource Planning (ERP) & SAP Systems &bull; Module 05</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=u9-osmHp9Zo" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/u9-osmHp9Zo" title="Simplilearn &bull; Enterprise Resource Planning (ERP) & SAP Systems" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Simplilearn &bull; Enterprise Resource Planning (ERP) & SAP Systems</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

---

### Opening

Professor Nash on camera. Title card: "Module 05 - Financial Management Modules.

Welcome back to CIS-4320. We have covered the foundation of enterprise systems, process modeling, vendor selection, and implementation methodology. Now we start diving into specific functional modules — and we begin with finance, because every ERP system is built around a financial core.

The financial module is the heartbeat of ERP. Every business transaction — every purchase order, every shipment, every payroll run — ultimately produces a financial posting. Understanding how the financial module works, what sub-modules exist, and how they connect to each other is essential for both the SAP Associate exam and for working in any enterprise environment.

Today we cover the General Ledger, Accounts Payable, Accounts Receivable, Asset Accounting, and the Controlling module. We'll also touch on how Salesforce handles financial process connections.

---

### The General Ledger

Cut to slide: "FI-GL — The Financial Core.

The General Ledger, abbreviated FI-GL in SAP, is the central repository for all financial transactions in the enterprise. Every financial event that occurs anywhere in the business — a vendor payment, a customer receipt, a depreciation calculation, a payroll posting — is ultimately recorded in the General Ledger as a journal entry.

The General Ledger is organized around accounts. An account is a category of financial activity. Revenue accounts capture income. Expense accounts capture costs. Asset accounts capture what the company owns. Liability accounts capture what the company owes. Equity accounts capture ownership value. The full set of accounts used by a company is called the Chart of Accounts.

The General Ledger produces the company's external financial statements: the Balance Sheet, Income Statement, and Cash Flow Statement. These statements are used by management, investors, lenders, and regulators to assess the company's financial health.

In SAP, the General Ledger is maintained in the FI module. In SAP S/4HANA, the New General Ledger (NewGL) supports parallel ledgers for reporting under multiple accounting standards simultaneously — for example, US GAAP and IFRS for the same company in the same system.

The key design principle to understand is that sub-ledgers (AP, AR, Asset Accounting) keep their own detailed records, but they post summarized totals to the General Ledger automatically. This means the GL always reflects the sum of all detailed transactions without manual reconciliation.

---

### Accounts Payable and the Three-Way Match

Cut to slide: "FI-AP — Accounts Payable and the Procure-to-Pay Cycle.

Accounts Payable — SAP module FI-AP — manages the company's obligations to its vendors. It is the financial side of the Procure-to-Pay process.

Here is how AP works in SAP. When the company purchases goods or services, a Purchase Order is created in Materials Management (MM). When the goods are delivered, the warehouse records a Goods Receipt. When the vendor sends their invoice, the AP clerk enters it into the system using SAP transaction MIRO.

At that point, SAP automatically executes the three-way match — a comparison of three documents: the Purchase Order, the Goods Receipt, and the Vendor Invoice. The system checks: does the invoice quantity match what was ordered on the PO? Does the invoice price match the PO price? Was the quantity on the invoice actually received?

If all three documents match within configured tolerance, the invoice is approved for payment. If there is a discrepancy, SAP blocks the invoice and generates a work item for the AP team to investigate. This prevents overpayments automatically.

Payment is released through the automatic payment run — SAP transaction F110. The payment run evaluates all due invoices, applies the configured payment terms, generates payment files for the bank, and automatically posts the accounting entries: debit the accounts payable liability, credit cash.

---

### Accounts Receivable

Cut to slide: "FI-AR — Accounts Receivable and the Order-to-Cash Cycle.

Accounts Receivable — FI-AR — manages money that customers owe the company. It is the financial side of the Order-to-Cash process.

When a sale is made and goods are shipped, SAP's Sales and Distribution module (SD) creates a billing document. That billing document posts automatically to FI-AR, creating an open receivable — the customer owes us this amount, due on this date.

When the customer pays, the payment is posted against the open receivable, clearing it. The process of matching payments to open invoices is called clearing.

One important FI-AR tool is the dunning process. When a customer's payment is overdue, the dunning run automatically generates collection notices — first a gentle reminder, then progressively firmer letters as the overdue period grows. SAP allows configuring multiple dunning levels with different notice text for each.

The customer balance in FI-AR feeds directly into the Balance Sheet as an asset — accounts receivable is money the company is owed. Accurate AR management directly impacts the company's reported asset values and cash position.

---

### Asset Accounting

Cut to slide: "FI-AA — Asset Accounting and Depreciation.

Asset Accounting — FI-AA — manages fixed assets: buildings, equipment, vehicles, computers — anything the company owns that has long-term value and is capitalized on the balance sheet.

Every fixed asset has a master record in FI-AA. The master record tracks the acquisition cost, the depreciation method, the useful life, and the current net book value. Net book value is acquisition cost minus accumulated depreciation.

Depreciation is the systematic reduction in an asset's book value over its useful life. SAP supports multiple depreciation methods: straight-line (same amount each period), declining balance (higher amounts early, decreasing over time), and more specialized methods for different asset types and tax purposes.

The depreciation run — SAP transaction AFAB — is executed monthly. It calculates the depreciation for all active assets based on their configured method and useful life, and posts the depreciation expense to the General Ledger automatically. This eliminates the manual spreadsheet work that companies without ERP must do every month.

When an asset is retired or sold, a disposal transaction closes the asset record, removes the net book value from the balance sheet, and records any gain or loss on disposal.

---

### Controlling: Internal Management Accounting

Cut to slide: "CO — Controlling — Internal Financial Reporting.

The Controlling module — SAP CO — provides the internal management accounting that the General Ledger alone cannot deliver. While FI provides external-facing financial statements required by law, CO provides the internal view of financial performance that managers need to make decisions.

Think of it this way: the General Ledger reports financial results by legal entity — 'Acme Corporation earned $50 million this year.' The Controlling module reports by internal dimension — 'The Texas division of Acme earned $22 million; the California division earned $28 million. Product Line A lost $3 million; Product Line B gained $8 million.' This is the information business unit leaders need, but it is not visible in the external financial statements.

CO is structured around several components:

Cost Center Accounting (CO-CCA): Tracks costs by organizational unit — departments, locations, functions. 'How much did the IT department spend this quarter?'

Profit Center Accounting (CO-PCA): Tracks revenues and costs by profit center — business unit, product line, geography. 'Is our retail division profitable?'

Internal Orders (CO-OPA): Tracks costs for specific initiatives — a marketing campaign, a capital project, a maintenance job.

Product Costing (CO-PC): Calculates the standard cost to produce one unit of product, enabling comparison to actual production costs and variance analysis.

The management reporting produced by CO is entirely internal — it does not affect the external financial statements. But it is critical for decision-making, budgeting, and performance management.

---

### Financial Period-End Close

Cut to slide: "The Month-End Close Process.

The month-end close is the process of finalizing all financial transactions for the period, producing the financial statements, and opening the next period. It is one of the highest-pressure processes in any ERP system.

A typical SAP month-end close sequence includes:

Depreciation run: Calculate and post asset depreciation for the period.

Overhead allocation: Allocate indirect costs from cost centers to profit centers and cost objects.

Raw material price variances: Reconcile inventory standard cost to actual cost.

Intercompany elimination: Remove transactions between group companies for consolidated reporting.

Balance sheet reconciliation: Confirm sub-ledger totals match General Ledger totals.

Financial statement generation: Produce the trial balance, income statement, and balance sheet.

Period close: Lock the closed period in SAP to prevent backdated postings.

ERP reduces close time dramatically. Companies that struggled with 10-day manual close cycles typically achieve 3-5 day closes after SAP implementation because the sub-ledger-to-GL posting is automatic rather than manual.

---

### Module Summary and Exam Tips

Cut to slide: "Module 05 Key Takeaways.

Key takeaways for Module 05:

One: The General Ledger is the central repository for all financial transactions. All sub-ledgers post to the GL automatically.

Two: Accounts Payable uses the three-way match to prevent overpayments — comparing the Purchase Order, Goods Receipt, and Vendor Invoice before releasing payment.

Three: Accounts Receivable manages customer billing, payment application, and collections through dunning.

Four: Asset Accounting tracks fixed asset lifecycle — acquisition, depreciation, and disposal. The depreciation run is automatic in SAP.

Five: Controlling provides internal management reporting by cost center, profit center, and product line — information not visible in the external General Ledger.

Six: Month-end close in SAP is faster because sub-ledger postings to the GL are automatic.

Exam tips: The three-way match is tested on both SAP and Salesforce-adjacent questions — know the three documents. The distinction between FI (external reporting) and CO (internal management reporting) is a core SAP exam concept. Asset depreciation run transaction AFAB is a specific SAP fact worth memorizing.

---

### [End Card]

Text on screen:

- Complete Reading Guide 05
- Complete Lab 05 (Financial Process Analysis)
- Complete Quiz 05 (10 questions)
- Post to Discussion Forum 05 (due Wednesday)
- Peer responses due Sunday
- Trailhead: trailhead.salesforce.com — search "Salesforce Billing" or "Revenue Cloud Basics
