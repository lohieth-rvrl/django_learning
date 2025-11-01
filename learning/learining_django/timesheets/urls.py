from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sheetshome'),
    path('create/', views.create, name='sheetcreate'),
    path('delete/<int:id>/', views.delete, name='sheetdelete'),
    path('edit/<int:id>/', views.edit, name='sheetedit'),
    # path('ajax/load-modules/', views.load_modules, name='ajax_load_modules'),
    # path('ajax/load-tasks/', views.load_tasks, name='ajax_load_tasks'),
]
