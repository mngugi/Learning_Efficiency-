# Learning_Efficiency-
---

📘 Quantifying Learning Efficiency During Research Preparation

Django + **REST** **API** + Python

- We’ll structure it like a real research system.

We define:

$$
Le = (Kg × Rq) / (Ts × Cl)
$$

---
# Quantifying Learning Efficiency During Research Preparation

A Django REST API for measuring and tracking research preparation efficiency using a quantitative model.

## Mathematical Model

$$
L_e = \frac{K_g \times R_q}{T_s \times C_l}
$$

| Symbol | Variable | Range |
|--------|----------|-------|
| `Le` | Learning Efficiency | computed |
| `Kg` | Knowledge gained | 0–100 |
| `Rq` | Research quality weight | 0.0–1.0 |
| `Ts` | Study time (hours) | > 0 |
| `Cl` | Cognitive load index | 1–10 |

**Compression Rate:**

```
Lc = PapersRead / StudyTime
```

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
    ├── services.py
    ├── urls.py
    └── migrations/
```

## Setup

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

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

## Efficiency Grade Scale

| Le Score | Grade |
|----------|-------|
| ≥ 15 | Exceptional |
| ≥ 10 | High |
| ≥ 5 | Moderate |
| ≥ 2 | Low |
| < 2 | Very Low |

## Theoretical Basis

- **Cognitive Load Theory** — Sweller (1988)
- **Learning Efficiency** — Ebbinghaus forgetting curve
- **Research Quality Indexing** — Bibliometric credibility weighting

## Future Extensions

- [ ] Statistical validation (Pearson correlation, regression)
- [ ] Predictive efficiency forecasting (linear regression / ML)
- [ ] JWT multi-user authentication
- [ ] PDF research report export
- [ ] Ebbinghaus forgetting curve integration
- [ ] Dockerized deployment
