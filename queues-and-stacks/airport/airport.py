from airplane import print_airplane
from airplane import create_airplane


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
    queue_manager.add_element_to_queue(create_airplane())


def listar_dados_avioes_na_fila(queue_manager):
    queue_manager.for_each(print_airplane)
