# Hypothesis Testing using Titanic Dataset

## 📌 Project Overview

This project demonstrates the implementation of **Hypothesis Testing** concepts using the **Titanic - Machine Learning from Disaster** dataset. The objective is to understand how statistical hypothesis testing can be used to make data-driven decisions using real-world data.

This project is the fourth project in the **Statistics for Data Analysts** series and focuses exclusively on **Hypothesis Testing** concepts without involving Machine Learning or Business Intelligence.

---

# 🎯 Objectives

- Understand the concept of Statistical Hypothesis Testing.
- Formulate Null and Alternative Hypotheses.
- Learn the importance of Significance Level (α).
- Perform One Sample t-Test.
- Perform Independent Two Sample t-Test.
- Demonstrate Paired t-Test.
- Perform Chi-Square Test of Independence.
- Perform One-Way ANOVA.
- Interpret P-values correctly.
- Calculate Confidence Intervals.
- Draw statistical conclusions based on hypothesis tests.

---

# 📂 Dataset

**Dataset Name:**

Titanic - Machine Learning from Disaster

**Source:**

Kaggle

The project uses the **Titanic_train.csv** dataset containing passenger information from the Titanic disaster.

### Dataset Information

- Total Records : **891**
- Total Features : **12**
- Numerical Features : **7**
- Categorical Features : **5**

---

# 📊 Statistical Concepts Covered

## 1. Dataset Understanding

- Dataset Shape
- First Five Records
- Data Types
- Statistical Summary

---

## 2. Data Cleaning

- Missing Values
- Duplicate Records
- Unique Values

---

## 3. Null Hypothesis (H₀)

- Definition
- Examples
- Statistical Assumptions

---

## 4. Alternative Hypothesis (H₁)

- Definition
- Examples
- Research Hypothesis

---

## 5. Significance Level (α)

- Alpha Value
- Decision Rule
- Type I Error Concept

---

## 6. One Sample t-Test

- Compare Sample Mean with Population Mean
- Test Statistic
- P-value
- Statistical Decision

---

## 7. Independent Two Sample t-Test

- Compare Male and Female Passenger Ages
- Test Statistic
- P-value
- Statistical Decision

---

## 8. Paired t-Test

- Educational Demonstration
- Before and After Comparison
- Statistical Decision

---

## 9. Chi-Square Test of Independence

- Contingency Table
- Chi-Square Statistic
- Degrees of Freedom
- P-value
- Association between Gender and Survival

---

## 10. One-Way ANOVA

- Compare Mean Age across Passenger Classes
- F-Statistic
- P-value
- Statistical Decision

---

## 11. Confidence Interval

- Sample Mean
- Standard Error
- 95% Confidence Interval

---

# 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- SciPy (stats)

---

# 📁 Project Structure

```text
Statistics_Project_04 using Titanic Dataset
│
├── Titanic_train.csv
├── Titanic_test.csv
├── Hypothesis_Testing.py
└── README.md
```

---

# 📦 Required Libraries

Install the required libraries before running the project.

```bash
pip install pandas numpy scipy
```

---

# ▶️ How to Run

1. Download the Titanic dataset from Kaggle.
2. Place `Titanic_train.csv` in the project folder.
3. Update the dataset path inside `Hypothesis_Testing.py`.
4. Run the program.

```bash
python Hypothesis_Testing.py
```

---

# 📖 Hypothesis Testing Techniques Implemented

- Null Hypothesis
- Alternative Hypothesis
- Significance Level
- One Sample t-Test
- Independent Two Sample t-Test
- Paired t-Test
- Chi-Square Test
- One-Way ANOVA
- Confidence Interval

---

# 🎓 Learning Outcomes

After completing this project, you will be able to:

- Formulate Null and Alternative Hypotheses.
- Interpret Statistical Significance.
- Perform t-Tests using Python.
- Conduct Chi-Square Tests for categorical variables.
- Perform One-Way ANOVA.
- Interpret P-values correctly.
- Calculate Confidence Intervals.
- Make statistical decisions based on hypothesis testing.

---

# 📷 Sample Output

```
Hypothesis Testing using Titanic Dataset

Dataset Loaded Successfully!

========== DATASET SHAPE ==========
(891, 12)

========== FIRST 5 ROWS ==========
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]

========== DATA TYPES ==========
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB

========== STATISTICAL SUMMARY ==========
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]

========== MISSING VALUES ==========
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

========== DUPLICATE ROWS ==========
0

========== UNIQUE VALUES ==========
PassengerId    891
Survived         2
Pclass           3
Name           891
Sex              2
Age             88
SibSp            7
Parch            7
Ticket         681
Fare           248
Cabin          147
Embarked         3
dtype: int64

========== NULL HYPOTHESIS (H0) ==========
1. Mean Age of passengers is equal to 30 years.
2. Mean Age of Male and Female passengers is the same.
3. Survival is independent of Gender.
4. Passenger Class has no effect on Age.

========== ALTERNATIVE HYPOTHESIS (H1) ==========
1. Mean Age of passengers is not equal to 30 years.
2. Mean Age of Male and Female passengers is different.
3. Survival depends on Gender.
4. Passenger Class affects Age.

========== SIGNIFICANCE LEVEL ==========
Alpha (a) = 0.05

Decision Rule
If p-value < 0.05 : Reject H0
If p-value >= 0.05 : Fail to Reject H0

========== ONE SAMPLE T-TEST ==========
Sample Mean Age : 29.70
T-Statistic : -0.5535
P-Value : 0.5801

Decision : Fail to Reject H0
Interpretation : There is insufficient evidence to conclude that the average passenger age differs from 30 years.

========== INDEPENDENT T-TEST ==========
Male Mean Age : 30.73
Female Mean Age : 27.92
T-Statistic : 2.5259
P-Value : 0.0118

Decision : Reject H0
Interpretation : Male and Female passengers have significantly different average ages.

========== PAIRED T-TEST ==========
Before : [65, 70, 75, 80, 85, 90]
After  : [67, 72, 74, 82, 87, 91]

T-Statistic : -2.6968
P-Value : 0.0429

Decision : Reject H0
Interpretation : The paired observations show a significant difference.

========== CHI-SQUARE TEST ==========

Contingency Table
Survived    0    1
Sex               
female     81  233
male      468  109

Chi-Square Statistic : 260.7170
Degrees of Freedom   : 1
P-Value              : 0.000000

Decision : Reject H0
Interpretation : Survival is significantly associated with Gender.

========== ONE-WAY ANOVA ==========
Class 1 Mean Age : 38.23
Class 2 Mean Age : 29.88
Class 3 Mean Age : 25.14

F-Statistic : 57.4435
P-Value     : 0.000000

Decision : Reject H0
Interpretation : Passenger class significantly affects average age.

========== 95% CONFIDENCE INTERVAL ==========
Sample Mean Age : 29.70
95% Confidence Interval : (28.63, 30.77)

==============================================
PROJECT COMPLETED SUCCESSFULLY
Statistics Project 04
Hypothesis Testing using Titanic Dataset
==============================================
```

---

# 🎓 Project Type

**Project Type:** Statistics Project

**Domain:** Data Analytics

**Category:** Hypothesis Testing

**Difficulty Level:** Intermediate

---

# 📚 Statistical Topics

- Statistical Hypothesis
- Null Hypothesis
- Alternative Hypothesis
- Significance Level
- One Sample t-Test
- Independent t-Test
- Paired t-Test
- Chi-Square Test
- One-Way ANOVA
- Confidence Interval
- P-value Interpretation

---

# 👩‍💻 Author

**Deekshitha U**

B.Tech Artificial Intelligence and Data Science

---

# 🚀 Future Work

This project establishes a strong foundation in **Hypothesis Testing**. Future enhancements and related statistical studies include:

- Perform Non-Parametric Tests such as Mann–Whitney U Test and Kruskal–Wallis Test.
- Apply Two-Way ANOVA for multiple independent variables.
- Study Logistic Regression for binary outcome prediction.
- Calculate Effect Size measures such as Cohen's d.
- Perform Statistical Power Analysis.
- Apply Bootstrapping techniques for hypothesis testing.
- Extend hypothesis testing to larger real-world datasets.
- Integrate this project with previous statistics projects to build a comprehensive Statistics Portfolio.

---