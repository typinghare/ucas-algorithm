def solve(arr, l, r) -> int:
    # conquer
    if l == r:
        return arr[l]

    # divide
    mid = (l + r) >> 1
    left = solve(arr, l, mid)
    right = solve(arr, mid + 1, r)

    # combine
    # a possibility that the sub-array go across division
    left_sum = left_max_sum = arr[mid]
    for i in range(mid - 1, l - 1, -1):
        left_sum += arr[i]
        if left_sum > left_max_sum:
            left_max_sum = left_sum

    right_sum = right_max_sum = arr[mid + 1]
    for i in range(mid + 2, r + 1):
        right_sum += arr[i]
        if right_sum > right_max_sum:
            right_max_sum = right_sum

    return max(left, right, left_max_sum + right_max_sum)


arr = [5, 4, -1, 7, 8]
print(solve(arr, 0, len(arr) - 1))
