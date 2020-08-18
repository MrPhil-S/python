import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime
#from datetime import datetime

today = date.today()
print("Today's date:", today)
now = datetime.now()
nowfilename = now.strftime("%d-%m-%Y_%H%M%S")

stock_prices = pd.read_csv('..\git\python_pandas\sample_data\\03 Data Analysis\intel_stock_price.csv')

print(stock_prices)

stock_prices.plot(y='price', x='month', kind='bar', color='gray' ,legend=False)

plt.xlabel('month')


plt.savefig('bar_{0}.png'.format(today))
plt.savefig('bar_{0}.png'.format(nowfilename))
plt.show()
