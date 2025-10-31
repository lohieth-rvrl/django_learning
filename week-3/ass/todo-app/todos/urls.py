from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.createTodo, name='create'),
    path('delete/<int:id>/', views.deleteTodo, name='delete'),
    path('edit/<int:id>/', views.editTodo, name='edit'),
    path('complete/<int:pk>/', views.mark_completed, name='mark_completed'),
]
