import time
from selenium import webdriver
#time to refresh page (seconds)
Timer = 20
#youtube link
link = input('please enter your link: ')
driver = webdriver.OperaDriver()
driver.get(link)

while True:
    time.sleep(Timer)
    driver.quit()
    print('done')
