"""Simple script to present a possible way of coding mergesort"""
from sys import argv
from random import randint


def mergesort(list):
    """Uses the mergesort algorythm to sort
    the given list

    Args:
        unsorted list
    returns:
        sorted list """
    result = []
    # Since we are talking about a tiny list, we'll simply use sorted which
    # will be faster
    if len(list) < 20:
        return sorted(list)
    mid = int(len(list) / 2)
    left = mergesort(list[:mid])  # Splitting the array in half
    right = mergesort(list[mid:])  # continuusly until we are left with
    # subarrays of length 1
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    return result


def main(list):
    """executes all functions in this script

    Args:
        list given by the user
    """
    print(mergesort(list))


def random_list():
    """Random List generator
    Returns:
        List with len of 500 including random ints between 0 and 500"""
    random_list = []
    for i in range(500):
        random_list.append(randint(0, 3000))
    return random_list


if __name__ == '__main__':
    list = list(map(int, argv[1].split(','))) if len(
        argv) == 2 else random_list()
    main(list)
