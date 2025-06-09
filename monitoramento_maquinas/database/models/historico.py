# Model para histórico de status

from sqlalchemy import Column, Integer, String
from monitoramento_maquinas.database.db_config import Base


class Historico(Base):
    __tablename__ = 'historico'

    id = Column(Integer, primary_key=True, autoincrement=True)
    maquina_id = Column(Integer, nullable=False)  # ID da máquina associada
    status = Column(String(20), nullable=False)
    timestamp = Column(String(50), nullable=False)  # Data e hora do registro

    def __init__(self, maquina_id: int, status: str, timestamp: str) -> None:
        self.maquina_id = maquina_id
        self.status = status
        self.timestamp = timestamp

    def __repr__(self):
        return (
            f"Historico(maquina_id={self.maquina_id}, status='{self.status}', "
            f"timestamp='{self.timestamp}')"
        )