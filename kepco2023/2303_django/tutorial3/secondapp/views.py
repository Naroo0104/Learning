from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

    
def secondapp_start(request) : 
    return render(request,
                  "secondapp/01_secondapp_start.html",
                  {})    

def main(request):
    msg='<u>Main</u>'
    return HttpResponse(msg)


def main2(request):
    msg='<u>Main2</u>'
    return HttpResponse(msg)