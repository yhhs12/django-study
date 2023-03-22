# 장고의 기본 라이브러리
from django.urls import path

# 현재 패키지에서 views를 import하세요~
from . import views

urlpatterns = [
    # localhost8000/board/ 이면~
    path('', views.index),
    path('read/<int:id>', views.read),
    path('find_board/', views.find_board),
    # path('update_board/', views.update_board),
    path('delete_board/<int:id>', views.delete_board),
    # path('create_board/', views.create_board),
    

    
     
    
]

