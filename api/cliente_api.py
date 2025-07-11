from domain.cliente import Cliente, ClienteContato, TipoContato
from services.cliente_service import ClienteService

class ClienteAPI:
    def __init__(self):
        self.service = ClienteService()

    def menu(self):
        while True:
            print("\n===== CLIENTES =====")
            print("1. Cadastrar cliente")
            print("2. Listar todos")
            print("3. Buscar por ID")
            print("4. Atualizar cliente")
            print("5. Deletar cliente")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar_todos()
            elif opcao == "3":
                self.buscar_por_id()
            elif opcao == "4":
                self.atualizar()
            elif opcao == "5":
                self.deletar()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def cadastrar(self):
        nome = input("Nome: ")
        documento = input("Documento: ")

        contatos = []
        while True:
            print("Tipos de contato:")
            for tipo in TipoContato:
                print(f"{tipo.value} - {tipo.name}")
            tipo_contato = int(input("Tipo de contato: "))
            valor = input("Valor do contato: ")
            contatos.append(ClienteContato(TipoContato(tipo_contato), valor))

            continuar = input("Adicionar outro contato? (s/n): ").lower()
            if continuar != "s":
                break

        cliente = Cliente(0, nome, documento, contatos)
        id = self.service.cadastrar(cliente)
        print(f"Cliente cadastrado com ID {id}")

    def listar_todos(self):
        clientes = self.service.listar_todos()
        for c in clientes:
            print(c)

    def buscar_por_id(self):
        id = int(input("ID do cliente: "))
        cliente = self.service.listar_por_id(id)
        print(cliente if cliente else "Cliente não encontrado.")

    def atualizar(self):
        id = int(input("ID do cliente a atualizar: "))
        nome = input("Novo nome: ")
        documento = input("Novo documento: ")

        contatos = []
        while True:
            print("Tipos de contato:")
            for tipo in TipoContato:
                print(f"{tipo.value} - {tipo.name}")
            tipo_contato = int(input("Tipo de contato: "))
            valor = input("Valor do contato: ")
            contatos.append(ClienteContato(TipoContato(tipo_contato), valor))

            continuar = input("Adicionar outro contato? (s/n): ").lower()
            if continuar != "s":
                break

        novo_cliente = Cliente(0, nome, documento, contatos)
        atualizado = self.service.atualizar(id, novo_cliente)
        print("Atualizado com sucesso!" if atualizado else "Cliente não encontrado.")

    def deletar(self):
        id = int(input("ID do cliente a deletar: "))
        deletado = self.service.deletar(id)
        print("Cliente deletado!" if deletado else "Cliente não encontrado.")
