import random


def create_random_list(list_size):
    return [random.randint(0, 1000) for i in range(list_size)]


def swap_elements(my_list, first_element_index, second_element_index):
    aux = my_list[first_element_index]
    my_list[first_element_index] = my_list[second_element_index]
    my_list[second_element_index] = aux


def sort_by_function(f, my_list, list_size):
    return f(my_list, list_size)
