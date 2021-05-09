from abc import ABC, abstractmethod


class abstract_queue_manager(ABC):

    @abstractmethod
    def for_each(self, function):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def number_of_elements(self):
        pass

    @abstractmethod
    def add_element(self, element):
        pass

    @abstractmethod
    def retrieve_first_element(self):
        pass
