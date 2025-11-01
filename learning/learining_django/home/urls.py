from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('timesheets/', include('timesheets.urls')),
    path('todos/', include('todos.urls')),
    path('article/', include('article_app.urls')),
]
