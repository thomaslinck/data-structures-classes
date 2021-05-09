from queue_manager_factory import *
from airplane_definition import *


def verifica_se_pista_esta_vazia(queue_manager):
    print("Pista está vazia" if queue_manager.is_queue_empty()
          else "Pista não está vazia")


def listar_numero_avioes_na_pista(queue_manager):
    print(queue_manager.number_of_elements_in())


def autorizar_decolagem(queue_manager):
    if queue_manager.is_queue_empty():
        print("Não há aviões na pista")
        return

    print("A decolagem do seguinte avião for autorizada:")
    print_airplane(queue_manager.get_first_element_from_queue())
    queue_manager.remove_first_element_from_queue()


def adicionar_aviao_na_fila(queue_manager):
    queue_manager.add_element_to_queue(create_new_airplane())


def listar_dados_avioes_na_fila(queue_manager):
    for aviao in queue_manager.get_queue():
        print_airplane(aviao)


def execute_program():

    possibilities = {
        "1": verifica_se_pista_esta_vazia,
        "2": listar_numero_avioes_na_pista,
        "3": autorizar_decolagem,
        "4": adicionar_aviao_na_fila,
        "5": listar_dados_avioes_na_fila
    }

    queue_manager = queue_manager_factory().make("sequential")
    queue_manager.create_queue()

    # queue_manager.add_element_to_queue(Airplane("ABC", "Teste1", "TAM"))
    # queue_manager.add_element_to_queue(Airplane("DEF", "Teste2", "GOL"))

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
