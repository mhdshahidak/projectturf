from django.urls import path, include
from . import views

app_name = "adminapp"

urlpatterns = [
    path('', views.login, name='adminlogin'),

    path('adminhome', views.admin_home, name='adminhome'),

    path('approve/<int:id>', views.approve, name='approve'),

    path('logout',views.logout, name='logout'),

    path('details',views.details, name='details'),

    #path('Activate',views.Activate, name='Activate'),

    path('DeActivate/<int:id>',views.Deactivate, name='DeActivate'),

    path('delete/<int:id>',views.delete, name='delete'),





]
