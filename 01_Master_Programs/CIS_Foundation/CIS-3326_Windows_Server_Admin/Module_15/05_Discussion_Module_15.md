# Discussion Forum: Module 15 — Monitoring and Performance Tuning

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

## Overview

This module covered the monitoring tools built into Windows Server, performance
counters and thresholds, Data Collector Sets, performance baselines, and event
log management. The discussion prompts below ask you to apply those concepts to
real-world scenarios. Reference specific tools, counter names, threshold values,
and PowerShell cmdlets from the course material.

---

## Scenario A — Production Web Server: Diagnosing an Intermittent Slowdown

A small university runs a web application on a Windows Server 2022 virtual
machine. Students report that the application becomes sluggish every weekday
between 9 AM and 11 AM but feels normal at other times. The server has 4 CPU
cores and 8 GB of RAM. No error events have been reported.

For your initial post, address all three points below.

- Describe your initial diagnostic approach using the four monitoring tools
  covered in Module 15. Which tool would you open first and why? What specific
  information would cause you to move from Task Manager to Resource Monitor?

- Identify which performance counters you would add to a Data Collector Set
  to capture the 9–11 AM window. Name at least four specific counter paths and
  explain what threshold value for each would indicate a bottleneck.

- The slowdown is time-bounded and intermittent. Why is a Data Collector Set
  more appropriate than manually watching a Performance Monitor live graph
  during this investigation? What output format would you use and why?

Post length: 175 to 225 words.

---

## Scenario B — Campus Print Server: Performance Alerts and Event Log Analysis

The campus print server handles print jobs for 400 faculty and staff. An
administrator receives user complaints that print jobs are queuing for 10–15
minutes starting on Monday mornings. The server hosts 12 shared printers through
a single Print Spooler process.

For your initial post, address all three points below.

- Describe how you would use `Get-WinEvent -FilterHashtable` to query the System
  log for Print Spooler events and errors from the previous weekend. Write the
  actual PowerShell command you would use, including the ProviderName and
  StartTime parameters.

- After reviewing the logs, you find no errors — only a pattern of the Spooler
  process consuming high CPU and disk I/O every Monday morning. Which performance
  counters would you monitor and what threshold values would confirm a bottleneck
  versus normal operation?

- Explain the difference between Filter Current Log and a Custom View in Event
  Viewer for this ongoing investigation. If you need to check Spooler events
  every Monday, which approach is better and why?

Post length: 175 to 225 words.

---

## Scenario C — File Server: Establishing a Baseline Before a Storage Upgrade

The university's file server is scheduled for a storage upgrade — the existing
HDDs will be replaced with SSDs next month. The server administrator wants to
document current disk performance before the upgrade so that post-upgrade
improvement can be measured objectively.

For your initial post, address all three points below.

- Describe the baseline capture plan. What counters would you include, what
  sample interval would you use, and how long should the baseline collection
  run? Justify your duration choice.

- Write the `Get-Counter` PowerShell command that collects the disk-related
  counters you identified above, samples every 60 seconds for 60 samples, and
  exports the result to a BLG file at `C:\PerfData\PreUpgrade.blg`.

- After the storage upgrade is complete, describe how you would compare the
  post-upgrade performance to the pre-upgrade baseline. Which specific counter
  values would you compare, and what improvement would you expect to see if the
  SSD upgrade was successful?

Post length: 175 to 225 words.

---

## Peer Response Requirements

Read at least two classmates' posts and reply to each. Each reply must be at
least 60 words and must add technical value — do not simply agree or restate
what they wrote.

Suggested approaches for peer replies:

- Challenge or refine their counter selection — is there an additional counter
  that would reveal information their list would miss?
- Offer an alternative threshold interpretation and explain when the default
  threshold might not apply (for example, SSDs vs. spinning disks for queue
  length).
- Extend their Event Viewer approach — if they described GUI filtering, suggest
  the PowerShell equivalent; if they used PowerShell, suggest a Custom View
  that would serve the same purpose.

---

## Grading Rubric — 20 Points Total

Initial post — 12 points:

- 10 to 12 points: All three sub-points fully addressed with correct tool names,
  specific counter paths or PowerShell commands, threshold values, and clear
  reasoning. Meets word count.
- 7 to 9 points: Most sub-points addressed but one lacks depth or contains a
  technical inaccuracy (wrong threshold, wrong counter object, wrong cmdlet).
- 4 to 6 points: Two or more sub-points are superficial, missing specific counter
  names, or technically incorrect.
- 0 to 3 points: Post is incomplete, missing, or demonstrates little
  understanding of the monitoring tools or counters.

Peer responses — 8 points:

- 7 to 8 points: Two or more substantive replies that add new technical content,
  challenge threshold assumptions, or extend the monitoring approach meaningfully.
- 4 to 6 points: Two replies submitted but one is superficial or fewer than
  60 words.
- 2 to 3 points: Only one peer reply submitted.
- 0 to 1 point: No peer replies, or replies are non-substantive ("Great post!").

---

## Due Dates

- Initial post: Wednesday at 11:59 PM
- Peer responses: Sunday at 11:59 PM

---

## Professor Nash — Note to Students

These scenarios come directly from the kinds of support tickets that land on a
server administrator's desk. The Monday morning print server pattern, for
example, reflects a real phenomenon — background indexing jobs, Group Policy
processing, and weekly scheduled tasks all fire at login time and create a
resource storm. Monitoring tools do not tell you the answer; they tell you
where to look next.

One common mistake students make is conflating the monitoring tools. Resource
Monitor and Performance Monitor are not interchangeable. Resource Monitor gives
you the right-now, per-process picture. Performance Monitor with a Data
Collector Set gives you the over-time, scheduled picture. Both are necessary.
Use the right tool for the question you are trying to answer.

For Scenario B: the `ProviderName = 'Service Control Manager'` filter in
`Get-WinEvent` is one of the most practically useful event queries you will use
on the job. Service start and stop events are recorded there and they will
frequently tell you exactly when a problem began.
