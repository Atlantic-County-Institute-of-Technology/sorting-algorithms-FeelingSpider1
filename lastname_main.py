#puts other files in this one
import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
#This is the code for the beginning of the project.

# EVALUATION
# 1: MENU CHOICES 4/5
# 2: INPUT VALIDATION 3/5
# 3: GENERATE VALUES 5/5
# 4: BUBBLE SORT 5/5
# 5: INSERTION SORT 5/5
# 6: SELECTION SORT 4/5
# 7: PERFORMANCE METRICS 4/5
# COMMENTS MISSING: -5
def main():
    while True:
        while True:
            try:
                selection = int(input("Welcome to the Sortinglibrary67! Please select your preferred type of sort you want to do. 1.Insertionsort 2.Bubblesort 3.Selectionsort 4.Exit "));
            except ValueError:
                print("No No No. 67 dosent approve of this input. now try again.")
                continue
            if selection < 1:
                print("Please type in a number from 1-4.")
                continue
            elif selection > 4:
                print("Please type in a number from 1-4.")
                continue
            else:
                break

# This is the code for selecting insertionsort
        if selection == 1:
            while True:
                try:
                    insertionsort = int(input("You Have Selected Insertionsort... How long do you want your list? Type in any positive number: "))
                    value1 = int(input("Okay now how low do you want the numbers in your list to taper? Type in any positive number: "))
                    value2 = int(input("Okay now how high do you want the numbers in your list until they fade? Type in any positive number: "))
                except ValueError:
                    print("No No No. 67 dosent approve of this input. now try again.")
                    continue
                else:
                    import random
                numbers = [random.randint(value1, value2) for i in range(insertionsort)]
                timer = time.perf_counter()
                print(numbers)
                i_pass = 0
                j_pass = 0

                n = len(numbers)

                for i in range(1, n):
                    insert_index = i
                    current_value = numbers.pop(i)
                    for j in range(i - 1, -1, -1):

                        if numbers[j] > current_value:
                            insert_index = j
                    numbers.insert(insert_index, current_value)
                urtimeisendingtimer = time.perf_counter()
                totaltime = urtimeisendingtimer - timer
                print(numbers)
                print(f"Bruh this sort took a whole {totaltime} seconds")
                break

# This is the code for selecting bubblesort
        if selection == 2:
            while True:
                try:
                    bubblesort = int(input("You Have Selected Bubblesort... How long do you want your list? Type in any positive number: "))
                    value3 = int(input("Okay now how low do you want the numbers in your list to taper? Type in any positive number: "))
                    value4 = int(input("Okay now how high do you want the numbers in your list until they fade? Type in any positive number: "))
                except ValueError:
                    print("No No No. 67 dosent approve of this input. now try again.")
                    continue
                else:
                    import random
                    numbers = [random.randint(value3, value4) for i in range(bubblesort)]
                    timer = time.perf_counter()
                    bubble_sort(numbers)
                    urtimeisendingtimer = time.perf_counter()
                    totaltime = urtimeisendingtimer - timer
                    print(totaltime)
                    print(numbers)
                    print(f"Bruh this sort took a whole {totaltime} seconds")
                    break

# This is the code to choose selectionsort
        if selection == 3:
            while True:
                try:
                    selectionsort = int(input("You Have Selected Selectionsort... How long do you want your list? Type in any positive number: "))
                    value5 = int(input("Okay now how low do you want the numbers in your list to taper? Type in any positive number: "))
                    value6 = int(input("Okay now how high do you want the numbers in your list until they fade? Type in any positive number: "))
                except ValueError:
                    print("No No No. 67 dosent approve of this input. now try again.")
                    continue
                else:
                    import random
                    numbers = [random.randint(value5, value6) for i in range(selectionsort)]
                    timer = time.perf_counter()
                    print(numbers)
                    i_pass = 0
                    j_pass = 0

                    n = len(numbers)

                    for i in range(n - 1):
                        min_index = i
                        for j in range(i + 1, n):

                            if numbers[j] < numbers[min_index]:
                                min_index = j
                        min_value = numbers.pop(min_index)
                        numbers.insert(i, min_value)
                        urtimeisendingtimer = time.perf_counter()
                        totaltime = urtimeisendingtimer - timer
                        print(numbers)
                        print(f"Bruh this sort took a whole {totaltime} seconds")
                        break

# Code to exit the program
        if selection == 4:
            while True:
                try:
                    print("Thank You for sorting with Sortinglibrary67. Have a 67 Day! ")
                except ValueError:
                    print()
                    continue
                else:
                    exit()
                    break


if __name__ == "__main__":
    main()
