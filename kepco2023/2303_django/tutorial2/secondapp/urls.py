from django.urls import path
from . import views

urlpatterns = [
   #firstapp의 urls.py 호출하기 위한 url 지정
    # http://127.0.0.1:8000/first/test
    path('login_chk/',views.getLoginChk),
    path('login_form/',views.getLoginForm),
    path('index/',views.index),
    path('tablefor2/',views.tableFor2),
    path('start/',views.secondapp_start),
    path('main/',views.main)
]
