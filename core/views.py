from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import CadastroModels


class IndexView(ListView):
    template_name = 'index.html'
    model = CadastroModels



    # def get_context_data(self, **kwargs) :
    #     context = super().get_context_data(**kwargs)
        
