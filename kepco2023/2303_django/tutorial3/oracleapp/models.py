from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
# Create your models here.


# 클래스 이름: 보통 테이블명과 똑같이 씀(규칙), 변수도 컬럼명과 똑같이 설정
class Cart(models.Model):
    cart_no=CharField(primary_key=True, max_length=13, null=False)
    cart_prod=CharField(max_length=10, null=False)
    cart_member=CharField(max_length=15, null=False)
    cart_qty=IntegerField(max_length=8, null=False)
    
    # 내부 클래스
    class Meta:
    # 실제 사용할 테이블 이름
        db_table='cart'
        # app 이름(router.py에 설정한 앱 이름과 동일)
        app_label='oracleapp'
        # managed : db에 실제 테이블이 존재하는지 여부 파악
        # -존재하면 False
        # -DB 설계에 따라 만들어진 DB 사용하기에
        # -일반적으로 False를 지정
        managed=False