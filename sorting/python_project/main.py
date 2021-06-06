import sys
import time
from tabulate import tabulate

from dependencies import create_random_list
from dependencies import sort_by_function
from dependencies import functions


def see_differences(function, initial_list, expected_list):
    actual_list = function(initial_list.copy())
    print(f"\nExpected:\n{expected_list}")
    print(f"Actual:\n{actual_list}")

    print("\nWrong Elements:")
    wrong_elements = [["Index", "Expected", "Actual"]]

    for index in range(len(initial_list)-1):
        if expected_list[index] != actual_list[index]:
            wrong_elements.append(
                [index, expected_list[index], actual_list[index]])

    print(tabulate(wrong_elements, headers="firstrow",
                   tablefmt="github", floatfmt=".10f"))


def test_suite():
    print("-----------------------------------------------------------------------")
    print("Status dos algoritmos:\n")

    list_size = 3

    random_list = create_random_list(list_size)
    sorted_list = sorted(random_list)

    for function in functions:
        if sort_by_function(function, random_list.copy()) == sorted_list:
            print(f"{functions.get(function)}: OK")
        else:
            print(f"{functions.get(function)}: Erro")
            see_differences(function, random_list.copy(),
                            sorted_list.copy())

    print("-----------------------------------------------------------------------")


def create_time_per_function_table():

    def measure_time_per_function(f, my_list):
        begin = time.perf_counter()
        sort_by_function(f, my_list)
        end = time.perf_counter()
        return end - begin

    times_table = [["List Size"]]
    times_table[0].extend(list(functions.values()))

    for list_size in range(1, 3, 1):
        table_row = [list_size]
        original_list = create_random_list(list_size)
        for f in functions:
            table_row.append(measure_time_per_function(
                f, original_list.copy()))
        times_table.append(table_row)

    print("\n")
    print(tabulate(times_table, headers="firstrow",
                   tablefmt="github", floatfmt=".10f"))


sys.setrecursionlimit(2000)
test_suite()
create_time_per_function_table()
