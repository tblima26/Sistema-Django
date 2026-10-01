from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  
        else:
            return render(request, 'login.html', {
                'error': 'Usuário ou senha inválidos.'
            })
    return render(request, 'login.html')

def novo_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        # NOTE -  Validação: As senhas coincidem
        if password != confirm_password:
            return render(request, 'novo-usuario.html', {
                'error': 'As senhas não são iguais.'
            })
        
        # NOTE -  Validação: O usuário já existe?
        if User.objects.filter(username=username).exists():
            return render(request, 'novo-usuario.html', {
                'error': 'Usuário já cadastrado.'
            })
        User.objects.create_user(username=username, password=password)
        return redirect('login')

    # Se o método for GET, apenas exibe a página vazia
    return render(request, 'novo-usuario.html')

def logout(request):
    auth_logout(request)
    return redirect('login')