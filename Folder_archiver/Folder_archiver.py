import os 
import zipfile
from data import Data
from tkinter import messagebox as mb
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io

try:
    name=Data.name
    path=Data.path
    name_folder=os.path.basename(path)
    en=os.path.dirname(os.path.abspath(__file__))

    dir=os.path.normpath(path  + os.sep + os.pardir)
    os.chdir(dir)

    zip_file = zipfile.ZipFile('{}.zip'.format(name),'w')

    for root, dirs, files in os.walk(name_folder):
        for file in files:
            zip_file.write(os.path.join(root,file), compress_type=zipfile.ZIP_DEFLATED)

    zip_file.close()

    pp = pprint.PrettyPrinter(indent=4)
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = r'{}\blackflame-e03e5e12ac0b.json'.format(en)
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    results = service.files().list(pageSize=10,
                                fields="nextPageToken, files(id, name, mimeType)").execute()

    pp.pprint(results)

    folder_id = '18k1-ReLCvjNrXnHG-lI8yrBLTCmn4gn1'
    name = '{}.zip'.format(name)
    file_path = '{}'.format(dir) + '\{}'.format(name)
    file_metadata = {
                        'name': name,
                        'mimeType': 'text/zip',
                        'parents': [folder_id]
                }
    media = MediaFileUpload(file_path, mimetype='text/zip', resumable=True)
    r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    mb.showinfo('Заархивировано','Архивация каталога прошла успешно.' + '\n' + 'Архив находится на пути: "{}"'.format(dir) + ', под названием "{}"'.format(name))
except:
    mb.showinfo('Ошибка','Возникла ошибка в процессе архивации каталога.')


