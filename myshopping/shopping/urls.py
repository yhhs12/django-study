from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('order/add/', views.add),
    path('<int:id>/', views.read),
    path('find_text/', views.find_text),
    path('<int:id>/update/', views.update),
    path('<int:id>/delete/', views.delete), 
    path('order/', views.order),
    
    
    
    
    
]