from django.urls import path

from . import views

urlpatterns = [
    # url : http://127.0.0.1:8000/oracle/cart_list/
    path('mem_cart_view/',views.getMemberCartView),
    path('mem_list2/',views.getMemberList2),
    
    path('mem_list/',views.getMemberList),
    path('mem_cart_join/',views.getMemberCartJoin),
    # path('cart_insert/',views.cartInsert),
]
