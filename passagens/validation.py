def origem_destino_iguais(origem, destino, lista_de_erros):
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais.'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = nome_campo + ' inválido: não pode conter números.'

def data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros):
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de ida não pode ser maior que data de volta.'

def data_ida_menor_data_hoje(data_ida, data_pesquisa, lista_de_erros):
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que data de hoje.'