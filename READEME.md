# 🚗 Projeto CRUD de Carros em Python

Este é um projeto simples para um sistema de **cadastro de carros** usando Python. 
Esse projeto faz parte da mentoria do Rafael Gottardi(Fino).

obs.: *Projeto ainda não finalizado*
----

## 🧠 Objetivo

Modelar a estrutura de um sistema de concessionária de carros com:
- Separação clara por **domínio**, **serviços**, **armazenamento** e **API simulada**
- Interface simples no terminal (CLI)
- Código didático e limpo
- Pronto para ser evoluído com cliente, transações, banco de dados e API real

---

## ⚙️ Funcionalidades já implementadas

✅ Cadastrar carro  
✅ Listar todos os carros  
✅ Buscar carro por ID  
✅ Atualizar dados de um carro  
✅ Deletar carro  

---

## 🗂️ Estrutura do Projeto


```txt
📁 meu_crud/
├── 🟩 main.py # Arquivo principal
│
├── 📁 domain/ # Entidades do sistema
│ └── 🚗 carro.py # Classe Carro + enums
│
├── 📁 services/ # Lógica de negócio
│ ├── 📁 interfaces/
│ │ └── i_carro.py # Interface ICarroService
│ └── carro_service.py # Implementação do serviço
│
├── 📁 storage/ # Camada de persistência (dados)
│ ├── 📁 interfaces/
│ │ └── i_carro.py # Interface ICarroStorage
│ └── 📁 memoria/
│ └── carro_storage.py # Armazenamento em memória
│
└── 📁 api/ # Interface do usuário (simulada via terminal - por enquanto)
    └── carro_api.py
```