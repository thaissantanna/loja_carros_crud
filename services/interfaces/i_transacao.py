from abc import ABC, abstractmethod

class ITransacaoService(ABC):
    @abstractmethod
    def cadastrar(self, transacao): pass

    @abstractmethod
    def listar_todos(self): pass

    @abstractmethod
    def listar_por_id(self, id): pass

    @abstractmethod
    def listar_por_tipo_mes(self, tipo, mes): pass
