from django.db import models
from django.utils import timezone  #시간정보에 관한 모듈


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length= 200)
    item_count = models.IntegerField(default = 1)

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    orderdate = models.DateTimeField(default = timezone.now)
    quantity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.item.item_name
        
    
    
    