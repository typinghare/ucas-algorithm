# author: ShotgunRO

# ---------- [ subject ] ----------
# <Money robbing>
# A robber is planning to rob houses along a street. Each house has a certain amount of
# money stashed, the only constraint stopping you from robbing each of them is that
# adjacent houses were broken into on the same night.
# 1. Given a list of non-negative integers representing the amount of money of each
#    house, determine the maximum amount of money you can rob tonight without alerting
#    the police.
# 2. What if all houses are arranged in a circle?


# ---------- [ code ] ----------
from typing import List


def money_robbing(nums):
    # <rob1> and <rob2> are two dynamic variables that update in each loop
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


# ---------- [ test ] ----------
# money of each house
nums = [4, 6, 8, 12, 13]
print(money_robbing(nums))


# -------------------------------
def money_robbing_s(nums: List[int]):
    rob1, rob2 = 0, nums[0]

    # [rob1, rob2, n, n+1, ...]
    for n in nums[1:]:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


def money_robbing_circle(nums: List[int]):
    return max(money_robbing(nums[1:]), money_robbing_s(nums[:-1]))

# take [4, 6, 8, 3] for example:
# At the beginning, the 'dynamic list' can be seen as:
# [rob1, rob2, 4, 6, 8, 3]
# Given the limitation, we have two alternative decisions in this case:
# (rob1 + 4) and (rob2).
# So we get the greater one by `max(rob1 + 4, rob2)`, and assign the result to <temp>.
# Now the value `4` has passed, the next 'dynamic list` can be described as:
# [rob1, rob2, 6, 8, 3]
# Similar to above, two decisions are: (rob1 + 6) and (rob2)

# Q1 - What does <rob2> stand for?
# A1 - The result in 'dynamic list'. When there are only two elements in 'dynamic list`,
#      namely <rob1> and <rob2>, <rob2> turns to be final answer.

# Q2 - What does <rob1> stand for?
# A2 - If the 'dynamic list' is [rob1, rob2, n, n+1, ...], then <rob1> is the result of:
#      [rob1, n-1, n, n+1]. (n-1) is not considered by <rob1> but <rob2>, we may not
#      choose (n-1) at the end, <rob1> helps backtracking.


# 假设函数 money_rob(nums) 用于计算房屋不成圈的情况， money_rob_circle(nums) 用于计算房屋成圈的情况
# 你给出的算式类似于：
# money_rob_circle(nums) = max(money_rob(nums[1:]), money_rob(nums))
# money_rob(nums[1:]) 的意义是：指明不选择 0 号房屋，那么 n-1 号房屋可被选；
# 但是 money_rob(nums) 表示可能选择 0 号房屋，但如果选择 0 号房屋，n-1 号房屋依然可选。
# 然而按题目的要求，如果选择了 0 号房屋，n-1 号房屋就不能被选，因此正确的算式应该是：
# money_rob_circle(nums) = max(money_rob(nums[1:]), money_rob_s(nums[:-1]))
# 其中 money_rob_s(nums[:-1]) 表示必然选 0 号房屋，那么第 n-1 号房屋直接移除不进行考虑
