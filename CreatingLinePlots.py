import pandas as pd
import matplotlib.pyplot as plt

stock_prices = pd.read_csv('..\git\python_pandas\sample_data\\03 Data Analysis\intel_amd_stock_prices.csv')

#investigate file
#print(stock_prices.info())
#print(stock_prices)

#y columns
y_columns = ['intel','amd']

#nams axis : month (name 'month' in file) and y (from above)
stock_prices.plot(x='month',y=y_columns)

plt.title('Monthly stock prices')

plt.ylabel('prices')

plt.show()
