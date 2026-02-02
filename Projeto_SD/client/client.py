from menu import exibir_menu_principal
from usuarios_client import menu_usuarios
from chamados_client import menu_chamados
from atendimentos_client import menu_atendimentos


def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_usuarios()
        elif opcao == "2":
            menu_chamados()
        elif opcao == "3":
            menu_atendimentos()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
