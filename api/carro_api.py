from domain.carro import *
from services.carro_service import CarroService

class CarroAPI:
    def __init__(self):
        self.service = CarroService()

    def menu(self):
        while True:
            print("\n--- MENU CARROS ---")
            print("1. Cadastrar Carro")
            print("2. Listar todos")
            print("3. Buscar por ID")
            print("4. Atualizar")
            print("5. Deletar")
            print("0. Sair")

            op = input("Escolha: ")
            if op == "1":
                modelo = input("Modelo: ")
                carro = Carro(id=0, marca=MarcaCarro.VW, modelo=modelo, ano_fab=2020,
                              ano_modelo=2021, km=10000, transmissao=TipoTransmissao.MANUAL,
                              valor=50000.0, cor="Prata", chassi="ABC123")
                carro_id = self.service.cadastrar(carro)
                print(f"Carro cadastrado com ID {carro_id}")
            elif op == "2":
                for c in self.service.listar_todos():
                    print(vars(c))
            elif op == "3":
                id = int(input("ID: "))
                carro = self.service.listar_por_id(id)
                print(vars(carro) if carro else "Não encontrado")
            elif op == "4":
                id = int(input("ID para atualizar: "))
                modelo = input("Novo Modelo: ")
                novo = Carro(id=0, marca=MarcaCarro.FORD, modelo=modelo, ano_fab=2022,
                             ano_modelo=2023, km=5000, transmissao=TipoTransmissao.AUTOMATICA,
                             valor=80000.0, cor="Preto", chassi="XYZ789")
                sucesso = self.service.atualizar(id, novo)
                print("Atualizado com sucesso" if sucesso else "ID não encontrado")
            elif op == "5":
                id = int(input("ID: "))
                sucesso = self.service.deletar(id)
                print("Deletado" if sucesso else "Não encontrado")
            elif op == "0":
                break
            else:
                print("Opção inválida")
