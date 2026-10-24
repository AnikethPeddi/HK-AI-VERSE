# Task 2: Audit and redesign of the CSE curriculum

Student work, not an official syllabus revision. Evidence labels: **Observed** (seen in a handout or official page), **Hypothesis** (not yet verified), **JD** (supported by a dated job description).

## 1. Programme, batch and version
**Baseline source:** course codes and credits come from my student information system (SIS), the college's official record for my registration and credit history. I have not seen a separate regulations or batch-syllabus document. The public structure page I linked is a newer scheme and is used only for comparison.

- Programme: B.Tech Computer Science and Engineering, IcfaiTech, IFHE Hyderabad.
- Batch: admission year 2023 is my inference from the transcript (first year 2023-24); the SIS shows "2027". This is unconfirmed.
- Curriculum version: my transcript's course codes (for example CS101, MT102) differ from the current official structure page (for example ES105, ES101). The page is a newer scheme. Credits also differ: Sem I is 21 on the page against 20 on my path, Sem II is 22 against 24, and the summer internship is 5 against 3. I use my SIS credit record as the credit base and the public page as a comparison.
- Regulations: I have not seen the academic regulations document. Minimum-credit and category rules are therefore unchecked (see limitations).

## 2. Credit map (full list in credit-map.csv)
| Semester | Credits |
|---|---|
| I | 20 |
| II | 24 |
| III | 23 |
| IV | 24 |
| Summer (Internship-I) | 3 |
| V | 21 |
| VI | 21 |
| VII (registered) | 16 |
| VIII (IP-2, planned) | 15 |
| **Total** | **167** |

## 3. Proposed changes (12 reasons; detail in proposed-changes.csv)
| # | Action | Course | Credits | Reason | Evidence |
|---|---|---|---|---|---|
| 1 | UPDATE | DS306 Deep Learning | 4 | RBMs and Boltzmann machines take lectures 25-29, 5 of 35; no transformers; ResNet/DenseNet only "beyond syllabus" | Observed |
| 2 | UPDATE | DS311 NLP | 3 | Syllabus stops at RNN/LSTM and encoder-decoder; no attention or transformers; two units labelled "Unit IV" | Observed |
| 3 | UPDATE | CS415 Ethical Hacking | 3 | Sniffing (lectures 24, 37), session hijacking (25, 39), DoS (26-27, 39) repeat; handout's gap table admits missing cloud/container, mobile, IoT; cloud is covered only by a 10% external Azure certificate | Observed |
| 4 | UPDATE | DS401 HCI | 3 | Handout's own gap table lists chatbots, emotion-aware UI, AI-driven UX, accessibility with no sessions | Observed |
| 5 | UPDATE | MG401 Entrepreneurship | 3 | Gap table lists digital tools, legal/IPR/GST, digital marketing; CO5 text mentions image analysis, which does not fit | Observed |
| 6 | REDUCE | EC102 Signal Processing | -3 | Speech features appear in NLP Unit V; vision content in CS305; fold remainder in | Hypothesis |
| 7 | REDUCE | DS303 Blockchain | -3 | Move from core to elective | Hypothesis (no JD found) |
| 8 | REDUCE | PHY101 -1, HS201 -1, MG201 -1, EC101 -1 | -4 | Light trims. Physics is 5 credits against Chemistry 4; the official page lists Physics at 4. MG401 already covers break-even and pricing | PHY101 Observed; others Hypothesis |
| 9 | ADD | Applied Generative AI and LLMs | +3 | No course covers transformers, RAG or prompting | Observed gap; JD3 (partial) |
| 10 | ADD | MLOps and Model Deployment Lab | +3 | DS306 gap table asks for model demonstration; no deployment course | Observed; JD1 |
| 11 | ADD | Cloud and Container Security Lab | +2 | CS415 gap table lists cloud and containers | Observed; JD2 |
| 12 | ADD | Human-AI Interaction and Accessible Design Studio | +2 | Delivers the missing DS401 content | Observed |

## 4. Balance and scale
- Base: 167. REDUCE: 10. ADD: 10. New total: 167 (balanced).
- Affected credits = UPDATE courses' full credits (16) + credits removed (10) + credits added (10) = 36, which is 21.6% of 167 (target 20-25%).
- Interactive check: credit-calculator.html (open in a browser; actions and credit amounts are editable).

### Credits by semester (semester-balance.csv)
Reductions fall in Sems I-V (-1, -1, -1, -4, -3 respectively, counting each course in its own semester) and additions in Sems V-VII, so Sem VI and VII become heavier. Check the table in the calculator before relying on it; a regulator may cap credits per semester.

## 5. Comparison with job descriptions (job-descriptions.csv)
| JD | Skills seen | Matches | Gap in current curriculum |
|---|---|---|---|
| JD1 Amgen, Associate ML Engineer, posted 2026-06-05 | MLOps pipelines, deployment, monitoring, MLflow/Kubeflow/Airflow, AWS/Databricks | Change 10 | No deployment or monitoring course; ML and Cloud exist as prerequisites |
| JD2 Insight Global, Container Security SME, posted 2026-04-14 | Container and Kubernetes security, remediation, scripting, CKS/CKA | Change 11 | CS415's lecture plan has no container or Kubernetes content (observed); cloud security appears only as the external NASSCOM Azure Security (AZ-500) certificate worth 10% of assessment, not as taught lectures or a lab. Role asks 4+ years, so only direction is evidence |
| JD3 Digitals AI, Generative AI Engineer (fresher), posted 2026-10-12 | Prompt engineering, testing, debugging, performance optimisation, production-ready code (responsibilities seen; the Requirements body was not readable) | Change 9 | Prompting is absent from the DL and NLP handouts; RAG and tool use are not confirmed by this posting |
Changes 7 and 12 have no JD support yet and stay labelled hypotheses.

## 6. Prerequisites and regulatory conditions
- Placement and prerequisites: change 9 in Sem VI (DS304); change 10 in Sem VII (DS304, CS307); change 11 in Sem VII (CS306, CS307; CS415 recommended); change 12 in Sem V (CS205). Prerequisites were kept to earlier semesters so each course can actually be taken in its slot.
- Removing or shrinking EC102, PHY101, HS201, MG201, EC101 and DS303 may breach minimum credits or mandatory category rules. These need the regulations and approval by the competent body before any real change.

## 7. Other deliverables in this folder
AI-use record: ai-use-record.md. Capstone: capstone-proposal.md. Faculty feedback: faculty-feedback.md. Sources: sources.csv.

## 8. Limitations
- I have not read the academic regulations document, so minimum-credit and category rules are unchecked. Every REDUCE is therefore conditional.
- Admission year 2023 is inferred from my SIS record (credits are official; only the batch label is inferred); my course codes differ from the current official structure page, so comparisons with that page are approximate.
- Only the five handouts for this semester were read in full. Rows 6-8 of the change table (EC102, DS303, PHY101, HS201, MG201, EC101) rest on course titles and are hypotheses, except that the official page lists Physics at 4 credits.
- DS304, CS307 and DS307 were not read, so "deployment and monitoring are absent" is unconfirmed.
- JD2 asks for 4+ years of experience and is a security role; JD3's Requirements text was not readable. The comparison shows direction, not entry-level demand.
- The AI exercises were run by Claude and checked by code or sources only partly (see ai-use-record.md). I re-ran the code checks for exercises 1, 2 and 5 myself on 24 Oct 2026 and got the same results; the Kneser-Ney and DNS statements are still unchecked against a source.
- No faculty or graduate feedback was obtained.
- Per-semester loads become uneven (Sem VI 24, Sem V 20) and I have not checked whether a per-semester cap applies.

## 9. Personal contribution
I am a final-year CSE student, and Task 2 is about my own degree. I supplied the course handouts, the SIS course list for Sem VII, my credit history (only codes and credits are used here, no grades), the fact that IP-2 is in Sem 8 for 15 credits, and the portal brief. I picked which courses and numbers go in. AI (Claude) wrote the first drafts of the report, tables, calculator and capstone, read the official structure page and found the job postings. It also ran the five AI exercises; I re-ran the code checks for exercises 1, 2 and 5 myself on 24 Oct 2026 and got the same results. Where something is a guess rather than something I read, the report says so.

## 9b. Handout cross-checks (against the uploaded handouts)
- DS306: lectures 25-29 are RBMs/Gibbs/DBMs (5 of 35); no transformers; ResNet/DenseNet only in the beyond-syllabus list. Confirmed.
- DS401: sessions 24-26 already teach heuristics and patterns; the gap table lists chatbots, emotion-aware UI, AI-driven UX, ethics and WCAG with no sessions. Confirmed.
- CS415: repeats confirmed (sniffing 24/37, hijacking 25/39, DoS 26-27/39, ARP/DNS spoofing 38/41). Cloud security is covered only by the external NASSCOM Azure certificate (10%).
- MG401: gap table lists digital tools, legal/IPR/GST, digital marketing; lean canvas (35-37) and break-even (41) are taught. Confirmed.
- NLP slides: no attention or transformers listed, but the second Unit IV already covers dialog systems/chatbots and speech recognition, so change 12 (chatbots) overlaps partly with DS311 and should stress accessibility and AI-driven UX instead.

## 10. Chosen role and strongest claim
Target role: entry-level AI application engineer.
JD1 and JD3 support changes 10 and 9 directly. JD2 is a senior container-security contract role (4+ years), so it is used only as evidence of skill direction for change 11, not of entry-level demand.
Strongest claim: the five handouts I read contain no practised deployment, monitoring or LLM-application content. I have NOT read the DS304, CS307 or DS307 handouts, so this claim is unconfirmed. It would be disproved if those handouts already cover deployment and monitoring with labs; in that case change 10 would be weakened and should become an UPDATE to CS307 instead of an ADD.
Absent versus present: see jd-requirement-map.csv.
