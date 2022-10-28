from django.db import models


class CadastroModels(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    telefone = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome