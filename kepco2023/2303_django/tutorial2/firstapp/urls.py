from django.urls import path
from . import views

urlpatterns = [
   #firstapp의 urls.py 호출하기 위한 url 지정
    # http://127.0.0.1:8000/first/test
    path('login_chk/',views.getLoginChk),
    path('login_form/',views.getLoginForm),
    path('css_js_img/', views.getCss_Js_Img),
    path('js/',views.getJavasript),
    path('css/',views.getCss),
    path('img/', views.getImg),
    path('tablefor2/', views.tableFor2),
    path('tablefor/', views.tableFor),
    path('start/',views.firstapp_start),
    path('home/', views.home),
    path('test/', views.test)
]
