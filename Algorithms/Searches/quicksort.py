from sys import argv
from random import randint

def quicksort(nums):
    if len(nums) < 2:
        return nums
    
    pivot = nums[-1]
    left = []
    right = []
    for num in nums:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quicksort(left), pivot, quicksort(right)


def main(list):
    """executes all functions in this script

    Args:
        list given by the user
    """
    print(list)
    print(quicksort(list))

def random_list():
    """Random List generator
    Returns:
        List with len of 500 including random ints between 0 and 3000"""
    random_list = []
    for i in range(500):
        random_list.append(randint(0, 3000))
    return random_list

if __name__ == '__main__':
    list = list(map(int, argv[1].split(','))) if len(
        argv) == 2 else random_list()
    main(list)