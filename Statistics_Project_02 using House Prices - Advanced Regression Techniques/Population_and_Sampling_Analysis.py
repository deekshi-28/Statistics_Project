# ==========================================================
# Population and Sampling Analysis using House Prices Dataset
# ==========================================================

print("Population and Sampling Analysis using House Prices Dataset")

# ==========================================================
# 1. Import Libraries
# ==========================================================

import pandas as pd
import numpy as np
import random

# ==========================================================
# 2. Load Dataset
# ==========================================================

file_path = r"C:\Users\deek\Downloads\data analytics\DA Projects\Statistics_Project\Statistics_Project_02 using House Prices - Advanced Regression Techniques\train.csv"
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
print(dataset.nunique())  # Print the number of unique values for each column

# ==========================================================
# 5. Population
# ==========================================================

print("\n========== POPULATION ==========")

population_size = len(dataset)
print("Total Number of Houses (Population) :", population_size)

# ==========================================================
# 6. Sample
# ==========================================================

print("\n========== SAMPLE ==========")

sample = dataset.sample(n=100, random_state=42)
print("Population Size :", len(dataset))
print("Sample Size :", len(sample))
print("\nFirst 5 Sample Records")
print(sample.head())

# ==========================================================
# 7. Random Sampling
# ==========================================================

print("\n========== RANDOM SAMPLING ==========")

random_sample = dataset.sample(n=50, random_state=42)
print("Population Size :", len(dataset))
print("Random Sample Size :", len(random_sample))
print("\nFirst 5 Random Samples")
print(random_sample.head())

# ==========================================================
# 8. Systematic Sampling
# ==========================================================

print("\n========== SYSTEMATIC SAMPLING ==========")

step = 15
systematic_sample = dataset.iloc[::step]
print("Sampling Interval :", step)
print("Systematic Sample Size :", len(systematic_sample))
print("\nFirst 5 Systematic Samples")
print(systematic_sample.head())

# ==========================================================
# 9. Stratified Sampling
# ==========================================================

print("\n========== STRATIFIED SAMPLING ==========")

stratified_sample = (
    dataset.groupby("OverallQual", group_keys=False)
    .sample(frac=0.10, random_state=42)
)
print("Total Population :", len(dataset))
print("Stratified Sample Size :", len(stratified_sample))
print("\nFirst 5 Stratified Samples")
print(stratified_sample.head())

# ==========================================================
# 10. Cluster Sampling
# ==========================================================

print("\n========== CLUSTER SAMPLING ==========")

clusters = dataset["Neighborhood"].unique()
selected_clusters = random.sample(list(clusters), 3)
cluster_sample = dataset[dataset["Neighborhood"].isin(selected_clusters)]
print("Selected Clusters :")
print(selected_clusters)
print("\nCluster Sample Size :", len(cluster_sample))
print("\nFirst 5 Cluster Samples")
print(cluster_sample.head())

# ==========================================================
# 11. Sampling Error
# ==========================================================

print("\n========== SAMPLING ERROR ==========")

population_mean = dataset["SalePrice"].mean()
sample_mean = sample["SalePrice"].mean()
sampling_error = population_mean - sample_mean
print(f"Population Mean Sale Price : {population_mean:.2f}")
print(f"Sample Mean Sale Price     : {sample_mean:.2f}")
print(f"Sampling Error             : {sampling_error:.2f}")

# ==========================================================
# 12. Sampling Distribution
# ==========================================================

print("\n========== SAMPLING DISTRIBUTION ==========")

sample_means = []
for i in range(100):
    sample_data = dataset.sample(n=50)
    sample_means.append(sample_data["SalePrice"].mean())

print("Number of Samples :", len(sample_means))
print("First 10 Sample Means")
print(sample_means[:10])
print("\nAverage of Sample Means :", round(np.mean(sample_means),2))

# ==========================================================
# 13. Central Limit Theorem
# ==========================================================

print("\n========== CENTRAL LIMIT THEOREM ==========")

population_mean = dataset["SalePrice"].mean()
average_sample_mean = np.mean(sample_means)
print(f"Population Mean           : {population_mean:.2f}")
print(f"Average Sample Mean       : {average_sample_mean:.2f}")
difference = abs(population_mean - average_sample_mean)
print(f"Difference                : {difference:.2f}")
if difference < 5000:
    print("\nConclusion : The average of the sample means is very close to the population mean.")
    print("This demonstrates the Central Limit Theorem.")
else:
    print("\nConclusion : Increase the sample size or number of samples for a better approximation.")

# ==========================================================
# 14. Conclusion
# ==========================================================

print("\n==============================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("Statistics Project 02")
print("Population and Sampling Analysis using House Prices Dataset")
print("==============================================")