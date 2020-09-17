from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#PATH = "C:\ProgramData\Anaconda3\Lib\site-packages\chromedriver_py\chromedriver.exe"
#browser = webdriver.Chrome(PATH)
#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)
#browser = webdriver.PhantomJS(executable_path = r"c:\programdata\anaconda3\lib\site-packages")
url = "https://finance.yahoo.com/quote/MSFT/key-statistics?p=MSFT"

browser = webdriver.Firefox()

browser.get(url)
#print(browser.page_source)
element = browser.find_element_by_xpath("html")
#print(element.text)
print(element.get_attribute("textContent"))
browser.quit()
