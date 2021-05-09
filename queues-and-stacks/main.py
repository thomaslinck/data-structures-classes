from queue_manager.queue_manager_factory import queue_manager_factory
from airport.airplane import *
from airport.airport import *


def execute_program():

    possibilities = {
        "1": verifica_se_pista_esta_vazia,
        "2": listar_numero_avioes_na_pista,
        "3": autorizar_decolagem,
        "4": adicionar_aviao_na_fila,
        "5": listar_dados_avioes_na_fila
    }

    lists = {
        "1": "linked",
        "2": "sequential"
    }

    try:
        print("Digite 1 para uma lista encadeada e 2 para uma lista sequencial")
        queue_manager = queue_manager_factory().make(lists.get(input()))
    except:
        print("Não foi possível criar")
        return

    queue_manager.add_element_to_queue(Airplane("ABC", "Teste1", "TAM"))
    queue_manager.add_element_to_queue(Airplane("DEF", "Teste2", "GOL"))

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

        possibilities.get(
            user_input, "Operação não é possível")(queue_manager)


execute_program()

print("Executou")
