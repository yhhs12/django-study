from django.db import models
from django.utils import timezone

# Create your models here.

class Coffee(models.Model):
    order_date = models.DateTimeField(default = timezone.now)
    order_text = models.TextField(null = False, blank = False)
    price = models.IntegerField()
    address = models.CharField(max_length= 100) 
