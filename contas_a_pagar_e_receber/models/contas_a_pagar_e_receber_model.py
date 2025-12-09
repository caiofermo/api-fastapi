from shared.database import Base
from sqlalchemy import Column, Integer, String, Float


class ContaAPagarReceber(Base):
    __tablename__ = "contas_a_pagar_e_receber"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)  # 'pagar' ou 'receber'
