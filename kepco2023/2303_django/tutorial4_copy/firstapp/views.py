from django.shortcuts import render

### 사용자 브라우저로 응답하는 라이브러리
from django.http import HttpResponse
# Create your views here.

### 9day #########################
### 1. 입력하기
def getLoginForm(request) :
    return render(request,
                  "firstapp/9day/login_form.html",
                  {})

### 2. 입력값 확인하기
def getLoginChk(request) :
    ### 사용자가 입력한 값들 추출하기
    ### get 방식 처리
    if request.method == "GET" :
        mem_id = request.GET["mem_id"]
        mem_pw = request.GET["mem_pw"]
    ### post 방식 처리
    elif request.method == "POST" :
        mem_id = request.POST["mem_id"]
        mem_pw = request.POST["mem_pw"]
        
    # return render(request,
    #               "firstapp/9day/login_ok.html",
    #               {"mem_id" : mem_id,
    #                "mem_pw" : mem_pw})
    context = {"mem_id" : mem_id,
                   "mem_pw" : mem_pw}
    
    ### 아이디 및 패스워드 정보 확인하기
    # - DB에서 확인
    id = "a001"
    pw = "pwa001"
    
    ### 전달받은 아이디와 패스워드가
    #   - id와 pw와 모두 같다면 
    #     ->> login_ok.html로 페이지 전환시키기
    #   - id와 pw 중에 하나라도 일치하지 않는다면..
    #     ->> 이전 페이지로 가서 아이디/패스워드 
    #         다시 입력하게 해야 합니다.
    
    # if (id == mem_id) and (pw == mem_pw) :    
    #     return render(request,
    #                 "firstapp/9day/login_ok.html",
    #                 context)
    # else :
    #     return HttpResponse("아이디/패스워드 불일치")
    if (id != mem_id) or (pw != mem_pw) :
        msg = """
            <script type='text/javascript'>
                alert('아이디 or 패스워드 확인하세요!');
                history.go(-1);
            </script>
        """
        # return HttpResponse("아이디/패스워드 불일치")
        return HttpResponse(msg)
    
    return render(request,
            "firstapp/9day/login_ok.html",
            context)
##################################


### index 시작페이지
def index(request) :
    return render(request,
                  "firstapp/index.html",
                  {})

def getCss_Js_Img(request) :
    return render(request,
                  "firstapp/07_css_js_img.html",
                  {})

### static - javascript
def getJavascript(request) :
    return render(request,
                  "firstapp/06_js.html",
                  {})

### static - css 불러들이기
def getCss(request) :
    return render(request,
                  "firstapp/05_css.html",
                  {})

### static - image 보여주기
def getImg(request) :
    return render(request,
                  "firstapp/04_img.html",
                  {})


def tableFor2(request) :
    ### render : html문서에 요청데이터 및 출력데이터를
    #            포함시켜서 사용자에게 리턴해주는 함수
    # - 세번째 값 : 딕셔너리 형태로만 지정가능
    lists = [{"id":"a001", "pw":"pwa001"},
                {"id":"b001", "pw":"pwb001"},
                {"id":"c001", "pw":"pwc001"}]
    context = {"lists" : lists}
    return render(request,
                  "firstapp/03_for.html",
                  context)

### 02_for.html 읽어 들이기
def tableFor(request) :
    ### render : html문서에 요청데이터 및 출력데이터를
    #            포함시켜서 사용자에게 리턴해주는 함수
    # - 세번째 값 : 딕셔너리 형태로만 지정가능
    content = {"id":"a0011", "pw":"pwa0011"}
    return render(request,
                  "firstapp/02_for.html",
                  content)

### Templates / 01_firstapp_start.html 불러들이기
def firstapp_start(request) :
    ### html을 render() 함수에게 전달
    # - render 함수는 html 내에 파이썬 프로그램을 
    #   컴파일해서 하나의 html로 변환해주는 역할 수행
    # - 동시에 HttpResponse()까지 수행합니다.
    return render(request,
                  "firstapp/01_firstapp_start.html",
                  {})

### home 텍스트가 출력되는 페이지함수 만들기
def home(request) :
    msg = "<h3>Home이 보이나?</h3>"
    return HttpResponse(msg)

### test 페이지 함수 생성하기
def test(request) :
    msg = """
            <h3>::: 웹프로그램 성공!! :::</h3>
            <table border='1'>
                <tr>
                    <th>아이디</th>
                    <th>패스워드</th>
                </tr>
                <tr>
                    <td>a001</td>
                    <td>pwa001</td>
                </tr>
            </table>
    """
    ### 브라우저로 전달하는 기능
    return HttpResponse(msg)