import random
import numpy as np


class ListInformation():
    def __init__(self, list_to_search, first_index, last_index):
        self.list_to_search = list_to_search

        self.first_index = first_index
        self.last_index = last_index

        self.__update_center()

        self.is_found = False
        self.found_element_index = - 1

    def copy(self):
        return ListInformation(self.list_to_search, self.first_index, self.last_index)

    def update_first_index(self):
        self.first_index = self.center_index + 1
        self.__update_center()

    def update_last_index(self):
        self.last_index = self.center_index - 1
        self.__update_center()

    def found(self):
        self.found_element_index = self.center_index
        self.is_found = True
        return self

    def __update_center(self):
        self.center_index = int(np.trunc((self.last_index-self.first_index)/2))
        self.element_in_center = self.list_to_search[self.center_index]


def create_random_list(list_size):
    return [random.randint(0, 1000) for i in range(list_size)]


def find_element_in_list(element_to_find, list_information):

    if element_to_find == list_information.element_in_center:
        return list_information.found()

    else:
        new_list_information = list_information.copy()

        if element_to_find < list_information.element_in_center:
            new_list_information.update_last_index()

        else:
            new_list_information.update_first_index()

        return find_element_in_list(element_to_find, new_list_information)


def search_for_element_in_list(element, list_to_search):
    list_information = find_element_in_list(
        element, ListInformation(list_to_search, 0, len(list_to_search)-1))

    if list_information.is_found == True:
        return list_information.found_element_index
    else:
        print("Not found")


def main():

    list_to_search = sorted(create_random_list(10))
    index_to_search = random.randint(0, len(list_to_search) - 1)
    element_to_search = list_to_search[index_to_search]

    element_index = search_for_element_in_list(
        element_to_search, list_to_search)

    print(element_index == index_to_search)


main()
