from django.shortcuts import render

# Create your views here.
def cadastro(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Cadastro'
};
    return render( request, 'cadastro/index.html', contexto)