# ==========================================================
# Probability Analysis using Mall Customer Segmentation Data
# ==========================================================
print("Probability Analysis using Mall Customer Segmentation Data" )
# ==========================================================
# 1. Import Libraries
# ==========================================================

import pandas as pd
import numpy as np
import math

# ==========================================================
# 2. Load Dataset
# ==========================================================

file_path = r"C:\Users\deek\Downloads\data analytics\DA Projects\Mall Customer Segmentation Data\Mall_Customers.csv"
dataset = pd.read_csv(file_path)
print("\nDataset Loaded Successfully!")

# ==========================================================
# 3. Dataset Understanding
# ==========================================================

print("\n===== Dataset Shape =====")
print(dataset.shape)

print("\n===== Statistical Summary =====")
print(dataset.describe())

print("\n===== First 5 Rows =====")
print(dataset.head())
print(dataset.info())

# ==========================================================
# 4. Data Cleaning
# ==========================================================

print("\n===== Missing Values =====")
print(dataset.isnull().sum())

print("\n===== Duplicated Values =====")
print(dataset.duplicated().sum())

print("\n===== Unique Values =====")
print(dataset.nunique())

print("\n========== GENDER DISTRIBUTION ==========")
print(dataset["Gender"].value_counts())

# ==========================================================
# 5. Permutation
# ==========================================================

print("\n========== PERMUTATION ==========")

n = len(dataset)

print(f"Total Customers : {n}")

# Arrange 2 customers
perm_2 = math.perm(n, 2)
print("Permutation of selecting 2 customers = %d" % perm_2)

# Arrange 3 customers
perm_3 = math.perm(n, 3)
print("Permutation of selecting 3 customers = %d" % perm_3)

# Arrange 5 customers
perm_5 = math.perm(n, 5)
print("Permutation of selecting 5 customers = %d" % perm_5)

# ==========================================================
# 6. Combination
# ==========================================================

print("\n========== COMBINATION ==========")

n = len(dataset)

print(f"Total Customers : {n}")

# Select 2 customers
comb_2 = math.comb(n, 2)
print("Combination of selecting 2 customers = %d" % comb_2)

# Select 3 customers
comb_3 = math.comb(n, 3)
print("Combination of selecting 3 customers = %d" % comb_3)

# Select 5 customers
comb_5 = math.comb(n, 5)
print("Combination of selecting 5 customers = %d" % comb_5)

# ==========================================================
# 7. Basic Probability
# ==========================================================

print("\n========== BASIC PROBABILITY ==========")

total_customers = len(dataset)
print("Total Customers :", total_customers)

#Example 1 : Probability of Selecting a Male Customer
male_customers = len(dataset[dataset["Gender"]=="Male"])
prob_male = male_customers / total_customers
print("\nMale Customers :", male_customers)
print("Probability of Selecting Male :", prob_male)

#Example 2 : Probability of Selecting a Female Customer
female_customers = len(dataset[dataset["Gender"]=="Female"])
prob_female = female_customers / total_customers
print("\nFemale Customers :", female_customers)
print("Probability of Selecting Female :", prob_female)

#Example 3 : Probability of Selecting Customer Age < 30
young_customers = len(dataset[dataset["Age"] < 30])
prob_young = young_customers / total_customers
print("\nCustomers Age < 30 :", young_customers)
print("Probability :", prob_young)

#Example 4 : Probability of Age ≥ 40
age_40 = len(dataset[dataset["Age"] >= 40])
prob_age40 = age_40 / total_customers
print("\nCustomers Age >= 40 :", age_40)
print("Probability :", prob_age40)

#Example 5 : Probability of High Income
high_income = len(dataset[dataset["Annual Income (k$)"] > 70])
prob_income = high_income / total_customers
print("\nIncome > 70k :", high_income)
print("Probability :", prob_income)

#Example 6 : Probability of High Spending Score
high_spending = len(dataset[dataset["Spending Score (1-100)"] > 70])
prob_spending = high_spending / total_customers
print("\nHigh Spending Customers :", high_spending)
print("Probability :", prob_spending)

#Example 7 : Probability of Medium Age
middle_age = len(dataset[(dataset["Age"] >= 30) & (dataset["Age"] <= 50)])
prob_middle = middle_age / total_customers
print("\nAge Between 30 and 50 :", middle_age)
print("Probability :", prob_middle)

#Example 8 : Probability of Low Spending Score
low_spending = len(dataset[dataset["Spending Score (1-100)"] < 30])
prob_low = low_spending / total_customers
print("\nLow Spending Customers :", low_spending)
print("Probability :", prob_low)

# ==========================================================
# 8. Conditional Probability
# ==========================================================

print("\n========== CONDITIONAL PROBABILITY ==========")

# Question 1: If the customer is Female, what is the probability that the Spending Score is greater than 70?
female = dataset[dataset["Gender"] == "Female"]
female_high_spending = female[female["Spending Score (1-100)"] > 70]
prob = len(female_high_spending) / len(female)
print("\nFemale Customers :", len(female))
print("Female Customers with Spending Score >70 :", len(female_high_spending))
print("Conditional Probability =", round(prob,4))

# Question 2: Given the customer is Male, what is the probability that Age is less than 30?
male = dataset[dataset["Gender"] == "Male"]
male_young = male[male["Age"] < 30]
prob = len(male_young) / len(male)
print("\nProbability (Age <30 | Male) =", round(prob,4))

# Question 3: Given Income >70k, what is the probability that Spending Score >70?
high_income = dataset[dataset["Annual Income (k$)"] > 70]
high_income_spending = high_income[high_income["Spending Score (1-100)"] > 70]
prob = len(high_income_spending) / len(high_income)
print("\nProbability (Spending >70 | Income >70) =", round(prob,4))

# Question 4: Given Spending Score >70, what is the probability that the customer is Female?
high_spending = dataset[dataset["Spending Score (1-100)"] > 70]
female_high = high_spending[high_spending["Gender"] == "Female"]
prob = len(female_high) / len(high_spending)
print("\nProbability (Female | Spending >70) =", round(prob,4))

# Question 5: Given Age >40, what is the probability that Income >60k?
age40 = dataset[dataset["Age"] > 40]
income60 = age40[age40["Annual Income (k$)"] > 60]
prob = len(income60) / len(age40)
print("\nProbability (Income >60 | Age >40) =", round(prob,4))

# Question 6: Given Female, what is the probability that Income >60k?
female = dataset[dataset["Gender"] == "Female"]
income60 = female[female["Annual Income (k$)"] > 60]
prob = len(income60) / len(female)
print("\nProbability (Income >60 | Female) =", round(prob,4))

# Question 7: Given Male, what is the probability that Spending Score <30?
male = dataset[dataset["Gender"] == "Male"]
low_spending = male[male["Spending Score (1-100)"] < 30]
prob = len(low_spending) / len(male)
print("\nProbability (Spending <30 | Male) =", round(prob,4))

# Question 8: Given Age <30, what is the probability that Spending Score >60?
young = dataset[dataset["Age"] < 30]
high_spending = young[young["Spending Score (1-100)"] > 60]
prob = len(high_spending) / len(young)
print("\nProbability (Spending >60 | Age <30) =", round(prob,4))

# ==========================================================
# 9. Independent & Dependent Events
# ==========================================================

print("\n========== INDEPENDENT & DEPENDENT EVENTS ==========")

total = len(dataset)
print("Total Customers :", total)

# ==========================================================
# Example 1: Event A = Female, Event B = Spending Score > 70
# ==========================================================

female = dataset["Gender"] == "Female"
high_spending = dataset["Spending Score (1-100)"] > 70

P_A = female.sum() / total
P_B = high_spending.sum() / total
P_AB = (female & high_spending).sum() / total

print("\n--------------------------------------------")
print("Example 1")
print("Event A : Female")
print("Event B : Spending Score > 70")

print(f"P(A) = {P_A:.4f}")
print(f"P(B) = {P_B:.4f}")
print(f"P(A & B) = {P_AB:.4f}")
print(f"P(A) * P(B) = {(P_A * P_B):.4f}")

if abs(P_AB - (P_A * P_B)) < 0.001:
    print("Result : Independent Events")
else:
    print("Result : Dependent Events")


# ==========================================================
# Example 2: Event A = Age < 30, Event B = Income > 70
# ==========================================================

young = dataset["Age"] < 30
high_income = dataset["Annual Income (k$)"] > 70

P_A = young.sum() / total
P_B = high_income.sum() / total
P_AB = (young & high_income).sum() / total

print("\n--------------------------------------------")
print("Example 2")
print("Event A : Age < 30")
print("Event B : Income > 70")

print(f"P(A) = {P_A:.4f}")
print(f"P(B) = {P_B:.4f}")
print(f"P(A & B) = {P_AB:.4f}")
print(f"P(A) * P(B) = {(P_A * P_B):.4f}")

if abs(P_AB - (P_A * P_B)) < 0.001:
    print("Result : Independent Events")
else:
    print("Result : Dependent Events")


# ==========================================================
# Example 3: Event A = Male, Event B = Income > 60
# ==========================================================

male = dataset["Gender"] == "Male"
income = dataset["Annual Income (k$)"] > 60

P_A = male.sum() / total
P_B = income.sum() / total
P_AB = (male & income).sum() / total

print("\n--------------------------------------------")
print("Example 3")
print("Event A : Male")
print("Event B : Income > 60")

print(f"P(A) = {P_A:.4f}")
print(f"P(B) = {P_B:.4f}")
print(f"P(A & B) = {P_AB:.4f}")
print(f"P(A) * P(B) = {(P_A * P_B):.4f}")

if abs(P_AB - (P_A * P_B)) < 0.001:
    print("Result : Independent Events")
else:
    print("Result : Dependent Events")


# ==========================================================
# Example 4: Event A = Age > 40, Event B = Spending Score > 50
# ==========================================================

age40 = dataset["Age"] > 40
spending50 = dataset["Spending Score (1-100)"] > 50

P_A = age40.sum() / total
P_B = spending50.sum() / total
P_AB = (age40 & spending50).sum() / total

print("\n--------------------------------------------")
print("Example 4")
print("Event A : Age > 40")
print("Event B : Spending Score > 50")

print(f"P(A) = {P_A:.4f}")
print(f"P(B) = {P_B:.4f}")
print(f"P(A & B) = {P_AB:.4f}")
print(f"P(A) * P(B) = {(P_A * P_B):.4f}")

if abs(P_AB - (P_A * P_B)) < 0.001:
    print("Result : Independent Events")
else:
    print("Result : Dependent Events")


# ==========================================================
# End of Project
# ==========================================================

print("\n==============================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("Statistics Project 01")
print("Probability Analysis using Mall Customer Segmentation Data")
print("==============================================")