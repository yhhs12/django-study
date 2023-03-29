# 장고의 기본 라이브러리
from django.urls import path

# 현재 패키지에서 views를 import하세요~
from . import views
#board/urls.py

app_name = 'board'

urlpatterns = [
    # localhost8000/board/ 이면~
    path('', views.index, name = 'index'),
    # path('find_board/', views.find_board),
    
    # 글읽기 주소 /board/0
    path('<int:id>/', views.read, name = 'detail'),
    #글쓰기 주소
    path('write/', views.write, name = 'write'),
    #수정 주소
    path('<int:id>/update/', views.update, name = 'update'),
    #삭제 주소
    path('<int:id>/delete/', views.delete , name = 'delete'),    
    #댓글쓰기 주소
    path('<int:id>/write_reply/', views.write_reply , name = 'write_reply'),
    #댓글삭제 주소(id:글번호, rid:댓글번호)
    path('<int:id>/delete_reply/<int:rid>', views.update_reply , name = 'delete_reply'),
    #댓글수정 주소(id:글번호)    
    path('<int:id>/update_reply/', views.update_reply , name = 'update_reply'),
    
    #AJAX    
    path('callAjax/', views.call_ajax),
    #AJAX_댓글목록       
    path('load_reply/', views.load_reply),  
    
    
    #path('update_board/<int:id>', views.update_board),

    #path('delete_board/<int:id>', views.delete_board),
    #path('create_board/', views.create_board),
    

    
     
    
]

