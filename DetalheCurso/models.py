from django.db import models

# Create your models here.
CodigoCurso = models.CharField(max_length=100)
CodigoTurma = models.CharField(max_length=100)

def __str__(self):
    return self.nome