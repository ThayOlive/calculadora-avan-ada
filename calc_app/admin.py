from django.contrib import admin
from .models import Usuario, Operacao
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreateForm, UsuarioChangeForm

# Formaulário para cadastrar um usuário no DjangoAdmin
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreateForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['username', 'email', 'first_name', 'is_staff']
    readonly_fields = ['dt_inclusao']

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