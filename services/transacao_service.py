from services.interfaces.i_transacao import ITransacaoService
from storage.memoria.transacao_storage import TransacaoStorageMemoria

class TransacaoService(ITransacaoService):
    def __init__(self):
        self.storage = TransacaoStorageMemoria()

    def cadastrar(self, transacao):
        return self.storage.salvar(transacao)

    def listar_todos(self):
        return self.storage.buscar_todos()

    def listar_por_id(self, id):
        return self.storage.buscar_por_id(id)

    def listar_por_tipo_mes(self, tipo, mes):
        return self.storage.buscar_por_tipo_mes(tipo, mes)
