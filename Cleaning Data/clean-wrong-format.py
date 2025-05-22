import pandas as pd

df = pd.read_csv("Cleaning Data/data.csv")

df['Date'] = pd.to_datetime(df['Date'], format = "mixed")

print(df.to_string())


#
print()
print()
#

#to delete the empty cells of only Date column:
df.dropna(subset=['Date'], inplace=True)
print(df.to_string())