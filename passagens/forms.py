from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe

class PassagensForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=200)
    destino = forms.CharField(label='Destino', max_length=200)
    data_ida = forms.DateField(label='Data ida', widget=DatePicker())
    data_volta = forms.DateField(label='Data volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data pesquisa', disabled=True, initial=datetime.today())
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='E-mail', max_length=200)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError("Origem inválida: Não inclua número.")
        else:
            return origem
