from django.urls import path

from . import views

urlpatterns = [
    # url : http://127.0.0.1:8000/first/login_form/
    path('login_chk/', views.getLoginChk),
    path('login_form/', views.getLoginForm),
    
    path('css_js_img/', views.getCss_Js_Img),
    path('js/', views.getJavascript),
    path('css/', views.getCss),
    path('img/', views.getImg),
    path('tablefor2/', views.tableFor2),
    path('tablefor/', views.tableFor),
    path('start/', views.firstapp_start),
    path('home/', views.home),
    path('test/', views.test),    
]
