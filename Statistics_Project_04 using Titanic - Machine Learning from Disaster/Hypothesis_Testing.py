# ==========================================================
# Hypothesis Testing using Titanic Dataset
# ==========================================================

print("Hypothesis Testing using Titanic Dataset")

# ==========================================================
# 1. Import Libraries
# ==========================================================

import pandas as pd
import numpy as np
from scipy import stats

# ==========================================================
# 2. Load Dataset
# ==========================================================

file_path = r"DA Projects\Statistics_Project\Statistics_Project_04 using Titanic - Machine Learning from Disaster\Titanic_train.csv"
dataset = pd.read_csv(file_path)
print("\nDataset Loaded Successfully!")

# ==========================================================
# 3. Dataset Understanding
# ==========================================================

print("\n========== DATASET SHAPE ==========")
print(dataset.shape)

print("\n========== FIRST 5 ROWS ==========")
print(dataset.head())

print("\n========== DATA TYPES ==========")
dataset.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(dataset.describe())

# ==========================================================
# 4. Data Cleaning
# ==========================================================

print("\n========== MISSING VALUES ==========")
print(dataset.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(dataset.duplicated().sum())

print("\n========== UNIQUE VALUES ==========")
print(dataset.nunique())

# ==========================================================
# 5. Null Hypothesis (H0)
# ==========================================================

print("\n========== NULL HYPOTHESIS (H0) ==========")

print("1. Mean Age of passengers is equal to 30 years.")
print("2. Mean Age of Male and Female passengers is the same.")
print("3. Survival is independent of Gender.")
print("4. Passenger Class has no effect on Age.")

# ==========================================================
# 6. Alternative Hypothesis (H1)
# ==========================================================

print("\n========== ALTERNATIVE HYPOTHESIS (H1) ==========")

print("1. Mean Age of passengers is not equal to 30 years.")
print("2. Mean Age of Male and Female passengers is different.")
print("3. Survival depends on Gender.")
print("4. Passenger Class affects Age.")

# ==========================================================
# 7. Significance Level (α)
# ==========================================================

print("\n========== SIGNIFICANCE LEVEL ==========")

alpha = 0.05

print("Alpha (a) =", alpha)
print("\nDecision Rule")
print("If p-value < 0.05 : Reject H0")
print("If p-value >= 0.05 : Fail to Reject H0")

# ==========================================================
# 8. One Sample t-Test
# ==========================================================

print("\n========== ONE SAMPLE T-TEST ==========")

age = dataset["Age"].dropna()

t_statistic, p_value = stats.ttest_1samp(age, popmean=30)

print(f"Sample Mean Age : {age.mean():.2f}")
print(f"T-Statistic : {t_statistic:.4f}")
print(f"P-Value : {p_value:.4f}")

if p_value < alpha:
    print("\nDecision : Reject H0")
    print("Interpretation : The average passenger age is significantly different from 30 years.")
else:
    print("\nDecision : Fail to Reject H0")
    print("Interpretation : There is insufficient evidence to conclude that the average passenger age differs from 30 years.")

# ==========================================================
# 9. Independent Two Sample t-Test
# ==========================================================

print("\n========== INDEPENDENT T-TEST ==========")

male_age = dataset[dataset["Sex"] == "male"]["Age"].dropna()

female_age = dataset[dataset["Sex"] == "female"]["Age"].dropna()

t_statistic, p_value = stats.ttest_ind(
    male_age,
    female_age,
    equal_var=False
)

print(f"Male Mean Age : {male_age.mean():.2f}")
print(f"Female Mean Age : {female_age.mean():.2f}")
print(f"T-Statistic : {t_statistic:.4f}")
print(f"P-Value : {p_value:.4f}")

if p_value < alpha:
    print("\nDecision : Reject H0")
    print("Interpretation : Male and Female passengers have significantly different average ages.")
else:
    print("\nDecision : Fail to Reject H0")
    print("Interpretation : No significant difference exists between Male and Female average ages.")

# ==========================================================
# 10. Paired t-Test (Educational Example)
# ==========================================================

print("\n========== PAIRED T-TEST ==========")

before = [65, 70, 75, 80, 85, 90]
after  = [67, 72, 74, 82, 87, 91]

t_statistic, p_value = stats.ttest_rel(before, after)

print("Before :", before)
print("After  :", after)

print(f"\nT-Statistic : {t_statistic:.4f}")
print(f"P-Value : {p_value:.4f}")

if p_value < alpha:
    print("\nDecision : Reject H0")
    print("Interpretation : The paired observations show a significant difference.")
else:
    print("\nDecision : Fail to Reject H0")
    print("Interpretation : No significant difference exists between the paired observations.")

# ==========================================================
# 11. Chi-Square Test
# ==========================================================

print("\n========== CHI-SQUARE TEST ==========")

contingency_table = pd.crosstab(dataset["Sex"], dataset["Survived"])

print("\nContingency Table")

print(contingency_table)

chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)

print(f"\nChi-Square Statistic : {chi2:.4f}")
print(f"Degrees of Freedom   : {dof}")
print(f"P-Value              : {p_value:.6f}")

if p_value < alpha:
    print("\nDecision : Reject H0")
    print("Interpretation : Survival is significantly associated with Gender.")
else:
    print("\nDecision : Fail to Reject H0")
    print("Interpretation : Survival is independent of Gender.")

# ==========================================================
# 12. One-Way ANOVA
# ==========================================================

print("\n========== ONE-WAY ANOVA ==========")

class1 = dataset[dataset["Pclass"] == 1]["Age"].dropna()
class2 = dataset[dataset["Pclass"] == 2]["Age"].dropna()
class3 = dataset[dataset["Pclass"] == 3]["Age"].dropna()

f_statistic, p_value = stats.f_oneway(class1, class2, class3)

print(f"Class 1 Mean Age : {class1.mean():.2f}")
print(f"Class 2 Mean Age : {class2.mean():.2f}")
print(f"Class 3 Mean Age : {class3.mean():.2f}")

print(f"\nF-Statistic : {f_statistic:.4f}")
print(f"P-Value     : {p_value:.6f}")

if p_value < alpha:
    print("\nDecision : Reject H0")
    print("Interpretation : Passenger class significantly affects average age.")
else:
    print("\nDecision : Fail to Reject H0")
    print("Interpretation : Passenger class does not significantly affect average age.")

# ==========================================================
# 13. Confidence Interval
# ==========================================================

print("\n========== 95% CONFIDENCE INTERVAL ==========")

age = dataset["Age"].dropna()

confidence = 0.95
mean_age = age.mean()
std_error = stats.sem(age)

interval = stats.t.interval(
    confidence,
    len(age)-1,
    loc=mean_age,
    scale=std_error
)

print(f"Sample Mean Age : {mean_age:.2f}")
print(f"95% Confidence Interval : ({interval[0]:.2f}, {interval[1]:.2f})")

# ==========================================================
# 14. Conclusion
# ==========================================================

print("\n==============================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("Statistics Project 04")
print("Hypothesis Testing using Titanic Dataset")
print("==============================================")