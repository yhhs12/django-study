# 장고의 기본 라이브러리
from django.urls import path

# 현재 패키지에서 views를 import하세요~
from . import views

#board/urls.py
urlpatterns = [
    # localhost8000/board/ 이면~
    path('', views.index),
    # 글읽기 주소 /board/0
    path('<int:id>/', views.read),
    path('find_board/', views.find_board),
    #글쓰기 주소
    path('write/', views.write),
    #수정주소
    path('<int:id>/update/', views.update),
    #삭제주소
    path('<int:id>/delete/', views.delete),
    
    
    
    #path('update_board/<int:id>', views.update_board),

    #path('delete_board/<int:id>', views.delete_board),
    #path('create_board/', views.create_board),
    

    
     
    
]

