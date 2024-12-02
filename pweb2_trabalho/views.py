from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import ensure_csrf_cookie

# Usando o modelo de usuário personalizado
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

# View para login via modal
@ensure_csrf_cookie
def login_modal_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login realizado com sucesso!'})
        else:
            return JsonResponse({'success': False, 'message': 'Usuário ou senha inválidos.'})
    return JsonResponse({'success': False, 'message': 'Requisição inválida.'})

# View para cadastro via modal
@ensure_csrf_cookie
def cadastro_modal_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validações
        if not username or not email or not password or not confirm_password:
            return JsonResponse({'success': False, 'message': 'Todos os campos são obrigatórios.'})

        if password != confirm_password:
            return JsonResponse({'success': False, 'message': 'As senhas não coincidem.'})

        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'success': False, 'message': 'Email inválido.'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Usuário já existe.'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email já está em uso.'})

        try:
            # Criação do usuário
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'success': True, 'message': 'Cadastro realizado com sucesso!'})
        except Exception as e:
            # Captura erros inesperados
            return JsonResponse({'success': False, 'message': f'Ocorreu um erro: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'Requisição inválida.'})
