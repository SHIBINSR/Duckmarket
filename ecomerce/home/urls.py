from django.urls import path
from . import views


urlpatterns = [
    path('base',views.base,name="Base"),
    path('',views.home,name="Home"),
     
    
]
