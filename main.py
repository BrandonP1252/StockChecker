from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup(user_input):
    options = Options()
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print("Type 'Stop' to stop checking")
    check_stock(user_input, driver)


def check_stock(string, driver):
    while True:
        driver.get(string)
        if check_element('//button[text()="Add to Cart"]', driver):
            print("In Stock")
            break
            # send email
        else:
            print("Out of Stock")
        time.sleep(3)


def check_element(string, driver):
    try:
        element = driver.find_element(By.XPATH, string)
        return True
    except:
        return False


def main():
    user_input = input("Enter bestbuy URL: ")
    print("Running...")
    setup(user_input)





if __name__ == "__main__":
    main()
