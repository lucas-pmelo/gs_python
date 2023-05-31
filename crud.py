from models import *
from functions import *
from db import *


def cadastrar_agricultor(fazenda: Fazenda) -> Agricultor:
    nome = input("Digite o nome do agricultor: ")
    # cnpj = get_int("Digite o CNPJ do agricultor: ")
    cnpj = None

    while True:
        cnpj = get_int("Digite o CNPJ do agricultor: ")

        if cnpj_existente(cnpj, buscar_todos_agricultores()):
            print("\nCNPJ já cadastrado\n")
            continue

        if not validar_cnpj(cnpj):
            print("\nCNPJ inválido, por favor digite um cnpj de 14 digitos\n")
            continue

        break

    telefone = get_int("Digite o telefone do agricultor: ")
    email = input("Digite o email do agricultor: ")
    agricultor = Agricultor(
        nome,
        cnpj,
        telefone,
        email,
        fazenda
    )
    escrever_agricultor(agricultor)
    return agricultor


def cadastrar_fazenda() -> Fazenda:
    nome = input("Digite o nome da fazenda: ")
    area = get_int("Digite a área da fazenda: ")
    renda = get_float("Digite o faturamento anual da fazenda: ")
    cep = get_int("Digite o CEP da fazenda: ")

    if not validar_renda(renda):
        print("\nInfelizmente você não se enquadra no perfil de pequeno agricultor, não podemos ajuda-lo\n")
        return False

    fazenda = Fazenda(
        nome,
        area,
        cep,
        renda,
        500000 - renda
    )
    return fazenda


def cadastrar_investidor() -> Investidor:
    nome_empresa = input("Digite o nome da empresa do investidor: ")
    # cnpj = get_int("Digite o CNPJ do investidor: ")
    cnpj = None

    while True:
        cnpj = get_int("Digite o CNPJ do investidor: ")

        if cnpj_existente(cnpj, buscar_todos_investidores()):
            print("\nCNPJ já cadastrado\n")
            continue

        if not validar_cnpj(cnpj):
            print("\nCNPJ inválido, por favor digite um cnpj de 14 digitos\n")
            continue

        break

    nome_representante = input(
        "Digite o nome do representante do investidor: ")
    telefone_representante = get_int(
        "Digite o telefone do representante do investidor: ")
    cep = get_int("Digite o CEP do investidor: ")
    investidor = Investidor(
        nome_empresa,
        cnpj,
        nome_representante,
        telefone_representante,
        cep,
    )
    escrever_investidor(investidor)
    return investidor


def cadastrar_doacao(id_investidor, valor, nota_fiscal) -> Doacao:
    doacao = Doacao(
        id_investidor,
        valor,
        nota_fiscal,
    )
    escrever_doacao(doacao)
    return doacao


def cadastrar_doacao_alimento(id_agricultor, quantidade, codigo_remessa) -> Doacao_Alimento:
    doacao_alimento = Doacao_Alimento(
        id_agricultor,
        quantidade,
        codigo_remessa,
    )
    escrever_doacao_alimento(doacao_alimento)
