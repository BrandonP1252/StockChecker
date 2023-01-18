import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import smtplib
from email.message import EmailMessage


def setup(user_input, user_email):
    options = Options()
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    check_stock(user_input, driver, user_email)


def check_stock(string, driver, user_email):
    while True:
        driver.get(string)
        if check_element('//button[text()="Add to Cart"]', driver):
            print("In Stock")
            driver.close()
            send_email(user_email, string)
            break
        else:
            print("Out of Stock")
        time.sleep(3)


def check_element(string, driver):
    try:
        element = driver.find_element(By.XPATH, string)
        return True
    except:
        return False


def send_email(user_email, user_input):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Item in Stock'
        msg['From'] = 'Stock Bot'
        msg['To'] = user_email
        msg.set_content("Item is in stock! Link: " + user_input)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.environ.get('stockemail'), os.environ.get('stockpass'))
        server.sendmail(os.environ.get('stockemail'), user_email, msg.as_string())
        print("Email sent successfully")
        server.quit()
    except:
        print("Failed to send email")

def main():
    user_input = input("Enter bestbuy URL: ")
    user_email = input("Enter your email: ")
    print("Running...")
    setup(user_input, user_email)


if __name__ == "__main__":
    main()
