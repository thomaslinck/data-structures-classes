
from airplane_definition import *
from queue_functions import *


def verifica_se_pista_esta_vazia(pista_de_decolagem):
    print("Pista está vazia" if is_queue_empty(
        pista_de_decolagem) else "Pista não está vazia")
    return pista_de_decolagem


def listar_numero_avioes_na_pista(pista_de_decolagem):
    print(number_of_elements_in(pista_de_decolagem))
    return pista_de_decolagem


def autorizar_decolagem(pista_de_decolagem):
    if is_queue_empty(pista_de_decolagem):
        print("Não há aviões na pista")
        return pista_de_decolagem

    print("A decolagem do seguinte avião for autorizada:")
    print_airplane(get_first_element_from_queue(pista_de_decolagem))
    return remove_first_element_from_queue(pista_de_decolagem)


def adicionar_aviao_na_fila(pista_de_decolagem):
    return add_element_to_queue(create_new_airplane(), pista_de_decolagem)


def listar_dados_avioes_na_fila(pista_de_decolagem):
    for aviao in pista_de_decolagem:
        print_airplane(aviao)
    return pista_de_decolagem


def execute_program():

    possibilities = {
        "1": verifica_se_pista_esta_vazia,
        "2": listar_numero_avioes_na_pista,
        "3": autorizar_decolagem,
        "4": adicionar_aviao_na_fila,
        "5": listar_dados_avioes_na_fila
    }

    pista_de_decolagem = []

    while True:
        print("\nDigite o número da operação desejada:")
        print("1 - Verificar se a pista de decolagem está vazia")
        print("2 - Listar a quantidade de aviões aguardando na pista de decolagem")
        print("3 - Autorizar a decolagem do primeiro avião da fila")
        print("4 - Adicionar um avião à pista de decolagem")
        print("5 - Listar os dados de todos os aviões que estão na pista de decolagem")
        print("6 - Sair")

        user_input = input()

        if user_input == "6":
            break

        operation = possibilities.get(user_input, "Operação não é possível")
        pista_de_decolagem = operation(pista_de_decolagem)


execute_program()

print("Executou")
