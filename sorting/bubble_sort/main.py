import random
import time

list_size = 30


def create_random_list():
    return [random.randint(0, 1000) for i in range(list_size)]


def bubble_sort(input_list):
    for i in range(list_size-1):
        for j in range(list_size-1-i):
            if input_list[j] > input_list[j+1]:
                aux = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = aux
    return input_list


original_list = create_random_list()
print(original_list)
list_copy = original_list.copy()

begin = time.perf_counter()
bubble_sorted_list = bubble_sort(list_copy)
end = time.perf_counter()

print(bubble_sorted_list)
print(f"Performance Bubble Sort {end-begin: 0.10f}\n")

begin = time.perf_counter()
sorted_list = sorted(original_list)
end = time.perf_counter()

print(sorted_list)
print(f"Performance Sorted function {end-begin: 0.10f}\n")

print(original_list)

begin = time.perf_counter()
original_list.sort()
end = time.perf_counter()

print(original_list)
print(f"Performance Sort Method {end-begin: 0.10f}\n")
