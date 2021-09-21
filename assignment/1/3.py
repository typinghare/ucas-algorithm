# author: ShotgunRO

# ---------- [ subject ] ----------
# Given an integer array, one or more consecutive integers in the array form a sub-array. Find
# the maximum value of the sum of all sub-arrays.
# Please give an algorithm with O(nlogn) complexity.


# ---------- [ code ] ----------
import math


def get_sum(arr: list, l: int, r: int):
    return sum(arr[l:r + 1])


def solve(arr: list, l: int, r: int) -> int:
    # Conquer
    if l == r:
        return arr[l]

    # Divide
    mid = (l + r) >> 1  # middle index
    left_solution = solve(arr, 0, mid)
    right_solution = solve(arr, mid + 1, r)

    # Combine
    # a probability that the sub-array go across division
    left_sum = left_max_sum = arr[mid]
    right_sum = right_max_sum = arr[mid + 1]
    for i in range(mid - 1, l, -1):
        left_sum += arr[i]
        if left_sum > left_max_sum:
            left_max_sum = left_sum
        pass
    for i in range(mid + 2, r):
        right_sum += arr[i]
        if right_sum > right_max_sum:
            right_max_sum = right_sum
        pass

    return max(left_solution, right_solution, left_max_sum + right_max_sum)


# ---------- [ test ] ----------
arr = [-2, 6, -1, 5, 4, -7, 2, 3]
result = solve(arr, 0, len(arr) - 1)
print(result)
