from __future__ import annotations
from abc import ABC, abstractmethod


class abstract_queue_manager(ABC):

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

    @abstractmethod
    def create_queue(self):
        pass
