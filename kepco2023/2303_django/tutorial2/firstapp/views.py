from django.shortcuts import render
#render: request 받은 걸 넘겨주어 
#        html에 프로그래밍(새롭게 구성, 데이터 있으면 넣어서)하는 역할
#        {{}} 돼 있는 건 
#        데이터 넘겨줄 때, 

# Create your views here.
from django.http import HttpResponse


   # render() : html문서에 요청 데이터 및 출력데이터를 포함시켜 사용자에게 return
    # 데이터는 오직 dict 형만
    #     ### html을 render() 함수에게 전달
    # - render 함수는 html 내에 파이썬 프로그램을
    # 컴파일해서 하나의 html로 변환해주는 역할 수행
    # -동시에 HttpResponse()까지 수행한다.
    

########################  9 day  #########################
###1.입력값 넣기
def getLoginForm(request):
    return render(request,
                  "firstapp/9day/login_form.html",
                  {})
    
    
###2.입력값 확인하기
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
                "firstapp/9day/login_ok.html",
                context)

##########################################################
    

# index 시작 페이지
def index(request):
    return render(request,
                  "firstapp/index.html",
                  {})

def getCss_Js_Img(request):
    return render(request,
                  "firstapp/07_css_js_img.html",
                  {})
    

# static - javascript 불러오기
def getJavasript(request):
    return render(request,
                  'firstapp/06_js.html',
                  {})


# static - css 불러오기
def getCss(request):
    return render(request,
                  "firstapp/05_css.html",
                  {})
    
    
# static - image 보여주기
def getImg(request):
    return render(request,
                  "firstapp/04_img.html",
                  {})


def tableFor2(request):
    col1={"id":"a01", "pw":"pw01"}
    col2={"id":"b02", "pw":"pw02"}
    col3={"id":"c03", "pw":"pw03"}

    cols=[col1, col2, col3]
    # context key값의 이름은 아무거나 상관없음, dict 형으로 넣어준다는 것만 기억
    context={"lists":cols}
    return render(request,
                  "firstapp/03_for.html",
                  context)
    
    
    
def tableFor(request):
 
    content = {"id":"a02","pw":"pw02"}
    return render(request,
                  "firstapp/02_for.html",
                  content)
    

# Teamplates / 01_firstapp_start.html 불러들이기
def firstapp_start(request) : 
    return render(request,
                  "firstapp/01_firstapp_start.html",
                  {})


def test(request):
    msg="""
            <h3>웹프로그램 성공~~!</h3>
            <table border='1'>
                <caption>성공하면 나타나는 표</caption>
                <tr>
                    <th>아이디</th>
                    <th>패스워드</th>
                </tr>
                <tr>
                    <td>a01</td>
                    <td>pw01</td>
                </tr>
            </table>
    """
    return HttpResponse(msg)


def index1(request):
	return HttpResponse('<u>Hello</u>')

def index2(request):
	return HttpResponse('<p>Hi</p>')

def main(request):
	return HttpResponse('<u>Main</u>')


def first(request):
    return 


def home(request):
    msg='<h3>Home</h3>'
    return HttpResponse(msg)