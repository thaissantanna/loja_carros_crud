class CarroStorageMemoria:
    def __init__(self):
        self._carros = {}
        self._proximo_id = 1

    def cadastrar(self, carro):
        carro.id = self._proximo_id
        self._carros[carro.id] = carro
        self._proximo_id += 1
        return carro.id

    def listar_todos(self):
        return list(self._carros.values())

    def listar_por_id(self, id):
        return self._carros.get(id)

    def atualizar(self, id, novo_carro):
        if id in self._carros:
            novo_carro.id = id
            self._carros[id] = novo_carro
            return True
        return False

    def deletar(self, id):
        return self._carros.pop(id, None) is not None
