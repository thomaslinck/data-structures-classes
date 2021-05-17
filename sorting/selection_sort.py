from commons import swap_elements


def selection_sort(my_list):
    for i in range(len(my_list)):
        maior = 0
        for j in range(len(my_list)-i):
            if my_list[j] > my_list[maior]:
                maior = j
        swap_elements(my_list, maior, j)
    return my_list
