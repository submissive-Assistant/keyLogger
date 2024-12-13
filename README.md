**Disclaimer:**  

This code is provided for educational purposes only. The author takes no responsibility for any misuse or harm caused by using this tool. Please use it responsibly and ethically.

-----------------------------------------------------------------------------X----------------------------------------------------------------------------------------------------------------------
This project captures screenshots, records videos, and handles logs. It uploads files directly to Google Drive, ensuring no local storage of pictures. Log files are scheduled to be uploaded the next day and then removed from the local system after a successful upload.

All required files, including the Google Drive Service Account Key, should be placed in the same folder as the project.

Features
Capture and upload screenshots and pictures directly to Google Drive without saving them locally.
Upload log files to Google Drive automatically on the next day.
Automatically delete local files once uploaded to Google Drive.
Prerequisites
Ensure you have Python installed on your system.
Google Drive credentials setup (service account key) should be placed in the same folder as your project.
Installation
Install the required dependencies by running the following command:

bash
Copy code
pip install Pillow pynput google-api-python-client opencv-python-headless
Setup
Place your Google Drive Service Account Key JSON file in the same folder as your project.
Ensure all project files are in this designated project folder.
Configure the key path directly in your project script if required.
Usage
Run the project to capture and automatically upload images and log files to Google Drive.
Log files will be scheduled for upload the next day and then automatically deleted from your system once uploaded.
Troubleshooting
Dependency Errors: Ensure all required libraries are installed. Run:

bash
Copy code
pip install Pillow pynput google-api-python-client opencv-python-headless
Google Drive Authentication Issues:
Make sure the service account key file (your-key.json) is placed in the same folder as your project and the path is properly referenced in your script.

File Upload Errors: Check your Google Drive quota and folder permissions.

License
This project is open-source and free to use.


