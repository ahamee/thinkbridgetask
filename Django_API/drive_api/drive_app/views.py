from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from .serializer import * 
import json
from django.http import HttpResponse, JsonResponse
from .gdrive_access import *
from rest_framework.response import Response
import pandas as pd
import sqlalchemy
from rest_framework.exceptions import NotFound
import pyodbc
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
import os

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type = 'text/json')

class fifa_data_View(ListAPIView):
    model = FifaData
    queryset = FifaData.objects.all()
    serializer_class = ListContentsSerializer
    
    def get_queryset(self):
        try:
            queryset_list = self.model.objects.all().filter(age=18)
            return queryset_list
        except Exception as e:
            msg = {
                "detail": "Invalid request --->" + str(e)
            }
            raise NotFound(msg)

class list_fulldrive_content_View(ListAPIView):
    serializer_class = ListFullDriveSerializer
    
    def get_queryset(self, *args, **kwargs):   
        try:     
            drive = Google_authentication('root')
            content_list = drive.authenticator()
            results = ListFullDriveSerializer(content_list, many=True).data
            return results
        except Exception as e:
            msg = {
                "detail": "Invalid request --->" + str(e)
            }
            raise NotFound(msg)
    
class list_specific_content_View(ListAPIView):
    serializer_class = ListFullDriveSerializer
    
    def get_queryset(self, *args, **kwargs):
        try:
            drive = Google_authentication(self.kwargs['id'])
            content_list = drive.authenticator()
            results = ListFullDriveSerializer(content_list, many=True).data
            return results
        except Exception as e:
            msg = {
                "detail": "Invalid request --->" + str(e)
            }
            raise NotFound(msg)
    
class list_download_content_View(ListAPIView):
    serializer_class = DownloadFileSerializer
    query_parameters = ['id', 'table_name']
    
    def get(self, *args, **kwargs):
        for key in self.request.query_params.keys():
            if key in self.query_parameters:
                pass
            else:
                msg = {
                    "detail": "Invalid request. "
                }
                raise NotFound(msg)
        try:
            if (self.request.GET.get('id') != None)  & (self.request.GET.get('table_name') != None):
                drive = Google_authentication(self.request.GET.get('id'))
                filedownloaded = drive.drive.CreateFile({'id':self.request.GET.get('id')})
                filedownloaded.GetContentFile('example.csv')
                df = pd.read_csv('example.csv')
                url = "mssql+pyodbc://"+os.getenv('user')+":"+os.getenv('password')+"@"+os.getenv('host')+":"+os.getenv('port')+"/"+os.getenv('db_name')+"?driver=ODBC+Driver+17+for+SQL+Server"
                engine = sqlalchemy.create_engine(url)
                df.to_sql(name=self.request.GET.get('table_name'), con=engine, if_exists='replace')
                msg = {'detail':"successfully downloaded file"}        
                return Response(msg)
            else:
                msg = {
                "detail": "Please provide query parameters id and table_name"
            }
            raise NotFound(msg)
        except Exception as e:
            msg = {
                "detail": "Invalid request --->" + str(e)
            }
            raise NotFound(msg)