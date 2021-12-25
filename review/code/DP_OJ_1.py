# 1. 递归（5 min）
def solve(triangle):
    """
    :param triangle: 二维数组
    """
    # 层数
    n = len(triangle)

    # 如果只有一层，直接返回
    if n == 1:
        return triangle[0][0]

    # a 是最后一层，b是倒数第二层
    a, b = triangle[n - 1], triangle[n - 2]

    # 遍历倒数第二层，将 a[i] 和 a[i + 1] 较小的那个加到 b[i] 上
    for i in range(len(b)):
        b[i] += min(a[i], a[i + 1])

    # 弹出最底层
    triangle.pop()

    return solve(triangle)


# 2. 迭代（5 min）
def solve2(triangle):
    # 从倒数第二层遍历到第一层
    for i in range(len(triangle) - 2, -1, -1):
        # i -> 层索引，注意第 i 层有 i+1 个元素
        # 遍历每一个元素，将其下层连接的元素中较小的加到其上
        for j in range(i + 2):
            # j -> 元素索引
            triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]


# test
triangle = [[1], [2, 3], [4, 5, 6]]
print(solve(triangle))
print(solve2(triangle))
