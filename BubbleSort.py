from random import sample


def random_numbers(range_numbers=10, count=3):
    rand_nums = sample(range(range_numbers), count)
    return rand_nums


def bubble_sort_func(list_numbers):
    counter = 0
    len_numbers = len(list_numbers)
    for j in range(len_numbers - 1):
        for i in range(len_numbers - 1 - j):
            if list_numbers[i] > list_numbers[i + 1]:
                counter += 1
                list_numbers[i], list_numbers[i + 1] = list_numbers[i + 1], list_numbers[i]
                print(counter, list_numbers)


rand_num = []
rand_num = random_numbers(50, 8)
bubble_sort_func(rand_num)
