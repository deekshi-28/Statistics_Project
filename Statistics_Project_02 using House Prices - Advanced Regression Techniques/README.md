# Population and Sampling Analysis using House Prices Dataset

## 📌 Project Overview

This project demonstrates the implementation of **Population and Sampling** concepts using the **House Prices - Advanced Regression Techniques** dataset. The objective is to understand different sampling techniques and statistical concepts through practical implementation in Python.

This project is the second project in the **Statistics for Data Analysts** series and focuses exclusively on **Population and Sampling** concepts without involving Machine Learning or Business Intelligence.

---

## 🎯 Objectives

- Understand the concept of Population and Sample.
- Learn different Sampling Techniques.
- Perform Random, Systematic, Stratified and Cluster Sampling.
- Calculate Sampling Error.
- Understand Sampling Distribution.
- Demonstrate the Central Limit Theorem (CLT) using Python.
- Interpret statistical results obtained from real-world data.

---

# 📂 Dataset

**Dataset Name:**
House Prices - Advanced Regression Techniques

**Source:**
Kaggle

The project uses the **train.csv** dataset containing information about residential house prices.

### Dataset Information

- Total Records : **1460**
- Total Features : **81**
- Numerical Features : **38**
- Categorical Features : **43**

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

## 3. Population

A **Population** is the complete collection of individuals, objects, or observations under study. It represents the entire dataset from which statistical conclusions are drawn.

- Total Number of Houses
- Population Size Identification
- Population Analysis

---

## 4. Sample

A **Sample** is a subset of the population selected for statistical analysis. It is used to make inferences about the entire population while reducing time and computational effort.

- Sample Selection
- Sample Size
- Sample Records

---

## 5. Random Sampling

**Random Sampling** is a sampling technique in which every member of the population has an equal chance of being selected. It minimizes selection bias and provides representative samples.

- Random Sample Selection
- Equal Selection Probability
- Python Implementation

---

## 6. Systematic Sampling

**Systematic Sampling** selects observations at regular intervals after choosing a random starting point. It is simple to implement and widely used in surveys.

- Sampling Interval (k)
- Every k-th Observation
- Python Implementation

---

## 7. Stratified Sampling

**Stratified Sampling** divides the population into homogeneous groups called strata and selects samples from each group. This ensures that every subgroup is properly represented.

- Population Stratification
- Sampling from Each Stratum
- Overall Quality Based Sampling

---

## 8. Cluster Sampling

**Cluster Sampling** divides the population into clusters and randomly selects one or more clusters for analysis. It is useful when the population is geographically or naturally grouped.

- Neighborhood-based Clusters
- Random Cluster Selection
- Cluster Analysis

---

## 9. Sampling Error

**Sampling Error** is the difference between a population parameter and the corresponding sample statistic. It occurs because only a subset of the population is analyzed.

- Population Mean
- Sample Mean
- Sampling Error Calculation

---

## 10. Sampling Distribution

A **Sampling Distribution** is the probability distribution of a sample statistic obtained from multiple random samples of the same size. It helps estimate the variability of sample statistics.

- Multiple Random Samples
- Distribution of Sample Means
- Average Sample Mean

---

## 11. Central Limit Theorem (CLT)

The **Central Limit Theorem (CLT)** states that, regardless of the population distribution, the sampling distribution of the sample mean approaches a normal distribution as the sample size becomes sufficiently large.

- Population Mean Comparison
- Average Sample Mean
- CLT Demonstration
- Statistical Interpretation

---

# 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- Random Module

---

# 📁 Project Structure

```
Statistics_Project_02 using House Prices - Advanced Regression Techniques
│
├── train.csv
├── test.csv
├── data_description.txt
├── sample_submission.csv
├── Population_and_Sampling_Analysis.py
└── README.md
```

---

# 📦 Required Libraries

Install the required libraries before running the project.

```bash
pip install pandas numpy random
```

---

# ▶️ How to Run

1. Download the dataset from Kaggle.
2. Place `train.csv` in the project folder.
3. Update the dataset path inside `Population_and_Sampling_Analysis.py`.
4. Run the program.

```bash
python Population_and_Sampling_Analysis.py
```

---

# 📖 Sampling Techniques Implemented

- Population
- Sample
- Random Sampling
- Systematic Sampling
- Stratified Sampling
- Cluster Sampling
- Sampling Error
- Sampling Distribution
- Central Limit Theorem

---

# 🎓 Learning Outcomes

After completing this project, you will be able to:

- Differentiate between Population and Sample.
- Apply multiple Sampling Techniques using Python.
- Understand how different sampling methods work.
- Calculate Sampling Error.
- Generate Sampling Distributions.
- Explain the Central Limit Theorem using practical examples.
- Perform statistical sampling using real-world datasets.

---

# 📷 Sample Output

```
Population and Sampling Analysis using House Prices Dataset

Dataset Loaded Successfully!

========== DATASET SHAPE ==========
(1460, 81)

========== FIRST 5 ROWS ==========
   Id  MSSubClass MSZoning  ...  SaleType  SaleCondition SalePrice
0   1          60       RL  ...        WD         Normal    208500
1   2          20       RL  ...        WD         Normal    181500
2   3          60       RL  ...        WD         Normal    223500
3   4          70       RL  ...        WD        Abnorml    140000
4   5          60       RL  ...        WD         Normal    250000

[5 rows x 81 columns]

========== DATA TYPES ==========
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1460 entries, 0 to 1459
Data columns (total 81 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             1460 non-null   int64  
 1   MSSubClass     1460 non-null   int64  
 2   MSZoning       1460 non-null   object 
 3   LotFrontage    1201 non-null   float64
 4   LotArea        1460 non-null   int64  
 5   Street         1460 non-null   object 
 6   Alley          91 non-null     object 
 7   LotShape       1460 non-null   object 
 8   LandContour    1460 non-null   object 
 9   Utilities      1460 non-null   object 
 10  LotConfig      1460 non-null   object 
 11  LandSlope      1460 non-null   object 
 12  Neighborhood   1460 non-null   object 
 13  Condition1     1460 non-null   object 
 14  Condition2     1460 non-null   object 
 15  BldgType       1460 non-null   object 
 16  HouseStyle     1460 non-null   object 
 17  OverallQual    1460 non-null   int64  
 18  OverallCond    1460 non-null   int64  
 19  YearBuilt      1460 non-null   int64  
 20  YearRemodAdd   1460 non-null   int64  
 21  RoofStyle      1460 non-null   object 
 22  RoofMatl       1460 non-null   object 
 23  Exterior1st    1460 non-null   object 
 24  Exterior2nd    1460 non-null   object 
 25  MasVnrType     588 non-null    object 
 26  MasVnrArea     1452 non-null   float64
 27  ExterQual      1460 non-null   object 
 28  ExterCond      1460 non-null   object 
 29  Foundation     1460 non-null   object 
 30  BsmtQual       1423 non-null   object 
 31  BsmtCond       1423 non-null   object 
 32  BsmtExposure   1422 non-null   object 
 33  BsmtFinType1   1423 non-null   object 
 34  BsmtFinSF1     1460 non-null   int64  
 35  BsmtFinType2   1422 non-null   object 
 36  BsmtFinSF2     1460 non-null   int64  
 37  BsmtUnfSF      1460 non-null   int64  
 38  TotalBsmtSF    1460 non-null   int64  
 39  Heating        1460 non-null   object 
 40  HeatingQC      1460 non-null   object 
 41  CentralAir     1460 non-null   object 
 42  Electrical     1459 non-null   object 
 43  1stFlrSF       1460 non-null   int64  
 44  2ndFlrSF       1460 non-null   int64  
 45  LowQualFinSF   1460 non-null   int64  
 46  GrLivArea      1460 non-null   int64  
 47  BsmtFullBath   1460 non-null   int64  
 48  BsmtHalfBath   1460 non-null   int64  
 49  FullBath       1460 non-null   int64  
 50  HalfBath       1460 non-null   int64  
 51  BedroomAbvGr   1460 non-null   int64  
 52  KitchenAbvGr   1460 non-null   int64  
 53  KitchenQual    1460 non-null   object 
 54  TotRmsAbvGrd   1460 non-null   int64  
 55  Functional     1460 non-null   object 
 56  Fireplaces     1460 non-null   int64  
 57  FireplaceQu    770 non-null    object 
 58  GarageType     1379 non-null   object 
 59  GarageYrBlt    1379 non-null   float64
 60  GarageFinish   1379 non-null   object 
 61  GarageCars     1460 non-null   int64  
 62  GarageArea     1460 non-null   int64  
 63  GarageQual     1379 non-null   object 
 64  GarageCond     1379 non-null   object 
 65  PavedDrive     1460 non-null   object 
 66  WoodDeckSF     1460 non-null   int64  
 67  OpenPorchSF    1460 non-null   int64  
 68  EnclosedPorch  1460 non-null   int64  
 69  3SsnPorch      1460 non-null   int64  
 70  ScreenPorch    1460 non-null   int64  
 71  PoolArea       1460 non-null   int64  
 72  PoolQC         7 non-null      object 
 73  Fence          281 non-null    object 
 74  MiscFeature    54 non-null     object 
 75  MiscVal        1460 non-null   int64  
 76  MoSold         1460 non-null   int64  
 77  YrSold         1460 non-null   int64  
 78  SaleType       1460 non-null   object 
 79  SaleCondition  1460 non-null   object 
 80  SalePrice      1460 non-null   int64  
dtypes: float64(3), int64(35), object(43)
memory usage: 924.0+ KB

========== STATISTICAL SUMMARY ==========
                Id   MSSubClass  ...       YrSold      SalePrice
count  1460.000000  1460.000000  ...  1460.000000    1460.000000
mean    730.500000    56.897260  ...  2007.815753  180921.195890
std     421.610009    42.300571  ...     1.328095   79442.502883
min       1.000000    20.000000  ...  2006.000000   34900.000000
25%     365.750000    20.000000  ...  2007.000000  129975.000000
50%     730.500000    50.000000  ...  2008.000000  163000.000000
75%    1095.250000    70.000000  ...  2009.000000  214000.000000
max    1460.000000   190.000000  ...  2010.000000  755000.000000

[8 rows x 38 columns]

========== MISSING VALUES ==========
Id                 0
MSSubClass         0
MSZoning           0
LotFrontage      259
LotArea            0
                ... 
MoSold             0
YrSold             0
SaleType           0
SaleCondition      0
SalePrice          0
Length: 81, dtype: int64

========== DUPLICATE ROWS ==========
0

========== UNIQUE VALUES ==========
Id               1460
MSSubClass         15
MSZoning            5
LotFrontage       110
LotArea          1073
                 ... 
MoSold             12
YrSold              5
SaleType            9
SaleCondition       6
SalePrice         663
Length: 81, dtype: int64

========== POPULATION ==========
Total Number of Houses (Population) : 1460

========== SAMPLE ==========
Population Size : 1460
Sample Size : 100

First 5 Sample Records
        Id  MSSubClass MSZoning  ...  SaleType  SaleCondition SalePrice
892    893          20       RL  ...        WD         Normal    154500
1105  1106          60       RL  ...        WD         Normal    325000
413    414          30       RM  ...        WD         Normal    115000
522    523          50       RM  ...        WD         Normal    159000
1036  1037          20       RL  ...        WD         Normal    315500

[5 rows x 81 columns]

========== RANDOM SAMPLING ==========
Population Size : 1460
Random Sample Size : 50

First 5 Random Samples
        Id  MSSubClass MSZoning  ...  SaleType  SaleCondition SalePrice
892    893          20       RL  ...        WD         Normal    154500
1105  1106          60       RL  ...        WD         Normal    325000
413    414          30       RM  ...        WD         Normal    115000
522    523          50       RM  ...        WD         Normal    159000
1036  1037          20       RL  ...        WD         Normal    315500

[5 rows x 81 columns]

========== SYSTEMATIC SAMPLING ==========
Sampling Interval : 15
Systematic Sample Size : 98

First 5 Systematic Samples
    Id  MSSubClass MSZoning  ...  SaleType  SaleCondition SalePrice
0    1          60       RL  ...        WD         Normal    208500
15  16          45       RM  ...        WD         Normal    132000
30  31          70  C (all)  ...        WD         Normal     40000
45  46         120       RL  ...        WD         Normal    319900
60  61          20       RL  ...       New        Partial    158000

[5 rows x 81 columns]

========== STRATIFIED SAMPLING ==========
Total Population : 1460
Stratified Sample Size : 146

First 5 Stratified Samples
        Id  MSSubClass MSZoning  ...  SaleType  SaleCondition SalePrice
1186  1187         190       RL  ...        WD        Abnorml     95000
968    969          50       RM  ...        WD        Abnorml     37900
1436  1437          20       RL  ...        WD         Normal    120500
207    208          20       RL  ...        WD         Normal    141000
1049  1050          20       RL  ...        WD        Abnorml     84900

[5 rows x 81 columns]

========== CLUSTER SAMPLING ==========
Selected Clusters :
['OldTown', 'Gilbert', 'NAmes']

Cluster Sample Size : 417

First 5 Cluster Samples
    Id  MSSubClass MSZoning  ...  SaleType  SaleCondition SalePrice
8    9          50       RM  ...        WD        Abnorml    129900
14  15          20       RL  ...        WD         Normal    157000
16  17          20       RL  ...        WD         Normal    149000
19  20          20       RL  ...       COD        Abnorml    139000
26  27          20       RL  ...        WD         Normal    134800

[5 rows x 81 columns]

========== SAMPLING ERROR ==========
Population Mean Sale Price : 180921.20
Sample Mean Sale Price     : 180421.70
Sampling Error             : 499.50

========== SAMPLING DISTRIBUTION ==========
Number of Samples : 100
First 10 Sample Means
[177998.62, 182436.36, 186844.7, 193406.48, 197474.12, 172050.56, 156740.44, 174064.44, 183884.8, 183415.68]

Average of Sample Means : 180259.71

========== CENTRAL LIMIT THEOREM ==========
Population Mean           : 180921.20
Average Sample Mean       : 180259.71
Difference                : 661.49

Conclusion : The average of the sample means is very close to the population mean.
This demonstrates the Central Limit Theorem.

==============================================
PROJECT COMPLETED SUCCESSFULLY
Statistics Project 02
Population and Sampling Analysis using House Prices Dataset
==============================================
```

---

## 🎓 Project Type

**Project Type:** Statistics Project

**Domain:** Data Analytics

**Category:** Population and Sampling

**Difficulty Level:** Beginner to Intermediate

---

# 📚 Statistical Topics

- Population
- Sample
- Sampling Methods
- Sampling Error
- Sampling Distribution
- Central Limit Theorem

---

# 👩‍💻 Author

**Deekshitha U**

B.Tech Artificial Intelligence and Data Science

---

# ⭐ Future Work

This project establishes a strong foundation in **Population and Sampling** concepts. Future enhancements and related statistical studies include:

- Perform **Probability Distribution** analysis using real-world datasets.
- Apply **Hypothesis Testing** techniques such as t-tests, Chi-Square tests, and ANOVA.
- Explore **Confidence Intervals** and Margin of Error calculations.
- Compare different sampling techniques using larger datasets.
- Visualize sampling distributions using statistical graphs.
- Extend the project by applying **Bootstrapping** and **Resampling** methods.
- Implement **Monte Carlo Simulation** for statistical sampling experiments.
- Integrate this project with future statistics projects to build a comprehensive statistical analysis portfolio.