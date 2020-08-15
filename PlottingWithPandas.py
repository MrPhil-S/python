import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('..\git\python_pandas\sample_data\\02 Introduction to Pandas\intel.csv', index_col='Date',parse_dates=True)

#investigate file
#print(df.info())
#print(df.head())

#create series
close_value = df['Close'].values

#Check the type of the close_value (array)
#print(type(close_value))

#numpy plot
#plt.plot(close_value)
#plt.show()


#pandas data frame pyplot
#df.plot()
#plt.show()

############
#Clean up the chart
#create series with grren (g), line (-) and legend
#df['Close'].plot(color='g',style='-',legend=True)

#plt.axis(('2017','2018',0,60))

#df.plot()
df.plot(color='blue')
plt.title('Stock Price')
plt.xlabel('Date')
plt.ylabel('Price($)')

#plt.show()
plt.savefig('df.png')
