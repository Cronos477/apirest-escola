import re
from validate_docbr import CPF

def nome_invalido(nome):
    return not nome.isalpha()


def cpf_invalido(cpf):
    validator_cpf = CPF()
    cpf_valido = validator_cpf.validate(cpf)
    return not cpf_valido


def celular_invalido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return not resposta
