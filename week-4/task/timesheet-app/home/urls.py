from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('timesheets/', include('timesheets.urls')),

]
