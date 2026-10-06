from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Paciente

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def novo_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        Paciente.objects.create(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento
        )
        return redirect('/novoPacienteSucesso')
    return render(request,'novo-paciente.html')

@login_required
def novo_paciente_sucesso(request):
    return render(request,'novo-paciente-sucesso.html')