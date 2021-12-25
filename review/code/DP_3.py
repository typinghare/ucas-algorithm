# 1. 迭代
def solve(n):
    # n >= 2
    dp = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n]


# 2. 递归
def solve2(n):
    if n <= 1:
        return 1

    ret = 0
    for i in range(n):
        ret += solve2(i) * solve2(n - i - 1)
    return ret


# 3. 递归（带 memo，效率高）
def solve3(n, memo=None):
    if memo is None:
        memo = [1, 1] + [0] * (n - 1)

    val = memo[n]
    if val > 0:
        return val

    ret = 0
    for i in range(n):
        ret += solve3(i, memo) * solve3(n - i - 1, memo)
    memo[n] = ret
    return ret


# test
print(solve(6), solve2(6), solve3(6))
