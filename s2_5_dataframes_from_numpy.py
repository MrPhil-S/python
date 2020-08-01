import numpy as np
import pandas as pd

new_array = np.arange(0,10).reshape(2,5)
#print(new_array)

df = pd.DataFrame(data=new_array, columns=['A','B','C','D','E'])
print (df)


#Create DataFrame from dictionary
