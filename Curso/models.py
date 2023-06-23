from django.db import models

# Create your models here.
Codigo = models.CharField(max_length=100)
Nome = models.CharField(max_length=100)

def __str__(self):
    return self.nome