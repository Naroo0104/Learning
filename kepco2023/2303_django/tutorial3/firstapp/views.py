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


def tableFor2(request):
    col1={"id":"a01", "pw":"pw01"}
    col2={"id":"b02", "pw":"pw02"}
    col3={"id":"c03", "pw":"pw03"}

    cols=[col1, col2, col3]
    # context key값의 이름은 아무거나 상관없음, dict 형으로 넣어준다는 것만 기억
    context={"list":cols}
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