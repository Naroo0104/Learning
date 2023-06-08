from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cart, Member





# 장바구니 담기(글 쓰기) 저장 처리하기
def cartInsert(request):   
    # 전송된 값 받아오기
    if request.method == "POST" :
        cart_no = request.POST["cart_no"]
        cart_prod = request.POST["cart_prod"]
        cart_mem = request.POST["cart_mem"]
        cart_qty = request.POST["cart_qty"]
                
    elif request.method == "GET" :        
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
        cart_mem = request.GET["cart_mem"]
        cart_qty = request.GET["cart_qty"]
        
        
    # DB에 저장시키기
        Cart.objects.create(cart_no=cart_no, cart_prod=cart_prod,
                            cart_mem=cart_mem, cart_qty=cart_qty)    
    
    # 저장 잘 됐다는 창 띄우고, 
    # -리스트 페이지로 가기
    msg="""
        <script type='text/javascript'>
            alert('정상적으로 저장됐다!');
            location.href='/oracle/cart_list/';
        </script>
    """
      
    
    return HttpResponse(msg) 




#장바구니 담기(글쓰기 폼) 화면처리
def cartInsertForm(request):        
    return render(request,
                  "oracleapp/cart/cart_insert_form.html",
                  {})


#cart 테이블 data 삭제하기
def cartDelete(request):
    if request.method == "POST" :
        cart_no = request.POST["cart_no"]
        cart_prod = request.POST["cart_prod"]
                
    elif request.method == "GET" :        
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
        
    
        
    # DB에서 삭제하기
    """
        DELETE FROM CART
        --아래 where 절은 filter() 부분
        WHERE CART_NO=cart_no값
        AND CART_PROD=cart_prod 값
    """
    Cart.objects.filter(cart_no=cart_no, 
                        cart_prod=cart_prod).delete()    
    
        
    msg="""
        <script type='text/javascript'>
            alert('정상적으로 삭제됐다!');
            location.href='/oracle/cart_list/';
        </script>
    """
      
    
    return HttpResponse(msg) 




### cart 테이블 전체 조회하기
def cartList(request) :
    ### 1. 모델을 통해 데이터 조회하기
    # 조회결과를 받아올 변수 정의
    # Select * From cart
    cart_list = Cart.objects.all()
    
    ## return HttpResponse("잘 보입니다!~")
    return render(request,
                  "oracleapp/cart/cart_list.html", 
                  {'cart_list' : cart_list})
   
   
   
    
### Cart 상세정보 조회하기(1건조회)
def cartView(request) :   
    ### request 데이터 받아오기
    if request.method == "POST" :
        cart_no = request.POST["cart_no"]
        cart_prod = request.POST["cart_prod"]
                
    elif request.method == "GET" :        
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
    
    ### 한건 조회하기(상세)
    # - get(Cart.cart_no = 전달받은request값)
    # Select * From cart
    # Where cart_no = request.cart_no값
    #   And cart_prod = request.cart_prod값
    cart = Cart.objects.get(cart_no = cart_no,
                            cart_prod = cart_prod)
    
    return render(request,
                  "oracleapp/cart/cart_view.html",
                  {"cart_no" : cart_no, 
                   "cart_prod" : cart_prod,
                   "cart" : cart})
        
        
        
        
        
# 장바구니 수정 페이지 보여주기
def cartUpdateView(request):
    if request.method == "POST" :
        cart_no = request.POST["cart_no"]
        cart_prod = request.POST["cart_prod"]
                
    elif request.method == "GET" :        
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
    
    
    cart = Cart.objects.get(cart_no = cart_no,
                            cart_prod = cart_prod)
    
    return render(request,
                    "oracleapp/cart/cart_update_view.html",
                    {"cart_no" : cart_no, 
                   "cart_prod" : cart_prod,
                   "cart":cart})    
    
    
    
    
#장바구니 수정
def cartUpdate(request):
    # cart_update_view.html에서
    # - 전송한 name=value 받아오기
    if request.method == "POST" :
        cart_no = request.POST["cart_no"]
        cart_prod = request.POST["cart_prod"]
        cart_qty = request.POST["cart_qty"]
                
    elif request.method == "GET" :        
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
        cart_qty = request.GET["cart_qty"]
        
    # 수정 데이터 DB에 전달해 수정
    """
    UPDATE CART
    SET CART_QTY=cart_gty값
    --아래 where 절이 filter() 부분
    WHERE CART_NO=cart_no값
    AND CART_PROD=cart_prod값
    """
        
    Cart.objects.filter(cart_no=cart_no, cart_prod=cart_prod).update(cart_qty=cart_qty)    
    
        
    # msg="""
    #     주문번호: {}<br/>
    #     상품코드: {}<br/>
    #     주문수량: {}
    # """.format(cart_no, cart_prod, cart_qty)
    
    # url 만들기
    # /?은 get 방식
    url="/oracle/cart_view/?"
    url=url+"cart_no="+cart_no+"&"
    url=url+"cart_prod="+cart_prod
    msg="""
        <script type='text/javascript'>
            alert('정상적으로 수정됐다!');
            location.href='{}';
        </script>
    """.format(url)
    
    return HttpResponse(msg)
        
    # 쌍따옴표 안에는 쌍따옴표 절대 넣지 말기! 작은 따옴표를 넣어야한다.
    
    
    
    
### 회원 전체 목록 조회하기
def memberList(request) :
    ### 리스트 변수 : mem_list
    ### URL : mem_list
    ### html 위치 : member/mem_list.html
    
    ### 1. 모델을 통해 데이터 조회하기
    # 조회결과를 받아올 변수 정의
    mem_list = Member.objects.all()
    
    ## return HttpResponse("잘 보입니다!~")
    return render(request,
                  "oracleapp/member/mem_list.html", 
                  {'mem_list' : mem_list})