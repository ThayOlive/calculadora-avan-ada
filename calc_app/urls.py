from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login' ),
    path('calculadora/',views.calculadora_view, name='calculadora'),
]
