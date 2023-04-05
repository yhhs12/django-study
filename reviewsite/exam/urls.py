from django.urls import path
from . import views
app_name = 'exam'

urlpatterns = [
    
    path('add/', views.add),
    path('', views.movie_list, name='movie_list'),
    path('<int:id>/', views.read),
    path('<int:id>/update/', views.update, name = 'update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/write_review/', views.write_review, name = 'write_review'),

    
    
    
    
    
    
    
]

