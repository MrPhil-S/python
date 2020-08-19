import pandas as pd



sales_data = pd.read_csv('..\\git\\python_pandas\\sample_data\\04 Time Series\\sales_data.csv', parse_dates=True, index_col='InvoiceDate')

#print(sales_data.head(100))
#weekly_max = sales_data.resample('W').sum()
#print(weekly_max)
new_columns = ['Quantity','UnitPrice']

#weekly_max = sales_data.resample('W').sum().max()[new_columns]
#print(weekly_max)

#2 week avg

#TwoWeekly_mean = sales_data.resample('2W').mean()[new_columns]
#print(TwoWeekly_mean)

#output only the Quantity
weeklyquantitysum = sales_data.loc[:,'Quantity'].resample('d').sum()
weeklyquantityavg = sales_data.loc[:,'Quantity'].resample('d').mean()
print(weeklyquantitysum)
print(weeklyquantityavg)
