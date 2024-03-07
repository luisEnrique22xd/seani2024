from django.urls import path
from . import views 

apps_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    
]
