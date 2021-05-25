
def insertion_sort(sorting_list):

    for index in range(len(sorting_list)):
        index_of_minimum_element = index

        for element_index in range(index + 1, len(sorting_list)):
            if sorting_list[element_index] < sorting_list[index_of_minimum_element]:
                index_of_minimum_element = element_index

        sorting_list[index], sorting_list[index_of_minimum_element] = sorting_list[index_of_minimum_element], sorting_list[index]

    return sorting_list
