def solve(A, k):
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
print(solve(A, 3))  # correct: 14
