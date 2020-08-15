import pandas as pd
import matplotlib.pyplot as plt

life = pd.read_csv('..\git\python_pandas\sample_data\\03 Data Analysis\irish_life_expec.csv')

#investigate file
#print (life.info())

# print dataframe
print(life)

#create scatter plot w x = yr and y = life irish_life_expec
life.plot(kind='scatter',x


#nams axis : month (name 'month' in file) and y (from above)
