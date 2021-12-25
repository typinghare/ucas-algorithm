def solve(arr):
    # arr: 正整数列表
    arr.sort()

    # 用以保存 i 及其可以整数的数的个数
    # 映射关系：数 => 该数可以整除的数的个数
    # 初始化 -1 => 0 的原因是当遍历到的数不与任何数匹配时，其至少可以和 -1 匹配
    d = {-1: 0}

    # 遍历数组中的所有元素
    for i in arr:
        # 遍历 d 中的所有数
        for j in list(d):
            # 如果 i 可以整除 j，则 i 可以整除所有 j 可以整数的数
            if i % j == 0 and (i not in d or d[j] >= d[i]):
                d[i] = d[j] + 1

    return max(d.values())


# test
print(solve([16, 2, 4, 5, 8, 7]))
