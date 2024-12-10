from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Task3Main(TemplateView):
    template_name = 'fourth_task/glavnaya.html'


class Task3Tovar(TemplateView):
    template_name = 'fourth_task/tovar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = ['Товар 1', 'Товар 2', 'Товар 3']
        return context


class Task3Korzina(TemplateView):
    template_name = 'fourth_task/korzina.html'
