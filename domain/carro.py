from enum import Enum

class MarcaCarro(Enum):
    VW = 0
    GM = 1
    FORD = 2
    TOYOTA = 3
    HONDA = 4

class TipoTransmissao(Enum):
    MANUAL = 0
    AUTOMATICA = 1
    AUTOMATIZADA = 2
    CVT = 3
    DSG = 4

class Carro:
    def __init__(self, id, marca, modelo, ano_fab, ano_modelo, km, transmissao, valor, cor, chassi):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano_fab = ano_fab
        self.ano_modelo = ano_modelo
        self.km = km
        self.transmissao = transmissao
        self.valor = valor
        self.cor = cor
        self.chassi = chassi
