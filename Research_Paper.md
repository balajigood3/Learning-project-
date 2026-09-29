# Learner Demographics and Course Enrollment Behavior Analysis on EduPro

**Technical Research Report**

Submitted to: Toronto Government Parks, Forestry & Recreation  
In partnership with: Unified Mentor  
Analysis Year: 2025  
Date: September 2026  

---

## 1. Abstract

This report presents a comprehensive descriptive analysis of learner demographics and course enrollment behavior on the EduPro online learning platform. Using integrated data from 3,000 registered learners, 60 courses spanning 12 subject categories, and 10,000 enrollment transactions recorded throughout the 2025 academic year, the study answers core questions about age distribution, gender participation, category popularity, and level preferences.

Key findings reveal that the **26–35 age group constitutes the largest active segment (48.0% of enrollments)**, female learners hold a marginal participation majority at **50.8%**, **Data Science** ranks as the most popular course category with **916 enrollments**, and **Beginner-level courses** remain the most preferred skill tier at **35.7%** of all enrollments. An interactive Streamlit analytics dashboard was developed as the primary deliverable, providing real-time filterable insights across four analytical modules.

The work supplies foundational learner intelligence that enables data-driven decision-making in course design, targeted outreach, and platform growth strategy. No predictive modeling or monetization analysis was performed.

**Keywords:** learner analytics, demographic segmentation, course enrollment behavior, descriptive analytics

---

## 2. Background and Context

Online learning platforms serve diverse learners with varying age groups, gender distributions, learning goals, and subject interests. For EduPro, understanding who the learners are and how they choose courses is foundational for designing relevant courses, improving engagement, targeted marketing, and enhancing inclusivity.

This project focuses exclusively on descriptive learner intelligence.

---

## 3. Problem Statement

Despite having user and transaction data, EduPro lacked clear answers to:

- Which age groups are most active?
- How do enrollment patterns differ by gender?
- What course categories are preferred by different segments?
- Are beginner, intermediate, or advanced courses more popular among specific age groups?

Without these insights, decisions remain intuition-driven rather than data-driven.

---

## 4. Dataset and Methodology

### 4.1 Dataset Composition

| Sheet         | Records | Fields Used (project scope)                          |
|---------------|---------|------------------------------------------------------|
| Users         | 3,000   | UserID, UserName, Age, Gender                        |
| Courses       | 60      | CourseID, CourseName, CourseCategory, CourseType, CourseLevel |
| Transactions  | 10,000  | TransactionID, UserID, CourseID, TransactionDate     |

(Additional sheets Teachers and extra transaction fields exist in the source workbook but were scoped out per project requirements.)

### 4.2 Data Integration
Tables joined on UserID and CourseID. Full referential integrity confirmed — every transaction maps to a valid user and course. All 3,000 registered learners appear in at least one transaction.

### 4.3 Analytical Steps
1. Segment learners into age bands (<18, 18–25, 26–35, 36–45, 45+).
2. Analyze gender distribution and participation.
3. Count enrollments by CourseCategory, CourseType, CourseLevel.
4. Cross-tabulate Age × Category, Age × Level, Gender × Level.
5. Compute average courses per learner and concentration metrics.

### 4.4 Tools
Python (pandas), Streamlit + Plotly for the interactive dashboard.

---

## 5. Key Performance Indicators

| KPI                              | Value                          |
|----------------------------------|--------------------------------|
| Total Enrollments                | 10,000                         |
| Unique Active Learners           | 3,000                          |
| Avg Courses per Learner          | 3.33                           |
| 26–35 Enrollment Share           | 48.0%                          |
| Female Participation Ratio       | 50.8%                          |
| Top Category (Data Science)      | 916 enrollments                |
| Beginner Level Share             | 35.7%                          |
| Free Course Share                | 64.0%                          |

---

## 6. Results and Insights

### 6.1 Age Distribution
| Age Band | Enrollments | Share | Unique Learners |
|----------|-------------|-------|-----------------|
| <18      | 1,469       | 14.7% | 433             |
| 18–25    | 3,732       | 37.3% | 1,121           |
| 26–35    | 4,799       | 48.0% | 1,446           |
| 36–45    | 0           | 0%    | 0               |
| 45+      | 0           | 0%    | 0               |

**Insight:** EduPro primarily serves learners aged 15–35, with the strongest concentration among early-career professionals (26–35).

### 6.2 Gender Participation
Female 50.8% (5,078) · Male 49.2% (4,922). Near parity; healthy inclusivity baseline.

### 6.3 Course Category Popularity
Data Science (916) leads, followed closely by Finance (864), Web Development (844), Business (833), Project Management & AI (829 each). Demand is relatively balanced across 12 categories.

### 6.4 Course Level Preference
Beginner 35.7% · Advanced 34.8% · Intermediate 29.5%. The Intermediate dip suggests opportunity for stronger bridge content. Level preferences are virtually identical across genders.

### 6.5 Cross-Segment Patterns
Age × Level and Age × Category cross-tabs show consistent patterns: all three age bands enroll across levels and categories, with absolute volume highest in 26–35. Free courses dominate (64%).

### 6.6 Behavioral Metrics
Average 3.33 courses per learner. All registered users are active. Enrollment concentration is moderate.

---

## 7. Streamlit Dashboard

Four modules with live filters (Age Group, Gender, Course Category, Course Level):

1. Learner demographic overview  
2. Age-wise enrollment charts & heatmaps  
3. Gender-based preference analysis  
4. Category & level popularity visuals  

---

## 8. Recommendations

1. Expand Data Science / AI / Finance / Web pathways.  
2. Design clearer Intermediate bridge courses.  
3. Prioritize 26–35 outreach while sustaining 18–25.  
4. Use free courses as onboarding funnel.  
5. Monitor participation ratios quarterly.  
6. Future work: completion analysis, pathway mining, recommenders.

---

## 9. Conclusion

This project provides foundational learner intelligence for EduPro. By systematically analyzing who the learners are and how they enroll, the platform can move toward data-driven education planning aligned with learner needs, preferences, and diversity.

---

## 10. Deliverables

- `EduPro_Dataset.xlsx` — Clean project-scoped data  
- `analysis.py` — Reproducible analysis script  
- `app.py` — Streamlit dashboard  
- `requirements.txt`  
- `Executive_Summary.md`  
- `Research_Paper.md` (this document)  
- `README.md`  

---
*End of Report*
