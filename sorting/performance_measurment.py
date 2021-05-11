import time

from commons import create_random_list
from commons import sort_by_function
from tabulate import tabulate
from functions_dictionary import functions


def measure_time_per_function(f, my_list, list_size):
    begin = time.perf_counter()
    sort_by_function(f, my_list, list_size)
    end = time.perf_counter()
    return end - begin


def print_time_per_function(f, my_list, list_size):
    print(
        f"{functions.get(f)}: {measure_time_per_function(f, my_list.copy(), list_size): .10f}")


def print_times_per_functions():
    for list_size in range(5, 2000, 25):
        original_list = create_random_list(list_size)
        print(
            f"\nPerformances das funções: para lista de {list_size} elementos")
        for f in functions:
            print_time_per_function(f, original_list, list_size)


def create_table_for_time_per_function():
    times_table = [["List Size"]]
    times_table[0].extend(list(functions.values()))

    for list_size in range(5, 2000, 25):
        table_row = [list_size]
        original_list = create_random_list(list_size)
        for f in functions:
            table_row.append(measure_time_per_function(
                f, original_list.copy(), list_size))
        times_table.append(table_row)

    print("\n")
    print(tabulate(times_table, headers="firstrow",
                   tablefmt="github", floatfmt=".10f"))
