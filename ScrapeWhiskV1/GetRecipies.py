import re
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sqlite3
import urllib
import whisk_secrets



conn = sqlite3.connect('whiskdata.db')

# create a cursor to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute('DROP TABLE IF EXISTS recipe')
#cursor.execute('CREATE TABLE recipe (id TEXT PRIMARY KEY, title TEXT)')
cursor.execute('''CREATE TABLE recipe (
      recipe_id INTEGER PRIMARY KEY,
      title TEXT,
      whisk_url TEXT UNIQUE,
      source_url TEXT,
      ingredient_count INTEGER, 
      total_time TEXT,
      prep_time TEXT,
      cook_time TEXT)''')

cursor.execute('DROP TABLE IF EXISTS recipe_ingredient')

cursor.execute('''CREATE TABLE recipe_ingredient (
      recipe_ingredient_id INTEGER PRIMARY KEY,
      recipe_id INTEGER,
      ingredient_id INTEGER,
      ingredient_written TEXT,
      ingredient_note TEXT)''')


# query the database
#cursor.execute('SELECT * FROM recipe')

# print the results
#for row in cursor.fetchall():
#    print(row)

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
def scroll_to_bottom():
  last_height = driver.execute_script("return document.body.scrollHeight")
  while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      sleep(2)
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height
#scroll_to_bottom()

#get Whisk recipe page URLs
whisk_urls = []
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

  whisk_url = card_headers_obj.get_attribute("href")
  whisk_url =  whisk_url.split('?')[0]
  whisk_urls.append(whisk_url)

  data = [title, whisk_url, ingredient_count, total_time]
  insert_statement = 'INSERT INTO recipe (title, whisk_url, ingredient_count, total_time) VALUES (?, ?, ?, ?)'
  conn.execute(insert_statement, data)
  
conn.commit()

total_recipes = len(whisk_urls)
print(f'{total_recipes} URLs found ')
#TESTING - limite the amount
#whisk_urls = whisk_urls[:30]

####for each Whisk page, navigate within and scrape
source_url_count = 0
source_urls = []
for whisk_url in whisk_urls:
  driver.get(whisk_url)
  random_sleep = random.uniform(1.5, 3)
  sleep(random_sleep)
  #get source URL
  find_href = driver.find_elements(By.XPATH, '//a[ contains(@class, "s321")]')  
  if len(find_href) > 0:
    for source_url in find_href:
      source_url = source_url.get_attribute("href")
      source_url =  source_url.split('?')[0]
      #some recipes do not have an extranal URL. If so, this will return the current URL
      if source_url.startswith('https://my.whisk.com/profile/'):
        source_url = driver.current_url
      conn.execute('''UPDATE recipe SET source_url = ? WHERE whisk_url = ?''', (source_url, whisk_url))
      conn.commit()

      source_urls.append(source_url)


    #Prints progress status
    source_url_count += 1
    print(f'{int((source_url_count/total_recipes)*100)}% complete. (Remaining source urls obtained: {total_recipes - source_url_count} of {total_recipes}))')
  else:
    source_urls.append("Not Found")
   
  #get cooking time
  types = driver.find_elements(By.XPATH, '//div[ @class="s12604"]')
  for type in types:
    time_amount = type.text.split('\n')[1]
    if 'Prep' in type.text:
      conn.execute('''UPDATE recipe SET prep_time = ? WHERE whisk_url = ?''', (time_amount, whisk_url))
    elif 'Cook' in type.text:
      conn.execute('''UPDATE recipe SET cook_time = ? WHERE whisk_url = ?''', (time_amount, whisk_url))
    else: 
      print('not found')
  conn.commit()
  

  #get ingredients
  cursor.execute('''SELECT recipe_id from recipe WHERE whisk_url = ?''', (whisk_url,))
  current_recipe = cursor.fetchone()
  current_recipe_id = current_recipe[0]

  ingredients = driver.find_elements(By.XPATH, '//span[ @data-testid="recipe-ingredient"]')
  for ingredient in ingredients:
    
    ingredient_written = ingredient.text.split('\n')[0]
    try:
      ingredient_note = ingredient.text.split('\n')[1]
    except:
      ingredient_note = None
    ingredient_data = [current_recipe_id, ingredient_written, ingredient_note ]
    insert_statement = '''INSERT INTO recipe_ingredient (recipe_id, ingredient_written, ingredient_note ) VALUES (?, ?, ?)'''
    conn.execute(insert_statement, ingredient_data)
  conn.commit()

  #click on image to expand
  image = driver.find_element("xpath", '//img[ contains(@class, "s321")]')
  image.click()
  sleep(2)
  #open file in write and binary mode
  with open(f'images//{current_recipe_id}.jpg', 'wb') as file:
  #identify image to be captured
    large_image = driver.find_element('xpath', '//img[ contains(@class, "s11933")]')
    #write file
    file.write(large_image.screenshot_as_png)
  #close the overlay window by clicking
  large_image.click()

  #need to get and match ingredient image

conn.close()

#driver.quit()