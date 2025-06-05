# Conexão e inicialização do banco
from sqlalchemy import create_engine ,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database.models import Usuarios
# Base para nossos modelos
Base = declarative_base()

#  Conectar ao banco de dados
engine = create_engine('sqlite:///crud_sqlalchemy.db', echo=True)
Base.metadata.create_all(engine)

# Criar uma classe de sessão
Session = sessionmaker(bind=engine)
session = Session()

def criar_usuario(nome: str , idade: int):
    session = Session()
    novo_usuario = Usuarios(nome=nome, idade=idade)
    session.add(novo_usuario)
    session.commit()
    session.close()
    return novo_usuario