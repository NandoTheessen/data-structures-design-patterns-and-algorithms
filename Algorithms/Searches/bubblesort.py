from sys import argv
from random import randint

def bubblesort(nums):
    while True:
        changed = False
        for x in range(0, len(nums) -1):
            if nums[x] > nums[x+1]:
                nums[x], nums[x+1] = nums[x+1], nums[x]
                changed = True
        if not changed:
            return nums

def main(list):
    """executes all functions in this script

    Args:
        list given by the user
    """
    print(bubblesort(list))

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