#-*- utf-8 -*-
from django.urls import path, re_path
from . import views
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "files"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

urlpatterns = [
    re_path('createAliasStudentMessage/$',views.createAliasStudentMessage,name='createAliasStudentMessage'),
    re_path('createStudent/$',views.createStudent,name='createStudent'),
    re_path('createTeacher/$',views.createTeacher,name='createTeacher'),
]
app_name='app_sayhi'
