from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
# Create your models here.

class Cart(models.Model) :
    cart_no = CharField(primary_key=True,
                        max_length=13, 
                        null = False)
    cart_prod = CharField(max_length=10, 
                            null = False) 
    cart_member = CharField(max_length=15, 
                            null = False) 
    cart_qty = IntegerField(max_length=8, 
                            null = False) 
    
    class Meta :
        # 실제 사용할 테이블 이름
        db_table = "cart"
        
        # app 이름(router.py에 설정한 앱 이름과 동일)
        app_label = "oracleapp"
        
        # 데이터베이스에 실제 테이블이 존재하는지 여부
        # - 존재하면 False, 존재하지 않으면 True
        # - DB설계에 따라 만들어진 DB를 사용하기에
        #   일반적으로 False를 지정
        managed = False
        
        
### 회원정보 클래스 생성
class Member(models.Model) :
    mem_id = CharField(primary_key=True, 
                       max_length=15, null=False)
    mem_pass = CharField(max_length=15, null=False)
    mem_name = CharField(max_length=20, null=False)
    
    class Meta :
        # 실제 사용할 테이블 이름
        db_table = "member"
        
        # app 이름(router.py에 설정한 앱 이름과 동일)
        app_label = "oracleapp"
        
        # 데이터베이스에 실제 테이블이 존재하는지 여부
        # - 존재하면 False, 존재하지 않으면 True
        # - DB설계에 따라 만들어진 DB를 사용하기에
        #   일반적으로 False를 지정
        managed = False