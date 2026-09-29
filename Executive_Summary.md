# Executive Summary  
**EduPro Learner Demographics and Course Enrollment Behavior Analysis**

**Prepared for:** Toronto Government Parks, Forestry & Recreation  
**In partnership with:** Unified Mentor  
**Analysis Year:** 2025  
**Date:** September 2026  

---

## Purpose
This analysis delivers foundational, descriptive learner intelligence for the EduPro online learning platform. It answers who the learners are and how they choose courses, enabling data-driven decisions on course design, marketing, inclusivity, and platform growth. The study is strictly descriptive — no predictive modeling or monetization analysis was performed.

## Dataset at a Glance
| Entity        | Records |
|---------------|---------|
| Learners      | 3,000   |
| Courses       | 60      |
| Enrollments   | 10,000  |

Data integrated across three sheets (Users, Courses, Transactions) using UserID and CourseID.

## Key Findings

### 1. Age Distribution
- The **26–35 age band** is the dominant active segment (**48.0%** of enrollments, 4,799 enrollments).
- **18–25** is the second-largest cohort (**37.3%**, 3,732 enrollments).
- Learners under 18 account for **14.7%** (1,469 enrollments).
- No learners aged 36+ appear in the active enrollment data.
- Unique learners: 1,446 (26–35), 1,121 (18–25), 433 (<18).
- **Implication:** Platform primarily serves young working professionals and university-age learners.

### 2. Gender Participation
- Female learners hold a **marginal majority at 50.8%** of enrollments (5,078).
- Male participation is 49.2% (4,922).
- **Implication:** Gender balance is healthy and nearly equal.

### 3. Course Category Popularity
- **Data Science** ranks first with **916 enrollments**.
- Close followers: Finance (864), Web Development (844), Business (833), Project Management & Artificial Intelligence (829 each).
- Demand is relatively evenly distributed across the 12 categories (range ~806–916).
- **Implication:** Technical and business-oriented offerings drive engagement; no single category monopolizes demand.

### 4. Course Level Preference
- **Beginner-level** courses are preferred at **35.7%** (3,573 enrollments).
- Advanced: **34.8%** (3,475).
- Intermediate: **29.5%** (2,952) — a relative dip.
- Gender differences in level preference are negligible.
- **Implication:** Many learners enter at foundational level or move toward advanced content; intermediate pathways can be strengthened.

### 5. Course Type & Behavioral Patterns
- Free courses dominate (**64.0%** of enrollments).
- Average courses per learner: **3.33**.
- All 3,000 registered learners have at least one enrollment.

## Recommended Actions for Stakeholders

1. **Course Portfolio**  
   - Maintain and expand Data Science / AI / Finance / Web Development pathways.  
   - Design clearer Intermediate “bridge” courses to address the observed dip.

2. **Marketing & Outreach**  
   - Prioritize messaging to the 26–35 segment while sustaining strong presence among 18–25.  
   - Continue gender-balanced campaigns.

3. **Learner Experience**  
   - Surface personalized beginner-to-intermediate recommendations.  
   - Leverage the high free-course uptake as an onboarding funnel.

4. **Inclusivity & Accessibility**  
   - Track participation ratios quarterly.  
   - Ensure content remains accessible across the 15–35 age range.

5. **Next Analytical Steps** (out of current scope)  
   - Completion / dropout analysis.  
   - Learning pathway sequence mining.  
   - Lightweight recommendation prototypes.

## Deliverables Provided
- Interactive Streamlit dashboard (filterable by age, gender, category, level)
- Full analysis script (`analysis.py`)
- Clean dataset (`EduPro_Dataset.xlsx`) matching project schema
- Technical documentation and this executive summary

## Conclusion
EduPro reaches a diverse and engaged learner base concentrated in the 18–35 range with near gender parity. By acting on the demographic and preference insights above, the platform can move from intuition-driven to evidence-based education planning, ensuring its offerings remain aligned with learner needs, preferences, and diversity.

---
*This summary is intended for government and institutional stakeholders. Detailed methodology, tables, and visualizations are available in the accompanying research paper and live dashboard.*
