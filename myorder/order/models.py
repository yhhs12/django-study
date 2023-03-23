from django.db import models
from django.utils import timezone
# Create your models here.

class Order(models.Model):
    #번호는 pk설정 안하면 장고가 자동으로 id 부여해줌
    ### 필드와 필드 사이에 컴마 금지 ###
    
    #주문일시
    order_date = models.DateTimeField(default = timezone.now)
    #주문내역 
    order_text = models.TextField(null = False, blank = False)
    #금액  
    price = models.IntegerField()
    #주소
    address = models.CharField(max_length= 100) 
    





