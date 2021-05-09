from abstract_queue_manager import *


class sequential_queue_manager(abstract_queue_manager):

    def __init__(self):
        self.queue = []

    def for_each(self, function):
        for e in self.queue:
            function(e)

    def is_queue_empty(self):
        return not self.queue

    def number_of_elements_in(self):
        return len(self.queue)

    def add_element_to_queue(self, element):
        self.queue.append(element)

    def get_first_element_from_queue(self):
        return self.queue[0] if not self.is_queue_empty() else "none"

    def remove_first_element_from_queue(self):
        def by_first_element(element): return self.queue.index(element) != 0
        self.queue = list(filter(by_first_element, self.queue))
