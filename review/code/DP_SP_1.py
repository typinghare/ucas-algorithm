# 0-1 Knapsack Problem

def solution(n, w, W, V):
    """
    :param n: 物品数量
    :param w: 总重
    :param W: 物品重量（向量）
    :param V: 物品价值（向量）
    :return:
    """
    dp = [[0] * (w + 1) for _ in range(n + 1)]  # size: (n+1) * (w+1)
    print(dp[0])
    for i in range(1, n + 1):
        # i -> 第 i 件物品
        for j in range(1, w + 1):
            # 第 i 件物品的重量为 W[i-1]，价值为 V[i-1]
            if j - W[i - i] >= 0:
                # 能装下第 i 件物品，那就选较大者：
                dp[i][j] = max(dp[i - 1][j], V[i - 1] + dp[i - 1][j - W[i - 1]])
            else:
                # 装不下，不选第 i 件物品，dp 的值不变
                dp[i][j] = dp[i - 1][j]


# test
print(solution(4, 15, [12, 2, 1, 1], [4, 2, 2, 1]))
