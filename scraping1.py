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

#create a list
splitlist = htmlText.split("1y Target Est")
print(len(splitlist))

#parse the split
#we know that the elemement we want is the 2nd item in the splitlist
#print(splitlist[1]) --too long

#get the first [0:n] characters
#print(splitlist[1][0:1000]), get the [2] elemement occurance
#print(splitlist[1][0:1000].split("\">")[2])
leadingsplit = splitlist[1][0:1000].split("\">")[2]
trailingsplit = leadingsplit.split("</span>")
data = trailingsplit[0]
print(data)
