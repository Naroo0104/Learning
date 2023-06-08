from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 테이블
# import models
#- 이 경우: models.Cart 하면 됨
from .models import Cart, Member


# Cart 상세정보 조회하기(1건 조회)
def cartView(request):
    # request 데이터 받아오기
    if request.method =="POST":
        cart_no=request.POST["cart_no"]
        cart_prod=request.POST["cart_prod"]
    elif request.method == "GET":
        cart_no=request.GET["cart_no"]
        cart_prod=request.GET["cart_prod"]
        
        
    #한 건 조회하기(상세)
    # get(Cart.cart_no = 전달 받은 request 값)
    cart=Cart.objects.get(cart_no=cart_no, cart_prod=cart_prod)
    
    
    
    return render(request,
                  "oracleapp/cart/cart_view.html",
                  {'cart_no':cart_no, 'cart_prod':cart_prod, 'cart':cart})


# cart 테이블 전체 조회
def cartList(request):
    # 1. 모델을 통해 데이터 조회
    # 조회결과를 받아올 변수 정의 
    # objects: 객체, 여기서는 col을 뜻함
    # QUERY : SELECT * FROM CART
    # WHERE CART_NO=request.cart_no값
    # WHERE CART_PROD=request.cart_prod값
    cart_list=Cart.objects.all()
    
    # return HttpResponse('잘 보인다~')
    return render(request,
                  "oracleapp/cart/cart_list.html",
                  {'cart_list':cart_list})
    
    
# 회원 전체 목록 조회
def memberList(request):
    mem_list=Member.objects.all()
    return render(request,
                  "oracleapp/mem/mem_list.html",
                  {'mem_list':mem_list})