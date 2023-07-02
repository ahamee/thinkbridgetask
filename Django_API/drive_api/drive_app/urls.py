from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from . import views

app_name = "drive_app"

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^fifadata/$', views.fifa_data_View.as_view(), name='fifa_data'),
    re_path(r'^googledrive/$', views.list_fulldrive_content_View.as_view(), name='contents'),
    re_path(r'^googledrive/id/(?P<id>\w+)/$', views.list_specific_content_View.as_view(), name=''),
    re_path(r'^googledrive/download/$', views.list_download_content_View.as_view(), name=''),
]
