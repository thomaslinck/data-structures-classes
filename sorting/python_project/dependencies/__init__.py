import random

from .sorting_functions import bubble_sort
from .sorting_functions import sort_method
from .sorting_functions import sorted_function
from .sorting_functions import selection_sort
from .sorting_functions import insertion_sort

functions = {
    bubble_sort.bubble_sort: "Bubble Sort",
    sort_method.sort_method: "Sort Method",
    sorted_function.sorted_function: "Sorted Function",
    selection_sort.selection_sort: "Selection Sort",
    insertion_sort.insertion_sort: "Insertion Sort"
}


def create_random_list(list_size):
    return [random.randint(0, 1000) for i in range(list_size)]


def sort_by_function(f, my_list):
    return f(my_list)
