import requests
import json
from config import BASE_URL


def menu_atendimentos():
    while True:
        print("\n--- GERENCIAMENTO DE ATENDIMENTOS ---")
        print("1 - Criar atendimento")
        print("2 - Listar por chamado")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_atendimento()
        elif opcao == "2":
            listar_por_chamado()
        elif opcao == "0":
            break


def criar_atendimento():
    descricao = input("Descrição: ")
    chamado_id = input("ID do chamado: ")

    dados = {
        "descricao": descricao,
        "chamado_id": chamado_id
    }

    response = requests.post(
        f"{BASE_URL}/atendimentos",
        headers={"Content-Type": "application/json"},
        data=json.dumps(dados)
    )

    print(response.json())


def listar_por_chamado():
    chamado_id = input("ID do chamado: ")
    response = requests.get(f"{BASE_URL}/atendimentos/chamado/{chamado_id}")
    if response.status_code == 200:
        atendimentos = response.json()

        if not atendimentos:
            print("Nenhum atendimento encontrado.")
            return

        print("\n--- ATENDIMENTOS DO CHAMADO ---")
        for a in atendimentos:
            print(f"""
            ID do atendimento : {a['id']}
            Descrição         : {a['descricao']}
            Data              : {a['data_atendimento']}
            -------------------------------
            """)
    else:
        print(response.json().get("erro", "Erro ao listar atendimentos"))
