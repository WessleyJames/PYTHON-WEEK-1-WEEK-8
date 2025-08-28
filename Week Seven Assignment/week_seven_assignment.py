# Week 7 Assignment: Data Analysis with Pandas and Visualization
# Author: Your Name

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ----------------------------
# Task 1: Load and Explore the Dataset
# ----------------------------

try:
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame

    # Display first few rows
    print("First 5 rows of dataset:")
    print(df.head(), "\n")

    # Dataset info
    print("Dataset info:")
    print(df.info(), "\n")

    # Check for missing values
    print("Missing values in dataset:")
    print(df.isnull().sum(), "\n")

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# ----------------------------
# Task 2: Basic Data Analysis
# ----------------------------

try:
    # Basic statistics
    print("Descriptive statistics:")
    print(df.describe(), "\n")

    # Group by species (target column) and compute mean
    grouped = df.groupby("target").mean()
    print("Mean values grouped by target (species):")
    print(grouped, "\n")

except Exception as e:
    print(f"An error occurred during analysis: {e}")

# ----------------------------
# Task 3: Data Visualization
# ----------------------------

try:
    # Set Seaborn style
    sns.set(style="whitegrid")

    # 1. Line chart (cumulative sum of sepal length to simulate trend)
    df["sepal length cumulative"] = df["sepal length (cm)"].cumsum()
    plt.figure(figsize=(8, 5))
    plt.plot(df.index, df["sepal length cumulative"], label="Cumulative Sepal Length", color="blue")
    plt.title("Line Chart: Cumulative Sepal Length Over Samples")
    plt.xlabel("Sample Index")
    plt.ylabel("Cumulative Sepal Length (cm)")
    plt.legend()
    plt.show()

    # 2. Bar chart (average petal length per species)
    plt.figure(figsize=(8, 5))
    sns.barplot(x="target", y="petal length (cm)", data=df, estimator="mean", palette="viridis")
    plt.title("Bar Chart: Average Petal Length per Species")
    plt.xlabel("Species (0=setosa, 1=versicolor, 2=virginica)")
    plt.ylabel("Average Petal Length (cm)")
    plt.show()

    # 3. Histogram (distribution of sepal length)
    plt.figure(figsize=(8, 5))
    sns.histplot(df["sepal length (cm)"], bins=20, kde=True, color="green")
    plt.title("Histogram: Distribution of Sepal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Scatter plot (sepal length vs petal length)
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", palette="deep", data=df)
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.show()

except Exception as e:
    print(f"An error occurred during visualization: {e}")
 
