from models import *
import os
import json


NOMES_ARQUIVOS = ["db/agricultores.json", "db/doacoes_alimentos.json",
                  "db/doacoes.json", "db/investidores.json"]


def inicializar():
    for nome in NOMES_ARQUIVOS:
        arquivo = open(nome, "a")
        isempty = os.stat(nome).st_size == 0
        if isempty:
            conteudo = {
                nome[3:-5]: []
            }

            arquivo.write(json.dumps(conteudo))
        arquivo.close()

# NÃO REPETIR TANTO CÓDIGO


def escrever_agricultor(agricultor: Agricultor) -> None:
    arquivo_agricultor = open(NOMES_ARQUIVOS[0], "r")
    conteudo = json.load(arquivo_agricultor)

    if len(conteudo["agricultores"]) == 0:
        agricultor.setId(1)
    else:
        agricultor.setId(conteudo["agricultores"][-1]["id"] + 1)

    conteudo["agricultores"].append(agricultor.transformar_dicionario())

    arquivo_agricultor = open(NOMES_ARQUIVOS[0], "w")
    arquivo_agricultor.write(json.dumps(conteudo))

    arquivo_agricultor.close()


def escrever_investidor(investidor: Investidor) -> None:
    arquivo_investidor = open(NOMES_ARQUIVOS[3], "r")
    conteudo = json.load(arquivo_investidor)

    if len(conteudo["investidores"]) == 0:
        investidor.setId(1)
    else:
        investidor.setId(conteudo["investidores"][-1]["id"] + 1)

    conteudo["investidores"].append(investidor.transformar_dicionario())

    arquivo_investidor = open(NOMES_ARQUIVOS[3], "w")
    arquivo_investidor.write(json.dumps(conteudo))

    arquivo_investidor.close()


def escrever_doacao(doacao: Doacao) -> None:
    arquivo_doacao = open(NOMES_ARQUIVOS[2], "r")
    conteudo = json.load(arquivo_doacao)

    if len(conteudo["doacoes"]) == 0:
        doacao.setId(1)
    else:
        doacao.setId(conteudo["doacoes"][-1]["id"] + 1)

    conteudo["doacoes"].append(doacao.transformar_dicionario())

    arquivo_doacao = open(NOMES_ARQUIVOS[2], "w")
    arquivo_doacao.write(json.dumps(conteudo))

    arquivo_doacao.close()


def escrever_doacao_alimento(doacao_alimento: Doacao_Alimento) -> None:
    arquivo_doacao_alimentos = open(NOMES_ARQUIVOS[1], "r")
    conteudo = json.load(arquivo_doacao_alimentos)

    if len(conteudo["doacoes_alimentos"]) == 0:
        doacao_alimento.setId(1)
    else:
        doacao_alimento.setId(conteudo["doacoes_alimentos"][-1]["id"] + 1)

    conteudo["doacoes_alimentos"].append(
        doacao_alimento.transformar_dicionario())

    arquivo_doacao_alimentos = open(NOMES_ARQUIVOS[1], "w")
    arquivo_doacao_alimentos.write(json.dumps(conteudo))

    arquivo_doacao_alimentos.close()


def buscar_agricultor(cnpj: int) -> Agricultor:
    arquivo_agricultor = open(NOMES_ARQUIVOS[0], "r")
    conteudo = json.load(arquivo_agricultor)

    for agricultor in conteudo["agricultores"]:
        if agricultor["cnpj"] == cnpj:
            return agricultor


def buscar_investidor(cnpj: int) -> Investidor:
    arquivo_investidor = open(NOMES_ARQUIVOS[3], "r")
    conteudo = json.load(arquivo_investidor)

    for investidor in conteudo["investidores"]:
        if investidor["cnpj"] == cnpj:
            return investidor


def buscar_doacao(id_investidor: int) -> Doacao:
    arquivo_doacao = open(NOMES_ARQUIVOS[2], "r")
    conteudo = json.load(arquivo_doacao)

    for doacao in conteudo["doacoes"]:
        if doacao["id_investidor"] == id_investidor:
            return doacao


def buscar_doacao_alimento(id_agricultor: int) -> Doacao_Alimento:
    arquivo_doacao_alimento = open(NOMES_ARQUIVOS[1], "r")
    conteudo = json.load(arquivo_doacao_alimento)

    for doacao_alimento in conteudo["doacoes_alimentos"]:
        if doacao_alimento["id_agricultor"] == id_agricultor:
            return doacao_alimento


def buscar_todos_agricultores() -> list:
    arquivo_agricultor = open(NOMES_ARQUIVOS[0], "r")
    conteudo = json.load(arquivo_agricultor)
    return conteudo["agricultores"]


def buscar_todos_investidores() -> list:
    arquivo_investidor = open(NOMES_ARQUIVOS[3], "r")
    conteudo = json.load(arquivo_investidor)
    return conteudo["investidores"]


def buscar_todas_doacoes() -> list:
    arquivo_doacao = open(NOMES_ARQUIVOS[2], "r")
    conteudo = json.load(arquivo_doacao)
    return conteudo["doacoes"]


def atualiza_agricultor(agricultor_dict):
    agricultores = buscar_todos_agricultores()

    for agricultor in agricultores:
        if agricultor["id"] == agricultor_dict["id"]:
            if "fazenda" in agricultor_dict:
                fazenda_atualizada = agricultor_dict.pop("fazenda")
                agricultor["fazenda"].update(fazenda_atualizada)
            agricultor.update(agricultor_dict)
            break

    with open(NOMES_ARQUIVOS[0], "w") as arquivo_agricultor:
        arquivo_agricultor.write(json.dumps({"agricultores": agricultores}))


inicializar()
