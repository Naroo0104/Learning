from django.urls import path

from . import views

urlpatterns = [
    # url : http://127.0.0.1:8000/nonmodell/
    path('cart_list_page/',views.getCartListPaging),
    
    path('logout/',views.logout),
    path('login/',views.login),
    path('login_logout/',views.login_logout),
    
    path('logout_session/', views.logoutCheck), 
    path('login_session2/', views.loginCheck), 
    
    path('login_form2/', views.loginForm),
    path('login_session/',views.goLoginSession),
    path('login_form/',views.goLoginForm),
    
    path('mem_view/',views.getMemberView),
    path('cart_list/',views.getCartList),
    path('mem_list3/',views.getMemberList),
    path('mem_list/',views.getMemberList),
]
