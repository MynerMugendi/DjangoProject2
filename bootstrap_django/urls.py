"""
URL configuration for bootstrap_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from Bootstrap_template import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('401/', views.four_one, name='401'),
    path('404/', views.four_four, name='404'),
    path('500/', views.five_five, name='500'),
    path('charts/', views.charts, name='charts'),
    path('layout-sidenav-light/', views.layout_sidenav_light, name='layout-sidenav-light'),
    path('layout-static/', views.layout_static, name='layout-static'),
    path('login/', views.login, name='login'),
    path('password/', views.password, name='password'),
    path('register/', views.register, name='register'),
    path('tables/', views.tables, name='tables'),


]
