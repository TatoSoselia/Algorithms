"""

<Binary search algorithm>

In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop,
is a search algorithm that finds the position of a target value within a sorted array. Binary search compares
the target value to the middle element of the array.

Worst-case complexity: O(log n)
Best complexity: O(1)
Class: Search algorithm

"""


def binary_search(array, value):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == value:
            return mid
        if guess > value:
            high = mid - 1
        else:
            low = mid + 1
    return None
