import random

def bubble_sort(numbers):
    i_pass = 0
    j_pass = 0

    for i in range(len(numbers)):
        i_pass += 1
        for j in range(len(numbers) - i - 1):
            j_pass += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(f"Passes with i = {i_pass} | Passes with j = {j_pass}")
    print(numbers)