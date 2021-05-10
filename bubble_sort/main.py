import random

numbers = []

for i in range(0, 20):
    numbers.append(random.randint(0, 1000))

print(numbers)

changes = True

while changes:
    changes = False

    for i in range(0, 19):
        if numbers[i] > numbers[i+1]:
            changes = True
            aux = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = aux

print(numbers)
