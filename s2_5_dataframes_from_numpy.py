import numpy as np
import pandas as pd

#createing DataFrame from numpy numbers
new_array = np.arange(0,10).reshape(2,5)
print(new_array)

#convert to dataframe with no column names (they become automatically numbered)
dfn = pd.DataFrame(data=new_array)
print (dfn)

#Create the dataframe with column names
df = pd.DataFrame(data=new_array, columns=['A','B','C','D','E'])
print (df)


#Create DataFrame from dictionary
