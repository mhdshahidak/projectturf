from django.urls import path,include
from . import views

app_name ="app"

urlpatterns = [
    path('',views.home,name=''),
    # path('login',views.log,name='login'),
    path('loginpage',views.login,name='loginpage'),
]