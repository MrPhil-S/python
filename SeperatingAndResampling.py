import pandas as pd

sales_data = pd.read_csv('..\\git\\python_pandas\\sample_data\\04 Time Series\\sales_data.csv', parse_dates=True, index_col='InvoiceDate')

print(sales_data)
print('---------')
morning_sales = sales_data['Quantity']['2010-12-01']
#print(morning_sales)
#downsample
high_quantity = morning_sales.resample('H').max()

#print(high_quantity)
