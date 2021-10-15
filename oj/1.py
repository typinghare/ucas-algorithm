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
# Line 1: a integers
# Line 2: a array
# [Output]
# one integer

# ---------- [ code ] ----------
DIVISOR = 1337
a = int(input())
line_2 = input()
b = []
for n in line_2[1:-1].split(','):
    b.append(int(n.strip()))


def solve(a, b):
    return sub(a % DIVISOR, b)


def sub(r, b):
    length = len(b)
    # conquer
    if length == 1 and b[0] == 1:
        return r

    # b /= 2
    half = []
    if b[0] == 1:
        carry = 1
    else:
        half.append(b[0] >> 1)
        carry = b[0] & 1
    for i in range(1, length):
        half.append((b[i] >> 1) + carry * 5)
        carry = b[i] & 1

    # divide and combine
    if carry == 1:
        # odd
        return (sub(r, half) ** 2 * r) % DIVISOR
    else:
        # even
        return sub(r, half) ** 2 % DIVISOR


print(solve(a, b))
