from commons import swap_elements


def bubble_sort(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-1-i):
            if my_list[j] > my_list[j+1]:
                swap_elements(my_list, j, j+1)
    return my_list
