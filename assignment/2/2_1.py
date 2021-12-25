# author: ShotgunRO

# ---------- [ subject ] ----------
# <Largest Divisible Subset>
# Given a set of distinct positive integers, find the largest subset such that every pair
# (S_i, S_j) of elements in this subset satisfies: S_i % S_j = 0 or S_j % S_i = 0.
# Please return the largest size of the subset.
# Note: S_i % S_j = 0 means that S_i is divisible by S_j.
# leetcode 368 - https://leetcode.com/problems/largest-divisible-subset/


# ---------- [ code ] ----------
# recursion
def largest_divisible_subset(i):
    # recursion termination
    if i == n:
        return 0

    num = nums[i]

    # judge whether  [num] can be selected
    flag = True
    for j in selected:
        if not (num % j == 0 or j % num == 0):
            flag = False
            break

    result_select = 0
    if flag:
        # [num] can be selected
        selected.append(num)
        if len(selected) > len(opt):
            opt.clear()
            opt.extend(selected)
        result_select = 1 + largest_divisible_subset(i + 1)
        selected.remove(num)

    # skip
    result_skip = largest_divisible_subset(i + 1)

    return max(result_select, result_skip)


# ---------- [ test ] ----------
nums = [1, 2, 3]
n = len(nums)
selected = []
opt = []
largest_divisible_subset(0)
print(opt)
