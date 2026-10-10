import pandas as pd

df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("\nShape (rows, columns):")
print(df.shape)

print("\nInfo (column types, missing values):")
df.info()

print("\nBasic statistics:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())