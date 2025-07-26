from django.contrib import admin
from .models import Usuario, Operacao
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreateForm, UsuarioChangeForm

# Formaulário para cadastrar um usuário no DjangoAdmin - feito com ajuda da IA
class UsuarioAdmin(UserAdmin): # Herda da classe UserADmin, modelo padrao para administração de usuarios
    #form de criação
    add_form = UsuarioCreateForm
    #for de edição
    form = UsuarioChangeForm
    model = Usuario # modelo base para a configuração dessa classe
    list_display = ['username', 'email', 'first_name', 'is_staff'] # campos mostrados na listagem de usuários
    readonly_fields = ['dt_inclusao'] # define o campo dt_inclusão como só leitura - n permite edição

    # Personalizar os campos no formulário de ediçao
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Datas importantes', {'fields': ('dt_inclusao',)}),
    )

    # Campos do formulário de cadastro
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Operacao)