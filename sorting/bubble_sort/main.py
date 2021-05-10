import random

list_size = 30


def create_random_list():
    return [random.randint(0, 1000) for i in range(list_size)]


def swap_list_item_with_next(list, index):
    aux = list[index]
    list[index] = list[index+1]
    list[index+1] = aux
    return list


numbers = create_random_list()
print(numbers)

changes = True

while changes:
    changes = False

    for i in range(list_size-1):
        if numbers[i] > numbers[i+1]:
            changes = True
            numbers = swap_list_item_with_next(numbers, i)

print(numbers)
