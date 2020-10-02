import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#time to refresh page (seconds)
Timer = 20
#youtube link
link = input('please enter your link: ')
binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get(link)

while True:
    time.sleep(Timer)
    driver.quit()
    print('done')
