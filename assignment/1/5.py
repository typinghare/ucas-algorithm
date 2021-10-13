# author: ShotgunRO

# ---------- [ subject ] ----------
# Given a convex polygon with n vertices, we can divide it into several separated pieces,
# such that every piece is a triangle. When n=4, there are two different ways to divide
# the polygon; When n=5, there are five different ways.
# Give an algorithm that decides how many ways we can divide a convex
# polygon with n vertices into triangles.


# ---------- [ code ] ----------
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

# use dict
def solve(n, cache=None):
    if cache is None:
        cache = {2: 1, 3: 1}

    # Conquer
    if n in cache:
        return cache[n]

    # Divide and Combine
    ans = 0
    mid = (n >> 1) + 1
    for i in range(2, mid):
        ans += solve(i, cache) * solve(n - i + 1, cache)
    ans <<= 1
    if n % 2 == 1:
        # n is odd number
        ans += solve(mid, cache) ** 2
    cache[n] = ans
    return ans

# use list
# def solve(n, cache=None):
#     if cache is None:
#         cache = [0, 0, 1, 1] + [0] * (n - 3)
#
#     # Conquer
#     if cache[n] > 0:
#         return cache[n]
#
#     # Divide and Combine
#     ans = 0
#     mid = (n >> 1) + 1
#     for i in range(2, mid):
#         ans += solve(i, cache) * solve(n - i + 1, cache)
#     ans <<= 1
#     if n % 2 == 1:
#         # n is odd number
#         ans += solve(mid, cache) ** 2
#     cache[n] = ans
#     return ans


# ---------- [ test ] ----------
N = 7
result = solve(N)
print(result)

# ---------- [ correctness ] ----------
# Loop invariant:
