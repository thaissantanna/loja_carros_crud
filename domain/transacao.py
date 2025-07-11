from enum import Enum
from datetime import datetime

class TipoTransacao(Enum):
    COMPRA = 0
    VENDA = 1

class Transacao:
    def __init__(self, id: int, tipo: TipoTransacao, carro_id: int, cliente_id: int, valor: float, data: datetime):
        self.id = id
        self.tipo = tipo
        self.carro_id = carro_id
        self.cliente_id = cliente_id
        self.valor = valor
        self.data = data

    def __str__(self):
        return f"ID: {self.id} | Tipo: {self.tipo.name} | Carro ID: {self.carro_id} | Cliente ID: {self.cliente_id} | Valor: R${self.valor:.2f} | Data: {self.data.strftime('%d/%m/%Y')}"
