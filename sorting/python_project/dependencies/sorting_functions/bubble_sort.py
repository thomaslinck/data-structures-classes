
def bubble_sort(sorting_list):
    for i in range(len(sorting_list)-1):
        for j in range(len(sorting_list)-1-i):
            if sorting_list[j] > sorting_list[j+1]:
                sorting_list[j], sorting_list[j +
                                              1] = sorting_list[j+1], sorting_list[j]

    return sorting_list
