import requests
import json
from config import BASE_URL


def menu_chamados():
    while True:
        print("\n--- GERENCIAMENTO DE CHAMADOS ---")
        print("1 - Listar chamados")
        print("2 - Criar chamado")
        print("3 - Alterar status")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_chamados()
        elif opcao == "2":
            criar_chamado()
        elif opcao == "3":
            alterar_status_chamado()
        elif opcao == "0":
            break


def listar_chamados():
        try:
            response = requests.get(f"{BASE_URL}/chamados")

            if response.status_code == 200:
                chamados = response.json()

                if not chamados:
                    print("\nNenhum chamado encontrado.")
                    return

                print(f"\n{len(chamados)} chamado(s) encontrado(s):\n")

                for c in chamados:
                    print(f"ID: {c['id']}")
                    print(f"Título: {c['titulo']}")
                    print(f"Descrição: {c['descricao']}")
                    print(f"Usuário ID: {c['usuario_id']}")
                    print(f"Prioridade: {c['prioridade']}")
                    print(f"Status: {c['status']}")
                    print(f"Data de abertura: {c['data_abertura']}")
                    print("-" * 40)

            else:
                print("Erro:", response.json())

        except requests.exceptions.ConnectionError:
            print("\n Não foi possível conectar à API.")


def criar_chamado():
    print("\n--- Criar chamado ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade (Baixa/Média/Alta): ")
    usuario_id = input("ID de Usuário a Atribuir: ")

    dados = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "usuario_id": usuario_id
    }

    response = requests.post(
        f"{BASE_URL}/chamados",
        headers={"Content-Type": "application/json"},
        json=dados
    )

    if response.status_code == 201:
        print("✓ Chamado criado com sucesso")
    else:
        print("Erro:", response.text)


def alterar_status_chamado():
    chamado_id = input("\nID do chamado: ")

    print("\nStatus disponíveis:")
    print("1 - Aberto")
    print("2 - Em Atendimento")
    print("3 - Concluído")

    opcao = input("Escolha o novo status: ")

    status_map = {  
        "1": "Aberto",
        "2": "Em Atendimento",
        "3": "Concluído"
    }

    novo_status = status_map.get(opcao)

    if not novo_status:
        print("Status inválido.")
        return

    dados = {
        "status": novo_status
    }

    response = requests.patch(
        f"{BASE_URL}/chamados/{chamado_id}/status",
        headers={"Content-Type": "application/json"},
        data=json.dumps(dados)
    )

    if response.status_code == 200:
        print("\n✓ Status atualizado com sucesso!")
    else:
        try:
            print("\nErro:", response.json().get("erro"))
        except Exception:
            print("\nErro inesperado ao atualizar status.")
