from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('order/', views.order),
    path('order/add/', views.add),
    path('<int:id>/', views.read),
    
    
    
    
    
]
