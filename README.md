# EduPro Learner Demographics & Course Enrollment Behavior Analysis

**Complete project package** using the official EduPro Online Platform dataset.

## Project Overview
Descriptive analysis of who EduPro learners are and how they enroll in courses. Focus: demographics, category popularity, level preference, and cross-segment insights. No prediction or monetization.

## Dataset
- **File:** `EduPro_Dataset.xlsx` (clean project-scoped version)
- **Sheets:** Users (3,000), Courses (60), Transactions (10,000)
- Source: Official EduPro Online Platform workbook (Users / Courses / Transactions only; Teachers scoped out per requirements).

## Key Results (from analysis)
| Metric                        | Value      |
|-------------------------------|------------|
| Total Enrollments             | 10,000     |
| Unique Learners               | 3,000      |
| Avg Courses / Learner         | 3.33       |
| 26–35 Enrollment Share        | 48.0%      |
| Female Participation          | 50.8%      |
| Top Category                  | Data Science (916) |
| Beginner Level Share          | 35.7%      |
| Free Course Share             | 64.0%      |

## Deliverables

| File                    | Description                                      |
|-------------------------|--------------------------------------------------|
| `EduPro_Dataset.xlsx`   | Clean data (Users / Courses / Transactions)      |
| `analysis.py`           | Full descriptive analysis script                 |
| `app.py`                | Interactive Streamlit dashboard                  |
| `requirements.txt`      | Python dependencies                              |
| `Executive_Summary.md`  | Stakeholder-facing executive summary             |
| `Research_Paper.md`     | Technical research report                        |
| `README.md`             | This file                                        |

## How to Run

```bash
pip install -r requirements.txt
python analysis.py          # prints all KPIs and tables
streamlit run app.py        # launches interactive dashboard
```

## Dashboard Modules
1. **Demographics** – Age-band bar, gender pie, unique-learner counts  
2. **Age-wise Enrollments** – Heatmap (Age × Category), Age × Level, Age × Type  
3. **Gender Preferences** – Level preference by gender, top categories by gender  
4. **Category & Level Popularity** – Ranking, level pie, Free vs Paid  

Sidebar filters: Age Group · Gender · Course Category · Course Level (all update KPIs and charts live).

## Notes
- Analysis is strictly descriptive and matches the original problem statement.
- All numbers in the reports are derived directly from the official dataset.
