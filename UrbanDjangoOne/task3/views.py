from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Task3Main(TemplateView):
    template_name = 'third_task/glavnaya.html'


class Task3Tovar(TemplateView):
    template_name = 'third_task/tovar.html'


class Task3Korzina(TemplateView):
    template_name = 'third_task/korzina.html'
