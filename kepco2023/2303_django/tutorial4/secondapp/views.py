from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

### main 함수 페이지
def main(request) :
    msg = "<h3>secondapp 잘 보입니다.</h3>"
    return HttpResponse(msg)

### main2 함수 페이지
# http://127.0.0.1:8000/main2/
def main2(request) :
    msg = "<h3>Main2 잘 보입니다.</h3>"
    return HttpResponse(msg)