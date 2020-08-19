import pandas as pd

'''
#creare dataframs
playdata = pd.read_csv('../git/python_pandas/sample_data/02 Introduction to Pandas/Googleplaystore.csv')


#print(playdata)
#print(playdata.columns)

#print(playdata[playdata['Rating'] == 3])

#above average rating
#avg = playdata['Rating'].mean()
#print(playdata[playdata['Rating'] > avg])

#print(playdata[playdata['Rating'] > 5 ])

arcade_data = playdata[playdata['Genres'] == 'Arcade']
print(arcade_data)
'''


stock_data = pd.read_csv('..\\git\\python_pandas\sample_data\\03 Data Analysis\\tesla.csv')

#print(stock_data['Open'])
#                  Go into dafaframe
print (stock_data[stock_data['Open'] == 315])
