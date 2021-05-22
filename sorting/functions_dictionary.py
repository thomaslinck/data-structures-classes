from sorting_functions.bubble_sort import bubble_sort
from sorting_functions.selection_sort import selection_sort
from sorting_functions.insertion_sort import insertion_sort


def sort_method(my_list):
    my_list.sort()
    return my_list


def sorted_function(my_list):
    return sorted(my_list)


functions = {
    bubble_sort: "Bubble Sort",
    sort_method: "Sort Method",
    sorted_function: "Sorted Function",
    selection_sort: "Selection Sort",
    insertion_sort: "Insertion Sort"
}
