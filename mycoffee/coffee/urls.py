from django.urls import path
from . import views

#order/urls.py
urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('<int:id>/', views.read),
    path('find_ordertext/', views.find_ordertext),
    path('<int:id>/update/', views.update),
    path('<int:id>/delete/', views.delete),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login),
    path('logout/', views.logout),
]