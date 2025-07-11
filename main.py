from api.carro_api import CarroAPI
from api.cliente_api import ClienteAPI
from api.transacao_api import TransacaoAPI

def main():
    carro_api = CarroAPI()
    cliente_api = ClienteAPI()
    transacao_api = TransacaoAPI()

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Carros")
        print("2. Clientes")
        print("3. Transações")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carro_api.menu()
        elif opcao == "2":
            cliente_api.menu()
        elif opcao == "3":
            transacao_api.menu()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
