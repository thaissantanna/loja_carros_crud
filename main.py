from api.carro_api import CarroAPI
from api.cliente_api import ClienteAPI

def main():
    carro_api = CarroAPI()
    cliente_api = ClienteAPI()

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. CRUD Carros")
        print("2. CRUD Clientes")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carro_api.menu()
        elif opcao == "2":
            cliente_api.menu()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
