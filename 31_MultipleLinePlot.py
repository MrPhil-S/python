import pandas as pd
import matplotlib.pyplot as plt

stock_price = pd.read_csv ('..\git\python_pandas\sample_data\\04 Time Series\intel.csv', parse_dates=True, index_col='Date')

#print(stock_price.columns)
#print(stock_price.info)

#print(stock_price.head())
#plaot with date range and
#stock_price.loc ['2017-10-16':'2017-10-20','Close'].plot(kind='area', style='k.-', title='Intel')
stock_price.loc ['2017-10-16':'2017-10-20',['Open','Close']].plot(style='.-', title='Intel')
#stock_price.loc ['2017-10-16':'2017-10-20',['Open','Close']].plot(style='.-', title='Intel', subplots=True)
plt.ylabel('Closing Price')
plt.show()
