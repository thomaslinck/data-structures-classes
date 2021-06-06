import random
import numpy as np


class ListInformation():
    def __init__(self, list_to_search, first_index, last_index):
        self.list_to_search = list_to_search

        self.first_index = first_index
        self.first_element = list_to_search[first_index]
        self.last_index = last_index
        self.last_element = list_to_search[last_index]

        self.__update_center()

        self.is_found = False
        self.found_element_index = - 1

    def update_first(self):
        self.first_index = self.center_index + 1
        self.first_element = self.list_to_search[self.first_index]
        self.__update_center()

    def update_last(self):
        self.last_index = self.center_index - 1
        self.last_element = self.list_to_search[self.last_index]
        self.__update_center()

    def found(self, index):
        self.found_element_index = index
        self.is_found = True
        return self

    def __update_center(self):
        self.center_index = int(np.trunc((self.last_index-self.first_index)/2))
        self.element_in_center = self.list_to_search[self.center_index]


def create_random_list(list_size):
    return [random.randint(0, 1000) for i in range(list_size)]


def find_element_in_list(element_to_find, list_information):

    if element_to_find == list_information.element_in_center:
        return list_information.found(list_information.center_index)

    elif element_to_find == list_information.first_element:
        return list_information.found(list_information.first_index)

    elif element_to_find == list_information.first_element:
        return list_information.found(list_information.last_index)

    else:
        if element_to_find < list_information.element_in_center:
            list_information.update_last()

        else:
            list_information.update_first()

        return find_element_in_list(element_to_find, list_information)


def search_for_element_in_list(element, list_to_search):
    return find_element_in_list(
        element, ListInformation(list_to_search, 0, len(list_to_search)-1)).found_element_index


def main():

    list_to_search = sorted(create_random_list(100))
    index_to_search = random.randint(0, len(list_to_search) - 1)
    element_to_search = list_to_search[index_to_search]

    element_index = search_for_element_in_list(
        element_to_search, list_to_search)

    print(element_index == index_to_search)


main()
