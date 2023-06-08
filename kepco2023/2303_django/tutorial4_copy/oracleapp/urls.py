from django.urls import path

from . import views

urlpatterns = [
    # url : http://127.0.0.1:8000/oracle/cart_list/
    path('cart_insert/',views.cartInsert),
    path('cart_insert_form/', views.cartInsertForm),
    path('cart_delete/',views.cartDelete),
    path('cart_update/',views.cartUpdate),
    path('cart_update_view/',views.cartUpdateView),
    path('cart_view/', views.cartView),
    path('cart_list/', views.cartList),
    
    
    path('mem_list/', views.memberList),
]
