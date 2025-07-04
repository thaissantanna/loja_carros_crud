from abc import ABC, abstractmethod

class ICarroService(ABC):
    @abstractmethod
    def cadastrar(self, carro): pass

    @abstractmethod
    def listar_todos(self): pass

    @abstractmethod
    def listar_por_id(self, id): pass

    @abstractmethod
    def atualizar(self, id, novo_carro): pass

    @abstractmethod
    def deletar(self, id): pass
