from django.db import models
from django.utils import timezone  #시간정보에 관한 모듈

# Create your models here.

class Board(models.Model):
    #번호는 pk설정 안하면 장고가 자동으로 id 부여해줌
    ### 필드와 필드 사이에 컴마 금지 ###
    title = models.CharField(max_length= 100)  #제목
    content = models.TextField(null = False, blank = False)  #내용
    writer = models.CharField(max_length= 10)  #글쓴이
    input_date = models.DateTimeField(default = timezone.now) #작성시간
    view_count = models.IntegerField(default = 0) #조회수