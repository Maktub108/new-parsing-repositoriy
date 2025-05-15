import pandas as pd

df = pd.read_csv("referees.csv")

print(df.head())

print(df.info())

print(df.describe())


df = pd.read_csv('dz (4).csv')
print(df)

group = df.groupby('City')['Salary'].mean()
print(group)
