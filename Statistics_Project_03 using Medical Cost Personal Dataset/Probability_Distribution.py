# ==========================================================
# Probability Distribution Analysis using Medical Cost Personal Dataset
# ==========================================================

print("Probability Distribution Analysis using Medical Cost Personal Dataset")

# ==========================================================
# 1. Import Libraries
# ==========================================================

import pandas as pd
import numpy as np
from scipy import stats

# ==========================================================
# 2. Load Dataset
# ==========================================================

file_path = r"DA Projects\Statistics_Project\Statistics_Project_03 using Medical Cost Personal Dataset\insurance.csv"

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
# 5. Random Variable
# ==========================================================

print("\n========== RANDOM VARIABLE ==========")

print("\nDiscrete Random Variable")
print("Children")

print("\nUnique Values of Children")

print(sorted(dataset["children"].unique()))

print("\nContinuous Random Variables")

continuous = ["age", "bmi", "charges"]

for column in continuous:
    print(column)


# ==========================================================
# 6. Probability Distribution
# ==========================================================

print("\n========== PROBABILITY DISTRIBUTION ==========")

variables = ["age", "bmi", "children", "charges"]

for column in variables:

    print("\n---------------------------------------")
    print("Variable :", column)

    print("Minimum :", dataset[column].min())
    print("Maximum :", dataset[column].max())
    print("Mean :", round(dataset[column].mean(),2))
    print("Median :", round(dataset[column].median(),2))
    print("Standard Deviation :", round(dataset[column].std(),2))

# ==========================================================
# 7. Normal Distribution
# ==========================================================

print("\n========== NORMAL DISTRIBUTION ==========")

variables = ["age", "bmi", "charges"]

for column in variables:

    mean = dataset[column].mean()
    median = dataset[column].median()
    std = dataset[column].std()

    print("\n---------------------------------------")
    print("Variable :", column)
    print(f"Mean : {mean:.2f}")
    print(f"Median : {median:.2f}")
    print(f"Standard Deviation : {std:.2f}")

    difference = abs(mean - median)

    if difference < std * 0.1:
        print("Observation : Approximately Normally Distributed")
    else:
        print("Observation : Not Approximately Normally Distributed")

# ==========================================================
# 8. Uniform Distribution
# ==========================================================

print("\n========== UNIFORM DISTRIBUTION ==========")

children_frequency = dataset["children"].value_counts().sort_index()

print(children_frequency)

maximum = children_frequency.max()
minimum = children_frequency.min()

print("\nMaximum Frequency :", maximum)
print("Minimum Frequency :", minimum)

if (maximum - minimum) < 100:
    print("Observation : Approximately Uniform Distribution")
else:
    print("Observation : Not Uniformly Distributed")

# ==========================================================
# 9. Binomial Distribution
# ==========================================================

print("\n========== BINOMIAL DISTRIBUTION ==========")

smoker_counts = dataset["smoker"].value_counts()
print("Smoker Frequency\n",smoker_counts)

total = len(dataset)

success = smoker_counts["yes"]
failure = smoker_counts["no"]

prob_success = success / total
prob_failure = failure / total

print(f"\nTotal Individuals : {total}")
print(f"Smokers : {success}")
print(f"Non-Smokers : {failure}")
print(f"P(Smoker) = {prob_success:.4f}")
print(f"P(Non-Smoker) = {prob_failure:.4f}")

# ==========================================================
# 10. Poisson Distribution
# ==========================================================

print("\n========== POISSON DISTRIBUTION ==========")

children = dataset["children"]

mean_children = children.mean()
variance_children = children.var()

print(f"Mean Number of Children : {mean_children:.2f}")
print(f"Variance : {variance_children:.2f}")

print("\nChildren Frequency")
print(children.value_counts().sort_index())

if abs(mean_children - variance_children) < 1:
    print("\nObservation : Approximately follows a Poisson Distribution")
else:
    print("\nObservation : Does not closely follow a Poisson Distribution")

# ==========================================================
# 11. Skewness
# ==========================================================

print("\n========== SKEWNESS ==========")

variables = ["age", "bmi", "charges"]

for column in variables:
    skew_value = dataset[column].skew()

    print("\n-----------------------------------")

    print("Variable :", column)
    print(f"Skewness : {skew_value:.4f}")

    if skew_value > 0.5:
        print("Distribution : Positively Skewed")
    elif skew_value < -0.5:
        print("Distribution : Negatively Skewed")
    else:
        print("Distribution : Approximately Symmetric")

# ==========================================================
# 12. Kurtosis
# ==========================================================

print("\n========== KURTOSIS ==========")

variables = ["age", "bmi", "charges"]

for column in variables:
    kurt = dataset[column].kurt()
    print("\n-----------------------------------")

    print("Variable :", column)
    print(f"Kurtosis : {kurt:.4f}")

    if kurt > 0:
        print("Distribution : Leptokurtic(Heavy Tails)")
    elif kurt < 0:
        print("Distribution : Platykurtic(Light Tails)")
    else:
        print("Distribution : Mesokurtic(Normal)")

# ==========================================================
# 13. Z-Score
# ==========================================================

print("\n==================== Z-SCORE ====================")

variables = ["age", "bmi", "charges"]

for column in variables:
    print("\n-------------------------------------")
    print("Variable :", column)
    z_scores = stats.zscore(dataset[column])
    print("First 10 Z-Scores")
    print(np.round(z_scores[:10], 1))
    outliers = np.sum(np.abs(z_scores) > 3)
    print("Number of Outliers :", outliers)

# ==========================================================
# 14. Standardization
# ==========================================================

print("\n========== STANDARDIZATION ==========")

standardized_dataset = dataset.copy()

variables = ["age", "bmi", "charges"]

for column in variables:
    standardized_dataset[column] = stats.zscore(dataset[column])

print("\nFirst 5 Original Records")
print(dataset[variables].head())
print("\nFirst 5 Standardized Records")
print(standardized_dataset[variables].head())

print("\nMean Before Standardization")
print(dataset[variables].mean())
print("\nMean After Standardization")
print(standardized_dataset[variables].mean())

print("\nStandard Deviation Before Standardization")
print(dataset[variables].std())
print("\nStandard Deviation After Standardization")
print(standardized_dataset[variables].std())

# ==========================================================
# 14. Conclusion
# ==========================================================

print("\n==============================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("Statistics Project 03")
print("Population Distribution Analysis using Medical Cost Personal Dataset")
print("==============================================")