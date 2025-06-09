# Conexão e inicialização do banco
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from __future__ import annotations

from models.Usuario import Usuario
# from models.Historico import Historico
# from models.Leitura import Leitura
from models.Maquinas import Maquinas

# Base para nossos modelos
Base = declarative_base()

engine = create_engine('sqlite:///crud_sqlalchemy.db', echo=True)

Base.metadata.create_all(engine)

# Criar uma classe de sessão
Session = sessionmaker(bind=engine)
session = Session()

def criar_usuario(nome: str, email: str, senha: str) -> Usuario:
    """Cria um novo usuário."""
    usuario = Usuario(nome=nome, email=email, senha=senha)
    session.add(usuario)
    session.commit()
    return usuario

def cadastrar_maquina(nome: str, descricao: str) -> Maquinas:
    """Cadastra uma nova máquina."""
    maquina = Maquinas(nome=nome, descricao=descricao)
    session.add(maquina)
    session.commit()
    return maquina
        