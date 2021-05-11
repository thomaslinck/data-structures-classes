from bubble_sort import bubble_sort
from selection_sort import selection_sort


def sort_method(my_list, list_size):
    my_list.sort()
    return my_list


def sorted_function(my_list, list_size):
    return sorted(my_list)


functions = {
    bubble_sort: "Bubble Sort",
    sort_method: "Sort Method",
    sorted_function: "Sorted Function",
    selection_sort: "Selection Sort"
}
