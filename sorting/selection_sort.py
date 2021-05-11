from commons import swap_elements


def selection_sort(my_list, list_size):
    for i in range(list_size):
        maior = 0
        for j in range(list_size-i):
            if my_list[j] > my_list[maior]:
                maior = j
        swap_elements(my_list, maior, j)
    return my_list
