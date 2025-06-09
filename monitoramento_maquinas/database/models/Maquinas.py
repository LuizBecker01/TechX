# Model para máquinas
from monitoramento_maquinas.database.db_config import Base, Column, Session, String, Integer

class Maquina(Base):
    __tablename__ = 'maquinas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    modelo = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)
    localizacao = Column(String(100), nullable=False)

    def __init__(self, nome: str, modelo: str, ano: int, status: str, localizacao: str) -> None:
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.status = status
        self.localizacao = localizacao

    def __repr__(self):
        return (
            f"Maquina(nome='{self.nome}', modelo='{self.modelo}', "
            f"ano={self.ano}, status='{self.status}', localizacao='{self.localizacao}')"
        )

def get_maquina_by_id(maquina_id: int) -> Maquina:
    """Retorna uma máquina pelo ID."""
    return Session.query(Maquina).filter(Maquina.id == maquina_id).first()

def add_maquina(maquina: Maquina) -> None:
    """Adiciona uma nova máquina ao banco de dados."""
    Session.add(maquina)
    Session.commit()
    
def update_maquina(maquina: Maquina) -> None:
    """Atualiza uma máquina existente no banco de dados."""
    existing_maquina = get_maquina_by_id(maquina.id)
    if existing_maquina:
        existing_maquina.nome = maquina.nome
        existing_maquina.modelo = maquina.modelo
        existing_maquina.ano = maquina.ano
        existing_maquina.status = maquina.status
        existing_maquina.localizacao = maquina.localizacao
        session.commit()
        
def delete_maquina(maquina_id: int) -> None:
    """Remove uma máquina do banco de dados pelo ID."""
    maquina = get_maquina_by_id(maquina_id)
    if maquina:
        Session.delete(maquina)
        Session.commit()
    else:
        print(f"Máquina com ID {maquina_id} não encontrada.")