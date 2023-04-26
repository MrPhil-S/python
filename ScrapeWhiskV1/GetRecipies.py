import re
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sqlite3
import whisk_secrets



conn = sqlite3.connect('whiskdata.db')

# create a cursor to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute('DROP TABLE IF EXISTS recipe')
#cursor.execute('CREATE TABLE recipe (id TEXT PRIMARY KEY, title TEXT)')
cursor.execute('''CREATE TABLE recipe (
      title TEXT,
      whisk_url TEXT,
      source_url TEXT,
      ingredient_count INT, 
      total_time TEXT)''')

# query the database
cursor.execute('SELECT * FROM recipe')

# print the results
for row in cursor.fetchall():
    print(row)


url =  'https://my.whisk.com/recipes'
email =  whisk_secrets.email
password =  whisk_secrets.password

#Selenium config:
PATH = "C:\\projects\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(url)

wait = WebDriverWait(driver, 10) # wait up to 10 seconds
username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))

# enter the email and click continue
username_field.send_keys(email)

username_field.send_keys(Keys.ENTER)

#wait 30s unitl password field present

element = WebDriverWait(driver, 30).until(
	EC.presence_of_element_located((By.ID, "_input-3"))
)
inputElement = driver.find_element(By.ID, '_input-3')

#inputElement = driver.find_element_by_class_name(fieldID)
inputElement.send_keys(password)
inputElement.send_keys(Keys.ENTER)

sleep(2)
#navigate to page
driver.get("https://my.whisk.com/recipe-box")


x = 4
print(f'Search will start in {x} seconds')
while x > 1:
  x -= 1
  sleep(1)
  print(f'{x}')
print(f'{x} seconds left, continuing...')

#scroll to bottom of cards
#last_height = driver.execute_script("return document.body.scrollHeight")
#while True:
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#    sleep(2)
#    new_height = driver.execute_script("return document.body.scrollHeight")
#    if new_height == last_height:
#        break
#    last_height = new_height

#get Whisk recipe page URLs
card_urls = []
card_headers_objs = driver.find_elements(By.XPATH, '//a[ contains(@class, "s189")]')  
for card_headers_obj in card_headers_objs:
  card_headers = card_headers_obj.text
  # print(f'HEADERS: {card_headers}')

  title = card_headers.split('\n')[0]
  
  try:
    ingredient_count = card_headers.split('\n')[1]
    if "ingredients" in ingredient_count:
      ingredient_count = ingredient_count.replace('ingredients','')
    else:
      ingredient_count = None
  except:
    ingredient_count = None
  
  
  try:
    total_time = card_headers.split('\n')[2]
    matches = ['h ', "min"]
    if any([x in total_time for x in matches]):
      pass
    else:
      total_time = None
  except:
    total_time = None

  url = card_headers_obj.get_attribute("href")
  url =  url.split('?')[0]
  card_urls.append(url)

  data = [title, url, ingredient_count, total_time]
  insert_statement = 'INSERT INTO recipe (title, whisk_url, ingredient_count, total_time) VALUES (?, ?, ?, ?)'
  conn.execute(insert_statement, data)
  
conn.commit()

total_recipes = len(card_urls)
print(f'{total_recipes} URLs found ')
#TESTING - limite the amount
card_urls = card_urls[:30]

#for each Whisk page, navigate within and get the souce URL
source_url_count = 0
source_urls = []
for whisk_url in card_urls:
  driver.get(whisk_url)
  random_sleep = random.uniform(1.5, 3)
  sleep(random_sleep)
  find_href = driver.find_elements(By.XPATH, '//a[ contains(@class, "s321")]')  
  if len(find_href) > 0:
    for source_url in find_href:
      source_url = source_url.get_attribute("href")
      source_url =  source_url.split('?')[0]
      #some recipes do not have an extranal URL. If so, this will return the current URL
      if source_url.startswith('https://my.whisk.com/profile/'):
        source_url = driver.current_url
      print(f'UPDATE recipe SET source_url = {source_url} WHERE whisk_url = {whisk_url}')
      conn.execute('''UPDATE recipe SET source_url = ? WHERE whisk_url = ?''', (source_url, whisk_url))
      conn.commit()

      source_urls.append(source_url)

    source_url_count += 1
    print(f'Remaining source urls obtained: {total_recipes - source_url_count} of {total_recipes}, ({int((source_url_count/total_recipes)*100)}%)')
  else:
    source_urls.append("Not Found")
   

  #times = driver.find_elements(By.XPATH, '//div[ @class="s12604"]/span[@class="s120 s1479"]')
  #types = driver.find_elements(By.XPATH, '//*div[ @class="s12604"]')
  types = driver.find_elements(By.XPATH, '//div[ @class="s12604"]')
  times = driver.find_elements(By.XPATH, '//div[ @class="s120 s1479"]')
  
  #alltime = zip(types, times)
  #print(alltime)
  print(times)

  prep = []
  cook = []
  othertime = []
  for type in types:
    print(type.text)
    for time in times:
      
      print(time.text)
      if type.text =='Prep:':
        prep.append(time.text)
      elif type.text == 'Cook:':
        cook.append(time.text)
      else: 
        othertime.append(type.text + ' ' + time.text)
  print(prep)
  print(cook)
  print(othertime)
  all = zip(prep, cook, othertime)
  print(all)
  
conn.close()

#driver.quit()