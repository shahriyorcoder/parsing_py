# from bs4 import BeautifulSoup
# import requests
# with open('home.html','r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml' )
#     course_card = soup.find_all("div",class_='card')
#     for course in course_card:
#         print(course.a.text.split()[-1])

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options




options=Options() 
options.add_experimental_option('detach', True) 
driver = webdriver.Chrome( options=options)
driver.maximize_window()
driver.get('https://www.olx.uz/d/myaccount')

driver.find_element(By.NAME,'username').send_keys('mahsudaliyevshahriyor398@gmail.com')
driver.find_element(By.NAME,'password').send_keys('Devoloper_0279')
driver.find_element(By.CLASS_NAME,'css-ypypxs').click()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,'css-2txnih').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,'css-v49bm8').send_keys('Iphone x OLED Multi-Touch displayHDR display2436')

driver.find_element(By.CLASS_NAME,'css-cjlwns').click()
time.sleep(1)

driver.find_element(By.CLASS_NAME,'css-kfy9sk').click()
driver.find_element(By.CLASS_NAME,'css-1grn515').click()
driver.find_element(By.CLASS_NAME,'css-7lx9dr').click()

driver.find_element(By.CLASS_NAME,'css-1kv2wi0').send_keys("5.8-inch (diagonal) all-screen OLED Multi-Touch displayHDR display2436-by-1125-pixel resolution at 458 ppi1,000,000:1 contrast ratio (typical)True Tone displayWide color display (P3)3D Touch625 cd/m2 max brightness (typical)Fingerprint-resistant oleophobic coatingSupport for display of multiple languages and characters simultaneouslyThe iPhone X display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 5.85 inches diagonally (actual viewable area is less) ")
time.sleep(6)

driver.find_element(By.CLASS_NAME,'css-6u0yjk').send_keys('3000')
time.sleep(3)

driver.find_element(By.CLASS_NAME,'css-19wrg31').click()

driver.find_element(By.CLASS_NAME,'css-v49bm8').send_keys('+998 91 603 0279')

driver.find_element(By.CLASS_NAME,'css-1anknvg').click()

driver.find_element(By.CLASS_NAME,'css-18l8bp6').click()
