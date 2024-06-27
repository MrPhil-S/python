import os
import smtplib
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Function to send email notification
def send_email(subject, body):
    sender_email = "nopschims@gmail.com"
    receiver_email = "pschims@gmail.com"
    password = "temppass1"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Setup the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')  # Disable GPU acceleration
driver = webdriver.Chrome(options=options)

url = "https://bevmo.com/products/8644"

# Open the URL
driver.get(url)

try:
    # Wait for the price element to be present and visible
    price_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".price-item.price-item--regular"))
    )
    
    # Get the text of the price element
    current_price = price_element.text

    # Read previous price from file or database
    previous_price_file = "price.txt"
    if os.path.exists(previous_price_file):
        with open(previous_price_file, 'r') as f:
            previous_price = f.read().strip()
    else:
        previous_price = None

    # Compare current price with previous price
    if previous_price is not None and current_price != previous_price or 1==1:
        # Notify price change
        subject = "Price Change Alert"
        body = f"The price has changed!\nPrevious Price: {previous_price}\nCurrent Price: {current_price}"
        send_email(subject, body)
        print('email sent')

    # Update previous price file
    with open(previous_price_file, 'w') as f:
        f.write(current_price)

except Exception as e:
    print("Price check failed:", str(e))

finally:
    # Close the driver
    driver.quit()
