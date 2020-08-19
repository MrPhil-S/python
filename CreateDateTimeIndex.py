import pandas as pd

#create from scratch
datetime_string = ['3/17/2010 08:26','3/22/2010 16:38','3/9/2010 12:24','4/21/2010 01:15','4/2/2010 23:44','4/11/2010 15:04']

time_format = '%m/%d/%Y %H:%M'

#convert date_list inot datetime object
new_datetime = pd.to_datetime(datetime_string, format=time_format)

print(new_datetime)
