import pandas as pd

df = pd.read_csv("Cleaning Data/data.csv")

print(df.duplicated())  #to spot the duplicates in the file


#
print()
print()
#


#to remove the duplicates:
df.drop_duplicates(inplace=True)

print(df.to_string)