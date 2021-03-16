from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *
from passagens.models import Pessoa, Passagem, ClasseViagem

class PassagensForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data pesquisa', disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de ida',
            'data_volta': 'Data de volta',
            'classe_viagem': 'Classe da viagem',
            'informacoes': 'Informações'
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }


    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}
        origem_destino_iguais(origem, destino, lista_erros)
        campo_tem_algum_numero(origem, 'origem', lista_erros)
        campo_tem_algum_numero(destino, 'destino', lista_erros)
        data_ida_maior_data_volta(data_ida, data_volta, lista_erros)
        data_ida_menor_data_hoje(data_ida, data_pesquisa, lista_erros)
        if lista_erros is not None:
            for erro, mensagem_erro in lista_erros.items():
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
        #fields = ['email']