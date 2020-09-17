import requests

SP500 = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
SP500response = requests.get(SP500)

data = {"Company":[]}

SPTable = SP500response.text.split("<tbody>")[1]

row = SPTable.split("<tr>")
for position in range(len(row)):
   #print(position)
    if position > 1:
        tempdata = row[position].split("\">")[1].split("</a>")[0]
        data["Company"].append(tempdata)

#print(data["Company"])

#create a dictionary
Indicators = {  "Previous Close":[],
                "Open":[],
                "Bid":[],
                "Ask":[],
                "Day&#x27;s Range":[],
                "52 Week Range":[],
                "Volume":[],
                "Avg. Volume":[],
                "Market Cap":[],
                "Beta (5Y Monthly)":[],
                "PE Ratio (TTM)":[],
                "EPS (TTM)":[],
                "Earnings Date":[],
                "Forward Dividend &amp; Yield":[],
                "Ex-Dividend Date":[],
                "1y Target Est":[]}


#url = "https://finance.yahoo.com/quote/MSFT?p=MSFT"#&.tsrc=fin-srch

#print(response)
#print(response.status_code)

#print(response.text)
#save it


#split - split the string to a list at the () na_values
#example = "AbBdDbe"
#print(example.split("b"))
#print(htmlText)
counter = 0
#loop through the data dictionary vaiable in the "company" key
for ticker in data["Company"]:
   # url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker+"&.tsrc=fin-srch"
    url = ("https://finance.yahoo.com/quote/"+ticker+"?p="+ticker)
    print(url)

    #url = "https://finance.yahoo.com/quote/msft?p=msft"
    response = requests.get(url)
    htmlText = response.text

    for indicator in Indicators:

        #create a list


        #print(htmlText[0:100000])

        splitlist = htmlText.split(indicator)


        #parse the split
        #we know that the elemement we want is the 2nd item in the splitlist
        #print(splitlist[1]) #too long

        #get the first [0:n] characters
        #print(splitlist[1][0:9000]) #, get the [2] elemement occurance
        if indicator in ("Day&#x27;s Range","52 Week Range", "Forward Dividend &amp; Yield"):
            splitloc = 1
        else:
            splitloc = 2

        #print(splitlist[1].split("\">")[splitloc])


        leadingsplit = splitlist[1].split("\">")[splitloc]
        trailingsplit = leadingsplit.split("</")
        #data = trailingsplit[0]
        #print(data)
        dataValue = trailingsplit[0]
        #print(dataValue)

    #leadingsplit = splitlist[1][0:1000].split("\">")[1]
    #print (leadingsplit)
    #replacespan = leadingsplit.replace("</span>","")
        Indicators[indicator].append(dataValue)

    counter += 1
    if counter > 10:
        break



print(Indicators)
    #print(data)
