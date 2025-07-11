from storage.interfaces.i_cliente import IClienteStorage

class ClienteStorageMemoria(IClienteStorage):
    def __init__(self):
        self.clientes = {}
        self.proximo_id = 1

    def salvar(self, cliente):
        cliente.id = self.proximo_id
        self.clientes[self.proximo_id] = cliente
        self.proximo_id += 1
        return cliente.id

    def buscar_todos(self):
        return list(self.clientes.values())

    def buscar_por_id(self, id):
        return self.clientes.get(id)

    def atualizar(self, id, novo_cliente):
        if id in self.clientes:
            novo_cliente.id = id
            self.clientes[id] = novo_cliente
            return True
        return False

    def deletar(self, id):
        return self.clientes.pop(id, None) is not None
