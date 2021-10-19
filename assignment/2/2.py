# author: ShotgunRO

# ---------- [ subject ] ----------
# <Largest Divisible Subset>
# Given a set of distinct positive integers, find the largest subset such that every pair
# (S_i, S_j) of elements in this subset satisfies: S_i % S_j = 0 or S_j % S_i = 0.
# Please return the largest size of the subset.
# Note: S_i % S_j = 0 means that S_i is divisible by S_j.


# ---------- [ code ] ----------
def largest_divisible_subset(i):
    if i in cache:
        return cache[i]

    # recursion termination
    if i == n:
        return 0

    num = S[i]

    # judge whether or not [num] can be selected
    flag = True
    result_select = 0
    for j in selected:
        if not (num % j == 0 or i % num == 0):
            flag = False
            break
    if flag:
        # [num] can be selected
        selected.append(num)
        opt = 1 + largest_divisible_subset(i + 1)
        selected.remove(num)

    # skip
    result_skip = largest_divisible_subset(i + 1)

    result = max(result_select, result_skip)
    cache[i] = result
    return result


# ---------- [ test ] ----------
S = [2, 3, 4, 5, 6, 7, 8]
n = len(S)
selected = []
cache = {}
largest_divisible_subset(0)
print(selected)
