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


#View 1+ columns side by side
# [] brings us into the data frama
#print(df[['Open','Close']].head(50))
#print(df[['Open','Close']].head())

#avg, min, max, %25tile
#print(df.describe())
print(df.describe())

###COONDITIONAL FILTERING####
#my_open = df['Open'] > 40
#print(my_open)
#print(df[my_open])
#print(df[df['Open'] > 55])

##using NumpPy and pandas together###
#open = df['Open']
#what type of data are we using
#print(type(open))
#new_open = open.values
#print(type(new_open))
#print(new_open)
