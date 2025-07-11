from domain.transacao import Transacao, TipoTransacao
from services.transacao_service import TransacaoService
from datetime import datetime

class TransacaoAPI:
    def __init__(self):
        self.service = TransacaoService()

    def menu(self):
        while True:
            print("\n--- MENU TRANSAÇÕES ---")
            print("1. Registrar transação")
            print("2. Listar todas")
            print("3. Buscar por ID")
            print("4. Filtrar por tipo e mês")
            print("0. Voltar")

            op = input("Escolha: ")
            if op == "1":
                self.registrar()
            elif op == "2":
                self.listar_todas()
            elif op == "3":
                self.buscar_por_id()
            elif op == "4":
                self.filtrar()
            elif op == "0":
                break
            else:
                print("Opção inválida")

    def registrar(self):
        print("Tipos de transação:")
        for t in TipoTransacao:
            print(f"{t.value} - {t.name}")
        tipo = TipoTransacao(int(input("Escolha o tipo: ")))
        carro_id = int(input("ID do carro: "))
        cliente_id = int(input("ID do cliente: "))
        valor = float(input("Valor da transação: "))
        data_str = input("Data (dd/mm/aaaa): ")
        data = datetime.strptime(data_str, "%d/%m/%Y")

        transacao = Transacao(0, tipo, carro_id, cliente_id, valor, data)
        id = self.service.cadastrar(transacao)
        print(f"Transação registrada com ID {id}")

    def listar_todas(self):
        for t in self.service.listar_todos():
            print(t)

    def buscar_por_id(self):
        id = int(input("ID da transação: "))
        t = self.service.listar_por_id(id)
        print(t if t else "Não encontrada.")

    def filtrar(self):
        print("Tipos de transação:")
        for t in TipoTransacao:
            print(f"{t.value} - {t.name}")
        tipo = TipoTransacao(int(input("Escolha o tipo: ")))
        mes = int(input("Informe o número do mês (1-12): "))
        transacoes = self.service.listar_por_tipo_mes(tipo, mes)
        for t in transacoes:
            print(t)
