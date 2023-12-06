# Need to install ( pip install pynput )
from pynput.keyboard import Listener


# To listen to the keys and flow it
def on_press(key):
    listen = str(key).replace("'", "")
    print(listen)


with Listener(on_press=on_press, on_release=None) as listener:
    listener.join()
