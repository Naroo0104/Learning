from django.shortcuts import render
from django.http import HttpResponse 
from .models import Cart, Member, Prod

# Create your views here.





# 예제. 회원정보 통해 회원 주문정보 확인
def getMemberList2(request):
    # return HttpResponse("hello")
    
    member_list = Member.objects.all()
    
    return render(request,
                "modelapp/memcart/mem_list.html",
                {"member_list":member_list})  
    
    
    
    

def getMemberCartView(request):
    # return HttpResponse("hi")
    if request.method == "POST" :
        mem_id = request.POST["mem_id"]
        
                
    elif request.method == "GET" :        
        mem_id = request.GET["mem_id"]
        
    member=Member.objects.get(mem_id=mem_id)
    cart = Cart.objects.select_related().filter(member=mem_id)
    
    return render(request,
                "modelapp/memcart/cart_list.html",
                {"cart":cart})   
    
    
    
    


# 회원정보와 장바구니(주문)정보 모두 조회
def getMemberCartJoin(request):
    # select_related():cart 테이블의 FK 정보까지 모두 갖고 오기
    """
    
    -select_related(): 정참조 방식, 자식->부모 순으로 처리
                        n:1의 관계(다대일)
    -prefetch_related(): 역참조 방식, 부모->자식 순으로 처리
                        1:n의 관계(일대다)
                        
    """
    
    cart=Cart.objects.select_related().filter(member__mem_id="a001").order_by("cart_no", "-cart_qty","member__mem_name")
    cart_query=cart.query   
     
    # return HttpResponse(cart_query)
    return render(request, 
                  "modelapp/mem_cart_list.html",
                  {"cart":cart, "cart_query":cart_query})




def getMemberList(request):
    member_list = Member.objects.all()
    # member = Member.objects.all()
    
    return render(request,
                "modelapp/mem_list.html",
                {"member_list":member_list})        
    

