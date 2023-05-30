from crud import *
from db import *
from functions import *
import random

id = None
logado = None


def main():
    if not id:
        opcao = menu_principal()
        if opcao == 1:
            login_agricultor()
        elif opcao == 2:
            login_investidor()
        elif opcao == 3:
            opcao_cadastrar_agricultor()
        elif opcao == 4:
            opcao_cadastrar_investidor()
        elif opcao == 5:
            sair()
        else:
            print("Opção inválida")

# while true meio suspeito
    while True:
        if logado == "agricultor":
            opcao = menu_agricultor()
            if opcao == 1:
                opcao_ver_fundos_disponiveis()
            elif opcao == 2:
                opcao_registrar_producao()

            elif opcao == 3:
                sair()
            else:
                print("Opção inválida")
        elif logado == "investidor":
            opcao = menu_investidor()
            if opcao == 1:
                opcao_cadastrar_doacao()
            elif opcao == 2:
                sair()
            else:
                print("Opção inválida")
        else:
            main()


def login_agricultor():
    cnpj = get_int("Digite o CNPJ do agricultor: ")
    agricultor = buscar_agricultor(cnpj)
    global id, logado
    id = agricultor["id"]
    logado = "agricultor"
    print(f"\nOlá {agricultor['nome']}, você foi logado com sucesso\n")


def login_investidor():
    cnpj = get_int("Digite o CNPJ do investidor: ")
    investidor = buscar_investidor(cnpj)
    global id, logado
    id = investidor["id"]
    logado = "investidor"
    print(
        f"\nOlá {investidor['nome_representante']}, você foi logado com sucesso\n")


def opcao_cadastrar_agricultor():
    fazenda = cadastrar_fazenda()
    if not fazenda:
        return

    agricultor = cadastrar_agricultor(
        fazenda)
    if not agricultor:
        return

    agricultor = agricultor.transformar_dicionario()

    global id, logado
    id = agricultor["id"]
    logado = "agricultor"
    print(
        f"\nBem vindo {agricultor['nome']}, você foi cadastrado com sucesso e já está logado\n")


def opcao_cadastrar_investidor():
    investidor = cadastrar_investidor().transformar_dicionario()
    global id, logado
    id = investidor["id"]
    logado = "investidor"
    print(
        f"\nBem vindo {investidor['nome_representante']}, você foi cadastrado com sucesso e já está logado\n")


def opcao_registrar_producao():
    kilos_produzidos = registrar_producao()
    kilos_doados = kilos_produzidos * 0.1
    codigo_remessa = random.randint(100000, 999999)

    cadastrar_doacao_alimento(
        id, kilos_doados, codigo_remessa)

    print(f"\nDoação de {kilos_doados}kg registrada com sucesso\n")


def opcao_cadastrar_doacao():
    print("Agricultores que precisam de doações: \n")

    for agricultor in buscar_todos_agricultores():
        if agricultor["fazenda"]["valor_necessario"] != 0:
            print(
                f'> ID: {agricultor["id"]}\nNome: {agricultor["nome"]}\nValor necessário: {agricultor["fazenda"]["valor_necessario"]}\n')

    id_agricultor = get_int("Digite o ID do agricultor que deseja doar: ")
    valor_necessario = buscar_agricultor(
        id_agricultor)["fazenda"]["valor_necessario"]
    nota_fiscal = random.randint(100000, 999999)

    cadastrar_doacao(id, valor_necessario, nota_fiscal)

    atualiza_agricultor(
        {"id": id_agricultor, "fazenda": {"valor_necessario": 0}})

    print(f"\nDoação de R${valor_necessario} registrada com sucesso\n")


def opcao_ver_fundos_disponiveis():
    agricultor = buscar_agricultor(id)
    print(
        f"\nVocê tem R${agricultor['fazenda']['valor_necessario']} disponíveis para receber\n")


print("Bem vindo ao Projeto Global Solution\n")
main()
