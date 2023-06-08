from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import pickle
import numpy as np


    
#render(request, templates_name, response)
##HttpResponse(html_str)
##HttpResponseRedirect(htmlurl)
##외부링크 'https://naver.com'
##내부링크 '/app/index/'
##절대링크 localhost:8000/app/1/ 
##상대링크 ../../index

# Create your views here.

def index(request):
    if request.GET.get('name') == None:
        contents={'name': None, 'age': None}
    else:
        name=request.GET.get('name')
        age=request.GET.get('age')
        age=int(age)
        if age>50:
            age='노중년'
        elif age>40:
            age='중장년'
        elif age>=20:
            age='청년'
        else:
            age='미성년자'
            
        contents={'name': name, 'age': age}
    return render(request, 'app/index.html', contents)

# def index(request):
#     request.GET.get('abc')
#     # request.GET['abc']
#     contents={
#         'name':'snoopy',
#         'age':100
#     }
#     return render(request, 'app/index.html', contents)
    ## contents=object(서버에서 보내주는 값, dictionary 형태)
    ## dictionary가 중요한 이유: key를 갖고 value를 꺼내기 때문(편해서)

def index2(request):
    html_str="""
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    
    <h1 style='font-size:3em'>{{name}}</h1>
    <h2 style='font-size:10px'>{{age}}</h2>
    <hr/>
    """
    return render(request, 'app/index2.html')
    
