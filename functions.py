from db import *

BARRA = "\n--------------------------------------------------"


def sair():
    print(BARRA)
    print("\nObrigado por usar o Projeto Global Solution")
    print(BARRA)
    exit()


def get_int(message):
    while True:
        try:
            value = input(message)
            value = int(value)
            return value
        except ValueError:
            print("Digite um número inteiro\n")


def get_float(message):
    while True:
        try:
            value = input(message)
            value = float(value)
            return value
        except ValueError:
            print("Digite um número inteiro ou decimal\n")


def menu_principal():
    print("\n1 - Logar como agricultor")
    print("2 - Logar como investidor")
    print("3 - Cadastrar agricultor")
    print("4 - Cadastrar investidor")
    print("5 - Sair")
    opcao = get_int("\nDigite a opção desejada: ")
    return opcao


def menu_agricultor():
    print("\n1 - Quantidade de fundos disponíveis")
    print("2 - Registro de produção")
    print("3 - Sair")
    opcao = get_int("\nDigite a opção desejada: ")
    return opcao


def menu_investidor():
    print("\n1 - Cadastrar doação")
    print("2 - Ver doações feitas")
    print("3 - Sair")
    opcao = get_int("\nDigite a opção desejada: ")
    return opcao


def cnpj_existente(cnpj, agricultores):
    for agricultor in agricultores:
        if agricultor["cnpj"] == cnpj:
            return True
    return False


def validar_cnpj(cnpj):
    if len(str(cnpj)) == 14:
        return True


def validar_renda(renda):
    return not (renda < 415000 or renda > 500000)


def registrar_producao():
    kilos_produzidos = get_int(
        "Digite quantos kilos de alimento você produziu: ")
    return kilos_produzidos
