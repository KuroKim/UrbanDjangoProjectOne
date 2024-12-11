"""
URL configuration for UrbanDjangoOne project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task2.views import task2_func_view, Task2ClassView
# from task3.views import Task3Tovar, Task3Korzina, Task3Main
from task4.views import Task3Tovar, Task3Korzina, Task3Main
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', task2_func_view, name="func_template"),
    path('class/', Task2ClassView.as_view(), name="class_template"),
    path('main/', Task3Main.as_view(), name="glavnaya"),
    path('main/items/', Task3Tovar.as_view(), name="tovar"),
    path('main/cart/', Task3Korzina.as_view(), name="korzina"),
    path('', sign_up_by_html, name='html_sign_up'),
    path('django_sign_up/', sign_up_by_django, name='django_sign_up'),
]
