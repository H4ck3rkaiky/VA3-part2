from django.db import models

# Create your models here.
Nome = models.CharField(max_length=100)
Sexo = models.CharField(max_length=100)
Registro = models.CharField(max_length=100)

def __str__(self):
    return self.nome