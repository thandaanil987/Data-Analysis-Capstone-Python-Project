import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1. Load Data
# ------------------------------
# Make sure 'sales_data.csv' is in the same folder as this script
df = pd.read_csv("sales_data.csv")

print("✅ Data Loaded Successfully!")
print(df.head())

# ------------------------------
# 2. Data Cleaning
# ------------------------------
# Fill missing values
df.fillna({
    "Quantity": df["Quantity"].median(),
    "Price": df["Price"].median()
}, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])

# Add TotalSales column
df["TotalSales"] = df["Quantity"] * df["Price"]

print("✅ Data Cleaning Completed!")

# ------------------------------
# 3. Exploratory Data Analysis
# ------------------------------
print("\n📊 Summary Statistics:")
print(df.describe(include="all"))

print("\n📊 Top 5 Products by Sales:")
if "Product" in df.columns:
    print(df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False).head())

# ------------------------------
# 4. Visualizations
# ------------------------------

# 4.1 Daily Sales Trend
plt.figure(figsize=(10,5))
df.groupby("Date")["TotalSales"].sum().plot()
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 4.2 Top 10 Products by Sales
if "Product" in df.columns:
    plt.figure(figsize=(10,5))
    df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False).head(10).plot(kind="bar")
    plt.title("Top 10 Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

# 4.3 Sales by Region
if "Region" in df.columns:
    plt.figure(figsize=(8,5))
    df.groupby("Region")["TotalSales"].sum().plot(kind="bar", color="orange")
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()

# 4.4 Monthly Sales Trend
plt.figure(figsize=(10,5))
df.groupby(df["Date"].dt.to_period("M"))["TotalSales"].sum().plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

print("✅ Analysis & Visualizations Completed!")
