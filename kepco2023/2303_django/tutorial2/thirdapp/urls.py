from django.urls import path
from . import views

urlpatterns = [
   #firstapp의 urls.py 호출하기 위한 url 지정
    # http://127.0.0.1:8000/first/test
    path('tablefor2/',views.tableFor2)
]
