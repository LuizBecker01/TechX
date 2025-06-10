# Model para autenticação
from sqlalchemy import Column, Integer, String
from monitoramento_maquinas.database.db_config import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return f"Usuario(nome='{self.nome}', email='{self.email}')"

def add_usuario(usuario: Usuario, session) -> None:
    """Adiciona um novo usuário ao banco de dados."""
    session.add(usuario)
    session.commit()