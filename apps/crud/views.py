from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente

# Create your views here.
@login_required
def index(request):
    pacientes = Paciente.objects.all()
    return render(request, 'index.html', {'pacientes': pacientes})

@login_required
def novo_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            nome = nome.strip().title()
        sintomas = request.POST.get('sintomas')
        if sintomas:
            sintomas = sintomas.strip()
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        
        Paciente.objects.create(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            sintomas=sintomas
        )
        return redirect('novo-paciente-sucesso') 
        
    return render(request, 'novo-paciente.html')

@login_required
def novo_paciente_sucesso(request):
    return render(request, 'novo-paciente-sucesso.html')

@login_required
def alterar_paciente(request, codigo_paciente):
    # Garante 404 se o paciente não for encontrado
    paciente = get_object_or_404(Paciente, codigo_paciente=codigo_paciente)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            nome = nome.strip().title()
            
        paciente.nome = nome
        paciente.cpf = request.POST.get('cpf')
        paciente.email = request.POST.get('email')
        paciente.telefone = request.POST.get('telefone')
        paciente.data_nascimento = request.POST.get('data_nascimento')   
        paciente.save()
        return redirect('index')
        
    # Passando o dicionário {'paciente': paciente} para o contexto do template
    return render(request, "alterar-dados.html", {'paciente': paciente})

@login_required
def excluir_paciente(request, codigo_paciente):
    paciente = get_object_or_404(Paciente, codigo_paciente=codigo_paciente)
    paciente.delete()
    return redirect('index')

@login_required
def buscar_paciente(request):
    query = request.GET.get('pesquisa', '')  # Pega o termo ou define vazio
    if query:
        pacientes = Paciente.objects.filter(nome__icontains=query)
    else:
        pacientes = Paciente.objects.all() # Se não pesquisou nada, traz todos   
    return render(request, 'index.html', {
        'pacientes': pacientes,
        'termo_pesquisa': query # Usando termo_pesquisa para bater com o HTML que ajustamos antes
    })