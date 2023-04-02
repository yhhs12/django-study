from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'request'
urlpatterns = [
    # path('admin/', admin.site.urls),
    
    path('', views.index, name = 'index'),
    path('<int:id>/', views.read, name = 'detail'),
    path('write/', views.write, name = 'write'),
    path('<int:id>/write_reply/', views.write_reply , name='write_reply'),
    path('<int:id>/', views.read, name = 'detail'),
    
    
    
    
]
