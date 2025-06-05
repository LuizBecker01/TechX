# Model da máquina (id, nome, modelo, etc.)

class Maquina:
    def __init__(self, nome: str, modelo: str, ano: int, status: str, localizacao: str) -> None:
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.status = status
        self.localizacao = localizacao

    def __repr__(self):
        return f"Maquina(nome='{self.nome}', modelo='{self.modelo}', ano='{self.ano}', status='{self.status}' ,localizacao='{self.localizacao}')"