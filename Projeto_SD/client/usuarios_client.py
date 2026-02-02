import requests
import json
from config import BASE_URL


def menu_usuarios():
    while True:
        print("\n--- GERENCIAMENTO DE USUÁRIOS ---")
        print("1 - Listar usuários")
        print("2 - Buscar usuário por ID")
        print("3 - Criar usuário")
        print("4 - Atualizar usuário")
        print("5 - Deletar usuário")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_usuarios()
        elif opcao == "2":
            buscar_usuario()
        elif opcao == "3":
            criar_usuario()
        elif opcao == "4":
            atualizar_usuario()
        elif opcao == "5":
            deletar_usuario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def listar_usuarios():
    response = requests.get(f"{BASE_URL}/usuarios")

    if response.status_code == 200:
        usuarios = response.json()

        if not usuarios:
            print("\nNenhum usuário cadastrado.")
            return

        for u in usuarios:
            print("-" * 40)
            print(f"ID: {u['id']}")
            print(f"Nome: {u['nome']}")
            print(f"Email: {u['email']}")
            print(f"Setor: {u['setor']}")
    else:
        print("Erro:", response.json())


def buscar_usuario():
    usuario_id = input("ID do usuário: ")
    response = requests.get(f"{BASE_URL}/usuarios/{usuario_id}")

    if response.status_code == 200:
        u = response.json()
        print("\nUsuário encontrado:")
        print(f"ID: {u['id']}")
        print(f"Nome: {u['nome']}")
        print(f"Email: {u['email']}")
        print(f"Setor: {u['setor']}")
    else:
        print("Erro:", response.json())


def criar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    setor = input("Setor: ")

    dados = {
        "nome": nome,
        "email": email,
        "setor": setor
    }

    response = requests.post(
        f"{BASE_URL}/usuarios",
        headers={"Content-Type": "application/json"},
        data=json.dumps(dados)
    )

    if response.status_code == 201:
        print("✓ Usuário criado com sucesso")
    else:
        print("Erro:", response.json())


def atualizar_usuario():
    usuario_id = input("ID do usuário: ")
    nome = input("Novo nome: ")
    email = input("Novo email: ")
    setor = input("Novo setor: ")

    dados = {
        "nome": nome,
        "email": email,
        "setor": setor
    }

    response = requests.put(
        f"{BASE_URL}/usuarios/{usuario_id}",
        headers={"Content-Type": "application/json"},
        data=json.dumps(dados)
    )

    print(response.json())


def deletar_usuario():
    usuario_id = input("ID do usuário: ")

    response = requests.delete(f"{BASE_URL}/usuarios/{usuario_id}")

    if response.status_code in (200, 204):
        print("✓ Usuário removido com sucesso")
    elif response.status_code == 404:
        print("Usuário não encontrado")
    else:
        print("Erro:", response.text)
