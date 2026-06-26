
# WALMART SALES FORECASTING
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
# 1. LOAD DATASETS
# -----------------------------------------

train = pd.read_csv("train.csv")
features = pd.read_csv("features.csv")
stores = pd.read_csv("stores.csv")

print("Train Shape:", train.shape)
print("Features Shape:", features.shape)
print("Stores Shape:", stores.shape)

# -----------------------------------------
# 2. MERGE DATASETS
# -----------------------------------------

df = pd.merge(
    train,
    features,
    on=["Store", "Date", "IsHoliday"],
    how="left"
)

df = pd.merge(
    df,
    stores,
    on="Store",
    how="left"
)

print("\nMerged Dataset Shape:", df.shape)

# -----------------------------------------
# 3. DATA INSPECTION
# -----------------------------------------

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# -----------------------------------------
# 4. CHECK MISSING VALUES
# -----------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------------------
# 5. CHECK DUPLICATES
# -----------------------------------------

print("\nDuplicate Rows:", df.duplicated().sum())

# -----------------------------------------
# 6. DATA CLEANING
# -----------------------------------------

# Fill MarkDown columns with 0
markdown_cols = [
    'MarkDown1',
    'MarkDown2',
    'MarkDown3',
    'MarkDown4',
    'MarkDown5'
]

for col in markdown_cols:
    if col in df.columns:
        df[col] = df[col].fillna(0)

# Fill remaining missing values
if 'CPI' in df.columns:
    df['CPI'] = df['CPI'].fillna(df['CPI'].median())

if 'Unemployment' in df.columns:
    df['Unemployment'] = df['Unemployment'].fillna(
        df['Unemployment'].median()
    )

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------------------
# 7. EDA VISUALIZATIONS
# -----------------------------------------

# Weekly Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Weekly_Sales'], bins=50, kde=True)
plt.title("Weekly Sales Distribution")
plt.show()

# Sales Trend Over Time
sales_trend = df.groupby('Date')['Weekly_Sales'].sum()

plt.figure(figsize=(12,5))
plt.plot(sales_trend.index, sales_trend.values)
plt.title("Weekly Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# Holiday vs Non-Holiday Sales
plt.figure(figsize=(8,5))
sns.boxplot(
    x='IsHoliday',
    y='Weekly_Sales',
    data=df
)
plt.title("Holiday vs Non-Holiday Sales")
plt.show()

# Store Type Distribution
plt.figure(figsize=(6,4))
sns.countplot(
    x='Type',
    data=df
)
plt.title("Store Type Distribution")
plt.show()

# Correlation Heatmap
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10,8))
sns.heatmap(
    numeric_df.corr(),
    cmap='coolwarm',
    annot=False
)
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------------------
# 8. SAVE CLEANED DATA
# -----------------------------------------

df.to_csv(
    "Walmart_Cleaned_Data.csv",
    index=False
)

print("\nCleaned Dataset Saved Successfully")

# -----------------------------------------
# 9. SUMMARY
# -----------------------------------------

print("\n===== WEEK 1-2 COMPLETED =====")
print("Total Records:", len(df))
print("Total Stores:", df['Store'].nunique())
print("Total Departments:", df['Dept'].nunique())
print("Average Weekly Sales:", round(df['Weekly_Sales'].mean(), 2))
