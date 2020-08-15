import pandas as pd

#df = pd.read_csv('../git/python_pandas/sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv')
#print(df)
#make filepath easier

column_names = ['App','Rating','Reviews','Size','Number of Install','Type','Price','Last Updated']

#declare filepath variable
filepath = '../git/python_pandas/sample_data/02 Introduction to Pandas/edited_googleplaystore_dataset.csv'
#print(df.info())

#pandas uses the first row of data as the header
#remove this pandas default for first for header
#df = pd.read_csv(filepath,header=None)
#use the column_names that I set up above ^
#df = pd.read_csv(filepath,header=None, names=column_names)

#print(df.head())

#find erronous data
#print(df.tail())
#rating has a '-1' what we want to replace with NaN  not a number
df = pd.read_csv(filepath,header=None, names=column_names, na_values='-1')

###testing multiple NaNs)
##navals= ['159','967']
##df = pd.read_csv(filepath,header=None, names=column_names, na_values=navals)
######

#define own index (not the 0...# default)
df.index = df['Last Updated']
#print(df)
#define new columns (only the relevant columns we want)
new_columns = ['App','Reviews','Type']
#assign to dataframs
df = df[new_columns]

#print(df)
out_csv = 'Google Play Data.csv'
out_xlsx = 'Google Play Data xl.xlsx'
df.to_csv(out_csv)
df.to_excel(out_xlsx)

print(df)
#pd.set_option('display.max_rows', 40)
#pd.options.display.max_rows = 100
#print(pd.options.display.max_rows)
