from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 테이블
# import models
#- 이 경우: models.Cart 하면 됨
from .models import Cart


# cart 테이블 전체 조회
def cartList(request):
    # 1. 모델을 통해 데이터 조회
    # 조회결과를 받아올 변수 정의 
    # objects: 객체, 여기서는 col을 뜻함
    cart_list=Cart.objects.all()
    return HttpResponse('잘 보인다~')
    # return render(request,
    #               "oracleapp/cart/cart_list.html",
    #               {'cart_list':cart_list})