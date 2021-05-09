
from airplane_definition import *
from queue_functions import *


def print_all_elements_in_queue(queue):
    for element in queue:
        print_airplane(element)


def test_execution():
    pista_de_decolagem = []

    print(number_of_elements_in(pista_de_decolagem))
    print(is_queue_empty(pista_de_decolagem))

    pista_de_decolagem = add_element_to_queue(
        Airplane("a", "b", "c"), pista_de_decolagem)

    pista_de_decolagem = add_element_to_queue(
        Airplane("d", "e", "f"), pista_de_decolagem)

    pista_de_decolagem = add_element_to_queue(
        Airplane("g", "h", "i"), pista_de_decolagem)

    print_all_elements_in_queue(pista_de_decolagem)

    print(number_of_elements_in(pista_de_decolagem))
    print(is_queue_empty(pista_de_decolagem))

    print_airplane(get_first_element_from_queue(pista_de_decolagem))
    pista_de_decolagem = remove_first_element_from_queue(
        pista_de_decolagem)

    print(number_of_elements_in(pista_de_decolagem))
    print_airplane(get_first_element_from_queue(pista_de_decolagem))


def execute_program():

    print("Digite o número da operação desejada:")
    print("1 - Verificar se a pista de decolagem está vazia")
    print("2 - Listar a quantidade de aviões aguardando na pista de decolagem")
    print("3 - Autorizar a decolagem do primeiro avião da fila")
    print("4 - Adicionar um avião à pista de decolagem")
    print("5 - Listar os dados de todos os aviões que estão na pista de decolagem")


test_execution()

execute_program()

print("Executou")
