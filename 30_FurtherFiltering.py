import pandas as pd

sales_data = pd.read_csv('..\\git\\python_pandas\\sample_data\\04 Time Series\\sales_data.csv', parse_dates=True, index_col = 'InvoiceDate')

#print(sales_data.head())
#
#                    InvoiceNo StockCode                          Description  ...  UnitPrice  CustomerID         Country
#InvoiceDate                                                                   ...
#2010-12-01 08:26:00    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER  ...       2.55       17850  United Kingdom
#2010-12-01 08:26:00    536365     71053                  WHITE METAL LANTERN  ...       3.39       17850  United Kingdom
#2010-12-01 08:26:00    536365    84406B       CREAM CUPID HEARTS COAT HANGER  ...       2.75       17850  United Kingdom
#2010-12-01 08:26:00    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE  ...       3.39       17850  United Kingdom
#2010-12-01 08:26:00    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.  ...       3.39       17850  United Kingdom

#search only 1 column for partial string that containes something
search = sales_data['Description'].str.contains('POPPY')

#prints boolean True/False for ea column
#print(search)

total_poppy_sales = search.resample('H').sum()

print(total_poppy_sales)
