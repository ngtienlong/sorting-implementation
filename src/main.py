
from random import randint
from colorama import Fore
import algorithm
from Inteface import Interface
from time import process_time


def algorithm_option(option, array):
    if option == 1:
        return algorithm.bubble_sort(array)
    if option == 2:
        return algorithm.merge_sort(array)
    if option == 3:
        return algorithm.quick_sort(array)


def main():
    user_input = Interface()
    UNSORTED_COLOR = Fore.RED  # red
    SORTED_COLOR = Fore.GREEN  # green

    array_options = int(input(
        "Please choose an array size: \n1. 10\n2. 20\n3. 30\n4. 40\nYour option: "))
    numbers = [randint(10, 99)
               for x in range(user_input.array_size(array_options))]
    print(UNSORTED_COLOR + f"{numbers}")

    algorithm_input = int(input(
        Fore.WHITE + "Please choose an option:\n1. Bubble Sort\n2. Merge Sort\n3. Quick Sort\nYour option: "))
    time_start = process_time()
    sorted_numbers = algorithm_option(algorithm_input, numbers)
    time_end = process_time()
    print(SORTED_COLOR + f"{sorted_numbers}")
    print(Fore.WHITE + f"Time algorithm run: {time_end - time_start}")


if __name__ == "__main__":
    main()
