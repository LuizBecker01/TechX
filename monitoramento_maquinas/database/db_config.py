# Conexão e inicialização do banco
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from __future__ import annotations
from typing import List

from models.Usuario import Usuario
from models.Historico import Historico
from models.Leitura import Leitura
from models.Maquinas import Maquinas

# Base para nossos modelos
Base = declarative_base()

engine = create_engine('sqlite:///crud_sqlalchemy.db', echo=True)

Base.metadata.create_all(engine)

# Criar uma classe de sessão
Session = sessionmaker(bind=engine)
session = Session()

        