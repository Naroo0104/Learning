from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def getLoginChk(request):
# >get 방식 처리<
# get방식으로 정보를 받으면 .method=="GET"<대문자
# GET 자체가 변수, 받아온 정보니까 항상 dict 형
    if request.method=="GET":
        mem_id=request.GET["mem_id"]
        mem_pw=request.GET["mem_pw"]

    # >post 방식 처리<
    elif request.method=="POST":
        mem_id=request.POST["mem_id"]
        mem_pw=request.POST["mem_pw"]

    # return render(request,
    #               "firstapp/9day/login_ok.html",
    #               {"mem_id":mem_id, 
    #                "mem_pw":mem_pw})

    context={"mem_id":mem_id, 
            "mem_pw":mem_pw}


    # 아이디 및 패스워드 정보 확인
    # -DB에서 확인
    id='hi01'
    pw='wow01'

    # 전달받은 id와 pw
    # - id, pw와 모두 같다면
    #  => login_ok.html로 페이지 전환
    # - id, pw 중 하나라도 일치하지 않는다면...
    #  => 이전 페이지로 이동해서 재입력

    # if (id==mem_id) and (pw==mem_pw) :      
    #     return render(request,
    #                 "firstapp/9day/login_ok.html",
    #                 context)
    # else:
    #     return HttpResponse("아이디/패스워드 불일치")
    if (id!=mem_id) or (pw !=mem_pw):
        msg=""" 
            <script type='text/javascript'>
                alert('아이디/패스워드 확인');
                history.go(-1);
            </script>
        """
        return  HttpResponse(msg)
        
    return render(request,
                "secondapp/9day/login_chk.html",
                context)

def getLoginForm(request):
    return render(request,
                  "secondapp/9day/login_form.html",
                  {})

def index(request):
    return render(request,
                  "secondapp/index.html",
                  {})


def tableFor2(request):
    col1={"id":"a01", "pw":"pw01"}
    col2={"id":"b02", "pw":"pw02"}
    col3={"id":"c03", "pw":"pw03"}

    cols=[col1, col2, col3]
    context={"lists":cols}
    return render(request,
                  "secondapp/03_for.html",
                  context)

    
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