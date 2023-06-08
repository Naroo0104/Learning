from django.urls import path
from .views import index
# from django.http import HttpResponseRedirect


urlpatterns = [
    path('index/', index),
]
