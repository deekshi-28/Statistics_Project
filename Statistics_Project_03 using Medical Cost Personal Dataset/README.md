# Probability Distribution Analysis using Medical Cost Personal Dataset

## 📌 Project Overview

This project demonstrates the implementation of **Probability Distribution** concepts using the **Medical Cost Personal Dataset**. The objective is to understand how numerical and categorical variables are distributed and how different probability distributions can be analyzed using Python.

This project is the third project in the **Statistics for Data Analysts** series and focuses exclusively on **Probability Distribution** concepts without involving Machine Learning or Business Intelligence.

---

# 🎯 Objectives

- Understand Random Variables.
- Study Probability Distribution concepts.
- Analyze Normal Distribution.
- Examine Uniform Distribution.
- Apply Binomial Distribution.
- Demonstrate Poisson Distribution.
- Measure Skewness and Kurtosis.
- Calculate Z-Scores for Outlier Detection.
- Perform Standardization using Z-Score transformation.
- Interpret statistical results using real-world medical insurance data.

---

# 📂 Dataset

**Dataset Name:**

Medical Cost Personal Dataset

**Source:**

Kaggle

The project uses the **insurance.csv** dataset containing demographic and medical insurance information.

### Dataset Information

- Total Records : **1338**
- Total Features : **7**
- Numerical Features : **4**
- Categorical Features : **3**

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

## 3. Random Variable

A **Random Variable** is a variable whose value depends on the outcome of a random experiment. It can be classified as either **Discrete** (countable values) or **Continuous** (measurable values).

- Discrete Random Variable
- Continuous Random Variable
- Dataset Examples

---

## 4. Probability Distribution

A **Probability Distribution** describes how the values of a random variable are distributed. It shows the likelihood of different outcomes and helps understand the behavior of data.

- Mean
- Median
- Standard Deviation
- Minimum and Maximum Values
- Distribution Analysis

---

## 5. Normal Distribution

A **Normal Distribution** is a continuous probability distribution where data is symmetrically distributed around the mean, forming a bell-shaped curve. Many real-world measurements approximately follow this distribution.

- Mean and Median Comparison
- Standard Deviation
- Normality Check
- Statistical Interpretation

---

## 6. Uniform Distribution

A **Uniform Distribution** is a probability distribution in which every possible outcome has an equal probability of occurring. It is used to determine whether data values are evenly distributed.

- Frequency Distribution
- Uniformity Check
- Children Variable Analysis

---

## 7. Binomial Distribution

A **Binomial Distribution** models the probability of obtaining a fixed number of successes in a fixed number of independent trials, where each trial has only two possible outcomes.

- Success and Failure Events
- Smoker Probability
- Non-Smoker Probability
- Statistical Interpretation

---

## 8. Poisson Distribution

A **Poisson Distribution** models the probability of a given number of events occurring within a fixed interval of time or space. It is commonly used for count-based data.

- Mean and Variance Comparison
- Children Count Analysis
- Poisson Distribution Check

---

## 9. Skewness

**Skewness** measures the asymmetry of a probability distribution. It indicates whether the data is skewed to the left, skewed to the right, or approximately symmetric.

- Positive Skewness
- Negative Skewness
- Symmetric Distribution
- Distribution Interpretation

---

## 10. Kurtosis

**Kurtosis** measures the tailedness of a probability distribution. It helps identify whether a distribution has heavier or lighter tails compared to a normal distribution.

- Leptokurtic Distribution
- Platykurtic Distribution
- Mesokurtic Distribution
- Statistical Interpretation

---

## 11. Z-Score

A **Z-Score** measures how many standard deviations a data point is from the mean. It is commonly used to compare observations and detect outliers.

- Standard Score Calculation
- Outlier Detection
- Z-Score Interpretation

---

## 12. Standardization

**Standardization** is the process of transforming numerical variables so that they have a mean of **0** and a standard deviation of **1**. This allows variables with different scales to be compared fairly.

- Z-Score Transformation
- Mean Standardization
- Standard Deviation Standardization
- Standardized Dataset Analysis

---

# 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- SciPy (stats)

---

# 📁 Project Structure

```text
Statistics_Project_03 using Medical Cost Personal Dataset
│
├── insurance.csv
├── Probability_Distribution.py
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

1. Download the dataset from Kaggle.
2. Place `insurance.csv` in the project folder.
3. Update the dataset path inside `Probability_Distribution.py`.
4. Run the program.

```bash
python Probability_Distribution.py
```

---

# 📖 Probability Distribution Techniques Implemented

- Random Variable
- Probability Distribution
- Normal Distribution
- Uniform Distribution
- Binomial Distribution
- Poisson Distribution
- Skewness
- Kurtosis
- Z-Score
- Standardization

---

# 🎓 Learning Outcomes

After completing this project, you will be able to:

- Differentiate between Discrete and Continuous Random Variables.
- Analyze Probability Distributions using Python.
- Identify approximately Normal and Uniform Distributions.
- Apply Binomial and Poisson Distribution concepts.
- Measure Skewness and Kurtosis.
- Detect Outliers using Z-Score.
- Perform Standardization for numerical variables.
- Interpret statistical distributions using real-world datasets.

---

# 📷 Sample Output
```

Probability Distribution Analysis using Medical Cost Personal Dataset

Dataset Loaded Successfully!

========== DATASET SHAPE ==========
(1338, 7)

========== FIRST 5 ROWS ==========
   age     sex     bmi  children smoker     region      charges
0   19  female  27.900         0    yes  southwest  16884.92400
1   18    male  33.770         1     no  southeast   1725.55230
2   28    male  33.000         3     no  southeast   4449.46200
3   33    male  22.705         0     no  northwest  21984.47061
4   32    male  28.880         0     no  northwest   3866.85520

========== DATA TYPES ==========
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1338 non-null   int64  
 1   sex       1338 non-null   object 
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object 
 5   region    1338 non-null   object 
 6   charges   1338 non-null   float64
dtypes: float64(2), int64(2), object(3)
memory usage: 73.3+ KB

========== STATISTICAL SUMMARY ==========
               age          bmi     children       charges
count  1338.000000  1338.000000  1338.000000   1338.000000
mean     39.207025    30.663397     1.094918  13270.422265
std      14.049960     6.098187     1.205493  12110.011237
min      18.000000    15.960000     0.000000   1121.873900
25%      27.000000    26.296250     0.000000   4740.287150
50%      39.000000    30.400000     1.000000   9382.033000
75%      51.000000    34.693750     2.000000  16639.912515
max      64.000000    53.130000     5.000000  63770.428010

========== MISSING VALUES ==========
age         0
sex         0
bmi         0
children    0
smoker      0
region      0
charges     0
dtype: int64

========== DUPLICATE ROWS ==========
1

========== UNIQUE VALUES ==========
age           47
sex            2
bmi          548
children       6
smoker         2
region         4
charges     1337
dtype: int64

========== RANDOM VARIABLE ==========

Discrete Random Variable
Children

Unique Values of Children
[0, 1, 2, 3, 4, 5]

Continuous Random Variables
age
bmi
charges

========== PROBABILITY DISTRIBUTION ==========

---------------------------------------
Variable : age
Minimum : 18
Maximum : 64
Mean : 39.21
Median : 39.0
Standard Deviation : 14.05

---------------------------------------
Variable : bmi
Minimum : 15.96
Maximum : 53.13
Mean : 30.66
Median : 30.4
Standard Deviation : 6.1

---------------------------------------
Variable : children
Minimum : 0
Maximum : 5
Mean : 1.09
Median : 1.0
Standard Deviation : 1.21

---------------------------------------
Variable : charges
Minimum : 1121.8739
Maximum : 63770.42801
Mean : 13270.42
Median : 9382.03
Standard Deviation : 12110.01

========== NORMAL DISTRIBUTION ==========

---------------------------------------
Variable : age
Mean : 39.21
Median : 39.00
Standard Deviation : 14.05
Observation : Approximately Normally Distributed

---------------------------------------
Variable : bmi
Mean : 30.66
Median : 30.40
Standard Deviation : 6.10
Observation : Approximately Normally Distributed

---------------------------------------
Variable : charges
Mean : 13270.42
Median : 9382.03
Standard Deviation : 12110.01
Observation : Not Approximately Normally Distributed

========== UNIFORM DISTRIBUTION ==========
children
0    574
1    324
2    240
3    157
4     25
5     18
Name: count, dtype: int64

Maximum Frequency : 574
Minimum Frequency : 18
Observation : Not Uniformly Distributed

========== BINOMIAL DISTRIBUTION ==========
Smoker Frequency
 smoker
no     1064
yes     274
Name: count, dtype: int64

Total Individuals : 1338
Smokers : 274
Non-Smokers : 1064
P(Smoker) = 0.2048
P(Non-Smoker) = 0.7952

========== POISSON DISTRIBUTION ==========
Mean Number of Children : 1.09
Variance : 1.45

Children Frequency
children
0    574
1    324
2    240
3    157
4     25
5     18
Name: count, dtype: int64

Observation : Approximately follows a Poisson Distribution

========== SKEWNESS ==========

-----------------------------------
Variable : age
Skewness : 0.0557
Distribution : Approximately Symmetric

-----------------------------------
Variable : bmi
Skewness : 0.2840
Distribution : Approximately Symmetric

-----------------------------------
Variable : charges
Skewness : 1.5159
Distribution : Positively Skewed

========== KURTOSIS ==========

-----------------------------------
Variable : age
Kurtosis : -1.2451
Distribution : Platykurtic(Light Tails)

-----------------------------------
Variable : bmi
Kurtosis : -0.0507
Distribution : Platykurtic(Light Tails)

-----------------------------------
Variable : charges
Kurtosis : 1.6063
Distribution : Leptokurtic(Heavy Tails)

==================== Z-SCORE ====================

-------------------------------------
Variable : age
First 10 Z-Scores
[-1.4 -1.5 -0.8 -0.4 -0.5 -0.6  0.5 -0.2 -0.2  1.5]
Number of Outliers : 0

-------------------------------------
Variable : bmi
First 10 Z-Scores
[-0.5  0.5  0.4 -1.3 -0.3 -0.8  0.5 -0.5 -0.1 -0.8]
Number of Outliers : 4

-------------------------------------
Variable : charges
First 10 Z-Scores
[ 0.3 -1.  -0.7  0.7 -0.8 -0.8 -0.4 -0.5 -0.6  1.3]
Number of Outliers : 7

========== STANDARDIZATION ==========

First 5 Original Records
   age     bmi      charges
0   19  27.900  16884.92400
1   18  33.770   1725.55230
2   28  33.000   4449.46200
3   33  22.705  21984.47061
4   32  28.880   3866.85520

First 5 Standardized Records
        age       bmi   charges
0 -1.438764 -0.453320  0.298584
1 -1.509965  0.509621 -0.953689
2 -0.797954  0.383307 -0.728675
3 -0.441948 -1.305531  0.719843
4 -0.513149 -0.292556 -0.776802

Mean Before Standardization
age           39.207025
bmi           30.663397
charges    13270.422265
dtype: float64

Mean After Standardization
age       -1.805565e-16
bmi       -2.124194e-16
charges   -8.098488e-17
dtype: float64

Standard Deviation Before Standardization
age           14.049960
bmi            6.098187
charges    12110.011237
dtype: float64

Standard Deviation After Standardization
age        1.000374
bmi        1.000374
charges    1.000374
dtype: float64

==============================================
PROJECT COMPLETED SUCCESSFULLY
Statistics Project 03
Population Distribution Analysis using Medical Cost Personal Dataset
==============================================
```

---

# 🎓 Project Type

**Project Type:** Statistics Project

**Domain:** Data Analytics

**Category:** Probability Distribution

**Difficulty Level:** Beginner to Intermediate

---

# 📚 Statistical Topics

- Random Variable
- Probability Distribution
- Normal Distribution
- Uniform Distribution
- Binomial Distribution
- Poisson Distribution
- Skewness
- Kurtosis
- Z-Score
- Standardization

---

# 👩‍💻 Author

**Deekshitha U**

B.Tech Artificial Intelligence and Data Science

---

# 🚀 Future Work

This project establishes a strong foundation in **Probability Distribution** concepts. Future enhancements and related statistical studies include:

- Perform **Hypothesis Testing** using t-tests, Chi-Square Tests, and ANOVA.
- Study additional probability distributions such as Exponential, Gamma, Beta, and Log-Normal distributions.
- Apply Normality Tests such as the Shapiro–Wilk Test and Kolmogorov–Smirnov Test.
- Visualize distributions using Histograms, Density Plots, Box Plots, and Q-Q Plots.
- Compare probability distributions across multiple real-world datasets.
- Apply Confidence Intervals and Statistical Inference techniques.
- Extend this project into a complete Statistical Analysis workflow for Data Analytics.
- Integrate this project with future Statistics projects to build a comprehensive Statistics Portfolio.

---