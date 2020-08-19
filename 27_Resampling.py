import pandas as pd

#Resampling used to apply statistical methods (mean, SM , count etc) over different time periods (ex: day, wk, month)

sales_data = pd.read_csv('..\\git\\python_pandas\\sample_data\\04 Time Series\\resampling_sales_data.csv', parse_dates=True, index_col='InvoiceDate')

#print(sales_data)

#downsampling

#weekly_mean = sales_data.resample('W').mean()
#print(weekly_mean)

#mean sales/month
monthly_mean = sales_data.resample('M').mean()
print(monthly_mean)
print('----------')

#2010-01-31    6.000000   2.100000
#2010-02-28    3.833333   5.641667
#2010-03-31   23.333333   2.136667
#2010-04-30         NaN        NaN
#2010-05-31         NaN        NaN

#(first col is end of month)

#investigate NaN - ensure ther are no sales (only selecting specific columns)
print(monthly_mean.loc['2010-03-31'])
#print(monthly_mean.loc['2010-01-31','Quantity'])


#monthly_sum = sales_data.resample('M').sum()
#print(monthly_sum)
#print('-------')
#print(monthly_sum.loc['2010-03-31'])
