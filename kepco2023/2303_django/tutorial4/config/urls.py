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

### include 라이브러리 불러들이기
from django.urls import path, include

### firstapp 폴더의 views.py 파일을 불러들이기
from firstapp import views as fViews
from secondapp import views as sViews
from modelapp import views
from nonmodelapp import views


urlpatterns = [
    ### index 시작페이지
    path('index.html', fViews.index),
    path('index', fViews.index),
    path('', fViews.index),
    
    path('main2/', sViews.main2),
    path('home/', fViews.home),
    
    path('nonmodel/',include('nonmodelapp.urls')),
    path('model/',include('modelapp.urls')),
    path('oracle/', include('oracleapp.urls')),
    path('second/', include('secondapp.urls')),
    path('first/', include('firstapp.urls')),
    
    path('admin/', admin.site.urls),
]
