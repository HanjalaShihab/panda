# a series is like a column in a table
#it is a one-dimentional array holding data of any type


import  pandas as pd

print(pd.__version__)

#
print()
#

print(pd.Series([1,5,9]))

#
print()
#

a = [3, 7, 9]

b = pd.Series(a)
print(b[1])


print()
#creating labels(with the index argument):
a = [ 2, 5, 6]

m = pd.Series(a, index=["i.", "ii.", "iii."])

print(m)
print()
print(m["ii."])



print()
#creating a panda series from a dictionary:
calories = {
    "day 1": 420,
    "day 2": 380,
    "day 3": 390
}
x = pd.Series(calories, name = "calory table")
print(x)