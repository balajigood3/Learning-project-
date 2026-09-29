"""
EduPro Learner Demographics & Course Enrollment Behavior Analysis
Full descriptive analysis on the official dataset.
"""

import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "EduPro_Dataset.xlsx"

users = pd.read_excel(DATA_PATH, sheet_name="Users")
courses = pd.read_excel(DATA_PATH, sheet_name="Courses")
transactions = pd.read_excel(DATA_PATH, sheet_name="Transactions")

df = (
    transactions
    .merge(users, on="UserID", how="inner")
    .merge(courses, on="CourseID", how="inner")
)

def age_band(age: int) -> str:
    if age < 18:
        return "<18"
    elif age <= 25:
        return "18-25"
    elif age <= 35:
        return "26-35"
    elif age <= 45:
        return "36-45"
    else:
        return "45+"

df["AgeBand"] = df["Age"].apply(age_band)
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

print("=" * 65)
print("EDUPRO LEARNER DEMOGRAPHICS & COURSE ENROLLMENT ANALYSIS")
print("=" * 65)

# KPIs
total = len(df)
unique = df["UserID"].nunique()
avg = df.groupby("UserID").size().mean()

print(f"\nTotal Enrollments          : {total:,}")
print(f"Unique Active Learners     : {unique:,}")
print(f"Avg Courses per Learner    : {avg:.2f}")

print("\n--- Enrollments by Age Band ---")
age_enroll = df["AgeBand"].value_counts().reindex(["<18", "18-25", "26-35", "36-45", "45+"]).fillna(0).astype(int)
age_share = (age_enroll / total * 100).round(1)
print(pd.DataFrame({"Enrollments": age_enroll, "Share (%)": age_share}))

print("\n--- Unique Learners by Age Band ---")
print(df.groupby("AgeBand")["UserID"].nunique().reindex(["<18", "18-25", "26-35", "36-45", "45+"]).fillna(0).astype(int))

print("\n--- Gender Participation (Enrollments) ---")
g = df["Gender"].value_counts()
print(pd.DataFrame({"Enrollments": g, "Share (%)": (g / total * 100).round(1)}))

print("\n--- Course Category Popularity ---")
print(df["CourseCategory"].value_counts())

print("\n--- Course Level Preference ---")
lvl = df["CourseLevel"].value_counts()
print(pd.DataFrame({"Enrollments": lvl, "Share (%)": (lvl / total * 100).round(1)}))

print("\n--- Course Type ---")
print(df["CourseType"].value_counts())
print((df["CourseType"].value_counts(normalize=True) * 100).round(1))

print("\n--- Age Band × Course Level ---")
print(pd.crosstab(df["AgeBand"], df["CourseLevel"]))

print("\n--- Gender × Course Level (% within gender) ---")
print((pd.crosstab(df["Gender"], df["CourseLevel"], normalize="index") * 100).round(1))

print("\n--- Age Band × Course Category ---")
print(pd.crosstab(df["AgeBand"], df["CourseCategory"]))

print("\n--- Enrollment Concentration ---")
cpu = df.groupby("UserID").size()
print(f"Learners with 1 course    : {(cpu == 1).sum()}")
print(f"Learners with 2-4 courses : {((cpu >= 2) & (cpu <= 4)).sum()}")
print(f"Learners with 5+ courses  : {(cpu >= 5).sum()}")
print(f"Max courses by one learner: {cpu.max()}")

print("\nAnalysis complete.")
