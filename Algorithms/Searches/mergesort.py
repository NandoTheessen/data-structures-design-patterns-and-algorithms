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
    # Since we are talking about a tiny list, we'll simply use sorted
    if len(list) < 20:
        return sorted(list)
    mid = int(len(list) / 2)
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    result += left[i:]  # adds the last straggler from either the right or the
    result += right[j:]  # left list to the results list
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
        List with len of 50 including random ints between 0 and 500"""
    random_list = []
    for i in range(50):
        random_list.append(randint(0, 500))
    return random_list


if __name__ == '__main__':
    list = list(map(int, argv[1].split(','))) if len(
        argv) == 2 else random_list()
    main(list)
