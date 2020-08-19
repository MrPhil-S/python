import pandas as pd
import matplotlib.pyplot as plt

#create dataframe
stock_prices = pd.read_csv('..\\git\\python_pandas\sample_data\\03 Data Analysis\\tesla.csv')

#call the dataframe
#print(stock_prices)

#describe methode (non null numberical data only)
#print(stock_prices.describe())

print(stock_prices['Open'].min())
print(stock_prices['Open'].max())
print(stock_prices['Open'].mean())

#box plot
stock_prices[('Open')].plot(kind='box')

plt.show()
