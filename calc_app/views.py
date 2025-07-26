from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .models import Operacao, Usuario

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
           user = form.get_user()
           auth_login(request, user)
           return redirect('calculadora')
    else:
        form = AuthenticationForm()         

    context = {
        "form": form
            }
    return render(request, 'login.html', context)

@login_required
def calculadora_view(request):
    # View feita com ajuda da IA 
    usuario = request.user
    resultado = None
    expressao = ""

    if request.method == 'POST':
        if 'limpar_historico' in request.POST:
            Operacao.objects.filter(usuario=usuario).delete()
            return redirect('calculadora')
    
        expressao = request.POST.get('expressao', '')
         # Trocar caracteres da expressão para Python, se precisar
        expressao_python = expressao.replace('×', '*').replace('−', '-').replace('÷', '/')
        # Avalia a expressão com segurança - cuidado com eval em produção!
        resultado = str(eval(expressao_python))
        # Salvar operação no banco
        Operacao.objects.create(
            usuario=usuario,
            parametros=expressao,
            resultado=resultado,
                )
    # Busca histórico
    historico_operacoes = Operacao.objects.filter(usuario=usuario).order_by('-dt_inclusao')

    context = {
        'resultado': resultado,
        'expressao': expressao if resultado is None else resultado,
        'historico_operacoes': historico_operacoes,
        'usuario': usuario,
    }
    return render(request, 'calculadora.html', context)
   


