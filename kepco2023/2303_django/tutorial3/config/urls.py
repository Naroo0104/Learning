"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# include 라이브러리 불러들이기 (,include)
from django.urls import path, include
from firstapp import views as fViews
from secondapp import views as sViews


urlpatterns = [
    path('oracle/',include('oracleapp.urls')),
    # path('index1/', views.index1),
    # path('index2/', views.index2),
    # path('main/', views.main),    
    # path('test/', views.test),
    
    
    #firstapp의 urls.py 호출하기 위한 url 지정
    # http://127.0.0.1:8000/first/xxxx 모두 가버려라
    path('main2/', sViews.main2),
    path('second/', include('secondapp.urls')),
    path('first/', include('firstapp.urls')),
    path('admin/', admin.site.urls)
]

