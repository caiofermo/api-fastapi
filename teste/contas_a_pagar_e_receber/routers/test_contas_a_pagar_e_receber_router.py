from fastapi.testclient import TestClient
from main import app
from typing import List

client = TestClient(app)

def test_deve_listar_contas_a_pagar_e_receber():
    response = client.get("/contas-a-pagar-e-receber")
    assert response.status_code == 200
    assert response.json() == [
        {'id': 1, 'descricao': 'Conta de luz', 'valor': '150.75', 'tipo': 'pagar'}, 
        {'id': 2, 'descricao': 'Salario', 'valor': '5000.0', 'tipo': 'pagar'}
    ]


def test_deve_criar_conta_a_pagar_ou_receber():
    payload ={
         'descricao': 'Conta de água', 'valor': '190.75', 'tipo': 'pagar'
        }
    
    payload_copy: dict = payload.copy()

    payload_copy["id"] = 3

    response = client.post("/contas-a-pagar-e-receber", json=payload)
    assert response.status_code == 201
    assert response.json() == payload_copy