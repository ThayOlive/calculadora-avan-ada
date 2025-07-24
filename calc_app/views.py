from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, 'login.html', context)

def calculadora_view(request):
    return render(request, 'calculadora.html')


