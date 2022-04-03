from os import name
from django.urls import path, include
from . import views

app_name = "owners"

urlpatterns = [
    path('', views.owelogin, name='owelogin'),

    path('register', views.register, name='register'),

    path('booking/<int:id>', views.booking, name='booking'),

    path('turfhome', views.turfhome, name='turfhome'),

    path('update', views.update, name='update'),

    path('logout', views.logout, name='logout'),

    path('book/<int:id>', views.book, name="book"),

    path('clogout', views.clogout, name='clogout'),

]
