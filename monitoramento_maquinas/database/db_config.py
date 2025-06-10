# Conexão e inicialização do banco
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from __future__ import annotations

from models.Usuario import Usuario

# Base para nossos modelos
Base = declarative_base()

engine = create_engine('sqlite:///tx_sqlalchemy.db', echo=True)

Base.metadata.create_all(engine)

# Criar uma classe de sessão
Session = sessionmaker(bind=engine)
session = Session()

        