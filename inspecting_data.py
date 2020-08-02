##Skillshare https://www.skillshare.com/classes/Learn-Python-for-Data-Analysis-and-Visualization/1698648511/projects
import pandas as pd

#df = pd.read_csv ('..\git\python_pandas\sample_data\\02 Introduction to Pandas\intel.csv')
df = pd.read_csv ('..\git\python_pandas\sample_data\\02 Introduction to Pandas\intel.csv')
#df is a variable

#print(df)

# How to check data type
# print(type(df))
#print (type(df))

#print(df.shape)

# column names
#print(df.columns)

# limit data result to first x  number of rows (5 by default)
#print(df.head())

#print("limit data result to last x  number of rows (5 by default)")
#print(df.tail())

# data info
#print(df.info())

# print the "Open" col  (case sensitive to the data header) - in a panda series
# [] brings us into the data frama
# open = df['Open']
# print(open)
#or

#high = df['High']
#print(high)

#open = df['Open']
#print(open.head())

#Do it in 1 step
#print(df['High'].head())


#View 1+ columns side by side
# [] brings us into the data frama
#print(df[['Open','Close']].head(50))
#print(df[['Open','Close']].head())

#avg, min, max, %25tile
#print(df.describe())

###10. COONDITIONAL FILTERING####
#my_open = df['Open'] > 55
#return only the boolean for columns only - not useful
#print(my_open)

#print the data where condition is met, put the variable in a Dataframe "[]"
#print(df[my_open])

#orint in the same in 1 step without variable
#print(df[df['Open'] > 55.5 ])

# 11) #using NumpPy and pandas together###
#open = df['Open']
#Print the column as dataframe
#print(open)

#what type of data are we using?
#print(type(open))

#extract values from the variable (open)
#new_open = open.values
#print(new_open)
#they are an array
#print(type(new_open))

#or as 1 step:
#print(type(df['Open'].values))

#when we extract the .values from a  DataFrame column, it becomes a series
#print(new_open)
