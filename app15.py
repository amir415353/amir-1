import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#time to refresh page (seconds)
Timer = 20
#youtube link
link = input('please enter your link: ')
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap, executable_path="/usr/bin/firefox")
driver.get(link)

while True:
    time.sleep(Timer)
    driver.quit()
    print('done')
