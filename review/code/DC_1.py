def solve(arr, low, high, k):
    if k == high - low + 1:
        return min(arr[low:high + 1])
    # if low == high:
    #     return arr[low]

    # partition
    pivot = arr[high]  # pivot can be any element in arr[low:high+1]

    pi = low  # partition index
    # elements in left part are less than pivot, while elements in right part are larger than or equal to pivot

    for i in range(low, high):
        if arr[i] < pivot:
            # swap arr[pi] and arr[i]
            arr[pi], arr[i] = arr[i], arr[pi]
            pi += 1

    # swap arr[pi] and arr[high]
    arr[pi], arr[high] = arr[high], arr[pi]

    # We denote x as the number of elements in right part, pivot not included.
    # if x is greater than or equal to k, we can find our target in right part;
    # otherwise, the target element is in left part, we find the p-largest element in left part,
    # where p = k - x;
    x = high - pi
    if x >= k:
        # k-largest is in right part
        return solve(arr, pi + 1, high, k)
    elif k == x + 1:
        return pivot
    else:
        # k-largest is in left part
        return solve(arr, low, pi - 1, k - x - 1)


arr = [5, 7, 2, 1, 3, 6, 0, 12, 4, 9]
print(solve(arr, 0, len(arr) - 1, 1))
