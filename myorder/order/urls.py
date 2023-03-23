# 장고의 기본 라이브러리
from django.urls import path
# 현재 패키지에서 views를 import하세요~
from . import views

#order/urls.py
urlpatterns = [
    # localhost8000/order/ 이면~
    path('', views.index),
    path('find_ordertext/', views.find_ordertext),
    path('add/', views.add),
    path('<int:id>/', views.read),
    path('<int:id>/update/', views.update),
    path('<int:id>/delete/', views.delete),
    
]