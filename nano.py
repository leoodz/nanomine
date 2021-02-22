from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()

options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

browser = webdriver.Chrome()
browser.get('https://www.freenanofaucet.com/')
nanoaddr = browser.find_element_by_id('nanoAddr')
nanoaddr.send_keys('nano_3i8g53fikikuopx1ntbtotj6jchjfyqssjphek6dpwruykd9agtd1o4oactn')
button = browser.find_element_by_id('getNano')
button.click()
sleep(3)
browser.quit()
