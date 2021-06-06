import sys
import numpy as np


class Infinite():
    value = 99999999

    @staticmethod
    def is_infinite(other_value):
        return Infinite.value == other_value

    @staticmethod
    def is_not_infinite(other_value):
        return not Infinite.value == other_value


def sublist(input_list, start, end):
    return [input_list[i] for i in range(start, end)]


def merge(sorting_list, first_index, center_index, last_index):
    merged_list = []

    list1 = sublist(sorting_list, first_index, center_index)
    list2 = sublist(sorting_list, center_index + 1, last_index)

    list1.append(Infinite.value)
    list2.append(Infinite.value)

    while Infinite.is_not_infinite(list1[0]) and Infinite.is_not_infinite(list2[0]):
        if list1[0] >= list2[0]:
            element_to_add = list1.pop(0)
        else:
            element_to_add = list2.pop(0)

        merged_list.append(element_to_add)

    return merged_list


def recursion_merge_sort(sorting_list, first_index, last_index):
    if first_index < last_index:
        center_index = int(np.trunc((last_index-first_index)/2))
        updated_list = recursion_merge_sort(
            sorting_list, first_index, center_index)
        updated_list = recursion_merge_sort(
            updated_list, center_index+1, last_index)
        return merge(updated_list, first_index, center_index, last_index)
    else:
        return sorting_list


def merge_sort(sorting_list):
    sys.getrecursionlimit()
    return recursion_merge_sort(sorting_list, 0, len(sorting_list))
