from django.db import models

# 컬럼 타입 라이브러리 정의
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
from django.db.models.fields import DateTimeField
# Create your models here.

# 예제용 prod 테이블 클래스 생성
class Prod(models.Model):
    prod_id=CharField(primary_key=True, max_length=10, null=False)
    prod_name=CharField(max_length=40, null=False)
    prod_lgu=CharField(max_length=4, null=False)
    prod_buyer=CharField(max_length=6, null=False)
    prod_cost=IntegerField(max_length=10, null=False)
    prod_price=IntegerField(max_length=10, null=False)
    prod_sale=IntegerField(max_length=10, null=False)
    prod_outline=CharField(max_length=100, null=False)
    prod_detail=CharField(max_length=3000)
    prod_img=CharField(max_length=40, null=False)
    prod_totalstock=IntegerField(max_length=10, null=False)
    prod_insdate=DateTimeField()
    prod_properstock=IntegerField(max_length=10, null=False)
    prod_size=CharField(max_length=20)
    prod_color=CharField(max_length=20)
    prod_delivery=CharField(max_length=255)
    prod_unit=CharField(max_length=6)
    prod_qtyin=IntegerField(max_length=10)
    prod_qtysale=IntegerField(max_length=10)
    prod_mileage=IntegerField(max_length=10)
       
    
    class Meta : 
        db_table = "prod"            
        app_label = "modelapp"
        managed = False
        

#회원정보 테이블 클래스 생성
class Member(models.Model):
    #컬럼 정의
    mem_id=CharField(primary_key=True, max_length=15, null=False)
    mem_pass=CharField(max_length=15, null=False)
    mem_name=CharField(max_length=20, null=False)
    mem_regno1=CharField(max_length=6, null=False)
    mem_regno2=CharField(max_length=7, null=False)
    mem_bir=DateTimeField()
    mem_zip=CharField(max_length=7, null=False)
    mem_add1=CharField(max_length=100, null=False)
    mem_add2=CharField(max_length=80, null=False)
    mem_hometel=CharField(max_length=14, null=False)
    mem_comtel=CharField(max_length=14, null=False)
    mem_hp=CharField(max_length=15)
    mem_mail=CharField(max_length=40, null=False)
    mem_job=CharField(max_length=40)
    mem_like=CharField(max_length=40)
    mem_memorial=CharField(max_length=40)
    mem_memorialday=DateTimeField()
    mem_mileage=IntegerField(max_length=10)
    mem_delete=CharField(max_length=1)
    
    #메타 정보 정의
    class Meta : 
        db_table = "member"            
        app_label = "modelapp"
        managed = False



#장바구니(주문) 테이블 클래스 생성
class Cart(models.Model):
    #컬럼 정의
    cart_no=CharField(primary_key=True, max_length=13, null=False)
    # cart_prod=CharField(max_length=10, null=False)
    cart_qty=IntegerField(max_length=8, null=False)
    
    #member 테이블과 연결(FK)
    # cart_mem=CharField(max_length=15, null=False)
    
    # to_field : 부모 테이블의 PK 컬럼(참조될 컬럼명)
    # db_column : 자식 테이블의 FK 컬럼(참조할 컬럼명)
    # on_delete : 부모 데이터가 삭제될 때 참조되는 자식 테이블
    # PROTECT : 자식 삭제 시, 부모는 냅둬라(삭제하지 마라)-->오류 발생시키도록 처리됨
    # CASCADE : 부모가 삭제되면, 관련된 자식(모든 참조 데이터)도 다 삭제(위험해서 PROTECT 씀)
    member=models.ForeignKey(Member, 
                             to_field='mem_id', 
                             db_column='cart_member',
                             on_delete=models.PROTECT)
    # member_id라고 해도 됨
    # cart_prod=CharField(max_length=10,null=False)
    prod=models.ForeignKey(Prod, 
                           to_field="prod_id",
                           db_column="cart_prod",
                           on_delete=models.PROTECT)
    
    #메타 정보 정의
    class Meta : 
        db_table = "cart"            
        app_label = "modelapp"
        managed = False