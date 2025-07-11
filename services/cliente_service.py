from services.interfaces.i_cliente import IClienteService
from storage.memoria.cliente_storage import ClienteStorageMemoria

class ClienteService(IClienteService):
    def __init__(self):
        self.storage = ClienteStorageMemoria()

    def cadastrar(self, cliente):
        return self.storage.salvar(cliente)

    def listar_todos(self):
        return self.storage.buscar_todos()

    def listar_por_id(self, id):
        return self.storage.buscar_por_id(id)

    def atualizar(self, id, novo_cliente):
        return self.storage.atualizar(id, novo_cliente)

    def deletar(self, id):
        return self.storage.deletar(id)
