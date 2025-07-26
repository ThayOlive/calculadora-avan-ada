from django.db import models
from django.contrib.auth.models import AbstractUser

# Uso da classe AbstractUser para personalizar o usuario
class Usuario(AbstractUser):
    # necessário a definição desses campos para que eles sejam obrigatórios
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    dt_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Operacao(models.Model):
    #Relacionamento 1-N (um para muitos)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    parametros = models.CharField(max_length=50,blank=False, null=False)
    resultado = models.CharField(max_length=50, blank=False, null=False)
    dt_inclusao = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.parametros} - {self.resultado} - {self.dt_inclusao}'