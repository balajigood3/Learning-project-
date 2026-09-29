"""
EduPro Learner Analytics Dashboard
Streamlit interactive application for descriptive learner intelligence.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Page config
st.set_page_config(
    page_title="EduPro Learner Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 2.2rem; font-weight: 700; color: #1f4e79; margin-bottom: 0.2rem;}
    .sub-header {font-size: 1.1rem; color: #555; margin-bottom: 1.5rem;}
    .kpi-box {background: #f0f7ff; border-radius: 10px; padding: 1rem; text-align: center; border-left: 4px solid #1f4e79;}
    .kpi-value {font-size: 1.8rem; font-weight: 700; color: #1f4e79;}
    .kpi-label {font-size: 0.9rem; color: #666;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    path = Path(__file__).parent / "EduPro_Dataset.xlsx"
    users = pd.read_excel(path, sheet_name="Users")
    courses = pd.read_excel(path, sheet_name="Courses")
    trans = pd.read_excel(path, sheet_name="Transactions")
    df = trans.merge(users, on="UserID").merge(courses, on="CourseID")
    
    def age_band(age):
        if age < 18: return "<18"
        elif age <= 25: return "18-25"
        elif age <= 35: return "26-35"
        elif age <= 45: return "36-45"
        else: return "45+"
    
    df["AgeBand"] = df["Age"].apply(age_band)
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.title("🔍 Filters")
st.sidebar.markdown("---")

age_options = ["All"] + sorted(df["AgeBand"].unique().tolist())
selected_age = st.sidebar.multiselect("Age Group", options=age_options[1:], default=age_options[1:])

gender_options = sorted(df["Gender"].unique().tolist())
selected_gender = st.sidebar.multiselect("Gender", options=gender_options, default=gender_options)

cat_options = sorted(df["CourseCategory"].unique().tolist())
selected_cat = st.sidebar.multiselect("Course Category", options=cat_options, default=cat_options)

level_options = sorted(df["CourseLevel"].unique().tolist())
selected_level = st.sidebar.multiselect("Course Level", options=level_options, default=level_options)

# Apply filters
mask = (
    df["AgeBand"].isin(selected_age if selected_age else df["AgeBand"].unique()) &
    df["Gender"].isin(selected_gender if selected_gender else df["Gender"].unique()) &
    df["CourseCategory"].isin(selected_cat if selected_cat else df["CourseCategory"].unique()) &
    df["CourseLevel"].isin(selected_level if selected_level else df["CourseLevel"].unique())
)
filtered = df[mask]

# Header
st.markdown('<p class="main-header">📊 EduPro Learner Analytics</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Learner Demographics & Course Enrollment Behavior Analysis</p>', unsafe_allow_html=True)

# KPI row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-value">{len(filtered):,}</div>
        <div class="kpi-label">Total Enrollments</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-value">{filtered['UserID'].nunique():,}</div>
        <div class="kpi-label">Unique Learners</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    avg = filtered.groupby("UserID").size().mean() if len(filtered) > 0 else 0
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-value">{avg:.1f}</div>
        <div class="kpi-label">Avg Courses / Learner</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    female_pct = (filtered["Gender"] == "Female").mean() * 100 if len(filtered) > 0 else 0
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-value">{female_pct:.1f}%</div>
        <div class="kpi-label">Female Participation</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "👥 Demographics", 
    "📈 Age-wise Enrollments", 
    "♀️ Gender Preferences", 
    "📚 Category & Level Popularity"
])

with tab1:
    st.subheader("Learner Demographic Overview")
    c1, c2 = st.columns(2)
    
    with c1:
        age_counts = filtered["AgeBand"].value_counts().reindex(["<18", "18-25", "26-35", "36-45", "45+"]).fillna(0)
        fig_age = px.bar(
            x=age_counts.index, y=age_counts.values,
            labels={"x": "Age Band", "y": "Enrollments"},
            title="Enrollments by Age Band",
            color=age_counts.values,
            color_continuous_scale="Blues"
        )
        fig_age.update_layout(showlegend=False, coloraxis_showscale=False)
        st.plotly_chart(fig_age, use_container_width=True)
    
    with c2:
        gender_counts = filtered["Gender"].value_counts()
        fig_gender = px.pie(
            values=gender_counts.values, names=gender_counts.index,
            title="Gender Distribution",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_gender, use_container_width=True)
    
    st.markdown("#### Unique Learners by Age Band")
    unique_age = filtered.groupby("AgeBand")["UserID"].nunique().reindex(["<18", "18-25", "26-35", "36-45", "45+"]).fillna(0).astype(int)
    st.dataframe(pd.DataFrame({"Age Band": unique_age.index, "Unique Learners": unique_age.values}), hide_index=True, use_container_width=True)

with tab2:
    st.subheader("Age-wise Enrollment Patterns")
    
    # Age × Category heatmap
    cross = pd.crosstab(filtered["AgeBand"], filtered["CourseCategory"])
    if not cross.empty:
        fig_heat = px.imshow(
            cross,
            labels=dict(x="Course Category", y="Age Band", color="Enrollments"),
            title="Age Band × Course Category Heatmap",
            color_continuous_scale="YlGnBu",
            aspect="auto"
        )
        st.plotly_chart(fig_heat, use_container_width=True)
    
    # Age × Level
    c1, c2 = st.columns(2)
    with c1:
        age_level = pd.crosstab(filtered["AgeBand"], filtered["CourseLevel"])
        fig_al = px.bar(age_level, barmode="group", title="Age Band vs Course Level")
        st.plotly_chart(fig_al, use_container_width=True)
    with c2:
        age_type = pd.crosstab(filtered["AgeBand"], filtered["CourseType"])
        fig_at = px.bar(age_type, barmode="group", title="Age Band vs Course Type")
        st.plotly_chart(fig_at, use_container_width=True)

with tab3:
    st.subheader("Gender-based Course Preference Analysis")
    
    c1, c2 = st.columns(2)
    with c1:
        g_level = pd.crosstab(filtered["Gender"], filtered["CourseLevel"], normalize="index") * 100
        fig_gl = px.bar(g_level, barmode="group", title="Course Level Preference by Gender (%)")
        st.plotly_chart(fig_gl, use_container_width=True)
    
    with c2:
        g_cat = filtered.groupby(["Gender", "CourseCategory"]).size().reset_index(name="Count")
        top_cats = filtered["CourseCategory"].value_counts().head(6).index
        g_cat = g_cat[g_cat["CourseCategory"].isin(top_cats)]
        fig_gc = px.bar(g_cat, x="CourseCategory", y="Count", color="Gender", barmode="group",
                        title="Top Categories by Gender")
        st.plotly_chart(fig_gc, use_container_width=True)
    
    st.markdown("#### Gender × Level (% within gender)")
    st.dataframe(g_level.round(1), use_container_width=True)

with tab4:
    st.subheader("Course Category & Level Popularity")
    
    c1, c2 = st.columns(2)
    with c1:
        cat_counts = filtered["CourseCategory"].value_counts().sort_values(ascending=True)
        fig_cat = px.bar(
            x=cat_counts.values, y=cat_counts.index, orientation="h",
            title="Enrollments by Course Category",
            labels={"x": "Enrollments", "y": "Category"},
            color=cat_counts.values,
            color_continuous_scale="Teal"
        )
        fig_cat.update_layout(showlegend=False, coloraxis_showscale=False)
        st.plotly_chart(fig_cat, use_container_width=True)
    
    with c2:
        level_counts = filtered["CourseLevel"].value_counts()
        fig_level = px.pie(
            values=level_counts.values, names=level_counts.index,
            title="Course Level Distribution",
            hole=0.35,
            color_discrete_sequence=["#2ecc71", "#3498db", "#e74c3c"]
        )
        st.plotly_chart(fig_level, use_container_width=True)
    
    # Type
    type_counts = filtered["CourseType"].value_counts()
    fig_type = px.bar(x=type_counts.index, y=type_counts.values, title="Free vs Paid Enrollments",
                      color=type_counts.index, color_discrete_map={"Free": "#27ae60", "Paid": "#2980b9"})
    st.plotly_chart(fig_type, use_container_width=True)

# Footer
st.markdown("---")
st.caption("EduPro Learner Analytics Dashboard | Descriptive Analysis only | Unified Mentor × Toronto Government Parks, Forestry & Recreation")
st.caption("Data: Synthetic dataset generated to match project schema (3,000 learners · 60 courses · 10,000 transactions)")
