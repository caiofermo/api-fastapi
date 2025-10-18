from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List

router = APIRouter(prefix="/contas-a-pagar-e-receber")

class ContaPagarReceberResponseModel(BaseModel):
    id : int
    descricao : str
    valor : Decimal
    tipo : str # 'pagar' ou 'receber'

class ContaPagarReceberCreateModel(BaseModel):
    descricao : str
    valor : Decimal
    tipo : str # 'pagar' ou 'receber'


@router.get("/", response_model=List[ContaPagarReceberResponseModel])
#Metodo listar contas a pagar e receber
def listar_contas_a_pagar_e_receber():
    return [
        ContaPagarReceberResponseModel(
            id=1, 
            descricao="Conta de luz", 
            valor=150.75, 
            tipo="pagar"
        ),
        ContaPagarReceberResponseModel(
            id=2, 
            descricao="Salario", 
            valor=5000.00, 
            tipo="pagar"
        ),
    ]

@router.post("/", response_model = ContaPagarReceberResponseModel, status_code=201) 
#Metódo de criar conta a pagar ou receber
def criar_conta_a_pagar_ou_receber(conta: ContaPagarReceberCreateModel):
    return ContaPagarReceberResponseModel(
        id=3, 
        descricao=conta.descricao, 
        valor=conta.valor, 
        tipo=conta.tipo
        )
    