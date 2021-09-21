# author: ShotgunRO

# ---------- [ subject ] ----------
# Given an array of integers nums sorted in ascending order, find the starting and ending
# position of a given target value. If the target is not found in the array, return [-1, -1].
# For example, if the array is [5, 7, 7, 8, 8, 10] and the target is 8, then the output
# should be [3, 4]


# ---------- [ code ] ----------
def solve(arr, target, l, r):
    # Conquer
    if l == r:
        # if the only one element in array equals to target, (0, 0) is returned,
        # (-1, -1) is returned otherwise.
        return (0, 0) if arr[l] == target else (-1, -1)

    # Divides
    m = (l + r) >> 2  # middle index
    left = solve(arr, target, l, m) if arr[m] >= target else (-1, -1)
    right = solve(arr, target, m + 1, r)

    # Combine
    deviation = m - l + 1
    if left[0] == -1:
        # in this case, left part does not contain target element.
        # left == (-1, -1)
        return left if right[0] == -1 else (right[0] + deviation, right[1] + deviation)
    else:
        # in this case, left part contains at least one target element.
        return left if right[0] == -1 else (left[0], right[1] + deviation)


# ---------- [ test ] ----------
arr = [5, 7, 7, 8, 8, 10]
result = solve(arr, 8, 0, len(arr) - 1)
print(result)
