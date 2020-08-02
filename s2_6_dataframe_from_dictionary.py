import pandas as pd

#create the dictionary
course_sales = {'course':['Python','Ruby','Excel','C++'],
                'day':['Mon','Tue','Wed','Tue'],
                'price':[5,18,15,20],
                'sale':[2,3,5,7]}
#show that type =  dictionay
#print(type(course_sales))
#print(course_sales)

#convert to DataFrame
df_sales = pd.DataFrame(course_sales)
#Show that it is a type = dataframe
#print(type(df_sales))
#print(df_sales)


######### try my own #########
demo = {'city':['San Diego','Bellingham','New York'],
        'population':['1500000','80000','10600000'],
        'region':['SW','NW','East'],
        'infected':['50%','65%','56%']
        }
#print(demo)
#df_demo = pd.DataFrame(demo)
#print(df_demo)
######### End my own  #########

#Create into individual LISTS
course  =  ['Python','Ruby','Excel','C++']
day = ['Mon','Tues','Wed','Tues']
price = [5,13,15,17]
sale = [2,3,5,7]

#combine above column names into a list
labels = ['Course','Day','Price','# Sales']
#take the lists and combine into a list called columns
cols = [course, day, price, sale  ]
#Combine the lists (list within lists)
master_list = list(zip(labels,cols))
print(master_list)
data = dict(master_list)
#take the dict data and convert to dataframe
new_sales = pd.DataFrame(data)
print(new_sales)

#Lecture 14
#use Broacasting to cerate new columns
new_sales['New_Price'] = 2
print(new_sales)

# Lecture 15
#rename column labels
column_labels = ['Course', 'Day','Price','24hr sale price','discount']
new_sales.columns = column_labels
print(new_sales)

#16 Broacasting  to dataframe
