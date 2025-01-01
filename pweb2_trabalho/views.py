from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

User = get_user_model()

# Views principais
def index(request):
    return render(request, 'index.html')

def campanhas(request):
    return render(request, 'campanhas.html')

def criar_campanha(request):
    return render(request, 'criar_campanha.html')

def doacao(request):
    return render(request, 'doacao.html')

# Página de registro
def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validações
        if not username or not email or not password or not confirm_password:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return redirect('registro')

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('registro')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Email inválido.')
            return redirect('registro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return redirect('registro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já está em uso.')
            return redirect('registro')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Ocorreu um erro: {e}')
            return redirect('registro')

    return render(request, 'registro.html')

# Página de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')

    return render(request, 'login.html')


@login_required
def perfil_view(request):
    return render(request, 'meuperfil.html')

@login_required
def atualizar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('perfil')