# not use memo
# def solve(n):
#     # Conquer
#     if n <= 3:
#         return 1
#
#     # Divide and Combine
#     ans = 0
#     for i in range(2, n):
#         ans += solve(i) * solve(n - i + 1)
#     return ans


# use memo
def solve(n, memo=None):
    if memo is None:
        memo = [0, 0, 1, 1] + [0] * (n - 3)

    # Conquer
    if memo[n] > 0:
        return memo[n]

    # Divide and Combine
    ans = 0
    mid = (n >> 1) + 1
    for i in range(2, mid):
        ans += solve(i, memo) * solve(n - i + 1, memo)
    ans <<= 1
    if n % 2 == 1:
        # n is odd number
        ans += solve(mid, memo) ** 2
    memo[n] = ans
    return ans


print(solve(7))
