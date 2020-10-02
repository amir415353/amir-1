import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 30

#youtube link
link = input('please enter your link:')

#number of views
views = 1

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
