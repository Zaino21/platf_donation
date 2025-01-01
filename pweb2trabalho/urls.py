from django.contrib import admin
from django.urls import path
from pweb2_trabalho import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('campanhas/', views.campanhas, name='campanhas'),
    path('criar_campanha/', views.criar_campanha, name='criar_campanha'),
    path('doacao/', views.doacao, name='doacao'),
    path('registro/', views.registro, name='registro'),  
    path('login/', views.login_view, name='login'),      
    path('admin/', admin.site.urls),
    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/atualizar/', views.atualizar_perfil, name='atualizar_perfil'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),  
]
