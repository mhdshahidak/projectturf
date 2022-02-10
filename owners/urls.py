from django.urls import path,include
from . import views

app_name ="owners"

urlpatterns = [
    path('register',views.register,name='register'),
    
    path('owelogin',views.owelogin,name='owelogin'),

    path('booking',views.booking,name='booking'),


   
]