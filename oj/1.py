# author: ShotgunRO

# ---------- [ subject ] ----------
# [Description]
# Bob has encountered a difficult problem, and hope you design an algorithm to calculate pow(a,b) mod 1337,
# where a is a positive integer, b is a very large positive integer and will be given in the form of an array.
# For example, pow(2,3) mod 1337 is 8.
# [Constraints]
# 1 <= a <= 2^31-1, 1 <= b.length <= 2000, 0 <= b[i] <= 9
# b doesn't contain leading zeros.
# Please give an algorithm with O(logn) complexity.
# [Input]
# Line 1a integers
# Line 2a array
# [Output]
# one integer

# ---------- [ code ] ----------
DIVISOR = 1337
a = int(input())
b = list(map(int, input().split(' ')))


def solve(a: int, b: list):
    # transfer b into an integer
    B = 0
    for i in range(len(b)):
        B = B * 10 + b[i]

    r = a % DIVISOR
    return sub(r, B)


def sub(r: int, b: int):
    # conquer
    if b == 1:
        return r

    # divide and combine
    if b & 1 == 1:
        # odd number
        return (sub(r, b // 2) ** 2 * r) % DIVISOR
    else:
        # even number
        return sub(r, b // 2) ** 2 % DIVISOR


print(solve(a, b))
