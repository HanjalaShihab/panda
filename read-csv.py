import pandas as pd

df = pd.read_csv('data.csv')

print(df) # this will print only the first and last 5 rows.

print()
print()
  #to print the whole table
print(df.to_string())



print()
print()
#or we can declare the max-row to a certain point like-

   #generally the max-rows are:
print(pd.options.display.max_rows)
          #this prints 60.So, the data-csv file will only print the first and last five rows.
          #we can change this by fixing the max-rows value


print()
print()
#but to set a value to max-rows:
pd.options.display.max_rows = 9999

print(df)