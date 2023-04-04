from django.db import models
from django.utils import timezone  #시간정보에 관한 모듈


# Create your models here.

class Shopping(models.Model):
    orderdate = models.DateTimeField(default = timezone.now)
    item_name = models.CharField(max_length= 200)
    item_count = models.IntegerField(null=True, blank=True, default = 0)
    
class Item(models.Model):
    quantity = models.IntegerField(default=0)
    item_code = models.IntegerField()
    