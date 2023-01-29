"""practice URL Configuration

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
from rest_framework import routers
from dummy.views import Test2ViewSet,async_main_view

router = routers.SimpleRouter()
router.register(r'users', Test2ViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include((router.urls,'dummy'))),
    path('async/',async_main_view,name='async_main_view'),
]
