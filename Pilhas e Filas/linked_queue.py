from abstract_queue_manager import *
import gc


class linked_queue_node:
    def __init__(self, element, predecessor, successor):
        self.element = element
        self.predecessor = predecessor
        self.successor = successor


class descritor:
    def __init__(self, inicio, fim, tamanho):
        self.inicio = inicio
        self.fim = fim
        self.tamanho = tamanho


class linked_queue_manager(abstract_queue_manager):
    def __init__(self):
        self.descritor = descritor(None, None, 0)

    def for_each(self, function):
        iterator = self.descritor.inicio
        while iterator is not None:
            function(iterator.element)
            iterator = iterator.successor

    def is_queue_empty(self):
        return True if self.descritor.tamanho == 0 else False

    def number_of_elements_in(self):
        return self.descritor.tamanho

    def add_element_to_queue(self, element):
        new_node = linked_queue_node(element, self.descritor.fim, None)
        if self.descritor.fim is not None:
            self.descritor.fim.successor = new_node
        elif self.descritor.inicio is None:
            self.descritor.inicio = new_node

        self.descritor.fim = new_node
        self.descritor.tamanho += 1

    def get_first_element_from_queue(self):
        return self.descritor.inicio.element if not self.is_queue_empty() else "none"

    def remove_first_element_from_queue(self):
        second_element = self.descritor.inicio.successor
        self.__free(self.descritor.inicio)
        self.descritor.inicio = second_element
        self.descritor.tamanho -= 1

    def __free(self, reference):
        del reference
        gc.collect()
