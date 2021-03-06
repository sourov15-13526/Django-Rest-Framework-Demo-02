"""drf_api URL Configuration

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
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

#from core.views import test_view
#from core.views import TestView
from core.views import PostView
from core.views import PostCreateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    #path('',test_view, name='test')
    #path('',TestView.as_view(), name='test'),
    path('',PostView.as_view(), name='test'),
    path('create/',PostCreateView.as_view(), name='create'),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
