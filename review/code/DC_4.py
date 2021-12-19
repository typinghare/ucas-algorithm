def solve(arr, target, l, r):
    if len(arr) == 0:
        return (-1, -1)

    # conquer
    if l == r:
        # leaf node position
        return (r, r) if arr[r] == target else (-1, -1)

    # divides
    m = (l + r) >> 1
    left = solve(arr, target, l, m) if arr[m] >= target else (-1, -1)
    right = solve(arr, target, m + 1, r) if arr[m + 1] <= target else (-1, -1)

    # combine
    if left[0] == -1:
        # in this case, left half does not contain target element.
        return right
    else:
        # in this case, left part contains at least one target element.
        return left if right[0] == -1 else (left[0], right[1])


arr = [5, 7, 7, 8, 8, 10]
print(solve(arr, 7, 0, len(arr) - 1))
