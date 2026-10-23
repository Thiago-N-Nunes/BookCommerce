from django.shortcuts import render
from .forms import ContatoForm

def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def produto(request):
    return render(request, 'produto.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            form.send_mail()
            form = ContatoForm()
        else:
            print('Erro ao enviar o formulário')

    context = {
        'formulario' : form ,
    }
    return render(request, 'contato.html', context)