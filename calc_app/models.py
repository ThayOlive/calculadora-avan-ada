from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    # Perfil complementar ao modelo padrão da classe User do Django, criado um objeto complementar da classe 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dt_inclusao = models.DateTimeField()

    def __str__(self):
        return self.user.username

class Operacao(models.Model):
    #Relacionamento 1-N (um para muitos)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parametros = models.CharField(max_length=50,blank=False, null=False)
    resultado = models.CharField(max_length=50, blank=False, null=False)
    dt_inclusao = models.DateTimeField()

    def __str__(self):
        return f'{self.parametros} - {self.resultado} - {self.dt_inclusao}'