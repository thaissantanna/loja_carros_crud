from enum import Enum

class TipoContato(Enum):
    CELULAR = 0
    EMAIL = 1
    WHATSAPP = 2

class ClienteContato:
    def __init__(self, tipo: TipoContato, valor: str):
        self.tipo = tipo
        self.valor = valor

class Cliente:
    def __init__(self, id: int, nome: str, documento: str, contatos: list):
        self.id = id
        self.nome = nome
        self.documento = documento
        self.contatos = contatos  # Lista de ClienteContato

    def __str__(self):
        contatos_str = "\n".join([f"   {c.tipo.name}: {c.valor}" for c in self.contatos])
        return f"ID: {self.id} | Nome: {self.nome} | Documento: {self.documento}\nContatos:\n{contatos_str}"
