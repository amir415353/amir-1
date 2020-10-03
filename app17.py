import time
from tbselenium.tbdriver import TorBrowserDriver
#time to refresh page (seconds)
Timer = 20
#youtube link
link = input('please enter your link: ')
with TorBrowserDriver() as driver:
    driver.get(link)
while True:
    time.sleep(Timer)
    driver.quit()
    print('done')
    exit()
