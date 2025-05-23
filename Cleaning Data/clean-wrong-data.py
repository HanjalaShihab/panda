import pandas as pd

df = pd.read_csv("Cleaning Data/data.csv")


#we can find out the wrong data one by one and replace them! Like-
df.loc[7, 'Duration'] = 45   #data.csv file has a wrong data in the 7th row of the duration column.

print(df.to_string())


#
print()
df.loc[7, 'Duration'] = 450
print()



#but when working with a million of data it's impossible to replace wrong datas ony by one.
#so we will use for loop to replace wrong datas

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
        

#we can also remove the wrong data rows:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)