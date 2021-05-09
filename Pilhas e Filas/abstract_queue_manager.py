from __future__ import annotations
from abc import ABC, abstractmethod


class abstract_queue_manager(ABC):

    @abstractmethod
    def for_each(self, function):
        pass

    @abstractmethod
    def is_queue_empty(self, queue):
        pass

    @abstractmethod
    def number_of_elements_in(self, queue):
        pass

    @abstractmethod
    def add_element_to_queue(self, element, queue):
        pass

    @abstractmethod
    def get_first_element_from_queue(self, queue):
        pass

    @abstractmethod
    def remove_first_element_from_queue(self, queue):
        pass


# class abstract_queue_iterator(ABC):

#     def __init__(self, queue):
#         self.queue = queue

#     @abstractmethod
#     def get_current_element(self):
#         pass

#     @abstractmethod
#     def get_previous_element(self):
#         pass

#     @abstractmethod
#     def get_next_element(self):
#         pass

#     @abstractmethod
#     def has_next_element(self):
#         pass

#     @abstractmethod
#     def go_to_last_element(self):
#         pass

#     @abstractmethod
#     def go_to_next_element(self):
#         pass
