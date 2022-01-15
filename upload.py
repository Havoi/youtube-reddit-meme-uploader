import datetime
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey
def credentials():
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    print(credentials)
    youtube = build('youtube', 'v3', credentials=credentials)
    return youtube

def upload(youtube):
    
    upload_date_time = datetime.datetime(2020, 8, 25, 12, 30, 0).isoformat() + '.000Z'

    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': 'funny reddit meme #shorts',
            'description': 'Did you like this meme? Comment Below',
            'tags': ['meme','shorts','funny','laugh','haha']
        },
        'status':{
            'privacyStatus':'public'
        }
    }

    mediaFile = MediaFileUpload('video.mp4')

    response_upload = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    """
    youtube.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload('thumbnail.png')
    ).execute()
    """

