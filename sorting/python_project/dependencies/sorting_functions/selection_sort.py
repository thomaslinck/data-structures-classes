def selection_sort(sorting_list):
    for i in range(len(sorting_list)):
        maior = 0
        for j in range(len(sorting_list)-i):
            if sorting_list[j] > sorting_list[maior]:
                maior = j
        sorting_list[maior], sorting_list[j] = sorting_list[j], sorting_list[maior]
    return sorting_list
