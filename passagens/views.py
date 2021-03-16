from django.shortcuts import render
from passagens.forms import PassagensForms, PessoaForms

# Create your views here.
def index(request):
    passagem_form = PassagensForms()
    pessoa_form = PessoaForms()
    return render(request, 'index.html', {'form': passagem_form,
                                          'pessoa_form': pessoa_form})

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagensForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            return render(request, 'minha_consulta.html', {'form': form,
                                                           'pessoa_form': pessoa_form})
        else:
            return render(request, 'index.html', {'form': form,
                                                  'pessoa_form': pessoa_form})