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
      url TEXT)''')

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
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# get all the cards' titles
card_titles = []
cards = driver.find_elements(By.XPATH, '//h3[ contains(@class, "s1279")]')
for card in cards:
  card_titles.append(card.text)
#card_titles = card_titles[:3]

#get Whisk recipe page URLs
card_urls = []
urls = driver.find_elements(By.XPATH, '//a[ contains(@class, "s189")]')  
for url in urls:
  url = url.get_attribute("href")
  url =  url.split('?')[0]
  card_urls.append(url)
  #print(url)
total_recipes = len(card_urls)
print(f'{total_recipes} URLs found ')
#card_urls = card_urls[:3]

#for each Whisk page, navigate within and get the souce URL
source_url_count = 0
source_urls = []
for page in card_urls:
  driver.get(page)
  random_sleep = random.uniform(1.5, 5)
  sleep(random_sleep)
  find_href = driver.find_elements(By.XPATH, '//a[ contains(@class, "s321")]')  
  for recipe_url in find_href:
    recipe_url = recipe_url.get_attribute("href")
    #print(recipe_url)
    source_urls.append(recipe_url)
  source_url_count += 1
  print(f'Remaining source urls obtained: {total_recipes - source_url_count} of {total_recipes}, ({int((source_url_count/total_recipes)*100)}%)')


if len(card_titles) == len(source_urls):
  data = zip(card_titles, source_urls)
  # insert the data into the table
  insert_statement = 'INSERT INTO recipe (title, url) VALUES (?, ?)'
  conn.executemany(insert_statement, data)
  conn.commit()
  conn.close()
  print(f'{len(card_titles)} records inserted successfully')
else:
  print(f'lists do not match. Card titles: {len(card_titles)} and source urls: {len(source_urls)}')
  print(card_titles)
  print(source_urls)



# print the card titles
#for title in card_titles:
 # print(title)
#  cursor.execute('insert into recipe (title) values (?)', (title,))

#driver.quit()