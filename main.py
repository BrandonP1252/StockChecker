import useragent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(
    "https://www.bestbuy.com/site/lenovo-ideapad-3i-15-6-hd-touch-laptop-core-i3-1115g4-8gb-memory-256gb-ssd-platinum-grey/6511950.p?skuId=6511950")
print("got here")
try:
    element = driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')
    print("In Stock")
except:
    print("Sold out")

