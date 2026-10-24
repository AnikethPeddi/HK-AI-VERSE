# Proposed capstone: Human-in-the-loop Workflow Tracker Lab

Developed from the Task 1 hosteler leave workflow (see ../task1/report.md). Synthetic data only. Proposed course names: NEW1 = Applied Generative AI and LLMs (change 9), NEW2 = MLOps and Model Deployment Lab (change 10), NEW3 = Cloud and Container Security Lab (change 11), NEW4 = Human-AI Interaction and Accessible Design Studio (change 12).

## Idea
Students build a small tracker for a campus request process (for example, a hostel leave or outpass request) and take it through design, an assisted-triage feature, security review and monitored deployment. It is the project component of NEW2 (MLOps and Model Deployment Lab, 3 credits), with milestones drawn from NEW1, NEW3 and NEW4, so it adds no credits beyond the proposal.

## Process design (aligned with the Task 1 hostel leave workflow)
- Inputs: student ID (synthetic), dates out and in, destination city, reason category, emergency flag, parental-permission recorded (yes or no).
- Statuses: Draft, Submitted, Mentor Approved, Parent Permission Recorded, Warden Approved, Exited, Returned; side statuses Rejected, Expired, Escalated, Overdue, Manual Fallback, Awaiting Parent Permission.
- Accountable owner: Chief Warden. Mentor owns academic clearance only.
- Approval boundary: mentor and warden approve (the warden only after parental permission is recorded); guards only mark Exited or Returned; no software feature ever approves. If a mentor is silent past the window, the request routes to the warden.
- Audit record: append-only row per action (request id, actor role, action, old and new status, timestamp, reason code).
- Fallback: paper form plus manual guard register, reconciled into the tracker within one working day.

## Five synthetic test cases (same as Task 1)
| Case | Input | Expected result | Who decides | Recovery |
|---|---|---|---|---|
| Normal | Complete request | Submitted to Warden Approved (with parental permission recorded), pass issued | Mentor, then warden | None |
| Missing information | No return date | Rejected, stays Draft with named field | Rule | Student resubmits |
| Duplicate | Same student, same dates | Blocked and linked to the first | Rule | Warden cancels the old one if needed |
| Unauthorized | Another person or a guard tries to approve | Refused and logged | Rule; Chief Warden reviews | Correction raised |
| Failed step | Service down or mentor silent | Routes to warden or manual register | Warden; guard | Reconciled within a working day, then Manual Fallback to Returned |

## Milestones and assessment
1. Process map and risk list (NEW4 studio: accessibility check of the form).
2. Build the tracker and triage helper (NEW1: prompt design, evaluation of outputs).
3. Security review of access control and secrets (NEW3).
4. Containerise, deploy, monitor and run the five cases (NEW2).
Assessment idea: working demo, test results for the five cases, a log of AI outputs that were wrong, and an individual contribution statement.

## Prerequisites and conditions
DS304 Machine Learning, CS307 Cloud Computing, CS306 Computer Networks. No real student data may be used. Any pilot needs written approval from the office that owns the process.

## Host course and outcomes
- Host course: NEW2 MLOps and Model Deployment Lab, Sem VII, 3 credits (proposed).
- Prerequisite knowledge: DS304 Machine Learning, CS307 Cloud Computing, basic Python.
- Learning outcomes: (1) map a manual process with roles, handoffs and exceptions; (2) implement statuses and an audit record; (3) enforce an approval boundary so an AI helper cannot approve; (4) recover from a failed step; (5) report measured time per request before and after.
- Synthetic dataset: 200 generated requests with fields id, requester role, request type, dates, completeness flag, with planted cases: 10 duplicates, 10 missing fields, 5 unauthorized requests, 5 simulated notification failures. No real names or IDs.
- Milestone: demo of all five cases on the synthetic set, with a written audit log.
- Acceptance tests: duplicates flagged 10 of 10; requests with missing fields never reach Submitted; unauthorized requests never change status; the AI helper never alters an approval; a failed notification leaves the request intact and is retried; every transition appears in the audit log.
- Measured value: time per request and rework rate from the Task 1 baseline compared with the tracker's logged times; report the range, not a single number.
