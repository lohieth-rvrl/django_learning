from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todoshome'),
    path('create/', views.createTodo, name='todocreate'),
    path('delete/<int:id>/', views.deleteTodo, name='tododelete'),
    path('edit/<int:id>/', views.editTodo, name='todoedit'),
    path('complete/<int:id>/', views.mark_completed, name='mark_completed'),
]
