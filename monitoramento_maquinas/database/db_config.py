# Conexão e inicialização do banco
from sqlalchemy import create_engine ,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

def criar_usuario(nome: str , idade: int):
    session = Session()
    novo_usuario = Usuario(nome=nome, idade=idade)
    session.add(novo_usuario)
    session.commit()
    session.close()
    return novo_usuario

#base de banco de dados

# from __future__ import annotations
# from typing import List

# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship

# Base = declarative_base()

# class Usuario(Base):

#     __tablename__ = 'usuario'
#     id : Mapped[int] = mapped_column(primary_key=True)
#     nome = Column(String(100), nullable = False)
#     cpf = Column(String(11), nullable = False)
#     placas: Mapped[List["Carro"]] = relationship(back_populates="usuario")

# class Carro(Base):

#     __tablename__ = 'carro'
#     id : Mapped[int]= mapped_column(primary_key=True)
#     placa = Column(String(8), nullable = False)
#     marca = Column(String(50), nullable = False)
#     modelo = Column(String(50), nullable = False)
#     ano = Column(Integer, nullable = False)
#     num_portas = Column(Integer, nullable = False)
#     id_proprietario: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
#     proprietario: Mapped[List["Usuario"]] = relationship(back_populates="carro")

# class Caminhao(Base):

#     __tablename__ = 'caminhao'
#     id : Mapped[int]= mapped_column(primary_key=True)
#     placa = Column(String(8), nullable = False)
#     marca = Column(String(50), nullable = False)
#     modelo = Column(String(50), nullable = False)
#     ano = Column(Integer, nullable = False)
#     capacidade_carga = Column(Integer, nullable = False)
#     id_proprietario: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
#     proprietario: Mapped[List["Usuario"]] = relationship(back_populates="caminhao")

# class Moto(Base):

#     __tablename__ = 'moto'
#     id : Mapped[int]= mapped_column(primary_key=True)
#     placa = Column(String(8), nullable = False)
#     marca = Column(String(50), nullable = False)
#     modelo = Column(String(50), nullable = False)
#     ano = Column(Integer, nullable = False)
#     cilindrada = Column(Integer, nullable = False)
#     id_proprietario: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
#     proprietario: Mapped[List["Usuario"]] = relationship(back_populates="moto")