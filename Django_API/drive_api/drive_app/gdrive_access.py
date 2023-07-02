from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

class Google_authentication:

    def __init__(self, folder_id):
        self.folder_id = folder_id
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

        
    def authenticator(self):
        file_list = self.drive.ListFile({'q': "'"+self.folder_id+"' in parents"}).GetList()
        # test_dict = {'id': [file1['id'] for file1 in file_list],
        #      'title': [file1['title'] for file1 in file_list]}
        list_details = [{'id':file1['id'], 
                         'title':file1['title']} for file1 in file_list]
        return list_details