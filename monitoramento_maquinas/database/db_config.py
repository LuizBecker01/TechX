from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base para nossos modelos
Base = declarative_base()

engine = create_engine('sqlite:///tx_sqlalchemy.db', echo=True)

# Criar uma classe de sessão
Session = sessionmaker(bind=engine)
session = Session()

# Imports dos modelos
from models.Usuario import Usuario
from models.Maquinas import Maquinas
from models.Leitura import Leitura
from models.Historico import Historico

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)