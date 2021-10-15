# author: ShotgunRO

# ---------- [ subject ] ----------
# [Description]
# Given an array of integers numbers sorted in ascending order, find the starting and ending position of several
# given target values. If a target is not found in the array, return [-1, -1]. You must write an algorithm with
# O(logn) runtime complexity for each given target.
# [Input]
# Line 1: two integers n and m(n >= 1, m <= 10^5) -- the length of array and the number of targets.
# Line 2: the all elements in array and split by spaces(for each element x, -2^31 <= x <= 2^31 - 1)
# Line 3 ~ Line m+2: targets
# [Output]
# For each target, print one line containing the starting and ending position split by spaces.

# ---------- [ code ] ----------
def solve(arr, target, l, r):
    if r < 0:
        return [-1, -1]

    # Conquer
    if l == r:
        # leaf node position
        return [r, r] if arr[r] == target else [-1, -1]

    # Divides
    m = (l + r) >> 1
    left = solve(arr, target, l, m) if arr[m] >= target else [-1, -1]
    right = solve(arr, target, m + 1, r) if arr[m + 1] <= target else [-1, -1]

    # Combine
    if left[0] == -1:
        # in this case, left half does not contain target element.
        return right
    else:
        # in this case, left part contains at least one target element.
        return left if right[0] == -1 else [left[0], right[1]]


n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
for i in range(m):
    target = int(input())
    result = solve(arr, target, 0, len(arr) - 1)
    print(result[0], result[1])
