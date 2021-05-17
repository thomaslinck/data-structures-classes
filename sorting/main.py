from test_suite import test_suite
import time

from commons import create_random_list
from commons import sort_by_function

from tabulate import tabulate

from functions_dictionary import functions


def measure_time_per_function(f, my_list):
    begin = time.perf_counter()
    sort_by_function(f, my_list)
    end = time.perf_counter()
    return end - begin


def create_time_per_function_table():
    times_table = [["List Size"]]
    times_table[0].extend(list(functions.values()))

    for list_size in range(5, 2000, 25):
        table_row = [list_size]
        original_list = create_random_list(list_size)
        for f in functions:
            table_row.append(measure_time_per_function(
                f, original_list.copy()))
        times_table.append(table_row)

    print("\n")
    print(tabulate(times_table, headers="firstrow",
                   tablefmt="github", floatfmt=".10f"))


test_suite()
create_time_per_function_table()
