from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 페이징 처리를 위한 라이브러리 불러들이기
from django.core.paginator import Paginator

import nonmodelapp.model_db.member.member as mem
import nonmodelapp.model_db.member.member2 as mem2
import nonmodelapp.model_db.member.member3 as mem3
import nonmodelapp.model_db.member.member3_copy as mem3_c
import nonmodelapp.model_db.cart.cart as cart



# 장바구니(주문) 정보 조회: 페이징 처리 추가
def getCartListPaging(request):
    # 현재 선택된 페이지 데이터 받아오기
    # -최초에는 GET방식으로 넘어오는 데이터가 없다.
    # =>데이터가 없으면 1로 초기화
    now_page=request.GET.get("page","1")
    
    try:
        # request로 넘어오는 모든 데이터==>문자열 데이터
        # 그치만 페이지 번호는 숫자형태를 사용해야 함(형변환 시켜야)
        now_page=request.GET.get("page","1")
        now_page=int(now_page)
    except:
        now_page=1
        
        
    # data 조회
    cart_list=cart.getCartList()
    
    
    #################################
    # 페이징 처리:페이지 번호 범위 계산
    # 1~10,...
    
    
    # 한 화면에 10개씩 보여주기
    num_row=10
    
    # 페이징 처리 라이브러리에
    # -DB에서 조회한 데이터 전체와 
    # -한 페이지에 보여줄 행의 개수를 넘긴다.
    p=Paginator(cart_list, num_row)
    
    # 현재 선택된 페이지 번호(now_page)에 해당하는 
    # -10개의 행을 추출하기
    
    row_data=p.get_page(now_page)
    
    # 게시물 하단에 표시할 시작 페이지 번호 계산
    start_page=(now_page-1)//num_row*num_row+1
    
    # 게시물 하단에 표시할 마지막 페이지번호 계산하기
    end_page=start_page+9
    
    # 마지막 페이지 번호 처리
    # p.num_pages: Pagenator가 관리하는 전체 페이지 번호
    if end_page>p.num_pages:
        end_page=p.num_pages
        
        
    #################################
    # 페이징 처리:다음/이전 버튼 처리
    
    #이전버튼: is_prev, 다음버튼: is_next 
    # 어떤 버튼 보여줄지 여부를 저장할 boolean 변수
    is_prev=False
    is_next=False
    
    # if 시작 페이지 번호(start_page) > 1
    # 이전 버튼 보이게 하기 위해 True 값으로 변경
    if start_page>1:
        is_prev=True
        
    # if 종료 페이지 번호(end_page)< 전체 페이지 번호
    # -다음 버튼 보이게하기 위해 True 값으로 변경
    if end_page<p.num_pages:
        is_next=True
    
    context={
        "row_data":row_data, 
        "is_prev":is_prev,
        "is_next":is_next,
        "start_page":start_page,
        "end_page":end_page,
        "page_range":range(start_page, end_page+1)
    }
    
    
    return render(request,
                  "nonmodelapp/cart/cart_list_page.html",
                  context)



##############################################################
############[로그인/로그아웃]하나의 HTML로 통합 처리############
##############################################################
def login_logout(request):
    return render(request, 
                  "nonmodelapp/login_copy/login_logout.html/",
                  {})
    

def login(request):
    #세션 있으면 
    if request.session.get("ses_mem_id"):
        return render(request, 
                  "nonmodelapp/login_copy/login_logout.html/",
                  {})
        
    
    try:
        if request.method == "POST" :
            mem_id = request.POST["mem_id"]
            mem_pass = request.POST["mem_pass"]
                    
        elif request.method == "GET" :        
            mem_id = request.GET["mem_id"]
            mem_pass = request.GET["mem_pass"]
    except:
        msg="""
            <script type='text/javascript'>
                alert('잘못된 접근입니다. 다시 입력!');
                location.href='/nonmodel/login_logout/';
            </script>
        """
        return HttpResponse(msg)
        
        
    ## DB
    dict_col = mem3_c.getLogin(mem_id, mem_pass)
    
    ### 성공여부
    if dict_col["rs"] == "no" :
        msg="""
            <script type='text/javascript'>
                alert('아이디 또는 비밀번호가 일치하지 않습니다. 다시 입력!');
                history.go(-1);
            </script>
        """
        return HttpResponse(msg)
        
    #로그인 성공(아이디/비밀번호 정보가 있는 경우)
    #세션 객체(세션 딕셔너리)에 로그인 회원 정보를 저장시킴
    #-세션: 서버영역에 특정 값을 저장시켜 놓고 
    #     : 어느 페이지에서든지 사용할 수 있는 값을 의미
    #     : 저장 변수-session, 타입-{}
    #     : session 변수는 서버가 실행되면서 자동으로 만들어 놓는 변수
    #     : request : session 변수를 가지고 있는 객체 -> 
    #     : =>(저장방법) request.session[key] =value
    #     : (py)(조회방법) request.session.get[key](get 안 하면 error 뜨니까)
    #     : (html)(조회방법) request.session.key
    
    
    # 세션 처리하기(key : value 값 넣기)
    # -세션 처리할 key는 각자 정한다. ex.ses_mem_id
    # -세션에 저장된 key값은 브라우저를 닫지 않으면
    # -다른 HTML에서 조회가능
    request.session["ses_mem_id"]=mem_id
    request.session["ses_mem_pass"]=mem_pass
    request.session["ses_mem_name"]=dict_col["mem_name"]
    
        
    return render(request,
                  "nonmodelapp/login_copy/login_logout.html",
                  dict_col)
    
def logout(request):
    if request.session.get("ses_mem_id"):
        # 세션 정보 삭제(flush: 깨끗이 비워라)
        request.session.flush()
    
        msg="""
                <script type='text/javascript'>
                    alert('로그아웃 되었습니다.');
                    location.href='c';
                </script>
            """
    
    else:
        msg="""
            <script type='text/javascript'>
                alert('잘못된 접근입니다. 다시 입력!');
                location.href='/nonmodel/login_logout/';
            </script>
        """
        
    return HttpResponse(msg)  



#쌤=>login_copy
def loginForm(request) :
    return render(request,
                  "nonmodelapp/login_copy/login_form.html",
                  {})

def loginCheck(request) :
    try:
        if request.method == "POST" :
            mem_id = request.POST["mem_id"]
            mem_pass = request.POST["mem_pass"]
                    
        elif request.method == "GET" :        
            mem_id = request.GET["mem_id"]
            mem_pass = request.GET["mem_pass"]
    except:
        msg="""
            <script type='text/javascript'>
                alert('잘못된 접근입니다. 다시 입력!');
                location.href='/nonmodel/login_form2/';
            </script>
        """
        return HttpResponse(msg)
        
        
    ## DB
    dict_col = mem3_c.getLogin(mem_id, mem_pass)
    
    ### 성공여부
    if dict_col["rs"] == "no" :
        msg="""
            <script type='text/javascript'>
                alert('아이디 또는 비밀번호가 일치하지 않습니다. 다시 입력!');
                history.go(-1);
            </script>
        """
        return HttpResponse(msg)
        
    #로그인 성공(아이디/비밀번호 정보가 있는 경우)
    #세션 객체(세션 딕셔너리)에 로그인 회원 정보를 저장시킴
    #-세션: 서버영역에 특정 값을 저장시켜 놓고 
    #     : 어느 페이지에서든지 사용할 수 있는 값을 의미
    #     : 저장 변수-session, 타입-{}
    #     : session 변수는 서버가 실행되면서 자동으로 만들어 놓는 변수
    #     : request : session 변수를 가지고 있는 객체 -> 
    #     : =>(저장방법) request.session[key] =value
    #     : (py)(조회방법) request.session.get[key](get 안 하면 error 뜨니까)
    #     : (html)(조회방법) request.session.key
    
    
    # 세션 처리하기(key : value 값 넣기)
    # -세션 처리할 key는 각자 정한다. ex.ses_mem_id
    # -세션에 저장된 key값은 브라우저를 닫지 않으면
    # -다른 HTML에서 조회가능
    request.session["ses_mem_id"]=mem_id
    request.session["ses_mem_pass"]=mem_pass
    request.session["ses_mem_name"]=dict_col["mem_name"]
    
        
    return render(request,
                  "nonmodelapp/login_copy/login_session.html",
                  dict_col)
        
        
# 로그아웃 처리
def logoutCheck(request):
    if request.session.get("ses_mem_id"):
        # 세션 정보 삭제(flush: 깨끗이 비워라)
        request.session.flush()
    
        msg="""
                <script type='text/javascript'>
                    alert('로그아웃 되었습니다.');
                    location.href='/nonmodel/login_form2/';
                </script>
            """
    
    else:
        msg="""
            <script type='text/javascript'>
                alert('잘못된 접근입니다. 다시 입력!');
                location.href='/nonmodel/login_form2/';
            </script>
        """
        
    return HttpResponse(msg)        
        

        
        
#me!        
def goLoginSession(request):
    if request.method == "GET" :        
        mem_id = request.GET["mem_id"]
        mem_pass = request.GET["mem_pass"]
        
    elif request.method == "POST" :        
        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
        
    login_data=mem3.getMember(mem_id, mem_pass)
    
    
    if login_data:
        return render(request,
                  "nonmodelapp/login/login_session.html",
                  {"mem_id":mem_id, "mem_pass":mem_pass})
    else: 
        return render(request,
                  "nonmodelapp/login/login_session_fail.html",
                  {})
    




def goLoginForm(request):
    # return HttpResponse("login~")
    return render(request,
                  "nonmodelapp/login/login_form.html",
                  {})


def getMemberView(request):
    if request.method == "GET" :        
        mem_id = request.GET["mem_id"]
    
    
    dict_data=mem2.getMember(mem_id)
    # return HttpResponse(dict_data)
    # dict_data=mem2.getMember()
    
    return render(request,
                  "nonmodelapp/member/mem_view.html",
                  {"dict_data":dict_data})




def getCartList(request):
    cart_list=cart.getCartList()
    # return HttpResponse(cart_list)
    
    return render(request,
                  "nonmodelapp/cart/cart_list.html",
                  {"cart_list":cart_list})



def getMemberList(request):
    mem_list=mem3.getMemberList()
    # return HttpResponse(mem_list)
    
    return render(request,
                  "nonmodelapp/member/mem_list3.html",
                  {"mem_list":mem_list})

# def getMemberList(request):
#     return HttpResponse("gogo")
    
    

    