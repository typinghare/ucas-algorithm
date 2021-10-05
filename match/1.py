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


# If b is not a list
def solve(a: int, b: int):
    # 1. 求 a 的余数
    r = a % DIVISOR

    # 2. 对 b 进行二分
    return sub(r, b)


def sub(r: int, b: int):
    # Conquer
    if b == 1:
        return r

    # Divide
    left = right = 0
    half = b // 2
    if b % 2 == 0:
        # b is even number
        left = right = sub(r, half)
        pass
    else:
        # b is odd number
        left = sub(r, half)
        right = sub(r, half + 1)
        pass

    # Combine
    return (left * right) % DIVISOR


print(solve(2, 3))

# def solve(a: int, b: list):
#     # 1. 求 a 的余数
#     r = a % DIVISOR
#
#     # 2. 对 b 进行二分
#     return sub(r, b)

# def sub(r: int, b: list):
#     mi = len(b) - 1  # max index of b
#
#     # Conquer
#     if b[mi - 2:] == [0, 1]:
#         return r
#
#     # Divide
#     left = right = 0
#     if b[mi] % 2 == 0:
#         # b is even number
#         left = right = 0
#         pass
#     else:
#         # b is odd number
#         pass
#
#     # Combine
