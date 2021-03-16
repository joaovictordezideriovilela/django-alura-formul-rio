from django.shortcuts import render
from passagens.forms import PassagensForms

# Create your views here.
def index(request):
    form = PassagensForms()
    return render(request, 'index.html', {'form': form})

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagensForms(request.POST)
        if form.is_valid():
            return render(request, 'minha_consulta.html', {'form': form})
        else:
            return render(request, 'index.html', {'form': form})