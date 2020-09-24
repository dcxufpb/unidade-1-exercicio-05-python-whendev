nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def dados_loja():
    # Implemente aqui
    global numero
    if (nome_loja == ""):
        raise Exception("O campo nome da loja é obrigatório")
    if (logradouro == ""):
        raise Exception("O campo logradouro do endereço é obrigatório")
    if (numero == 0):
        numero = "s/n"
    if (municipio == ""):
        raise Exception("O campo município do endereço é obrigatório")
    if (estado == ""):
        raise Exception("O campo estado do endereço é obrigatório")
    if (cnpj == ""):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (inscricao_estadual == ""):
        raise Exception("O campo inscrição estadual da loja é obrigatório")
        
    show = f'''{nome_loja}
{logradouro}, {numero} {complemento}
{bairro} - {municipio} - {estado}
CEP:{cep} Tel {telefone}
{observacao}
CNPJ: {cnpj}
IE: {inscricao_estadual}
'''
    return show
