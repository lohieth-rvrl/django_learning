from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),

]
