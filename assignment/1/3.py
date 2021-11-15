# author: ShotgunRO

# ---------- [ subject ] ----------
# Given an integer array, one or more consecutive integers in the array form a sub-array. Find
# the maximum value of the sum of all sub-arrays.
# Please give an algorithm with O(nlogn) complexity.


# ---------- [ code ] ----------
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
    # [left]
    left_sum = left_max_sum = arr[mid]
    for i in range(mid - 1, l, -1):
        left_sum += arr[i]
        if left_sum > left_max_sum:
            left_max_sum = left_sum
    # [right]
    right_sum = right_max_sum = arr[mid + 1]
    for i in range(mid + 2, r):
        right_sum += arr[i]
        if right_sum > right_max_sum:
            right_max_sum = right_sum

    return max(left_solution, right_solution, left_max_sum + right_max_sum)


# ---------- [ test ] ----------
arr = [-84, -87, -78, -16, -94, -36, -87, -93, -50, -22, -63, -28, -91, -60, -64, -27, -41, -27, -73, -37, -12, -69,
       -68, -30, -83, -31, -63, -24, -68, -36, -30, -3, -23, -59, -70, -68, -94, -57, -12, -43, -30, -74, -22, -20, -85,
       -38, -99, -25, -16, -71, -14, -27, -92, -81, -57, -74, -63, -71, -97, -82, -6, -26, -85, -28, -37, -6, -47, -30,
       -14, -58, -25, -96, -83, -46, -15, -68, -35, -65, -44, -51, -88, -9, -77, -79, -89, -85, -4, -52, -55, -100, -33,
       -61, -77, -69, -40, -13, -27, -87, -95, -40]
result = solve(arr, 0, len(arr) - 1)
print(result)
