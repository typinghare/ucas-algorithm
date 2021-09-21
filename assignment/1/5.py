# author: ShotgunRO

# ---------- [ subject ] ----------
# Given a convex polygon with n vertices, we can divide it into several separated pieces,
# such that every piece is a triangle. When n=4, there are two different ways to divide
# the polygon; When n=5, there are five different ways.
# Give an algorithm that decides how many ways we can divide a convex
# polygon with n vertices into triangles.


# ---------- [ code ] ----------
def solve(n):
    # Conquer
    if n <= 3:
        return 1

    # Divide and Combine
    ans = 0
    for i in range(2, n):
        ans += solve(i) * solve(n - i + 1)
    return ans


# ---------- [ test ] ----------
N = 6
result = solve(N)
print(result)
