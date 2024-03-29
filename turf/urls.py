"""turf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf.urls.static import static  # import media
from django.conf import settings    # impot settings for media

urlpatterns = [
    
    path('',include('app.urls')),
    path('owners/',include('owners.urls')),
    path('adminlog/',include('adminapp.urls')),

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
urlpatterns += staticfiles_urlpatterns()
