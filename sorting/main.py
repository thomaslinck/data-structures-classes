import random
import time
from tabulate import tabulate

list_size = 5


def create_random_list():
    return [random.randint(0, 1000) for i in range(list_size)]


def swap_elements(my_list, first_element_index, second_element_index):
    aux = my_list[first_element_index]
    my_list[first_element_index] = my_list[second_element_index]
    my_list[second_element_index] = aux


def bubble_sort(my_list):
    for i in range(list_size-1):
        for j in range(list_size-1-i):
            if my_list[j] > my_list[j+1]:
                swap_elements(my_list, j, j+1)
    return my_list


def sort_method(my_list):
    my_list.sort()
    return my_list


def sorted_function(my_list):
    return sorted(my_list)


def selection_sort(my_list):
    for i in range(list_size):
        maior = 0
        for j in range(list_size-i):
            if my_list[j] > my_list[maior]:
                maior = j
        swap_elements(my_list, maior, j)
    return my_list


functions = {
    bubble_sort: "Bubble Sort",
    sort_method: "Sort Method",
    sorted_function: "Sorted Function",
    selection_sort: "Selection Sort"
}


def sort_by_function(f, my_list):
    return f(my_list)


def measure_time_for_function(f, my_list):
    begin = time.perf_counter()
    sort_by_function(f, my_list)
    end = time.perf_counter()
    return end - begin


def print_time_per_function(f, my_list):
    print(
        f"{functions.get(f)}: {measure_time_for_function(f, my_list.copy()): .10f}")


def create_table_for_time_per_function():
    times_table = [["List Size"]]
    times_table[0].extend(list(functions.values()))

    for list_size in range(5, 2000, 25):
        table_row = [list_size]
        original_list = create_random_list()
        for f in functions:
            table_row.append(measure_time_for_function(
                f, original_list.copy()))
        times_table.append(table_row)

    print("\n")
    print(tabulate(times_table, headers="firstrow",
                   tablefmt="github", floatfmt=".10f"))


def see_differences(function, initial_list, expected_list):
    actual_list = function(initial_list.copy())
    print(f"\nExpected:\n{expected_list}")
    print(f"Actual:\n{actual_list}")

    print("\nWrong Elements:")
    wrong_elements = [["Index", "Expected", "Actual"]]

    for index in range(list_size-1):
        if expected_list[index] != actual_list[index]:
            wrong_elements.append(
                [index, expected_list[index], actual_list[index]])

    print(tabulate(wrong_elements, headers="firstrow",
                   tablefmt="github", floatfmt=".10f"))


def test_suite():
    print("-----------------------------------------------------------------------")
    print("Status dos algoritmos:\n")

    random_list = create_random_list()
    sorted_list = sorted(random_list)

    for function in functions:
        if sort_by_function(function, random_list.copy()) == sorted_list:
            print(f"{functions.get(function)}: OK")
        else:
            print(f"{functions.get(function)}: Erro")
            see_differences(function, random_list.copy(), sorted_list.copy())

    print("-----------------------------------------------------------------------")


test_suite()


for list_size in range(5, 2000, 25):
    original_list = create_random_list()
    print(f"\nPerformances das funções: para lista de {list_size} elementos")
    for f in functions:
        print_time_per_function(f, original_list)

create_table_for_time_per_function()
