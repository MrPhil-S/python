import requests
from bs4 import BeautifulSoup as bs

URL  = 'https://login.whisk.com/'
ORIGIN = 'https://my.whisk.com'
LOGIN_ROUTE = 'x/v1/auth/login'
#html = requests.get(url)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36'}

s = requests.session()

#access_token = s.get(URL).cookies['sessionId']

login_payload = {
        'email': 'dodehot848@maileze.net',
        'password': 'dff21234$op'
        }
 #       'access_token': access_token
        

login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
print(login_req.status_code)
print(login_req.reason)