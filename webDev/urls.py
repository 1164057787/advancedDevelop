"""webDev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.shortcuts import HttpResponse,render
from django.urls import path,re_path

from app02 import views


# def index(request):
    #业务逻辑


    #返回结果
    #return HttpResponse('INDEX') #返回一个字符串
    # return render(request,'index.html')



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('test/',views.test),


    #前后端分离的路由
    #re_path('admins/(?P<pk>\d+)',views.AdminView.as_view())
    # path('admins/',views.AdminView.as_view())
]


from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('admins',views.AdminViewSet)
urlpatterns += router.urls