"""Camera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.hello ),
    path('page1',views.page1),
    path('page_help',views.page_help),
    path('addHelp',views.addHelp),
    path('Table',views.Table),
    path('register',views.register),
    path('addregister',views.addregister),
    path('loginForm',views.loginForm),
    path('login',views.login),
    path('logout',views.logout),
    path('BorrowBack',views.BorrowBack),
    path('RanNumBR',views.RanNumBR),
    path('RanNumBack',views.RanNumBack),
    path('key_Num',views.key_Num)


]
