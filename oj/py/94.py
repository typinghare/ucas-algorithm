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
def solve(nums, target):

    pass


n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
for i in range(m):
    target = int(input())
    result = solve(arr, target, 0, len(arr) - 1)
    print(result[0], result[1])
