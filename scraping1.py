import requests
url = "https://finance.yahoo.com/quote/MSFT?p=MSFT"

response = requests.get(url)


indicators = ["Previous Close",
                "Open",
                "Bid",
                "Ask",
                "Day's Range",
                "52 Week Range",
                "Volume",
                "Avg. Volume",
                "Market Cap",
                "Beta (5Y Monthly)",
                "PE Ratio (TTM)",
                "EPS (TTM)",
                "Earnings Date",
                "Forward Dividend & Yield",
                "Ex-Dividend Date",
                "1y Target Est"]

print(response)
print(response.status_code)
#print(response.text)
#save it
htmlText = response.text

#split - split the string to a list at the () na_values
#example = "AbBdDbe"
#print(example.split("b"))

splitlist = htmlText.split("Previous Close")
print(len(splitlist))
