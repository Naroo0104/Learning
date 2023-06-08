# include 라이브러리 불러들이기 (,include)
from django.urls import path
from . import views


urlpatterns = [
    # http://127.0.0.1:8000/oracle/cart_list
    path('cart_view/',views.cartView),
    path('mem_list/',views.memberList),
    path('cart_list/',views.cartList),
]

