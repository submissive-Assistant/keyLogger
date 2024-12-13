from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload, MediaFileUpload
from google.oauth2 import service_account


#Path to your service account key file
SERVICE_ACCOUNT_FILE = 'path_to_your_credentials.json'

# Scopes required for accessing Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Authenticate using the service account
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Build the Google Drive API client
drive_service = build('drive', 'v3', credentials=credentials)

mime_type = 'image/jpeg'

def get_or_create_folder(folder_name):
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()

    folders = results.get('files', [])
    if folders:
        print(f"Folder '{folder_name}' found with ID: {folders[0]['id']}")
        return folders[0]['id']
    else:
        # If the folder doesn't exist, create it
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
        print(f"Folder '{folder_name}' created with ID: {folder['id']}")
        return folder['id']


def upload_in_memory_image(image_data, file_name, folder_id):
    try:
        # Specify the file metadata
        file_metadata = {
            'name': file_name,
            'parents' : [folder_id]
            }
        
        # Prepare the in-memory file for upload
        media = MediaIoBaseUpload(image_data, mimetype='image/jpeg', resumable=True)
        
        # Upload the file
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        print(f'File uploaded successfully. File ID: {file["id"]}')
    except Exception as e:
        print(f"Error: {e}")
    return

def upload_text_file(file_path, file_name, folder_id):
    try:
        # Define metadata for the file
        file_metadata = {
            'name': file_name,
            'parents' : [folder_id]
        }
        
        # If a folder ID is provided, add it to metadata
        if folder_id:
            file_metadata['parents'] = [folder_id]

        # Upload the file to Google Drive
        media = MediaFileUpload(file_path, mimetype='text/plain')
        file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        print(f'Text file "{file_name}" uploaded successfully. File ID: {file["id"]}')
    except Exception as e:
        print(f"Error: {e}")
    return

