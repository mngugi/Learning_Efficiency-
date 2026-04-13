# 📘 Learning Efficiency API

> A Django REST API for measuring and tracking research preparation efficiency, grounded in three interlocking learning science theories.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![REST API](https://img.shields.io/badge/REST-API-FF6B35?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## The Model

$$
L_e = \frac{K_g \times R_q}{T_s \times C_l}
$$

| Symbol | Variable | Range | Theoretical Grounding |
|--------|----------|-------|----------------------|
| `Le` | Learning Efficiency | computed | Composite output score |
| `Kg` | Knowledge gained | 0–100 | Ebbinghaus — retained knowledge after forgetting decay |
| `Rq` | Research quality weight | 0.0–1.0 | Bibliometric credibility weighting (h-index, field normalisation) |
| `Ts` | Study time (hours) | > 0 | Ebbinghaus — time-on-task relative to retention curve |
| `Cl` | Cognitive load index | 1–10 | Sweller's CLT — intrinsic + extraneous + germane load |

**Compression Rate:**
```
Lc = PapersRead / StudyTime
```

The formula encodes a key insight: efficiency is not just about how much you study, it is about **what you retain** (`Kg`), **how reliable your sources are** (`Rq`), and **how much mental overhead you carry** (`Cl`). Each variable maps directly to one of the three theoretical pillars below.

---

## Theoretical Foundations

### 1 · Cognitive Load Theory — Sweller (1988)

The `Cl` (cognitive load index, 1–10) is a direct operationalisation of Sweller's framework. Working memory holds roughly 4 chunks at a time. When it overflows, learning halts — no matter how many hours are logged.

Sweller identified three load types that together must not exceed working memory capacity:

```
┌──────────────────┬────────────────────┬──────────────────────┐
│  INTRINSIC       │  EXTRANEOUS        │  GERMANE             │
│                  │                    │                      │
│ Complexity of    │  Caused by poor    │  Schema-building     │
│ the material     │  presentation,     │  effort — the goal   │
│ itself           │  split attention,  │  of all instruction  │
│                  │  redundancy        │                      │
│  Fixed — managed │  Minimise this     │  Maximise this       │
│  via sequencing  │                    │                      │
└──────────────────┴────────────────────┴──────────────────────┘
  Total Load  =  Intrinsic  +  Extraneous  +  Germane  ≤  Capacity

```


**How `Cl` maps to load types:**

| `Cl` Score | Interpretation |
|------------|----------------|
| 1–3 | Low load — germane processing dominates, deep schema formation likely |
| 4–6 | Moderate load — efficient study under normal conditions |
| 7–8 | High load — extraneous sources likely present; review session design |
| 9–10 | Overload — learning efficiency collapses; split sessions recommended |

> A session with `Cl = 9` and `Kg = 80` scores lower than one with `Cl = 3` and `Kg = 70`. The model correctly penalises cognitive overload even when perceived knowledge gain appears high.

---

### 2 · Ebbinghaus Forgetting Curve (1885)

`Kg` is not raw input — it represents **retained** knowledge, shaped by the forgetting curve. Ebbinghaus showed that without reinforcement, memory decays exponentially:

$$
R = e^{-t/S}
$$

Where `R` = retention, `t` = time elapsed, `S` = memory stability (grows with each successful retrieval).

```
Retention
  100% │▓
       │ ▓▓
   75% │    ▓▓▓
       │        ▓▓▓▓
   50% │             ▓▓▓▓▓
       │                   ▓▓▓▓▓▓▓▓
   25% │                            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
       └────────────────────────────────────────────────▶ Time
         20min  1hr   9hr  1day  2days  6days  31days
```

**Spaced repetition optimal review intervals:**

| Review # | Interval | Rationale |
|----------|----------|-----------|
| 1st | 1 day | Catch decay before the steepest drop |
| 2nd | 6 days | Stability `S` has grown — safe to wait longer |
| 3rd | 14 days | Each retrieval flattens the next curve |
| 4th | 30 days | Long-term consolidation phase |
| 5th+ | 60+ days | Near-permanent retention |

**Implication for the API:** `Kg` scores logged immediately after a session will be higher than true retained knowledge measured days later. A planned `forgetting_decay` field — calculated as `Kg × e^(−t/S)` — is in the roadmap to model this drift over time.

> **Bjork (1994) — Desirable Difficulties:** Retrieval practice is more powerful than re-reading. A session involving active recall yields higher true `Kg` than passive review of the same duration, even when the immediate subjective score feels lower.

---

### 3 · Bibliometric Credibility Weighting

`Rq` (research quality weight, 0.0–1.0) encodes the credibility of sources consulted in a session. It is informed by bibliometric indices drawn from the literature on research quality measurement.

**Credibility tiers — how to assign `Rq`:**

```
Rq Range     Source Tier        Bibliometric Signal
──────────────────────────────────────────────────────────────────
0.90–1.00    Tier 1 journals    High Eigenfactor, Q1 SCImago,
                                field-normalised citation score > 2.0

0.70–0.89    Peer-reviewed      h-index authors, i10-index > 10,
             conferences        cited in systematic reviews

0.50–0.69    Preprints /        arXiv, SSRN — traceable but
             working papers     not yet peer-reviewed

0.30–0.49    Grey literature    Technical reports, white papers,
                                institutional publications

0.10–0.29    Informal sources   Blogs, forum posts, undated content

0.00–0.09    Uncredentialed     No author, no date, no citations
```

**Key bibliometric indices that inform `Rq`:**

| Index | Definition | Strength |
|-------|-----------|---------- |
| **h-index** (Hirsch, 2005) | `h` papers each cited ≥ `h` times | Balances breadth and depth of output |
| **Field-normalised score** | Paper citations ÷ field & year average | Corrects for discipline citation norms |
| **Eigenfactor** | PageRank-style weighting by journal influence | High-impact citing journals count more |
| **Altmetrics** | Policy, media, and social mention tracking | Captures real-world and societal impact |

> A session reading 4 Nature papers (`Rq = 0.95`) outscores a session reading 12 blog posts (`Rq = 0.20`) at identical `Kg` and `Cl`. The model correctly reflects that source quality mediates knowledge reliability.

---

## How the Three Theories Interact

```
  WHAT to trust          HOW efficiently         WHEN to revisit
  ─────────────          ───────────────         ───────────────
  Bibliometrics    ───►   CLT-aware study   ───►  Spaced repetition
  sets Rq                 minimises Cl            schedules Kg decay

  Poor Rq contaminates    High Cl wastes          Without review,
  Kg — bad sources        capacity even on        Kg decays to ~25%
  corrupt retained        good material           within a week
  knowledge
```

The formula `Le = (Kg × Rq) / (Ts × Cl)` is not arbitrary — it is a compression of this three-way interaction. Maximising `Le` requires attending to all three simultaneously: credible sources, managed cognitive load, and retention-aware scheduling.

---

## Project Structure

```
project/
├── manage.py
├── requirements.txt
├── learning_efficiency/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── research/
    ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── services.py          ← Le formula + grade logic lives here
    ├── urls.py
    └── migrations/
```

---

## Setup

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/sessions/` | List all sessions |
| `POST` | `/api/sessions/` | Create new session |
| `GET` | `/api/sessions/{id}/` | Retrieve session |
| `PUT` | `/api/sessions/{id}/` | Update session |
| `DELETE` | `/api/sessions/{id}/` | Delete session |
| `GET` | `/api/sessions/analytics/` | Aggregate statistics |
| `GET` | `/api/sessions/top/` | Top 5 most efficient sessions |

---

## Example Request

```bash
POST /api/sessions/
Content-Type: application/json

{
    "title": "AI Security Papers",
    "papers_read": 6,
    "study_time_hours": 4,
    "knowledge_score": 85,
    "research_quality": 0.92,
    "cognitive_load": 5,
    "notes": "Focused on adversarial ML and prompt injection"
}
```

### Example Response

```json
{
    "id": 1,
    "title": "AI Security Papers",
    "papers_read": 6,
    "study_time_hours": 4.0,
    "knowledge_score": 85.0,
    "research_quality": 0.92,
    "cognitive_load": 5.0,
    "notes": "Focused on adversarial ML and prompt injection",
    "learning_efficiency": 3.91,
    "compression_rate": 1.5,
    "efficiency_grade": "Moderate",
    "created_at": "2025-03-01T08:00:00Z",
    "updated_at": "2025-03-01T08:00:00Z"
}
```

### Analytics Response

```bash
GET /api/sessions/analytics/
```

```json
{
    "total_sessions": 12,
    "mean_efficiency": 4.23,
    "max_efficiency": 9.75,
    "min_efficiency": 1.20,
    "stdev_efficiency": 2.14,
    "mean_compression_rate": 1.85,
    "total_papers_read": 72,
    "total_study_hours": 38.5
}
```

---

## Efficiency Grade Scale

| `Le` Score | Grade | CLT Interpretation |
|------------|-------|--------------------|
| ≥ 15 | 🟢 Exceptional | Low `Cl`, high `Rq`, strong retention |
| ≥ 10 | 🔵 High | Well-managed load, credible sources |
| ≥ 5  | 🟡 Moderate | Typical research session |
| ≥ 2  | 🟠 Low | High cognitive load or weak sources |
| < 2  | 🔴 Very Low | Overload or low-credibility material |

---

## Roadmap

- [ ] `forgetting_decay` field — apply `R = e^(−t/S)` to `Kg` over time (Ebbinghaus)
- [ ] Spaced repetition scheduler — surface sessions due for review at optimal intervals
- [ ] `Rq` auto-scoring via DOI lookup against Crossref / Semantic Scholar APIs
- [ ] `Cl` variance analysis — flag sessions where load spikes correlate with score drops
- [ ] Statistical validation (Pearson correlation, regression across sessions)
- [ ] Predictive efficiency forecasting (linear regression / ML)
- [ ] JWT multi-user authentication
- [ ] PDF research report export with per-session breakdown
- [ ] Dockerized deployment

---

## References

| Theory | Citation |
|--------|---------|
| Cognitive Load Theory | Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science, 12*(2), 257–285 |
| Forgetting Curve | Ebbinghaus, H. (1885). *Über das Gedächtnis*. Leipzig: Duncker & Humblot |
| Desirable Difficulties | Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In *Metacognition* |
| Testing Effect | Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning. *Psychological Science, 17*(3), 249–255 |
| h-index | Hirsch, J.E. (2005). An index to quantify an individual's scientific research output. *PNAS, 102*(46) |
| Eigenfactor | Bergstrom, C.T. (2007). Eigenfactor: Measuring the value and prestige of scholarly journals. *College & Research Libraries News* |

---

<sub>Built by <a href="https://github.com/mngugi">@mngugi</a> · Learning Science × Software Engineering</sub>
