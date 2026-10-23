from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('produto/', views.produto, name='produto'),
    path('contato/', views.contato, name='contato')
]