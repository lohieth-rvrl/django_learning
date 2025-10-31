from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sheetshome'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    # path('ajax/load-modules/', views.load_modules, name='ajax_load_modules'),
    # path('ajax/load-tasks/', views.load_tasks, name='ajax_load_tasks'),
]
