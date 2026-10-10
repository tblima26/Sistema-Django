from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('novoPaciente/', views.novo_paciente, name='novo-paciente'),
    path('novoPacienteSucesso/', views.novo_paciente_sucesso, name='novo_paciente_sucesso'),
    path('alterarPaciente/<int:codigo_paciente>', views.alterar_paciente, name='alterar_paciente'),
    path('exluirPaciente/<int:codigo_paciente>', views.excluir_paciente, name='excluir_paciente'),
    path('buscar/', views.buscar_paciente, name='buscar_paciente'),
]