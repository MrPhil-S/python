import pandas as pd

#dataframe similar to a row/column Excel spreadsheet

#easy way to create input data is using a dictionary

#create "Data#" headers
inputData = {"Data1":[1,2,3,4,5,6],
             "Data2":[5,6,7,8,7,8],
             "Data3":[9,10,11,12,00,12]}
print (inputData)

df = pd.DataFrame(inputData)

print(df)
print(df.head(2))
print(df.tail(2))
