 # Model para dados simulados (temperatura, etc.)
 
from sqlalchemy import Column, Integer
from monitoramento_maquinas.database.db_config import Base


class Leitura(Base):
    __tablename__ = 'leituras'

    id = Column(Integer, primary_key=True, autoincrement=True)
    maquina_id = Column(Integer, nullable=False)  # ID da máquina associada
    temperatura = Column(Integer, nullable=False)
    umidade = Column(Integer, nullable=False)
    pressao = Column(Integer, nullable=False)

    def __init__(self, maquina_id: int, temperatura: int, umidade: int, pressao: int) -> None:
        self.maquina_id = maquina_id
        self.temperatura = temperatura
        self.umidade = umidade
        self.pressao = pressao

    def __repr__(self):
        return (
            f"Leitura(maquina_id={self.maquina_id}, temperatura={self.temperatura}, "
            f"umidade={self.umidade}, pressao={self.pressao})"
        )