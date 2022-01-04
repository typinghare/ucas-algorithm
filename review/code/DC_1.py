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


def solve2(A, k):
    """
    寻找数组 A 中第 k 大的元素（非原位策略版本）
    """
    # conquer
    if len(A) == 1:
        return A[0]

    # divide
    mid = len(A) // 2  # 定位数组 A 的中位索引
    pivot = A[mid]
    b, c = [], []  # b 记录小于 pivot 的元素，c 记录比大于等于 pivot 的元素

    # 遍历 A 中的元素，将它们分到数组 b 或 c 中
    for x in A:
        if x < pivot:
            b.append(x)
        else:
            c.append(x)

    # 将 pivot 从 c 中剔除出去，A 被分为三部分：b < pivot <= c
    c.remove(pivot)

    x = len(c)  # A 中大于等于 pivot 的元素数量
    if k == x + 1:
        # 比如 k = 5，恰好有 4 个数大于等于 pivot，则 pivot 即为所求
        return pivot
    elif k <= x:
        # 比如 k = 5，x = 5，那么第 k 大的数在 c 中，对 c 进行递归
        return solve(c, k)
    elif k > x:
        # 比如 k = 5，x = 3，说明第 k 大的数在 b 中，对 b 进行递归
        # 这里要注意的是，在 b 中找的是第 k - x - 1 大的数，因为前 x 大的数在 c 中，再减去一个 pivot
        return solve(b, k - x - 1)


# test
A = [8, 1, 15, 10, 4, 3, 2, 9, 7, 12, 5, 16, 14, 6, 13, 11]
print(solve(A, 3, 0, len(A) - 1))  # correct: 14
print(solve2(A, 3))  # correct: 14
