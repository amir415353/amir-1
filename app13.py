import webbrowser
import time
url = input('enter your link: ')

while True:
    webbrowser.open(url, new=0)
    time.sleep(30)
    exit()

else:
    pass
