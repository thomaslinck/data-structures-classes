from commons import create_random_list
from commons import sort_by_function
from tabulate import tabulate
from functions_dictionary import functions


def see_differences(function, initial_list, expected_list, list_size):
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

    list_size = 50

    random_list = create_random_list(list_size)
    sorted_list = sorted(random_list)

    for function in functions:
        if sort_by_function(function, random_list.copy(), list_size) == sorted_list:
            print(f"{functions.get(function)}: OK")
        else:
            print(f"{functions.get(function)}: Erro")
            see_differences(function, random_list.copy(),
                            sorted_list.copy(), list_size)

    print("-----------------------------------------------------------------------")
