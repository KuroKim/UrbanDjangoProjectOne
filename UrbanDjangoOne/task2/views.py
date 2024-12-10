# В представлениях (views) приложения task2 создайте представления: одно классовое, а другое функциональное, которые отображают шаблоны с соответствующими надписями. Названия для представлений можете определить самостоятельно.

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def task2_func_view(request):
    return render(request, 'second_task/func_template.html')


class Task2ClassView(TemplateView):
    template_name = 'second_task/class_template.html'
