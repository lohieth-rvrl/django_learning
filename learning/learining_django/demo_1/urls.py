from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='demo'),
    path('home/', views.home, name='home'),
    path("pro/<str:name>/<int:age>/", views.pro , name='pro'),
]
