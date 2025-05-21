import pandas as pd

df = pd.read_csv('Read CSV/data.csv')

print(df.head())  #only head() will return the first 5 rows

#
print()
print()
#

print(df.head(10)) #this will return the first 10 rows

#
print()
print()
#

#using tail() method:
print(df.tail())  #this will return the last 5 rows.we can specify number of rows like tail(10)

#
print()
print()
#

#Info about the data:
print(df.info())