from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import CadastroModels

class CadastroForm(ModelForm):
     class Meta:
          model = CadastroModels
          fields = '__all__'