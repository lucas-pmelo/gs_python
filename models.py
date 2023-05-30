class Fazenda:
    def __init__(self, nome: str, area: int, cep: int, renda: float, valor_necessario: float) -> None:
        self.nome = nome
        self.area = area
        self.cep = cep
        self.renda = renda
        self.valor_necessario = valor_necessario


class Agricultor:
    def __init__(self, nome: str, cnpj: int, telefone: int, email: str, fazenda: Fazenda, id: None or int = None) -> None:
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.fazenda = fazenda

    def setId(self, id: int) -> None:
        self.id = id

    def transformar_dicionario(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "cnpj": self.cnpj,
            "telefone": self.telefone,
            "email": self.email,
            "fazenda": {
                "nome": self.fazenda.nome,
                "area": self.fazenda.area,
                "cep": self.fazenda.cep,
                "renda": self.fazenda.renda,
                "valor_necessario": self.fazenda.valor_necessario
            }
        }


class Investidor:
    def __init__(self, nome_empresa: str, cnpj: int, nome_representante: str, telefone_representante: int, cep: int, id: None or int = None) -> None:
        self.id = id
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.nome_representante = nome_representante
        self.telefone_representante = telefone_representante
        self.cep = cep

    def setId(self, id: int) -> None:
        self.id = id

    def transformar_dicionario(self) -> dict:
        return {
            "id": self.id,
            "nome_empresa": self.nome_empresa,
            "cnpj": self.cnpj,
            "nome_representante": self.nome_representante,
            "telefone_representante": self.telefone_representante,
            "cep": self.cep
        }


class Doacao:
    def __init__(self, id_investidor: int, valor: float, nota_fiscal: int, id: None or int = None) -> None:
        self.id = id
        self.id_investidor = id_investidor
        self.valor = valor
        self.nota_fiscal = nota_fiscal

    def setId(self, id: int) -> None:
        self.id = id

    def transformar_dicionario(self) -> dict:
        return {
            "id": self.id,
            "id_investidor": self.id_investidor,
            "valor": self.valor,
            "nota_fiscal": self.nota_fiscal
        }


class Doacao_Alimento:
    def __init__(self, id_agricultor: int, quantidade: int, codigo_remessa: int, id: None or int = None) -> None:
        self.id = id
        self.id_agricultor = id_agricultor
        self.quantidade = quantidade
        self.codigo_remessa = codigo_remessa

    def setId(self, id: int) -> None:
        self.id = id

    def transformar_dicionario(self) -> dict:
        return {
            "id": self.id,
            "id_agricultor": self.id_agricultor,
            "quantidade": self.quantidade,
            "codigo_remessa": self.codigo_remessa
        }
