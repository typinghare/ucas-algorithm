# author: ShotgunRO

# ---------- [ subject ] ----------
# <Largest Divisible Subset>
# Given a set of distinct positive integers, find the largest subset such that every pair
# (S_i, S_j) of elements in this subset satisfies: S_i % S_j = 0 or S_j % S_i = 0.
# Please return the largest size of the subset.
# Note: S_i % S_j = 0 means that S_i is divisible by S_j.


# ---------- [ code ] ----------
def largest_divisible_subset(i, selected):
    # recursion termination
    if i == n:
        return 0

    # select
    num = S[i]
    opt = largest_divisible_subset(i + 1)

    # skip

    pass


# ---------- [ test ] ----------
S = [2, 3, 4, 5, 6, 7, 8]
n = len(S)