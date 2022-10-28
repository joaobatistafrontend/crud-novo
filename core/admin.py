from atexit import register
from django.contrib import admin
from .models import CadastroModels

@admin.register(CadastroModels)
class CadastroAdm(admin.ModelAdmin):
    list_display = ['nome','sobrenome','telefone','email']
