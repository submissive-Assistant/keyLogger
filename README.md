**Disclaimer:**  

This code is provided for educational purposes only. The author takes no responsibility for any misuse or harm caused by using this tool. Please use it responsibly and ethically.

Here's the updated `README.md` with steps to acquire the **Google Drive Service Account Key JSON file**:

---

# Project Name

## Description

This project captures screenshots, records videos, and handles logs. It uploads files directly to Google Drive, ensuring no local storage of pictures. Log files are scheduled to be uploaded the next day and then removed from the local system after a successful upload.

All required files, including the Google Drive Service Account Key, should be placed in the same folder as the project.

---

## Features

- Capture and upload screenshots and pictures directly to Google Drive without saving them locally.
- Automatically upload log files to Google Drive on the next day.
- Automatically delete local files once uploaded to Google Drive.

---

## Prerequisites

Make sure you have the following installed on your system:

- Python (https://www.python.org/downloads/)
- Google Drive Service Account key (JSON file placed in the project folder)

---

## How to Acquire the Google Drive Service Account Key JSON File

1. **Go to the Google Cloud Console**:  
   Visit: https://console.cloud.google.com/

2. **Create a New Project**:  
   - Click on the **"Select a project"** dropdown.
   - Click on **"New Project"**.
   - Enter the project name and click **"Create"**.

3. **Enable the Google Drive API**:  
   - In the Google Cloud Console, navigate to **APIs & Services** > **Library**.
   - Search for **"Google Drive API"**.
   - Click on it and enable the API for your project.

4. **Create a Service Account**:  
   - In the left sidebar, go to **IAM & Admin** > **Service Accounts**.
   - Click on **"Create Service Account"**.
   - Enter a service account name and description, then click **"Create"**.
   - Grant any necessary roles (e.g., **Project > Editor**) and click **"Continue"**.

5. **Generate the Key File**:  
   - In the Service Account details page, go to the **Keys** tab.
   - Click on **"Add Key"** > **"Create New Key"**.
   - Choose **JSON** as the key type and click **"Create"**.
   - This will download a JSON file to your system (`your-key.json`).

6. **Place the Key File in Your Project Folder**:  
   - Move the downloaded JSON file to the same folder where your project files are located.

---

## Installation

Install the required dependencies by running:

```
pip install Pillow pynput google-api-python-client opencv-python-headless
```

---

## Setup

1. Place your **Google Drive Service Account Key JSON file** in the same folder as your project.
2. Ensure all project files are organized in the main project folder.
3. Edit your script to reference the path to the key file if needed.

---

## Usage

Run the project to capture and automatically upload images and log files to Google Drive. The following happens:

- Images are directly uploaded to Google Drive without storing them locally.
- Log files are automatically scheduled for upload the next day and then deleted after a successful upload.

---

## Troubleshooting

### Dependency Errors

If you encounter dependency errors, make sure all required packages are installed:

```
pip install Pillow pynput google-api-python-client opencv-python-headless
```

### Google Drive Authentication Issues

- Ensure the **Service Account Key JSON file** is in the same folder as your project.
- Verify that the key path is correctly referenced in your script.

### File Upload Errors

- Check your **Google Drive quota**.
- Ensure that folder **permissions** allow read/write access.

---

## Contributing

We welcome contributions! Feel free to fork the project, submit issues, or make pull requests. Open discussions and contributions will help improve the project.

---

## License

This project is open-source and free to use.

---

## Contact

If you have questions, issues, or suggestions, please feel free to open an issue on this repository. Happy coding! 🚀
