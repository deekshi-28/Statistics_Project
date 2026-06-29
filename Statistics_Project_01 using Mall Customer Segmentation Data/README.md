# Probability Analysis using Mall Customer Segmentation Data

## 📌 Project Overview

This project demonstrates the implementation of fundamental **Probability and Combinatorics** concepts using the **Mall Customer Segmentation** dataset. The objective is to understand and apply statistical concepts such as **Permutation**, **Combination**, **Basic Probability**, **Conditional Probability**, and **Independent & Dependent Events** through Python.

This project is part of a Statistics for Data Analysts series and focuses only on probability-related statistical concepts.

---

## 🎯 Objectives

- Understand the structure of a real-world dataset.
- Perform basic data cleaning.
- Learn Permutation and Combination using Python.
- Calculate probabilities of different customer events.
- Apply Conditional Probability.
- Determine whether events are Independent or Dependent.
- Interpret statistical results using a real dataset.

---

## 📂 Dataset

**Dataset Name:** Mall Customer Segmentation Data

**Source:** Kaggle

The dataset contains information about customers visiting a shopping mall.

### Features

| Column | Description |
|---------|-------------|
| CustomerID | Unique customer identifier |
| Gender | Gender of the customer |
| Age | Age of the customer |
| Annual Income (k$) | Annual income in thousand dollars |
| Spending Score (1-100) | Spending score assigned by the mall |

---

## 📊 Statistical Concepts Covered

### 1. Dataset Understanding
- Dataset Shape
- Data Types
- Statistical Summary
- First Five Records

### 2. Data Cleaning
- Missing Values
- Duplicate Records
- Unique Values
- Category Verification

### 3. Permutation
- nPr Formula
- Customer Arrangement Problems
- Python Implementation

### 4. Combination
- nCr Formula
- Customer Selection Problems
- Python Implementation

### 5. Basic Probability
- Probability of Selecting Male Customer
- Probability of Selecting Female Customer
- Probability of Selecting Young Customers
- Probability of High Income Customers
- Probability of High Spending Customers

### 6. Conditional Probability
- P(Spending > 70 | Female)
- P(Age < 30 | Male)
- P(Income > 70 | Spending > 70)
- Multiple Conditional Probability Examples

### 7. Independent & Dependent Events
- Event Definition
- Intersection Probability
- Independence Verification
- Statistical Interpretation

---

## 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Math Module

---

## 📁 Project Structure

```
Statistics_Project_01 using Mall Customer Segmentation Data
│
├── Mall_Customers.csv
├── Probability_Analysis.py
└── README.md
```

---

## 📦 Required Libraries

Install the required libraries before running the project.

```bash
pip install pandas numpy math
```

---

## ▶️ How to Run

1. Download the dataset.
2. Place `Mall_Customers.csv` in the project folder.
3. Update the dataset path inside `Probability_Analysis.py`.
4. Run the Python file.

```bash
python Probability_Analysis.py
```

---

## 📖 Concepts Implemented

- Permutation (nPr)
- Combination (nCr)
- Probability
- Conditional Probability
- Independent Events
- Dependent Events

---

## 📌 Learning Outcomes

After completing this project, you will be able to:

- Understand the difference between Permutation and Combination.
- Calculate probabilities from real-world datasets.
- Apply Conditional Probability using Python.
- Verify Independent and Dependent Events.
- Interpret statistical results accurately.

---

## Sample Output
```

Probability Analysis using Mall Customer Segmentation Data

Dataset Loaded Successfully!

===== Dataset Shape =====
(200, 5)

===== Statistical Summary =====
       CustomerID         Age  Annual Income (k$)  Spending Score (1-100)
count  200.000000  200.000000          200.000000              200.000000
mean   100.500000   38.850000           60.560000               50.200000
std     57.879185   13.969007           26.264721               25.823522
min      1.000000   18.000000           15.000000                1.000000
25%     50.750000   28.750000           41.500000               34.750000
50%    100.500000   36.000000           61.500000               50.000000
75%    150.250000   49.000000           78.000000               73.000000
max    200.000000   70.000000          137.000000               99.000000

===== First 5 Rows =====
   CustomerID  Gender  Age  Annual Income (k$)  Spending Score (1-100)
0           1    Male   19                  15                      39
1           2    Male   21                  15                      81
2           3  Female   20                  16                       6
3           4  Female   23                  16                      77
4           5  Female   31                  17                      40
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 5 columns):
 #   Column                  Non-Null Count  Dtype 
---  ------                  --------------  ----- 
 0   CustomerID              200 non-null    int64 
 1   Gender                  200 non-null    object
 2   Age                     200 non-null    int64 
 3   Annual Income (k$)      200 non-null    int64 
 4   Spending Score (1-100)  200 non-null    int64 
dtypes: int64(4), object(1)
memory usage: 7.9+ KB
None

===== Missing Values =====
CustomerID                0
Gender                    0
Age                       0
Annual Income (k$)        0
Spending Score (1-100)    0
dtype: int64

===== Duplicated Values =====
0

===== Unique Values =====
CustomerID                200
Gender                      2
Age                        51
Annual Income (k$)         64
Spending Score (1-100)     84
dtype: int64

========== GENDER DISTRIBUTION ==========
Gender
Female    112
Male       88
Name: count, dtype: int64

========== PERMUTATION ==========
Total Customers : 200
Permutation of selecting 2 customers = 39800
Permutation of selecting 3 customers = 7880400
Permutation of selecting 5 customers = 304278004800

========== COMBINATION ==========
Total Customers : 200
Combination of selecting 2 customers = 19900
Combination of selecting 3 customers = 1313400
Combination of selecting 5 customers = 2535650040

========== BASIC PROBABILITY ==========
Total Customers : 200

Male Customers : 88
Probability of Selecting Male : 0.44

Female Customers : 112
Probability of Selecting Female : 0.56

Customers Age < 30 : 55
Probability : 0.275

Customers Age >= 40 : 84
Probability : 0.42

Income > 70k : 74
Probability : 0.37

High Spending Customers : 54
Probability : 0.27

Age Between 30 and 50 : 105
Probability : 0.525

Low Spending Customers : 46
Probability : 0.23

========== CONDITIONAL PROBABILITY ==========

Female Customers : 112
Female Customers with Spending Score >70 : 32
Conditional Probability = 0.2857

Probability (Age <30 | Male) = 0.2955

Probability (Spending >70 | Income >70) = 0.4459

Probability (Female | Spending >70) = 0.5926

Probability (Income >60 | Age >40) = 0.4359

Probability (Income >60 | Female) = 0.4732

Probability (Spending <30 | Male) = 0.2727

Probability (Spending >60 | Age <30) = 0.4364

========== INDEPENDENT & DEPENDENT EVENTS ==========
Total Customers : 200

--------------------------------------------
Example 1
Event A : Female
Event B : Spending Score > 70
P(A) = 0.5600
P(B) = 0.2700
P(A & B) = 0.1600
P(A) * P(B) = 0.1512
Result : Dependent Events

--------------------------------------------
Example 2
Event A : Age < 30
Event B : Income > 70
P(A) = 0.2750
P(B) = 0.3700
P(A & B) = 0.0700
P(A) * P(B) = 0.1018
Result : Dependent Events

--------------------------------------------
Example 3
Event A : Male
Event B : Income > 60
P(A) = 0.4400
P(B) = 0.5100
P(A & B) = 0.2450
P(A) * P(B) = 0.2244
Result : Dependent Events

--------------------------------------------
Example 4
Event A : Age > 40
Event B : Spending Score > 50
P(A) = 0.3900
P(B) = 0.4850
P(A & B) = 0.0900
P(A) * P(B) = 0.1892
Result : Dependent Events

==============================================
PROJECT COMPLETED SUCCESSFULLY
Statistics Project 01
Probability Analysis using Mall Customer Segmentation Data
==============================================
```

---

## 🎓 Project Type

**Project Type:** Statistics Project

**Domain:** Data Analytics

**Category:** Probability & Combinatorics

**Difficulty Level:** Beginner
---

## 📚 Statistical Topics

- Probability Theory
- Combinatorics
- Basic Statistics
- Conditional Probability
- Event Independence

---

## 👩‍💻 Author

**Deekshitha U**

B.Tech Artificial Intelligence and Data Science

---

## ⭐ Future Work

This project is the first project in the Statistics Project Series.

Upcoming projects include:

- Population & Sampling
- Probability Distribution
- Hypothesis Testing
- Comprehensive Statistics Project