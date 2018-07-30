"""Simple script to present a possible way of coding mergesort"""
from sys import argv


def mergesort(list):
    """Uses the mergesort algorythm to sort
    the given list

    Args:
        unsorted list
    returns:
        sorted list """
    result = []
    if len(list) < 20:
        return sorted(list)
    mid = int(len(list) / 2)
    left = msort4(list[:mid])
    right = msort4(list[mid:])
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


if __name__ == '__main__':
    if len(argv) == 2:
        list = list(map(int, argv[1].split(',')))
        main(list)
    else:
        print("Please provide a list!")
