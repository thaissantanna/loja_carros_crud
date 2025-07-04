from storage.memoria.carro_storage import CarroStorageMemoria

class CarroService:
    def __init__(self):
        self.storage = CarroStorageMemoria()

    def cadastrar(self, carro):
        return self.storage.cadastrar(carro)

    def listar_todos(self):
        return self.storage.listar_todos()

    def listar_por_id(self, id):
        return self.storage.listar_por_id(id)

    def atualizar(self, id, novo_carro):
        return self.storage.atualizar(id, novo_carro)

    def deletar(self, id):
        return self.storage.deletar(id)
