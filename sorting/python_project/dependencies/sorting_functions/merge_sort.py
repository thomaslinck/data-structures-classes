
import numpy as np


class Infinite():
    value = 99999999

    @staticmethod
    def is_infinite(other_value):
        return Infinite.value == other_value


def sublist(input_list, start, end):
    return [input_list[i] for i in range(start, end)]


def merge_lists(list1, list2):
    merged_lists = []

    def next_element_to_list():
        if Infinite.is_infinite(list1[0]) and Infinite.is_infinite(list2[0]):
            return merged_lists
        else:
            if list1[0] >= list2[0]:
                element_to_add = list1.pop(0)
            else:
                element_to_add = list2.pop(0)
            merged_lists.append(element_to_add)
            next_element_to_list()


def merge(sorting_list, first_index, center_index, last_index):
    merged_list = []

    first_list = sublist(sorting_list, first_index, center_index)
    second_list = sublist(sorting_list, center_index + 1, last_index)

    first_list.append(Infinite.value)
    second_list.append(Infinite.value)

    return merge_lists(first_list, second_list)


def recursion_merge_sort(sorting_list, first_index, last_index):
    if first_index < last_index:
        center_index = int(np.trunc((last_index-first_index)/2))
        updated_list = recursion_merge_sort(
            sorting_list, first_index, center_index)
        updated_list = recursion_merge_sort(
            sorting_list, center_index+1, last_index)
        return merge(updated_list, first_index, center_index, last_index)
    else:
        return sorting_list


def merge_sort(sorting_list):
    return recursion_merge_sort(sorting_list, 0, len(sorting_list)-1)
