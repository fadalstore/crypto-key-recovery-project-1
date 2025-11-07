"""
Google Drive backup client (optional feature)

Requires:
- google-api-python-client
- google-auth
- google-auth-oauthlib
- google-auth-httplib2

Setup:
1. Enable Google Drive API in Google Cloud Console
2. Create service account and download JSON credentials
3. Set GOOGLE_SERVICE_ACCOUNT_JSON env variable with JSON content or path
4. Set DRIVE_FOLDER_ID to target folder ID in Drive
"""

import os
import json
from typing import Optional
from config import config


def upload_to_drive(file_path: str) -> Optional[str]:
    """
    Upload a file to Google Drive
    
    Args:
        file_path: Path to the file to upload
    
    Returns:
        File ID if successful, None otherwise
    """
    if not config.has_drive_backup:
        return None
    
    try:
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
        from google.oauth2 import service_account
        
        # Load service account credentials
        creds_json = config.GOOGLE_SERVICE_ACCOUNT_JSON
        
        # Check if it's a file path or JSON string
        if os.path.exists(creds_json):
            credentials = service_account.Credentials.from_service_account_file(
                creds_json,
                scopes=['https://www.googleapis.com/auth/drive.file']
            )
        else:
            creds_data = json.loads(creds_json)
            credentials = service_account.Credentials.from_service_account_info(
                creds_data,
                scopes=['https://www.googleapis.com/auth/drive.file']
            )
        
        # Build Drive service
        service = build('drive', 'v3', credentials=credentials)
        
        # Prepare file metadata
        file_metadata = {
            'name': os.path.basename(file_path),
        }
        
        # Add folder parent if specified
        if config.DRIVE_FOLDER_ID:
            file_metadata['parents'] = [config.DRIVE_FOLDER_ID]
        
        # Upload file
        media = MediaFileUpload(file_path, resumable=True)
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id,name,webViewLink'
        ).execute()
        
        print(f"☁️  Uploaded to Google Drive: {file.get('name')} (ID: {file.get('id')})")
        return file.get('id')
    
    except ImportError:
        print("⚠️  Google Drive libraries not installed. Install: pip install google-api-python-client google-auth")
        return None
    
    except Exception as e:
        print(f"❌ Google Drive upload failed: {e}")
        return None
