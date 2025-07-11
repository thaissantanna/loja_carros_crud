from storage.interfaces.i_transacao import ITransacaoStorage
from datetime import datetime

class TransacaoStorageMemoria(ITransacaoStorage):
    def __init__(self):
        self.transacoes = {}
        self.proximo_id = 1

    def salvar(self, transacao):
        transacao.id = self.proximo_id
        self.transacoes[self.proximo_id] = transacao
        self.proximo_id += 1
        return transacao.id

    def buscar_todos(self):
        return list(self.transacoes.values())

    def buscar_por_id(self, id):
        return self.transacoes.get(id)

    def buscar_por_tipo_mes(self, tipo, mes):
        return [
            t for t in self.transacoes.values()
            if t.tipo == tipo and t.data.month == mes
        ]
