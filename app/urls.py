from django.urls import path, include
from . import views

app_name = "app"

urlpatterns = [
    path('', views.master, name='master'),
    path('home', views.home, name='userhome'),
    path('loginpage', views.login, name='loginpage'),
    path('signup', views.signup, name='signup'),
    path('search',views.search, name="search")
]
