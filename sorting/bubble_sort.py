from commons import swap_elements


def bubble_sort(my_list, list_size):
    for i in range(list_size-1):
        for j in range(list_size-1-i):
            if my_list[j] > my_list[j+1]:
                swap_elements(my_list, j, j+1)
    return my_list
