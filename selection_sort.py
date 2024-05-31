"""
<Selection sort>

In computer science, selection sort is an in-place comparison sorting algorithm.
It has an O(n²) time complexity, which makes it inefficient on large lists,
and generally performs worse than the similar insertion sort.

Worst-case complexity: n^2
Best complexity: n^2
Class: Sorting algorithm

"""


def find_smallest_index(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    sorted_array = []
    for i in range(len(arr)):
        smallest_index = find_smallest_index(arr)
        sorted_array.append(arr.pop(smallest_index))
    return sorted_array
