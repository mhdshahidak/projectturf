from django.urls import path, include
from . import views

app_name = "adminapp"

urlpatterns = [
    path('', views.login, name='adminlogin'),

    path('adminhome', views.admin_home, name='adminhome'),

    path('approve/<int:id>', views.approve, name='approve'),

    path('logout',views.logout, name='logout'),

]
