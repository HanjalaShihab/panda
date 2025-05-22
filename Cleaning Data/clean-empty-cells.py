import pandas as pd


#to only view the data.csv file:
with open('Cleaning Data/data.csv', 'r') as file:
    print(file.read())
    

#
print()
print()
#
    
#to remove all the Null or empty cells from the file:
df = pd.read_csv('Cleaning Data/data.csv')

new_df = df.dropna()   #dropna() method returns a new DataFrame, will not change the original
print(new_df.to_string())


#
print()
print()
#
    
#to change to the original file:
df = pd.read_csv('Cleaning Data/data.csv')

df.dropna(inplace=True)

print(df.to_string())


#
print()
print()
#
    

#use of fillna() method:
dff = pd.read_csv("Cleaning Data/data.csv")

dff.fillna(130, inplace=True)  #this will fill all the empty cells with 130
print(dff.to_string)


#
print()
print()
#
    

#to specificly insert any value in a column:
ds = pd.read_csv("Cleaning Data/data.csv")

ds.fillna({"Calories": 430}, inplace=True)
print(ds.to_string())


#
print()
print()
#
    

#to replace with mean() of a column:

ds = pd.read_csv("Cleaning Data/data.csv")

x = ds["Calories"].mean()

ds.fillna({"Calories": x}, inplace=True)
print(ds.to_string())


#
print()
print()
#

#to replace with median of a column:
ds = pd.read_csv("Cleaning Data/data.csv")

y = ds["Calories"].median()

ds.fillna({"Calories": y}, inplace=True)
print(ds.to_string())


#
print()
print()
#


#to replace with the mode() of a column:
dss = pd.read_csv("Cleaning Data/data.csv")

z = dss["Calories"].mode()[0]   #we used [0] because the mode can be multiple.So we are choosing the first one with [0]

dss.fillna({"Calories": z}, inplace=True)
print(dss.to_string())