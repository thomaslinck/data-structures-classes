from abstract_queue_manager import abstract_queue_manager


class sequential_queue_manager(abstract_queue_manager):

    def __init__(self):
        self.queue = []

    def for_each(self, function):
        for e in self.queue:
            function(e)

    def is_empty(self):
        return not self.queue

    def number_of_elements(self):
        return len(self.queue)

    def add_element(self, element):
        self.queue.append(element)

    def retrieve_first_element(self):
        if self.is_empty():
            return
        first_element = self.queue[0]
        self.__remove_first_element()
        return first_element

    def __remove_first_element(self):
        def out_first_element(element): return self.queue.index(element) != 0
        self.queue = list(filter(out_first_element, self.queue))
