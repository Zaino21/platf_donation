from django.contrib import admin
from django.urls import path

from pweb2_trabalho import views

urlpatterns = [
    path('', views.index, name='index'),
    path('campanhas/', views.campanhas, name='campanhas'),
    path('criar_campanha/', views.criar_campanha, name='criar_campanha'),
    path('doacao/', views.doacao, name='doacao'),
    path('login_modal/', views.login_modal_view, name='login_modal'),  # Rota do login via modal
    path('cadastro_modal/', views.cadastro_modal_view, name='cadastro_modal'),  # Rota do cadastro via modal
    path('admin/', admin.site.urls),  # Adicionando a rota do painel administrativo
]
