from abc import ABC, abstractmethod

class ITransacaoStorage(ABC):
    @abstractmethod
    def salvar(self, transacao): pass

    @abstractmethod
    def buscar_todos(self): pass

    @abstractmethod
    def buscar_por_id(self, id): pass

    @abstractmethod
    def buscar_por_tipo_mes(self, tipo, mes): pass
