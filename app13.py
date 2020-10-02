import webbrowser
import time
from pykeyboard import PyKeyboard
url = input('please enter your link: ')
k = PyKeyboard()

while True:
    webbrowser.open(url, new=0)
    time.sleep(30)
    k.press_keys(['Command','W'])
    exit()

else:
    pass
