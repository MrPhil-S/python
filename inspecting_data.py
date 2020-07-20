import pandas as pd

df = pd.read_csv ('..\git\python_pandas\sample_data\\02 Introduction to Pandas\intel.csv')
#df is a variable

# print(df)

# How to check data type
# print(type(df))

# print(df.shape)

# column names
# print(df.columns)

# limit data result to first x  number of rows (5 by default)
# print(df.head(100))

# limit data result to last x  number of rows (5 by default)
# print(df.tail(100))

# data info
# print(df.info())

# print the "Open" col  (case sensitive to the data header)
# open = df['Open']
# print(open)

#print(open.head())

#View 1+ columns side by side
# [] brings us into the data frama
#print(df[['Open','Close']].head(50))

#avg, min, max, %25tile
# print(df.describe())
