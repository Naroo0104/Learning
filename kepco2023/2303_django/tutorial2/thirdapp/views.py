from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def tableFor2(request):
    col1={"id":"a01", "pw":"pw01"}
    col2={"id":"b02", "pw":"pw02"}
    col3={"id":"c03", "pw":"pw03"}
	
    cols=[col1, col2, col3]
    
    context={"lists":cols}
    
    return render(request,
                  "thirdapp/03_for.html",
                  context)
    