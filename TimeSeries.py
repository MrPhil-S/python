import pandas as pd

#date and time stored in datetime objects.
#pandas read_csv function can be used to read strings into datetime objects

#indexing time series:

sales_data = pd.read_csv('..\git\python_pandas\sample_data\\04 Time Series\\sales_data.csv',parse_dates=True, index_col='InvoiceDate')

#print(sales_data)
#print(sales_data.head(20))

#show that we are dealing with a datetime index
#print(sales_data.info())



#use the .loc accessor to select data by row
#morningsale = sales_data.loc['2010-12-01 08:35:00']

#use the .loc accessor to select data by row and column
#                               partial datetime
#morningsale = sales_data.loc['2010-12']

#use slicing to select a datetime range:
morningsale = sales_data.loc['2010-12-01 08:26:00':'2010-12-01 09:00:00']

print(morningsale)
