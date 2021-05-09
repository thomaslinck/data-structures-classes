from abstract_queue_manager import abstract_queue_manager
import gc


class linked_queue_node:
    def __init__(self, element, predecessor, successor):
        self.element = element
        self.predecessor = predecessor
        self.successor = successor


class linked_queue_manager(abstract_queue_manager):
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def for_each(self, function):
        iterator = self.inicio
        while iterator is not None:
            function(iterator.element)
            iterator = iterator.successor

    def is_empty(self):
        return True if self.tamanho == 0 else False

    def number_of_elements(self):
        return self.tamanho

    def add_element(self, element):
        new_node = linked_queue_node(element, self.fim, None)
        if self.fim is not None:
            self.fim.successor = new_node
        elif self.inicio is None:
            self.inicio = new_node

        self.fim = new_node
        self.tamanho += 1

    def retrieve_first_element(self):
        if self.is_empty():
            return
        first_element = self.inicio.element
        self.__remove_first_element()
        return first_element

    def __remove_first_element(self):
        second_element = self.inicio.successor
        self.__free(self.inicio)
        self.inicio = second_element
        self.tamanho -= 1

    def __free(self, reference):
        del reference
        gc.collect()
