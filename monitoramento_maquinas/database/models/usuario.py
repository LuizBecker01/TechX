# Model para autenticação

from sqlalchemy import Column, Integer, String
from monitoramento_maquinas.database.db_config import Base, Session


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
    
def get_usuario_by_email(email: str) -> Usuario:
    """Retorna um usuário pelo email."""
    return Session.query(Usuario).filter(Usuario.email == email).first()

def add_usuario(usuario: Usuario) -> None:
    """Adiciona um novo usuário ao banco de dados."""
    Session.add(usuario)
    Session.commit()
    
def update_usuario(usuario: Usuario) -> None:
    """Atualiza um usuário existente no banco de dados."""
    existing_usuario = get_usuario_by_email(usuario.email)
    if existing_usuario:
        existing_usuario.nome = usuario.nome
        existing_usuario.senha = usuario.senha
        Session.commit()
    else:
        print(f"Usuário com email {usuario.email} não encontrado.")
        
def delete_usuario(email: str) -> None:
    """Remove um usuário do banco de dados pelo email."""
    usuario = get_usuario_by_email(email)
    if usuario:
        Session.delete(usuario)
        Session.commit()
    else:
        print(f"Usuário com email {email} não encontrado.")
        