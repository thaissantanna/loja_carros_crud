from abc import ABC, abstractmethod

class IClienteStorage(ABC):
    @abstractmethod
    def salvar(self, cliente): pass

    @abstractmethod
    def buscar_todos(self): pass

    @abstractmethod
    def buscar_por_id(self, id): pass

    @abstractmethod
    def atualizar(self, id, novo_cliente): pass

    @abstractmethod
    def deletar(self, id): pass
