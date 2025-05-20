import pandas as pd

data = {
    "Catagory": ["Islamic history", "fiction", "non-fiction"],
    "Books": [20, 15, 18]
}

x = pd.DataFrame(data)
print(x)



#
print()
print()
#

#renaming the labels or indices:
data = {
    "category": ["Islamic history", "Bangladesh history", "British history"],
    "Books": [20, 10, 8]
}

x = pd.DataFrame(data, index=["row-1", "row-2", "row-3"])
print(x)


#
print()
print()
#

#using the 'loc' attribute to locate row:
info = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

myvar = pd.DataFrame(info)
print(myvar)
print()

      #loc attribute:
print(myvar.loc[0])   #this returns a pandas series
print()

print(myvar.loc[[0]])  #this returns a pandas dataframe
print()

print(myvar.loc[[0, 1]])
print()
print()

# naming the indices or labels:
myvar2 = pd.DataFrame(info, index=["day1", "day2", "day3"])
print(myvar2)
print()
print()


#now we can locate the named indexes:
print(myvar2.loc[["day1"]])