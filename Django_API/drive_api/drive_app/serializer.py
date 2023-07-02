from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class ListContentsSerializer(ModelSerializer):
    class Meta:
        model = FifaData
        exclude = ('')
        
        
class ListFullDriveSerializer(serializers.Serializer):
   id = serializers.CharField()
   title = serializers.CharField()
   
   
class DownloadFileSerializer(serializers.Serializer):
   msg = serializers.CharField()
   