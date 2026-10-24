# Task 1 – Hosteler Leave Process: Study and Redesign

Student work, not an official IFHE proposal. Evidence is in `evidence-log.md`. Every figure is labelled Observed, Reported, Estimate, Derived or Assumption.

## 1. How I studied it, and limits of access
- Method: my own use of the process as a hosteler, plus one volume report relayed to me verbally by a friend (the original source's role was not recorded). Sample size: n = 1 first-hand, n = 1 second-hand. Nothing was timed with a stopwatch; times are my own approximations.
- Permission: I did not ask the warden office for formal permission. I described the process from my own use as a hosteler. For volumes I relied on a friend, who relayed what they were told; I did not record who that was. No one declined.
- Access limits: I have not heard from the warden office. What I know about parental permission and the absence of a signing limit is my own understanding, not confirmed (evidence log row 19). I collected no names, IDs, marks, fees or signatures.

## 2. Current process (as observed)
1. Student fills the leave form on the SIS (~5 min) and prints it (~5 min).
2. Student goes to college and gets mentor/HOD signatures. If the mentor is off campus, the warden signs both sets; if the HOD is unavailable the student waits until evening.
3. Student walks to the warden office (~5-12 min each way) for warden signatures. The warden signs once the student's parents have given permission (Reported; how parents are contacted was not recorded).
4. The form has 3 parts and 6 signatures (3 mentor + 3 warden).
5. Part 1 goes to the hostel security guard, part 2 to the college gate, part 3 stays with the student.
6. On return, part 3 is shown at the college gate and submitted to the hostel security guard.

**Handoffs:** student → mentor/HOD → warden (after parents' permission) → hostel guard → college gate → (return) college gate → hostel guard.
**Approvals:** mentor/HOD (academic), warden (hostel).
**Exceptions seen:** mentor absent (warden signs both); HOD absent (wait until evening); lost part 3 or no form (a fine, amount not recorded); late-night leave (not permitted).

## 3. Problem and scale
**Problem.** The SIS already holds the request, but only the printout counts. That means two physical trips, six wet signatures per leave, no status visibility, no digital record of who is out, and a rush before holidays.

**Time per leave, student side (Estimate), with rework.**
Form and print 10 min + mentor signature 10-30 min + warden round trip 10-25 min = 30-65 min (midpoint 47.5).
Rework (Assumption): 5% of leaves need a second trip of about 20 min, so +1 min on average.
Current time per leave: **31 / 48.5 / 66 min (low / mid / high)**.

**Volume (Reported + Assumption).** About 4,000 hostelers across all programmes (Reported, approximate, verbal; I use a ±25% sensitivity where it matters). Before holidays or occasions, 500+ leaves in one day (Reported; peak days only, no normal-day figure was given). The Dussehra holidays (17-20 Oct 2026) are my example; forms were issued on 16 Oct (see evidence log row 18).
Leave shares are my own estimates: 0.5-2% in a normal week and 85-95% in a long holiday. For a short festival break I use the reported peak instead of a percentage: leave forms were issued on 16 Oct, the day before the 17-20 Oct holidays, and 500+ came through that day. I therefore use 500 / 1,000 / 2,000 leaves (low = the reported floor, mid = twice that as an assumption, high = 50% of hostelers).

**Cross-check (Derived, not validation).** Because forms were issued on one day (16 Oct), the reported 500+ for that day is close to the whole event. That is about 12.5% of 4,000 hostelers, far below my earlier 50-80% festival estimate, so I replaced that estimate.
**Staff load (Derived):** 500 leaves/day × 6 signatures = about 3,000 signatures a day across mentors and wardens. The warden has no per-day limit on forms signed (Reported), so the limit is time, not a quota.

**Per month, current state (mid case, student hours at 48.5 min per leave):** see the monthly table in section 6.

## 4. Proposed process
**Principle:** keep the existing SIS form; make the SIS the source of truth; keep paper as fallback.

**Inputs:** student ID (from login), dates out and in, destination city, reason category, contact number, emergency flag, parental-permission status (recorded by the warden's office).

**Statuses:** `Draft → Submitted → Mentor Approved → Parent Permission Recorded → Warden Approved → Exited → Returned`. Side statuses: `Rejected`, `Expired`, `Escalated` (emergency), `Overdue`, `Manual Fallback`, `Awaiting Parent Permission`.

**Accountable owner:** Chief Warden (process and exceptions). The mentor is accountable for academic clearance only.

**Approval boundary (proposal):**
- Mentor approves or delegates. If silent beyond a window (Assumption: 24 h or until next evening), the request routes to the warden, as happens today.
- Warden approves hostel clearance, and only after parental permission is recorded. The tracker records that permission (yes or no, by which role, when) but does not change how it is obtained. Only the Chief Warden approves leaves outside the rules (emergency, unusual dates).
- Guards cannot approve; they only mark Exited or Returned against a pass code.
- Late-night departures stay not permitted; the system blocks submission after a cut-off (Assumption: to be confirmed with the warden).

**Pass:** an approved request gets a short code and a one-page printable pass replacing the three parts.

**Audit record (specified):** one append-only row per action with request id, actor role (not name), action, old status, new status, timestamp and reason code. No free text. Only the Chief Warden's office can read it. It is how the unauthorized and failed-step cases are reviewed.

**Fallback:** if the SIS or network is down, use the paper form, the guard keeps a manual register, and entries are reconciled into the SIS within one working day.

**Ordinary software or AI?** Ordinary software and rules are enough: a status machine, role checks, a duplicate rule (same student and overlapping dates) and a cut-off time. I see no step where AI adds value. If anyone later adds an AI helper (for example, drafting reminders), it must never approve, reject or change a status.

## 5. Five synthetic test cases (all data fictional; not run on a live system)
| # | Case | Input | Expected result | Who decides | Recovery |
|---|---|---|---|---|---|
| 1 | Normal | S1 submits for a festival; mentor and warden approve | Submitted → Mentor Approved → Parent Permission Recorded → Warden Approved; pass issued; guard marks Exited then Returned | Mentor, then warden | None needed |
| 2 | Missing information | S2 submits without a return date | Rejected with a message naming the field; stays Draft | Rule (system) | Student completes it and resubmits |
| 3 | Duplicate | S3 submits the same dates twice | Second request blocked and linked to the first; student sees existing status | Rule (system) | Warden can cancel the old one if dates changed |
| 4 | Unauthorized | Person B tries to submit or collect a pass for S4, or a guard tries to approve | Refused; attempt written to the audit record | Rule (system); Chief Warden reviews the log | Student or warden raises a correction |
| 5 | Failed step | SIS is down when S5 must leave, or the mentor never responds | Mentor silent: routes to warden. SIS down: paper fallback and manual guard register | Warden (routing); guard (manual register) | Reconciled within one working day; status Manual Fallback then Returned |

## 6. Net time saved (formula and ranges)
**Per leave:** student saving = current − proposed. Proposed time is about 10 min (range 8-15: online submit plus showing the pass at gates). Student saving is **16 / 38.5 / 58 min**.
Staff saving (Assumption): 6 signatures × 0.5 min = 3 min today, 2 digital approvals × 0.5 min = 1 min, so **2 min**. Review of exceptions (Assumption): 5% × 5 min = **0.25 min** per leave.
Net per leave = student saving + 2 − 0.25 = **17.75 / 40.25 / 59.75 min**. The parental-permission step is not changed by the redesign, so no saving is claimed for it.

**Per event or week:** net hours = leaves × net per leave ÷ 60 − support hours. Support effort (Assumption, scaled with about 4,000 hostelers): 2 h in a normal week, 20 h in a festival or holiday event.

| Scenario | Leaves (low / mid / high) | Gross mid (h) | Support (h) | Net hours saved (low / **mid** / high) |
|---|---|---|---|---|
| Normal week (0.5-2% leave) | 20 / 40 / 80 | 27 | 2 | 4 / **25** / 78 |
| Short festival break (500 reported floor / 1,000 assumed / 50% of hostelers) | 500 / 1,000 / 2,000 | 671 | 20 | 128 / **651** / 1,972 |
| Long holiday (85-95% leave) | 3,400 / 3,800 / 3,800 | 2,549 | 20 | 986 / **2,529** / 3,764 |

**Per month (mid case):**
| Month type | Leaves | Signatures (6 per leave) | Student hours today | Net hours saved |
|---|---|---|---|---|
| Quiet month (4 normal weeks) | 160 | 960 | 129 | 99 |
| Festival month (1 short festival break + 3 normal weeks) | 1,120 | 6,720 | 905 | 725 |
| Long-holiday month (1 holiday + 3 normal weeks) | 3,920 | 23,520 | 3,169 | 2,604 |

**Implementation effort (Assumption):** 40-200 hours of developer and testing time, one-off (reusing the existing SIS form is the low end). At the mid festival case (about 650 net hours) a 200-hour build is repaid in one event; at the low case (about 130 hours) it takes two or three events, or one long holiday (about 990 net hours even in the low case). In quiet months the net saving is small, so the case rests on peak weeks.

## 7. Risks and unknowns
- How parents' permission is obtained (call, message or form) is unknown. If it is slow, it may be the real bottleneck at peaks and the savings above would be overstated. Emergency leave handling, handling of duplicate or on-behalf requests, and any record of who is out of the hostel were not answered; I treat them as assumptions.
- Guards need a screen or pass-code check at two gates; that is untested.
- Leave shares and the 4,000 figure are approximate; results scale linearly with them. The festival volume rests on one reported floor (500+) and an assumed doubling; one count from the warden office would replace it. The long-holiday figures are estimates with no reported count behind them.
- Staff may not respond digitally faster than they sign on paper; the mentor wait is the biggest uncertainty.

## 8. What would make me abandon or change the design
If the warden office says wet signatures are mandatory under hostel rules, I would change the design to a digital pre-check that still prints a signed pass. If most of the student's time at the warden office is spent waiting for parental permission, I would redesign around that step, for example with a one-tap parent confirmation, which would need the college's approval. If timing 10 real leaves shows a median under 15 minutes, the per-request problem is small and the case rests only on peak volume.

## 9. Limitations
- Mainly my own experience as a hosteler, with one second-hand volume report.
- Times and shares are estimates; no stopwatch sample.
- I could not get a count of forms signed on 16 Oct. The festival range (500 / 1,000 / 2,000) rests on one reported floor and two assumptions, so I give a range and not a single figure.
- That the warden has no signing limit and signs after parental permission is my own understanding, unconfirmed.
- No live testing; expected results are design expectations.
- Fine amounts, cut-off time, delegation window and staff signing times are assumptions.
- No student data was collected.

## 10. My contribution
The process is one I use myself as a hosteler, so the steps, handoffs and exceptions come from my own experience. I got the volume figures (about 4,000 hostelers, 500+ leaves on a peak day) by asking a friend, and I used them as reported, not as verified. AI (Claude) helped me structure the report, set out the evidence log, and do the arithmetic and ranges; the estimates for rework, support and build effort are its assumptions, which I have labelled. I told the assistant that the warden signs any number of forms once parents give permission; that is my own understanding and I have not confirmed it with the warden office. I have not timed a leave with a stopwatch.
